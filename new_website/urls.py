"""new_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from my_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.welcome),
    path('search/', views.search),
    path('employee/create/', views.EmployeeCreate.as_view()),
    path('position/create/', views.PositionCreate.as_view()),
    path('department/create/', views.DepartmentCreate.as_view()),
    path('employees/', views.AllEmployees.as_view(), name='all_employees'),
    path('departments/', views.AllDeps.as_view(), name="all_departments"),
    path('delete_emp/<int:pk>/', views.EmpDelete.as_view()),
    path('detail_emp/<int:pk>/', views.EmpDetail.as_view()),
    path('update_emp/<int:pk>/', views.EmpUpdate.as_view()),
    path('detail_dep/<int:pk>/', views.DepDetail.as_view()),
    path('update_dep/<int:pk>/', views.DepUpdate.as_view()),
    path('employees/filter/<int:pk>/', views.filter_employees),





    
]
