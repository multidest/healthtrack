from django.contrib import admin

# Register your models here.

from Health.models import Patient, Appointment, PatientEncounter, Medication, PatientPrescribedMedication, PharmacyOrder, LabOrder

class PatientAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                  {'fields': ['PatientName']}),
        ('Patient information', {'fields': ['PatientGender']}),
        ('Patient contact',     {'fields': ['PatientPhone',
                                            'PatientDOB']}),
        (None,                  {'fields': ['PatientPrimaryPhysician',
                                            'PatientAddress']}),
    ]
    list_display = ('id', 'PatientName', 'PatientPrimaryPhysician')
    list_filter = ['PatientGender']
    search_fields = ['PatientName','PatientPhone','PatientPrimaryPhysician']

class AppointmentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                  {'fields': ['AppointmentDate']}),
        ('Information',         {'fields': ['AppointmentWithPatient',
                                            'AppointmentWithPhysician']}),
    ]
    list_display = ('id','AppointmentDate','AppointmentWithPatient','AppointmentWithPhysician')
    list_filter = ['AppointmentDate']
    search_fields = ['AppointmentDate','AppointmentWithPatient','AppointmentWithPhysician']
    
class PatientEncounterAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                  {'fields':[ 'EncounterDate', 'EncounterPatient']}),
        ('Encounter',           {'fields':[ 'EncounterSeeingPhysician',
                                            'EncounterPatientComplaints',
                                            'EncounterVitalSigns',
                                            'EncounterDiagnosis',
                                            'EncounterTreatmentPlan',
                                            'EncounterReferrals',
                                            'EncounterNotes']})
    ]
    #list_display = ('id')
    
admin.site.register(Patient,PatientAdmin)
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(PatientEncounter, PatientEncounterAdmin)
admin.site.register(Medication)
admin.site.register(PatientPrescribedMedication)
admin.site.register(PharmacyOrder)
admin.site.register(LabOrder)
