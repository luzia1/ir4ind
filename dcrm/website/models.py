from django.db import models

# Create your models here.

class Record(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	first_name = models.CharField(max_length=50)
	last_name =  models.CharField(max_length=50)
	email =  models.CharField(max_length=100)
	phone = models.CharField(max_length=15)
	address =  models.CharField(max_length=100)
	city =  models.CharField(max_length=50)
	state =  models.CharField(max_length=50)
	zipcode =  models.CharField(max_length=20)

	def __str__(self):
		return(f"{self.first_name} {self.last_name}")
#NOVO
class CurrentState(models.Model):
    current_state_id = models.IntegerField(primary_key=True)
    current_state = models.CharField(max_length=50)

    def __str__(self):
        return self.current_state


class Role(models.Model):
    role_id = models.IntegerField(primary_key=True)
    role = models.CharField(max_length=50)
    
    def __str__(self):
        return self.role

class Employee(models.Model):
    employee_id = models.IntegerField(primary_key=True)
    current_state = models.ForeignKey(CurrentState, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=50)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    birth_date = models.DateField()
    localization = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class WorkStation(models.Model):
    work_station_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    qrcode = models.ImageField(null=True, blank=True, upload_to="images/" )

    def __str__(self):
        return self.name

class Project(models.Model):
    project_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    work_station = models.ForeignKey(WorkStation, on_delete=models.CASCADE)
    assistent_remote = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    tutorial = models.FileField(upload_to='project_videos/', null=True, blank=True)
    description = models.TextField()

class Priority(models.Model):
    priority_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    qrcode = models.TextField(null=True)

class Detection(models.Model):
    detection_id = models.IntegerField(primary_key=True)
    classname = models.CharField(max_length=255)
    detected = models.BooleanField()

class Metadata(models.Model):
    metadata_id = models.IntegerField(primary_key=True)
    request_count = models.IntegerField(null=True)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)

class Hologram(models.Model):
    id = models.AutoField(primary_key=True)
    position = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    obj = models.FileField(upload_to='holograms/', null=True, blank=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    task_id = models.IntegerField(primary_key=True)
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    metadata = models.ForeignKey(Metadata, on_delete=models.CASCADE)
    detection = models.ForeignKey(Detection, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    completed = models.BooleanField()
    holograms = models.ManyToManyField(Hologram, blank=True)

