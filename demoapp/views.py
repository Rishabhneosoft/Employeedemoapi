
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from .models import Employee, Items ,AssignedItem
from .serializers import EmployeeSerializer, ItemSerializer, AssignedSerializer
from rest_framework.response import Response


class ItemAPI(APIView):
    def get(self,request, format=None):
        item = Items.objects.all()
        serializer = ItemSerializer(item,many=True)
        return Response (serializer.data)

    def post(self, request, format=None):
        # employee = Employee.objects.all()
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeAPI(APIView):
    def get(self,request, format=None):
        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee,many=True)
        return Response (serializer.data)

    def post(self, request, format=None):
        # employee = Employee.objects.all()
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    


class EmployeeUpdate(APIView):
    def put(self,request,pk,format=None):
        id = pk
        stu = Employee.objects.get(pk=id)
        serializer = EmployeeSerializer(stu,data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            # return Response(serializer.data, status=status.HTTP_200_SUCCESS)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

           
        
                
class EmployeeDeleteView(APIView):        
    def delete(self, request,pk,format=None):
        id = pk
        employee_obj = Employee.objects.get(pk=id)
        employee_obj.delete()
        return Response({"msg":"Deleted"},status=status.HTTP_200_OK)


class EmployeeAssignAPI(APIView):
    def get(self,request, format=None):
        employee = AssignedItem.objects.all()
        serializer = AssignedSerializer(employee,many=True)
        return Response (serializer.data)

    def post(self, request, format=None):
        # employee = Employee.objects.all()
        serializer = AssignedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
