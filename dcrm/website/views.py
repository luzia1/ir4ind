from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm, AddStationForm, AddProjectForm, AddTaskForm, AddHologramForm
from .models import Record, Employee, WorkStation, Project, Detection, Task, Hologram, Metadata

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

#WORKSTATION VIEWS

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
        workstation_detail = WorkStation.objects.get(work_station_id=pk)
        return render(request, 'workstation_detail.html', {'workstation_detail':workstation_detail})
    else:
        messages.success(request, "You Have Be Logged to see that page!")
        return redirect('workstation')

def update_workstation(request, pk):
	if request.user.is_authenticated:
		current_workstation = WorkStation.objects.get(work_station_id=pk)
		form = AddStationForm(request.POST or None, instance=current_workstation)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Has Been Updated!")
			return redirect('workstation')
		return render(request, 'update_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('workstation')
	
def delete_workstation(request, pk):
	if request.user.is_authenticated:
		delete_it = WorkStation.objects.get(work_station_id=pk)
		delete_it.delete()
		messages.success(request, "Record Deleted Successfully...")
		return redirect('workstation')
	else:
		messages.success(request, "You Must Be Logged In To Do That...")
		return redirect('workstation')

#PROJECT VIEWS
def add_project(request):
	form = AddProjectForm(request.POST, request.FILES or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_project = form.save()
				messages.success(request, "Project Added...")
				return redirect('project')
		return render(request, 'add_project.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('project')

def project(request):
    projects = Project.objects.all()

    #Check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, '"You have Been Logged In')
            return redirect('project')
        else: 
            messages.success(request, "There Was An Error Logging In, Please Try Again")
            return redirect('project')
    else:
        return render(request, 'project.html', {'projects':projects})
    
def project_detail(request, pk):
    if request.user.is_authenticated:
        #Look up records
        project_detail = Project.objects.get(project_id=pk)
        return render(request, 'project_detail.html', {'project_detail':project_detail})
    else:
        messages.success(request, "You Have Be Logged to see that page!")
        return redirect('project')

def update_project(request, pk):
	if request.user.is_authenticated:
		current_project = Project.objects.get(project_id=pk)
		form = AddProjectForm(request.POST or None, instance=current_project)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Has Been Updated!")
			return redirect('project')
		return render(request, 'update_project.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('project')
	
def delete_project(request, pk):
	if request.user.is_authenticated:
		delete_it = Project.objects.get(project_id=pk)
		delete_it.delete()
		messages.success(request, "Record Deleted Successfully...")
		return redirect('project')
	else:
		messages.success(request, "You Must Be Logged In To Do That...")
		return redirect('project')
	
#TASK VIEWS

def add_task(request):
	form = AddTaskForm(request.POST, request.FILES or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				
				add_task = form.save()
				messages.success(request, "Task Added...")
				return redirect('task')
		return render(request, 'add_task.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('hologram')
	
def task(request):
    tasks = Task.objects.all()

    #Check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, '"You have Been Logged In')
            return redirect('task')
        else: 
            messages.success(request, "There Was An Error Logging In, Please Try Again")
            return redirect('task')
    else:
        return render(request, 'task.html', {'tasks':tasks})
    
def task_detail(request, pk):
    if request.user.is_authenticated:
        #Look up records
        task_detail = Task.objects.get(task_id=pk)
        return render(request, 'task_detail.html', {'task_detail':task_detail})
    else:
        messages.success(request, "You Have Be Logged to see that page!")
        return redirect('task')
    
#HOLOGRAMA VIEWS

def add_hologram(request):
	form = AddHologramForm(request.POST, request.FILES or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				hologram.position = "0,0,0"  # Set the default value for the 'position' field
				add_hologram = form.save()
				messages.success(request, "Record Added...")
				return redirect('hologram')
		return render(request, 'add_hologram.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('hologram')

def hologram(request):
    holograms = Hologram.objects.all()

    #Check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, '"You have Been Logged In')
            return redirect('task')
        else: 
            messages.success(request, "There Was An Error Logging In, Please Try Again")
            return redirect('hologram')
    else:
        return render(request, 'hologram.html', {'holograms':holograms})

def dashboard(request):
	return render(request, 'dashboard.html')