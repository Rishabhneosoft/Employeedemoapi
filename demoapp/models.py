from django.db import models


STATE_CHOICE=((
    ('WFH','WFH'),
    ('WFO','WFO'),

))

class Employee(models.Model):
    name= models.CharField(max_length=100)
    email = models.EmailField()
    dob = models.DateField(auto_now=False, auto_now_add=False)
    # address = models.ForeignKey('demoapp.Address', null=True, on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
    state = models.CharField(choices=STATE_CHOICE, max_length=100)
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Items(models.Model):
    item_name= models.CharField(max_length=100)

    def __str__(self):
        return self.item_name

class AssignedItem(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    assign_items = models.ForeignKey(Items,on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.employee
# class Address(models.Model):
#     state = models.CharField(max_length=50)
#     district = models.CharField(max_length=50)
#     landmark = models.CharField(max_length=50)
#     country = models.CharField(max_length=50)
