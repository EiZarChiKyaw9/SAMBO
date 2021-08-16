from django.shortcuts import render, redirect
from .forms import Listform, WorkVolumeform, SlabLevelForm, SiteForm, WVMainForm, WVDailyReportDetailsForm
from .models import list, Work_Volume, Slab_Level, Site, WV_Main, WV_Daily_Report_Details
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
import csv
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
from datetime import datetime
from django.core.files.storage import FileSystemStorage


def home(request):
    if request.method == 'POST':
        form = Listform(request.POST or None)
        if form.is_valid():
            form.save()

        all_items = list.objects.all
        messages.success(request, ('Item has been added to the list!'))
        return render(request, 'home.html', {'all_items': all_items})
    else:
        all_items = list.objects.all
        return render(request, 'home.html', {'all_items': all_items})


def delete(request, list_id):
    item = list.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ('Item has been deleted!'))
    return redirect('home')


def cross_off(request, list_id):
    item = list.objects.get(pk=list_id)
    item.completed = True
    item.save()
    all_items = list.objects.all
    return redirect('home')


def uncross(request, list_id):
    item = list.objects.get(pk=list_id)
    item.completed = False
    item.save()
    all_items = list.objects.all
    return redirect('home')


def edit(request, list_id ):

    if request.method == 'POST':
        item = list.objects.get(pk=list_id)

        form = Listform(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            messages.success(request, ('Item has been updated!'))
            return redirect('home')

    else:
        item = list.objects.get(pk=list_id)
        return render(request, 'edit.html', {'item': item})


def logon(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('successful login!'))
            return redirect('home')
        else:
            messages.success(request, ('Wrong username and password!'))
            return redirect('logon')
    else:
        return render(request, 'authenticate/User_Logon.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out!')
    return redirect('logon')


def work_volume(request):
    if request.method == 'POST':
        form = WorkVolumeform(request.POST or None)
        if form.is_valid():
            form.save()

        work_volume_items = Work_Volume.objects.all
        messages.success(request, ('Item has been added to the list!'))
        return render(request, 'admin/work_volume_create.html', {'work_volume_items': work_volume_items})
    else:
        work_volume_items = Work_Volume.objects.all
        return render(request, 'admin/work_volume_create.html', {'work_volume_items': work_volume_items})


def work_volume_edit(request, wv_id):
    if request.method == 'POST':

        work_volume_item = Work_Volume.objects.get(pk=wv_id)
        form = WorkVolumeform(request.POST or None, instance=work_volume_item)

        if form.is_valid():
            form.save()

        messages.success(request, ('Item has been updated!'))
        return redirect('work_volume')
    else:
        work_volume_item = Work_Volume.objects.get(pk=wv_id)
        work_volume_items = Work_Volume.objects.all
        return render(request, 'admin/work_volume_create.html', {'work_volume_item': work_volume_item,
                                                                'work_volume_items': work_volume_items})


def slab_level(request):
    if request.method == 'POST':
        form = SlabLevelForm(request.POST or None)
        if form.is_valid():
            form.save()

        slab_level_items = Slab_Level.objects.all
        messages.success(request, ('Item has been added to the list!'))
        return render(request, 'admin/slab_level_create.html', {'slab_level_items': slab_level_items})
    else:
        slab_level_items = Slab_Level.objects.all
        return render(request, 'admin/slab_level_create.html', {'slab_level_items': slab_level_items})


def slab_level_edit(request, slab_id):
    if request.method == 'POST':

        slab_level_item = Slab_Level.objects.get(pk=slab_id)
        form = SlabLevelForm(request.POST or None, instance=slab_level_item)

        if form.is_valid():
            form.save()

        messages.success(request, ('Item has been updated!'))
        return redirect('slab_level')
    else:
        slab_level_item = Slab_Level.objects.get(pk=slab_id)
        slab_level_items = Slab_Level.objects.all
        return render(request, 'admin/slab_level_create.html', {'slab_level_items': slab_level_items,
                                                                'slab_level_item': slab_level_item})


def site(request):
        # uploaded_file_url = fs.url(filename)

    if request.method == 'POST': # and request.FILES['FU_Site_Image'] if 'FU_Site_Image' in request.FILES else False:
        form = SiteForm(request.POST or None, request.FILES)
        # FU_Site_Image = request.FILES['FU_Site_Image']
        # fs = FileSystemStorage()
        # filename = fs.save(FU_Site_Image.name, FU_Site_Image)

        if form.is_valid():
            form.save()

        site_items = Site.objects.all
        messages.success(request, ('Item has been added to the list!'))
        return render(request, 'admin/site_create.html', {'site_items': site_items})
    else:
        site_items = Site.objects.all
        return render(request, 'admin/site_create.html', {'site_items': site_items})


def site_edit(request, site_id):

    if request.method == 'POST': # and request.FILES['FU_Site_Image'] if 'FU_Site_Image' in request.FILES else True:
        site_item = Site.objects.get(pk=site_id)

        form = SiteForm(request.POST or None, request.FILES, instance=site_item)

        if form.is_valid():
            # form.save(update_fields=["TX_Site_Name"])
            form.save()

        # site_items = Site.objects.all
        messages.success(request, ('Item has been updated!'))
        return redirect('site')
    else:
        site_item = Site.objects.get(pk=site_id)
        site_items = Site.objects.all
        return render(request, 'admin/site_create.html', {'site_items': site_items, 'site_item': site_item})


def wv_main(request):
    if request.method == 'POST':
        form = WVMainForm(request.POST or None)
        if form.is_valid():
            form.save()

        wv_main_items = WV_Main.objects.all
        site_items = Site.objects.filter(Is_Active=True)
        messages.success(request, ('Item has been added to the list!'))
        return render(request, 'admin/site_info_create.html', {'wv_main_items': wv_main_items,
                        'site_items': site_items})
    else:

        wv_main_items = WV_Main.objects.all
        site_items = Site.objects.filter(Is_Active=True)
        return render(request, 'admin/site_info_create.html', {'wv_main_items': wv_main_items,
                        'site_items': site_items})


def wv_main_edit(request, wv_info_id):

    if request.method == 'POST':
        wv_main_item = WV_Main.objects.get(pk=wv_info_id)

        form = WVMainForm(request.POST or None, instance=wv_main_item)

        if form.is_valid():
            form.save()

        messages.success(request, ('Item has been updated!'))
        return redirect('site_info_create')
    else:
        wv_main_item = WV_Main.objects.get(pk=wv_info_id)
        wv_main_items = WV_Main.objects.all
        site_items = Site.objects.filter(Is_Active=True)
        return render(request, 'admin/site_info_create.html', {'wv_main_item': wv_main_item, 'site_item': site_items,
                                                               'wv_main_items': wv_main_items})


def submit_work_volume(request):
    wv_main_items = WV_Main.objects.filter(Is_Active=True)
    return render(request, 'submission/wv_submit_report.html', {'wv_main_items': wv_main_items})


def daily_wv_submission(request, site_id):
    if request.method == 'POST': # and request.FILES['FU_Site_Image'] if 'FU_Site_Image' in request.FILES else False:
        form = WVDailyReportDetailsForm(request.POST or None, request.FILES)

        if form.is_valid():
            form.save()

        wv_main_item = WV_Main.objects.get(pk=site_id)
        Daily_report_Details_item = WV_Daily_Report_Details.objects.filter(ID_WV_Main=wv_main_item.CD_Site,
                                                                           created_date=date.today())
        work_volume_items = Work_Volume.objects.all
        slab_level_items = Slab_Level.objects.all
        messages.success(request, ('Item has been added to the list!'))
        return render(request, 'submission/submit_daily_workvolume.html',
                      {'Daily_report_Details_items': Daily_report_Details_item,
                       'wv_main_item': wv_main_item,
                       'work_volume_items': work_volume_items,
                       'slab_level_items': slab_level_items})

    else:

        wv_main_item = WV_Main.objects.get(pk=site_id)
        work_volume_items = Work_Volume.objects.all
        slab_level_items = Slab_Level.objects.all # filter(ID_WV_Main="TEL 308").order_by('id').first()
        Daily_report_Details_items = WV_Daily_Report_Details.objects.filter(ID_WV_Main=wv_main_item.CD_Site,
                                                                            created_date=date.today())
        return render(request, 'submission/submit_daily_workvolume.html',
                      {'Daily_report_Details_items': Daily_report_Details_items,
                       'wv_main_item': wv_main_item,
                       'work_volume_items': work_volume_items,
                       'slab_level_items': slab_level_items})


def rp_work_volume(request):
    if request.method == 'POST':
        site_name = request.POST['site']

        from_date = request.POST.get('date_from', None)
        to_date = request.POST.get('date_to', None)
        # dt_from_date = datetime.strptime(from_date, 'M-D-yyyy')
        # to_date = request.POST['date_to']+':00:00.000000'
        site_items = Site.objects.all
        wv_rp_items = WV_Daily_Report_Details.objects.filter(ID_WV_Main=site_name,
                                                             created_date__range=(from_date, to_date))
        messages.success(request, ('Filter with site name: ' + site_name + ' From Date: ' + from_date
                                   + ' To Date: ' +to_date))

        return render(request, 'Report/rp_work_volume.html', {'wv_rp_items': wv_rp_items
            , 'site_items': site_items})
    else:
        site_items = Site.objects.all
        wv_rp_items = WV_Daily_Report_Details.objects.all

        return render(request, 'Report/rp_work_volume.html', {'wv_rp_items': wv_rp_items
            , 'site_items': site_items})


def export_report_csv(request):
    if request.method == 'POST':
        site_name = request.POST['site']
        from_date = request.POST.get('date_from', None)
        to_date = request.POST.get('date_to', None)

        response = HttpResponse(content_type='text/csv')

        writer = csv.writer(response)

        writer.writerow(['Site Name', 'Site Supervisor', 'In Charge Design', 'In Charge QS', 'Site Manager'
                            , 'Construction Manager', 'Created Date', 'Modified Date'])

        for report_wv_main in WV_Main.objects.filter(CD_Site=site_name)\
                .values_list("CD_Site","TX_Site_Supervisor","TX_Site_In_charge_Design"
                ,"TX_Site_In_charge_QS","TX_Site_Manager","TX_Construction_Manager","created_date"
                ,"modified_date"):
            writer.writerow(report_wv_main)
            writer.writerow('')
            writer.writerow(['Site Name','Panel No', 'Zone',  'Slab Level', 'Defect', 'Man Power', 'Surface or Joint'
                                , 'PU Kg','PU PKR','Length','Width','Height','Volume','AREA','Progress','Cement','Rebar Qty'
                             ,'Rebar Length','Rebar Size','created_date'])

        for report_wv in WV_Daily_Report_Details.objects.filter(ID_WV_Main=site_name,
                                                                created_date__range=(from_date, to_date))\
                .values_list("ID_WV_Main","TX_Panel_No","TX_Zone"
                ,"CD_Slab_Level","CD_Work","TX_Man_Power_Work","TX_Sur_Joint"
                ,"PU_Kg","PU_PKR","Volume_L","Volume_W","Volume_H","Volume","AREA","Progress","Cement","Rebar_Qty"
                ,"Rebar_Length","Rebar_Size","created_date"):
            writer.writerow(report_wv)

            local_dt = datetime.now()
            formated_date = local_dt.strftime("%Y-%m-%d_%H:%M_")
            extension = ".csv"
            file_name = str(formated_date)+site_name+extension

            response['Content-Disposition'] = f'attachment; filename={file_name}'

    return response


def site_info(request, site_id):
    wv_main_item = WV_Main.objects.get(pk=site_id)
    site_image = Site.objects.filter(TX_Site_Name=wv_main_item.CD_Site)

    return render(request, 'site_info.html',
                  {'wv_main_item': wv_main_item,
                   'site_image': site_image})


def download_image(request, img_url):
    fs = FileSystemStorage()
    # img = request.POST['FU_WV_Image']
    uploaded_file_url = 'media/' + fs.url(img_url)
    return render(request, 'image_viewer.html', {
        'uploaded_file_url': uploaded_file_url
    })
