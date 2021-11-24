from django.contrib import admin
from .models import list, Work_Volume, Slab_Level, WV_Main, WV_Daily_Report_Details, Site, Equipment\
    , Equipment_Specification, Designation, DR_Details, Classification, DR_Details
admin.site.register(list)
admin.site.register(Work_Volume)
admin.site.register(Slab_Level)
admin.site.register(Site)
admin.site.register(WV_Main)
admin.site.register(WV_Daily_Report_Details)
admin.site.register(Equipment)
admin.site.register(Equipment_Specification)
admin.site.register(Designation)
admin.site.register(DR_Details)
admin.site.register(Classification)
