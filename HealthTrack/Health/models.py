from django.db import models
from django.utils import timezone

# Create your models here.


class User(models.Model):
    Username = models.CharField(max_length = 45)
    Password = models.CharField(max_length = 45)

    def __unicode__(self):
        return self.id

class Physician(models.Model):
    PhysicianName = models.CharField(max_length= 45)
    UserTable_user_id = models.ForeignKey(User)

    def __unicode__(self):
        return self.id

class Patient(models.Model):
    PatientName = models.CharField(max_length = 45)
    PatientPhone = models.CharField(max_length = 45)
    PatientAddress = models.CharField(max_length = 100)
    PatientDOB =  models.DateField('date of birth')
    PatientGender = models.CharField(max_length = 10)
    PatientPrimaryPhysician = models.ForeignKey(Physician)

    def __unicode__(self):
        return self.id

class Appointment(models.Model):
    AppointmentDate = models.DateField()
    AppointmentWithPatient = models.ForeignKey(Patient)
    AppointmentWithPhysician = models.ForeignKey(Physician)
    AppointmentCreatedBy = models.ForeignKey(User)

    def __unicode__(self):
        return self.id

class Patient_has_encounter(models.Model):
    EncounterDate = models.DateTimeField('datetime of appointment')
    EncounterCreatedBy = models.ForeignKey(User)
    EncounterPatientComplaints = models.CharField(max_length = 500)
    EncounterSeeingPhysician = models.ForeignKey(Physician)
    EncounterPatient = models.ForeignKey(Patient)
    EncounterVitalSigns = models.CharField(max_length = 100)
    EncounterNotes = models.CharField(max_length = 100)
    EncounterDiagnosis = models.CharField(max_length = 100)
    EncounterTreatmentPlan = models.CharField(max_length = 100)
    EncounterReferrals = models.CharField(max_length = 100)

    def __unicode__(self):
        return self.id


class Medication(models.Model):
    MedicationName = models.CharField(max_length = 100)

    def __unicode__(self):
        return self.id

class Patient_prescribed_medication(models.Model):
    PatientID = models.ForeignKey(Patient)
    Patient_has_encounter_Encounter = models.ForeignKey(Patient_has_encounter)
    MedicationID = models.ForeignKey(Medication)

    def __unicode__(self):
        return self.id

class PharmacyOrder(models.Model):
    Patient_has_encounterID = models.ForeignKey(Patient_has_encounter)

    def __unicode__(self):
        return self.id

class LabOrder(models.Model):
    Patient_has_encounterID = models.ForeignKey(Patient_has_encounter)

    def __unicode__(self):
        return self.id









