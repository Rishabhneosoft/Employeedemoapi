from rest_framework import serializers
from .models import Employee, Items, AssignedItem

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = '__all__'

class AssignedSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignedItem
        fields = '__all__'

# yesterday = create ngrok local url,create django project database design in Employee app
# today =  create Empolyee apis, ItemSerializer
