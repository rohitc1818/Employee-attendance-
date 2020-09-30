"""dproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url,include
from django.urls import path
from dApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view),
    path('about/',views.about_view),
    path('contact/',views.contact_view),
    path('dash/',views.dashboard_view),
    url(r'^accounts/',include('django.contrib.auth.urls')),
    path('logout/',views.logout_view),
    path('employee1/',views.Employee_view),
    path('employee2/',views.EmployeeDetail_view),
    path('update/<int:pk>',views.update_view),
    path('delete/<int:pk>',views.delete_view),
    path('attendance1/',views.Attendance_view),
    path('attendance2/',views.AttendanceDetail_view),
    path('a_delete/<int:pk>',views.adelete_view),
]
