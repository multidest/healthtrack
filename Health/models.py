from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, Permission

class Physician(models.Model):
    PhysicianName = models.CharField(max_length= 45)
    userid = models.ForeignKey(User)
    def __unicode__(self):
        return str(self.id)+ " " + self.PhysicianName

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
    PatientPrimaryPhysician = models.ForeignKey(Physician,verbose_name="primary physician")
    def __unicode__(self):
        return str(self.id) + " " + self.PatientName

class Appointment(models.Model):
    AppointmentDate = models.DateTimeField()
    AppointmentWithPatient = models.ForeignKey(Patient)
    AppointmentWithPhysician = models.ForeignKey(Physician)
    #AppointmentCreatedBy = models.ForeignKey(User)
    def __unicode__(self):
        return str(self.id)

class Patient_has_encounter(models.Model):
    EncounterDate = models.DateTimeField()
    #EncounterCreatedBy = models.ForeignKey(User)
    EncounterPatientComplaints = models.CharField(max_length = 500)
    EncounterSeeingPhysician = models.ForeignKey(Physician)
    EncounterPatient = models.ForeignKey(Patient)
    EncounterVitalSigns = models.CharField(max_length = 100)
    EncounterNotes = models.CharField(max_length = 100)
    EncounterDiagnosis = models.CharField(max_length = 100)
    EncounterTreatmentPlan = models.CharField(max_length = 100)
    EncounterReferrals = models.CharField(max_length = 100)
    def __unicode__(self):
        return str(self.id)

class Medication(models.Model):
    MedicationName = models.CharField(max_length = 100)

class Patient_prescribed_medication(models.Model):
    PatientID = models.ForeignKey(Patient)
    Patient_has_encounter_Encounter = models.ForeignKey(Patient_has_encounter)
    MedicationID = models.ForeignKey(Medication)

class PharmacyOrder(models.Model):
    Patient_has_encounterID = models.ForeignKey(Patient_has_encounter)

class LabOrder(models.Model):
    Patient_has_encounterID = models.ForeignKey(Patient_has_encounter)










