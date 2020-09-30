from django import forms
from dApp.models import Employee,Attendance

# create your form here
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = '__all__'




