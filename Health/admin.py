from django.contrib import admin

# Register your models here.

from Health.models import Patient, Appointment, PatientEncounter, Medication, PatientPrescribedMedication, PharmacyOrder, LabOrder

#class PatientPrescribedMedicationAdmin(admin.ModelAdmin):
#     fieldsets = [
#        (None,                  {'fields':[]})
#     ]

from django.contrib import admin
#from models import MyModel

class PatientPrescribedMedicationInline(admin.TabularInline):
    verbose_name_plural  = 'Prescribed Medications'
    verbose_name =  'Prescribed Medication'
    model = PatientPrescribedMedication
    extra = 0
    #max_num = 0
    #exclude = ['PatientEncounter_Encounter']
    #readonly_fields = ['MedicationID','PatientEncounter_Encounter']
    
class PatientEncounterInline(admin.TabularInline):
    verbose_name_plural  = 'medical encounters'
    verbose_name =  'medical encounter'
    model = PatientEncounter
    extra = 0
    max_num = 0
    exclude = ['EncounterPatientComplaints','EncounterVitalSigns','EncounterDiagnosis','EncounterTreatmentPlan','EncounterReferrals','EncounterNotes']
    readonly_fields = ['EncounterDate','EncounterSeeingPhysician']
    
class AppointmentInline(admin.TabularInline):
    verbose_name_plural  = 'appointments'
    verbose_name =  'appointment'
    model = Appointment
    extra = 0
    max_num = None
    exclude = []
    readonly_fields = []
    
class PharmacyOrderInline(admin.TabularInline):
    verbose_name_plural  = 'pharmacy orders'
    verbose_name =  'pharmacy order'
    model = PharmacyOrder
    extra = 0
    max_num = None
    exclude = []
    readonly_fields = []
    
class LabOrderInline(admin.TabularInline):
    verbose_name_plural  = 'lab orders'
    verbose_name =  'lab order'
    model = LabOrder
    extra = 0
    max_num = None
    exclude = []
    readonly_fields = []    

class PatientAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                  {'fields': ['PatientName']}),
        ('Patient information', {'fields': ['PatientGender']}),
        ('Patient contact',     {'fields': ['PatientPhone',
                                            'PatientDOB']}),
        (None,                  {'fields': ['PatientPrimaryPhysician',
                                            'PatientAddress',
                                            'PatientInsuranceInfo']}),
    ]
    list_display = ('id', 'PatientName', 'PatientPrimaryPhysician')
    list_filter = ['PatientGender']
    search_fields = ['PatientName','PatientPhone']
    inlines = [AppointmentInline,PatientPrescribedMedicationInline,]
    

class AppointmentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                  {'fields': ['AppointmentDate']}),
        ('Information',         {'fields': ['AppointmentWithPatient',
                                            'AppointmentWithPhysician']}),
    ]
    list_display = ('id','AppointmentDate','AppointmentWithPatient','AppointmentWithPhysician')
    list_filter = ['AppointmentDate']
    search_fields = ['AppointmentDate']
    
    #def queryset(self, request):
    #    qs = super(AppointmentAdmin, self).queryset(request)
    #    print "Physicians" in request.user.groups.values_list('name',flat=True)
    #    if "Physicians" in request.user.groups.values_list('name',flat=True):
    #        return qs
    #    #return "Physicians" in request.user.groups.values_list('name',flat=True)
    #    return qs.filter(AppointmentWithPhysician=request.user)
    
class PatientEncounterAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                  {'fields':[ 'EncounterDate', 'EncounterPatient']}),
        ('Encounter',           {'fields':[ 'EncounterSeeingPhysician',
                                            'EncounterPatientComplaints',
                                            'EncounterVitalSigns',
                                            'EncounterDiagnosis',
                                            'EncounterTreatmentPlan',
                                            'EncounterReferrals',
                                            'EncounterFollowup',
                                            'EncounterNotes']})
    ]
    list_display = ('id','EncounterDate','EncounterPatient','EncounterSeeingPhysician')
    inlines = [PharmacyOrderInline,LabOrderInline]
    
admin.site.register(Patient,PatientAdmin)
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(PatientEncounter, PatientEncounterAdmin)
admin.site.register(Medication)
#admin.site.register(PatientPrescribedMedication)
#admin.site.register(PharmacyOrder)
#admin.site.register(LabOrder)
