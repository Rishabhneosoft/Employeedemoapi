# from django.urls import path, include
# from .views import *


# urlpatterns = [


    
#     path('item/create/', ItemAPI.as_view(), name='item-create'),
#     path('assigned/item/', EmployeeAssignAPI.as_view(), name='assigned-item'),

#     path('employee/create/', EmployeeAPI.as_view(), name='employee-create'),
#     path('employee/update/<int:pk>/', EmployeeUpdate.as_view(), name='employee-update'),
#     path('employee/delete/<int:pk>/', EmployeeDeleteView.as_view(), name='employee-delete'),

# ]

from django.contrib import admin
from django.urls import path, include
from . import views;

urlpatterns = [
    path('', views.index , name='index'),
    path('signup/', views.signup, name="Signup"),
    # path('', Index.as_view(), name='homepage'),
    path('login/', views.Userlogin, name="Login"),
]