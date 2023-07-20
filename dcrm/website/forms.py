from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record, CurrentState, Role, Employee, WorkStation, Project, Priority, Detection, Metadata, Task, Hologram

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}) )

    class Meta:
        model= User
        fields= ('username', 'first_name', 'last_name', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
            super(SignUpForm, self).__init__(*args, **kwargs)
                
            self.fields['username'].widget.attrs['class'] = 'form-control'
            self.fields['username'].widget.attrs['placeholder'] = 'User Name'
            self.fields['username'].label = ''
            self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

            self.fields['password1'].widget.attrs['class'] = 'form-control'
            self.fields['password1'].widget.attrs['placeholder'] = 'Password'
            self.fields['password1'].label = ''
            self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

            self.fields['password2'].widget.attrs['class'] = 'form-control'
            self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
            self.fields['password2'].label = ''
            self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'
        
# Create Add Record Form
class AddRecordForm(forms.ModelForm):
    employee_id = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control"}), label="Employee ID")
    current_state = forms.ModelChoiceField(queryset=CurrentState.objects.all(), required=True, widget=forms.widgets.Select(attrs={"class":"form-control"}), label="Select Current State")
    role = forms.ModelChoiceField(queryset=Role.objects.all(), required=True, widget=forms.widgets.Select(attrs={"class":"form-control"}), label="Select Role")
    name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control"}), label="Name")
    mobile_number = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control"}), label="Mobile Number")
    email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control"}), label="Email")
    password = forms.CharField(required=True, widget=forms.widgets.PasswordInput(attrs={"class":"form-control"}), label="Password")
    birth_date = forms.DateField(required=True, widget=forms.widgets.DateInput(attrs={"class":"form-control datepicker"}), label="Birth Date")
    localization = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control"}), label="Localization")

    class Meta:
        model = Employee
        exclude = ("user",)
        
        widgets = {
            "birth_date": forms.DateInput(attrs={"class": "form-control datepicker"}),
        }

        # Adicione um script no cabeçalho do formulário
        class Media:
            js = ("https://code.jquery.com/ui/1.12.1/jquery-ui.js",)


# Create Add Record Form
class AddStationForm(forms.ModelForm):
    work_station_id = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control"}), label="Work Station ID")
    name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control"}), label="Name")
    description = forms.CharField(widget=forms.widgets.Textarea(attrs={"class":"form-control"}), label="Description")
    qrcode = forms.ImageField(required=False, label="QR Code")
    
    class Meta:
        model = WorkStation
        exclude = ("user",)
        

# Create Add Project Form
class AddProjectForm(forms.ModelForm):
    project_id = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={"class": "form-control"}), label="Project ID")
    name = forms.CharField(max_length=255, widget=forms.widgets.TextInput(attrs={"class": "form-control"}), label="Name")
    employee = forms.ModelChoiceField(queryset=Employee.objects.filter(role__role_id=1), widget=forms.widgets.Select(attrs={"class": "form-control"}), label="Responsible Employee")
    assistent_remote = forms.CharField(max_length=255, widget=forms.widgets.TextInput(attrs={"class": "form-control"}), label="Email for Remote Assistant")
    work_station = forms.ModelChoiceField(queryset=WorkStation.objects.all(), widget=forms.widgets.Select(attrs={"class": "form-control"}), label="Work Station")
    start_date = forms.DateField(widget=forms.widgets.DateInput(attrs={"class": "form-control", "type": "date"}), label="Start Date")
    end_date = forms.DateField(widget=forms.widgets.DateInput(attrs={"class": "form-control", "type": "date"}), label="End Date")
    tutorial = forms.FileField(required=False, label="Tutorial Video", widget=forms.ClearableFileInput(attrs={"class": "form-control"}))
    description = forms.CharField(widget=forms.widgets.Textarea(attrs={"class": "form-control"}), label="Description")

    class Meta:
        model = Project
        fields = "__all__"  # Use this instead of exclude if you want all fields from the model
    
    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")

        if start_date and end_date and start_date > end_date:
            raise forms.ValidationError("Start date must be before end date.")

        return cleaned_data
    
# Create Add Task Form


class AddTaskForm(forms.ModelForm):
    task_id = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={"class": "form-control"}), label="Task ID")
    name = forms.CharField(max_length=255, widget=forms.widgets.TextInput(attrs={"class": "form-control"}), label="Name")
    priority = forms.ModelChoiceField(queryset=Priority.objects.all(), widget=forms.widgets.Select(attrs={"class": "form-control"}), label="Priority")
    project = forms.ModelChoiceField(queryset=Project.objects.all(), widget=forms.widgets.Select(attrs={"class": "form-control"}), label="Project")
    detection = forms.ModelChoiceField(queryset=Detection.objects.all(), widget=forms.widgets.Select(attrs={"class": "form-control"}), label="Detection")
    employee = forms.ModelChoiceField(queryset=Employee.objects.filter(role__role_id=2), widget=forms.widgets.Select(attrs={"class": "form-control"}), label="Employee")
    holograms = forms.ModelMultipleChoiceField(
        queryset=Hologram.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}),
        required=False
    )

    class Meta:
        model = Task
        exclude = ('completed',)
        fields = "__all__"
      
class AddHologramForm(forms.ModelForm):
 class Meta:
        model = Hologram
        exclude = ('position',)  # Exclude the 'position' field from the form fields
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
 obj = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}), label="Upload File")