from django.contrib import admin
from dApp.models import Employee
from dApp.models import Attendance

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['E_no','First_name','Last_name','E_salary','Contact_no','Email','Country','City','Pin_code','Address',]

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['E_no','E_name','In_date','Out_date','Description']

# Register your models here.
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Attendance,AttendanceAdmin)
