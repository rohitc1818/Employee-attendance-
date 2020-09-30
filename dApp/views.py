from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from dApp.models import Employee,Attendance
from dApp.forms import EmployeeForm,AttendanceForm
# Create your views here.
def home_view(request):
    return render(request,'dApp/home.html')
def about_view(request):
    return render(request,'dApp/about.html')
def contact_view(request):
    return render(request,'dApp/contact us.html')
@login_required
def dashboard_view(request):
    return render(request,'dApp/dashboard.html')

def logout_view(request):
    return render(request,'dApp/logout.html')

def Employee_view(request):
    form = EmployeeForm
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return redirect('/employee2')
    return render(request,'dApp/employee1.html',{'form':form})

def EmployeeDetail_view(request):
    Employee_list = Employee.objects.all()
    return render(request,'dApp/employee2.html',{'Employee_list':Employee_list})

def delete_view(request,pk):
    employee = Employee.objects.get(pk=pk)
    employee.delete()
    return redirect('/employee2')

def update_view(request,pk):
    employee = Employee.objects.get(id=pk)
    form = EmployeeForm(data=request.POST or None,instance=employee)
    if request.method=='POST':
        if form.is_valid():
            form.save()
        return redirect('/employee2')
    return render(request,'dApp/eupdate.html',{'Employee':form})

def Attendance_view(request):
    form = AttendanceForm
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return redirect('/attendance2')
    return render(request,'dApp/attendance1.html',{'form':form})

def AttendanceDetail_view(request):
    Attendance_list = Attendance.objects.all()
    return render(request,'dApp/attendance2.html',{'Attendance_list':Attendance_list})

def adelete_view(request,pk):
    attendance = Attendance.objects.get(pk=pk)
    attendance.delete()
    return redirect('/attendance2')



# uername:-hh
#pa:-hh1234