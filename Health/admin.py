from django.contrib import admin

# Register your models here.

from Health.models import Physician, Patient, Appointment, Patient_has_encounter, Medication, Patient_prescribed_medication, PharmacyOrder, LabOrder

class PatientAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                  {'fields': ['PatientName']}),
        ('Patient information', {'fields': ['PatientGender']}),
        ('Patient contact',     {'fields': ['PatientPhone',
                                            'PatientDOB']}),
        (None,                  {'fields': ['PatientPrimaryPhysician',
                                            'PatientAddress']}),
    ]
    list_display = ('id', 'PatientName')
    list_filter = ['PatientGender']
    search_fields = ['PatientName']
    
admin.site.register(Physician)
admin.site.register(Patient,PatientAdmin)
admin.site.register(Appointment)
admin.site.register(Patient_has_encounter)
admin.site.register(Medication)
admin.site.register(Patient_prescribed_medication)
admin.site.register(PharmacyOrder)
admin.site.register(LabOrder)
