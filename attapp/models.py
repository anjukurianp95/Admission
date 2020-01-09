from django.db import models

# Create your models here.
class sign(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    password=models.CharField(max_length=10)
    mob=models.IntegerField(max_length=10, null=True, blank=True)

class Meta:
    db_table = 'sign'
    db_table= 'faculty'
    db_table= 'student'
    db_table= 'fac_attendance'
    db_table= 'stud_att'
    db_table= 'mark'
    db_table= 'admin'
    db_table= 'leave'
    db_table= 'sleave'
    db_table= 'timetable'
    db_table= 'satt'
class faculty(models.Model):
    facid=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=50)
    dob=models.DateField()
    gender=models.CharField(max_length=10)
    qualification=models.CharField(max_length=20)
    mobile=models.IntegerField(max_length=10, null=True, blank=True)
    batchincharge=models.CharField(max_length=10)
    email=models.EmailField(max_length=20)
    password=models.CharField(max_length=10)

class student(models.Model):
    stid=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=20,null=True,blank=True)
    admissionno=models.IntegerField(null=True,blank=True)
    admissiondate=models.DateField(null=True,blank=True)
    address=models.CharField(max_length=50,null=True,blank=True)
    dob=models.DateField(null=True,blank=True)
    gender=models.CharField(max_length=10,null=True,blank=True)
    guardian=models.CharField(max_length=20,null=True,blank=True)
    batch=models.CharField(max_length=10,null=True,blank=True)
    mobile=models.IntegerField(max_length=10, null=True, blank=True)
    email=models.EmailField(max_length=20,null=True,blank=True)
    password=models.CharField(max_length=10,null=True,blank=True)

class fac_attendance(models.Model):
    facid=models.IntegerField()
    date=models.DateField()
    status_h1=models.CharField(max_length=5)
    status_h2=models.CharField(max_length=5)
    status_h3=models.CharField(max_length=5)
    status_h4=models.CharField(max_length=5)

class stud_att(models.Model):
    stid=models.IntegerField()
    date=models.DateField()
    status_h1=models.CharField(max_length=5,default='present')
    status_h2=models.CharField(max_length=5,default='present')
    status_h3=models.CharField(max_length=5,default='present')
    status_h4=models.CharField(max_length=5,default='present')

class satt(models.Model):
    stid=models.IntegerField()
    date=models.DateField()
    status=models.BinaryField()

class mark(models.Model):
    stid_id=models.IntegerField()
    assno=models.IntegerField()
    sub1=models.IntegerField()
    sub2=models.IntegerField()
    sub3=models.IntegerField()
    percentage=models.FloatField()
class admin(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=10)


class fleave(models.Model):
    fsid=models.IntegerField()
    fromdate=models.DateField()
    todate=models.DateField()
    reason=models.CharField(max_length=50)
    status=models.CharField(max_length=10)

class sleave(models.Model):
    sid=models.IntegerField()
    fromdate=models.DateField()
    todate=models.DateField()
    reason=models.CharField(max_length=50)
    status=models.CharField(max_length=10)

class timetable(models.Model):
    day=models.CharField(max_length=10)
    batch=models.CharField(max_length=10)
    hour1=models.CharField(max_length=10)
    hour2=models.CharField(max_length=10)
    hour3=models.CharField(max_length=10)
    hour4=models.CharField(max_length=10)


