from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Job, Event

DEPARTMENTS = (
    ("COMPS","COMPUTER ENGINEERING"),
    ("IT", "INFORMATION TECHNOLOGY ENGINEERING"),
    ("EXTC", "ELECTRONICS AND TELECOMMUNICATION ENGINEERING"),
    ("ETRX","ELECTRONICS ENGINEERING"),
    ("AIDS", "ARTIFICIAL INTELLIGENCE AND DATA SCIENCE ENGINEERING")
)

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    name = forms.CharField(required=True)
    phone = forms.CharField(required=True, max_length=10)
    passing_year = forms.IntegerField(required=True)
    registration_no = forms.IntegerField(required=True)
    branch = forms.ChoiceField(choices=DEPARTMENTS)
    company = forms.CharField(max_length=100)
    designation = forms.CharField(max_length=100)
    image_url = forms.URLField(max_length=500)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
        self.fields['username'].help_text = None

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email', 'name', 'phone', 'passing_year', 'registration_no', 'branch', 'company', 'designation', 'image_url']

class JobCreateForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ('company', 'title', 'location', 'ctc', 'description', 'mailto')

class EventCreateForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'schedule', 'description', 'event_image')