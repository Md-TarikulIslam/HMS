from django.db import models
from django.forms import DateTimeInput
from datetime import datetime


class EmployeeDetails(models.Model):
    employee_id = models.AutoField
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=50)
    image = models.ImageField(upload_to="crud/images")

    class Meta:
         verbose_name_plural = "Employee Details"

    def __str__(self):
        return self.name


class PatientDetails(models.Model):
    patient_id = models.AutoField
    pname = models.CharField(max_length=50)
    pemail = models.CharField(max_length=50)
    paddress = models.CharField(max_length=300)
    pphone = models.CharField(max_length=50)
   

    class Meta:
         verbose_name_plural = "Patient Details"

    def __str__(self):
        return self.pname

class DoctorDetails(models.Model):
    doctor_id = models.AutoField
    dname = models.CharField(max_length=50)
    demail = models.CharField(max_length=50)
    dspecialist = models.CharField(max_length=300)
    dphone = models.CharField(max_length=50)
   

    class Meta:
         verbose_name_plural = "Doctor Details"

    def __str__(self):
        return self.dname


class SalaryDetails(models.Model):
    salary_id = models.AutoField
    sname = models.CharField(max_length=50)
    saccountno = models.CharField(max_length=50)
    samount = models.CharField(max_length=50, null=True)
    smonth = models.CharField(max_length=50)
   

    class Meta:
         verbose_name_plural = "Salary Details"

    def __str__(self):
        return self.sname
   

class MedicineDetails(models.Model):
    medicine_id = models.AutoField
    mname = models.CharField(max_length=50)
    mtype = models.CharField(max_length=50, null=True )
    mprice = models.CharField(max_length=16, null=True)
    mstock = models.CharField(max_length=4)
   

    class Meta:
         verbose_name_plural = "Medicine Details"

    def __str__(self):
        return self.mname


class OPDDetails(models.Model):
    opd_id = models.AutoField
    oname = models.CharField(max_length=50)
    oaddress = models.CharField(max_length=50, null=True )
    ophone = models.CharField(max_length=16, null=True)
    odate = models.CharField(max_length=50)
   

    class Meta:
         verbose_name_plural = "OPD Details"

    def __str__(self):
        return self.oname

class IPDDetails(models.Model):
    IPD_id = models.AutoField
    iname = models.CharField(max_length=50)
    idate = models.CharField(max_length=50)
    iaddress = models.CharField(max_length=300)
    iphone = models.CharField(max_length=50)
   

    class Meta:
         verbose_name_plural = "IPD Details"

    def __str__(self):
        return self.iname

class OTDetails(models.Model):
    ot_id = models.AutoField
    opname = models.CharField(max_length=50)
    odname = models.CharField(max_length=50)
    opdate = models.CharField(max_length=50)
    opcause = models.CharField(max_length=50)
    oproom = models.CharField(max_length=300)
    opphone = models.CharField(max_length=50)
   

    class Meta:
         verbose_name_plural = "OT Details"

    def __str__(self):
        return self.opname

class BEDetails(models.Model):
    bed_id = models.AutoField
    broom = models.CharField(max_length=50)
    bfloor = models.CharField(max_length=50)
    bseat = models.CharField(max_length=50)
   

    class Meta:
         verbose_name_plural = "BED Details"

    def __str__(self):
        return self.broom