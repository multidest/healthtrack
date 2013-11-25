from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, Permission

class Patient(models.Model):
    PatientName = models.CharField('name', max_length = 45)
    PatientPhone = models.CharField('phone number', max_length = 45)
    PatientAddress = models.CharField('address', max_length = 100)
    PatientDOB =  models.DateField('date of birth')
    GENDER_CHOICES = (
            (u'M',u'Male'),
            (u'F',u'Female'),
            )
    PatientGender = models.CharField('gender', max_length = 2, choices=GENDER_CHOICES)
    PatientPrimaryPhysician = models.ForeignKey(User, verbose_name="primary physician")
    PatientInsuranceInfo = models.CharField('insurance info',max_length = 100)
    def __unicode__(self):
        return self.PatientName

class Appointment(models.Model):
    AppointmentDate = models.DateTimeField('date')
    AppointmentWithPatient = models.ForeignKey(Patient,verbose_name="patient")
    AppointmentWithPhysician = models.ForeignKey(User, verbose_name="physician")
    def __unicode__(self):
        return str(self.id)

class PatientEncounter(models.Model):
    EncounterDate = models.DateTimeField('date')
    EncounterPatientComplaints = models.CharField('complaints',max_length = 500)
    EncounterSeeingPhysician = models.ForeignKey(User, verbose_name="physician")
    EncounterPatient = models.ForeignKey(Patient, verbose_name="patient")
    EncounterVitalSigns = models.CharField('vital signs',max_length = 100)
    EncounterNotes = models.CharField('notes',max_length = 100)
    EncounterDiagnosis = models.CharField('diagnosis', max_length = 100)
    EncounterTreatmentPlan = models.CharField('treatment plan',max_length = 100)
    EncounterReferrals = models.CharField('referrals',max_length = 100)
    EncounterFollowup = models.CharField('Followup',max_length = 100)
    def __unicode__(self):
        return str(self.id)

class Medication(models.Model):
    MedicationName = models.CharField('medication name',max_length = 100)
    def __unicode__(self):
        return self.MedicationName

class PatientPrescribedMedication(models.Model):
    PatientID = models.ForeignKey(Patient, verbose_name="patient")
#    PatientEncounter_Encounter = models.ForeignKey(PatientEncounter, verbose_name="medical encounter")
    MedicationID = models.ForeignKey(Medication, verbose_name="medication name")
    def __unicode__(self):
        return str(self.MedicationID.MedicationName)

class PharmacyOrder(models.Model):
    PatientEncounterID = models.ForeignKey(PatientEncounter)

class LabOrder(models.Model):
    PatientEncounterID = models.ForeignKey(PatientEncounter)










