from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm, AddStationForm
from .models import Record, Employee, WorkStation

# Create your views here.
def employee(request):
    employees = Employee.objects.all()

    #Check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, '"You have Been Logged In')
            return redirect('employee')
        else: 
            messages.success(request, "There Was An Error Logging In, Please Try Again")
            return redirect('employee')
    else:
        return render(request, 'employee.html', {'employees':employees})


def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out")
    return redirect('employee')


def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('employee')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})


def employee_detail(request, pk):
    if request.user.is_authenticated:
        #Look up records
        employee_detail = Employee.objects.get(employee_id=pk)
        return render(request, 'employee_detail.html', {'employee_detail':employee_detail})
    else:
        messages.success(request, "You Have Be Logged to see that page!")
        return redirect('employee')
    
def delete_employee(request, pk):
	if request.user.is_authenticated:
		delete_it = Employee.objects.get(employee_id=pk)
		delete_it.delete()
		messages.success(request, "Record Deleted Successfully...")
		return redirect('employee')
	else:
		messages.success(request, "You Must Be Logged In To Do That...")
		return redirect('employee')

def add_employee(request):
	form = AddRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_employee = form.save()
				messages.success(request, "Record Added...")
				return redirect('employee')
		return render(request, 'add_employee.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('employee')


def update_record(request, pk):
	if request.user.is_authenticated:
		current_record = Employee.objects.get(employee_id=pk)
		form = AddRecordForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Has Been Updated!")
			return redirect('employee')
		return render(request, 'update_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('employee')


def add_workstation(request):
	form = AddStationForm(request.POST, request.FILES or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_workstation = form.save()
				messages.success(request, "Record Added...")
				return redirect('workstation')
		return render(request, 'add_workstation.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('workstation')

def workstation(request):
    workstations = WorkStation.objects.all()

    #Check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, '"You have Been Logged In')
            return redirect('workstation')
        else: 
            messages.success(request, "There Was An Error Logging In, Please Try Again")
            return redirect('workstation')
    else:
        return render(request, 'workstation.html', {'workstations':workstations})
    
def workstation_detail(request, pk):
    if request.user.is_authenticated:
        #Look up records
        employee_detail = Employee.objects.get(employee_id=pk)
        return render(request, 'workstation_detail.html', {'workstation_detail':employee_detail})
    else:
        messages.success(request, "You Have Be Logged to see that page!")
        return redirect('workstation')
