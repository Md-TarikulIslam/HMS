from django.contrib import admin
from .models import EmployeeDetails, PatientDetails, DoctorDetails,SalaryDetails, MedicineDetails, OPDDetails, IPDDetails, OTDetails, BEDetails

admin.site.register(EmployeeDetails) 
admin.site.register(PatientDetails)
admin.site.register(DoctorDetails)
admin.site.register(SalaryDetails)
admin.site.register(MedicineDetails)
admin.site.register(OPDDetails)
admin.site.register(IPDDetails)
admin.site.register(OTDetails)
admin.site.register(BEDetails)

class EmployeeDetails(admin.ModelAdmin):
    pass


class PatientDetails(admin.ModelAdmin):
    pass

class DoctorDetails(admin.ModelAdmin):
    pass


class SalaryDetails(admin.ModelAdmin):
    pass


class MedicineDetails(admin.ModelAdmin):
    pass

class OPDDetails(admin.ModelAdmin):
    pass

class IPDDetails(admin.ModelAdmin):
    pass

class OTDetails(admin.ModelAdmin):
    pass

class BEDetails(admin.ModelAdmin):
    pass