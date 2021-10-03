from django import forms
from .models import list, Work_Volume, Slab_Level, Site, WV_Main,WV_Daily_Report_Details,Equipment,Equipment_Specification,Designation,DR_Details,Classification

class Listform (forms.ModelForm):
    class Meta:
        model = list
        fields= ["item", "completed"]


class WorkVolumeform (forms.ModelForm):
    class Meta:
        model = Work_Volume
        fields= ["Tx_Name", "Is_Active"]


class SlabLevelForm (forms.ModelForm):
    class Meta:
        model = Slab_Level
        fields= ["TX_Slab_Level_Name", "Is_Active"]


class SiteForm (forms.ModelForm):
    class Meta:
        model = Site
        fields= ["TX_Site_Name", "Is_Active","FU_Site_Image"]


class WVMainForm (forms.ModelForm):
    class Meta:
        model = WV_Main
        fields= ["CD_Site", "TX_Site_Supervisor", "TX_Site_In_charge_Design", "TX_Site_In_charge_QS", "TX_Site_Manager", "TX_Construction_Manager", "Is_Active"]


class WVDailyReportDetailsForm (forms.ModelForm):
    class Meta:
        model = WV_Daily_Report_Details
        fields= ["ID_WV_Main","TX_Panel_No","TX_Zone","CD_Slab_Level","CD_Work","TX_Man_Power_Work","TX_Sur_Joint",
                 "PU_Kg","PU_PKR","Volume_L","Volume_W","Volume_H","Volume","AREA","Progress","Cement","Rebar_Qty",
                 "Rebar_Length","Rebar_Size","Is_Active","FU_WV_Image"]


class EquipmentForm (forms.ModelForm):
    class Meta:
        model = Equipment
        fields= ["TX_Equipment_Name", "Is_Active"]

class EquipmentSpecificationForm (forms.ModelForm):
    class Meta:
        model = Equipment_Specification
        fields= ["TX_Equipment_Specification_Name", "Is_Active"]

class DesignationForm (forms.ModelForm):
    class Meta:
        model = Designation
        fields= ["TX_Designation_Name", "Is_Active"]


class DRDetailsForm (forms.ModelForm):
    class Meta:
        model = DR_Details
        fields= ["ID_DR_Main","TX_Panel_No_Range","Start_Date","End_Casting_Concrete","Manpower_Classification","TX_Designation_No","Day_Night",
                 "CD_Equipment","CD_Equipment_Specification","TX_Equipment_Qty","TX_Equipment_Unit","Remark","Is_Active","FU_WV_Image","TX_Designation","TX_Activity","TX_Classification_Name"]

class ClassificationForm (forms.ModelForm):
    class Meta:
        model = Classification
        fields= ["TX_Classification_Name", "Is_Active"]
