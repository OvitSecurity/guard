from django.db import models
from django.utils import timezone
from datetime import date


class Guard(models.Model):
    name = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.EmailField(null=True)
    telephone = models.PositiveIntegerField(max_length=12)
    am = models.PositiveIntegerField(max_length=8)
    birthdate = models.DateField(null=True)
    fathersname = models.CharField(max_length=20,null=True)
    fatherslastname = models.CharField(max_length=20,null=True)
    mothersname = models.CharField(max_length=20,null=True)
    motherslastname = models.CharField(max_length=20,null=True)
    MARITAL_STATUS = (('m', 'Married'), ('d', 'Divorced'),('u', 'Unmarried'))
    marital = models.CharField(max_length=1, choices= MARITAL_STATUS, default='u')
    childs = models.SmallIntegerField(max_length=1)
    address = models.CharField(max_length=200, null=True)
    identity = models.CharField(max_length=20,null=True)
    amka = models.CharField(max_length=40,null=True)
    ama = models.CharField(max_length=40,null=True)
    afm = models.CharField(max_length=40,null=True)
    license_issue_date = models.DateField(null=True)
    height = models.IntegerField(max_length=3)
    weight = models.IntegerField(max_length=3)
    shoe = models.IntegerField(max_length=2)
    GENDER = (('m','Men'), ("f", "Female"))
    gender = models.CharField(max_length=1, choices=GENDER, null=False, default='m')




    created_date = models.DateTimeField(
            default=timezone.now)




    def __unicode__(self):
        return self.lastname

    def age(self):
        import datetime
        return int((datetime.date.today() - self.birthdate).days / 365.25)
    age = property(age)

