from django.db import models
from datetime import datetime, date


class list(models.Model):
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.item


class Work_Volume(models.Model):
    Tx_Name = models.CharField(max_length=200)
    Is_Active = models.BooleanField(default=True)

    def __str__(self):
        return self.Tx_Name


class Slab_Level(models.Model):
    TX_Slab_Level_Name = models.CharField(max_length=200)
    Is_Active = models.BooleanField(default=True)

    def __str__(self):
        return self.TX_Slab_Level_Name


class Site(models.Model):
    TX_Site_Name = models.CharField(max_length=200)
    Is_Active = models.BooleanField(default=True)
    FU_Site_Image = models.ImageField(null=True, blank=True, upload_to="media/%Y/%m/%d/")

    def __str__(self):
        return self.TX_Site_Name


class WV_Main(models.Model):
    CD_Site = models.CharField(max_length=200)
    TX_Site_Supervisor = models.CharField(max_length=200)
    TX_Site_In_charge_Design = models.CharField(max_length=200)
    TX_Site_In_charge_QS = models.CharField(max_length=200)
    TX_Site_Manager = models.CharField(max_length=200)
    TX_Construction_Manager = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    Is_Active = models.BooleanField(default=True)

    def __str__(self):
        return self.CD_Site


class WV_Daily_Report_Details(models.Model):
    ID_WV_Main = models.CharField(max_length=200)
    TX_Panel_No = models.CharField(max_length=200)
    TX_Zone = models.CharField(max_length=200, null=False)
    CD_Slab_Level = models.CharField(max_length=200)
    CD_Work = models.CharField(max_length=200)
    TX_Man_Power_Work = models.CharField(max_length=200)
    TX_Sur_Joint = models.CharField(max_length=200)
    PU_Kg = models.CharField(max_length=200, null=True, blank=True)
    PU_PKR = models.CharField(max_length=200, null=True, blank=True)
    Volume_L = models.CharField(max_length=200, null=True, blank=True)
    Volume_W = models.CharField(max_length=200, null=True, blank=True)
    Volume_H = models.CharField(max_length=200, null=True, blank=True)
    Volume = models.CharField(max_length=200, null=True, blank=True)
    AREA = models.CharField(max_length=200, null=True, blank=True)
    Progress = models.CharField(max_length=200)
    Cement = models.CharField(max_length=200, null=True, blank=True)
    Rebar_Qty = models.CharField(max_length=200, null=True, blank=True)
    Rebar_Length = models.CharField(max_length=200, null=True, blank=True)
    Rebar_Size = models.CharField(max_length=200, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    Is_Active = models.BooleanField(default=True)
    FU_WV_Image = models.ImageField(null=True, blank=True, upload_to="defect_submission/%Y/%m/%d/")

    def __str__(self):
        return self.ID_WV_Main



