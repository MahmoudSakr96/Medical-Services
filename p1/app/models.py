from django.db import models

# Create your models here.
class login (models.Model):
    userEmail = models.EmailField()
    userpass = models.CharField(max_length=50)

class userdata (models.Model):

    username = models.CharField(max_length=50)
    usernumber = models.IntegerField()
    useremail = models.EmailField()
    gender = models.CharField(max_length=128)
    userdate = models.DateField()
    userpassword = models.CharField(max_length=20)

class hospitaldata (models.Model):
    hospitalname = models.CharField(max_length=50)
    hospitalemail = models.EmailField()
    EmergencyNumber = models.IntegerField()
    Emergencycount = models.IntegerField()
    location = models.CharField(max_length=50)
    image = models.ImageField()
    hospitalpassword = models.CharField(max_length=20)
class contactldata (models.Model):
    contactalname = models.CharField(max_length=50)
    contactemail = models.EmailField()
    contactsubject = models.CharField(max_length=50)
    contactmassage = models.CharField(max_length=50)

class hospitaldata2 (models.Model):
    deptname = models.CharField(max_length=50, default='null')
    deptdescription = models.CharField(max_length=150 ,default='null')
    # hospitalname = models.ForeignKey(hospitaldata, on_delete=models.CASCADE ,default='null')



