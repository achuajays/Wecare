from django.db import models

# Create your models here.


class AudioFiles(models.Model):
    audio_file = models.FileField(upload_to='audio/')
    uploaded_at = models.DateTimeField(auto_now_add=True)





class TextFiles(models.Model):
    text_file = models.FileField(upload_to='text/', null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)



class UploadedFiles(models.Model):
    file_upload = models.FileField(upload_to='documents/')




class Doctor(models.Model):
    dname = models.CharField(max_length=100 , default=" ")
    department = models.CharField(max_length=100 , default= " ")
    phno = models.CharField(max_length=12 , default= " ")




class DoctorText(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE , default=" ")
    text_file = models.FileField(upload_to='text/', null=True, blank=True)





class BloodDonation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    blood_group = models.CharField(max_length=5, choices=[
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-')
    ], default='')









class DoctorInfo(models.Model):
    doctor_name = models.CharField(max_length=100)
    do_id = models.IntegerField(default= 1)




class DoctorInfoExtend(models.Model):
    doctor = models.ForeignKey(DoctorInfo, on_delete=models.CASCADE)
    patient = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)
    symptom = models.CharField(max_length=100 , default=" " )






class BugReport(models.Model):
    area = models.CharField(max_length=100 , default=" ")
    title = models.CharField(max_length=100)
    







class Ticket(models.Model):
    title = models.CharField(max_length=100)







