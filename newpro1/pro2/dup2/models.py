from django.db import models


class Employee_model(models.Model):
    eid = models.CharField(max_length=20)
    ename = models.CharField(max_length=50)
    eemail = models.EmailField()
    econtact = models.CharField(max_length=50)
    