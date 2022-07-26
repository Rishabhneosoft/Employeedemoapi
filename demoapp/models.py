from django.db import models


STATE_CHOICE=((
    ('WFH','WFH'),
    ('WFO','WFO'),

))

class Employee(models.Model):
    name= models.CharField(max_length=100)
    email = models.EmailField()
    dob = models.DateField(auto_now=False, auto_now_add=False)
    address = models.TextField(max_length=100)
    state = models.CharField(choices=STATE_CHOICE, max_length=100)
    gender = models.TextField(max_length=10)
