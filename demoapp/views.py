
# import re
# from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework import status
# from .models import Employee, Items ,AssignedItem
# from .serializers import EmployeeSerializer, ItemSerializer, AssignedSerializer
# from rest_framework.response import Response


# class ItemAPI(APIView):
#     def get(self,request, format=None):
#         item = Items.objects.all()
#         serializer = ItemSerializer(item,many=True)
#         return Response (serializer.data)

#     def post(self, request, format=None):
#         # employee = Employee.objects.all()
#         serializer = ItemSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class EmployeeAPI(APIView):
#     def get(self,request, format=None):
#         employee = Employee.objects.all()
#         serializer = EmployeeSerializer(employee,many=True)
#         return Response (serializer.data)

#     def post(self, request, format=None):
#         # employee = Employee.objects.all()
#         serializer = EmployeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    


# class EmployeeUpdate(APIView):
#     def put(self,request,pk,format=None):
#         id = pk
#         stu = Employee.objects.get(pk=id)
#         serializer = EmployeeSerializer(stu,data=request.data)
#         if serializer.is_valid(): 
#             serializer.save()
#             # return Response(serializer.data, status=status.HTTP_200_SUCCESS)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

           
        
                
# class EmployeeDeleteView(APIView):        
#     def delete(self, request,pk,format=None):
#         id = pk
#         employee_obj = Employee.objects.get(pk=id)
#         employee_obj.delete()
#         return Response({"msg":"Deleted"},status=status.HTTP_200_OK)


# class EmployeeAssignAPI(APIView):
#     def get(self,request, format=None):
#         employee = AssignedItem.objects.all()
#         serializer = AssignedSerializer(employee,many=True)
#         return Response (serializer.data)

#     def post(self, request, format=None):
#         # employee = Employee.objects.all()
#         serializer = AssignedSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



import re
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
# from django.contrib.auth import create_user
from demoapp.form import UserRegistrationForm ,UserLoginForm
from django.contrib import messages
from .models import *
from django.contrib.auth import authenticate
# from .forms import *
# from django.contrib.auth.forms import UserLoginForm


def index(request):
    return render(request, "index.html");

def signup(request):
    form = UserRegistrationForm()
    data= {
        'form':form,

    }
    if request.method == 'POST':
        # form = UserRegistrationForm(request.POST)
        # print(form)
        name = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        re_password = request.POST.get('re_password')
        # print(name,username,email,password,re_password)

        if (password != re_password):
            messages.add_message(request, message.INFO, 'password do not match')
        else:
            user = User.objects.create_user(username = username, password= password,email= email,first_name=name)
            if (user.is_active):
                print('register')
            else:
                print('error')

        
    return render (request,"signup.html",context= data)

def Userlogin(request):
    form = UserLoginForm()
    data ={
        'form':form,
    }

    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username, password)
        user=authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            print(user)
            return redirect('Home')
        else:
            return redirect('Login')


    return render(request, "login.html",context=data)
