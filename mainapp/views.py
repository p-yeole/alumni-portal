from django.shortcuts import render, redirect
from .forms import UserRegisterForm, JobCreateForm, EventCreateForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .models import Event, Job
from django.contrib.auth.decorators import login_required


def home_page(request):
    return render(request, 'mainapp/home.html', {'title': 'Home'})

def createNew(request):
    return render(request, 'mainapp/createNew.html', {'title': 'Create New'})

def events(request):
    events = Event.objects.all()
    eventContext = []
    for event in events:
        eventContext.append({
            'name' : event.name,
            'schedule' : event.schedule,
            'description' : event.description,
            'url' : event.event_image
        })
    return render(request, 'mainapp/events.html', {'title': 'Events', 'events' : eventContext})

def jobs(request):
    jobs = Job.objects.all()
    jobContext = []
    for job in jobs:
        jobContext.append({
            'company' : job.company,
            'title' : job.title,
            'description' : job.description,
            'location' : job.location,
            'ctc' : job.ctc,
            'mailto' : job.mailto
        })
    return render(request, 'mainapp/jobs.html', {'title': 'Jobs', 'jobs' : jobContext})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.name = form.cleaned_data.get('name')
            user.profile.email_id = form.cleaned_data.get('email_id')
            user.profile.phone = form.cleaned_data.get('phone')
            user.profile.designation = form.cleaned_data.get('designation')
            user.profile.company = form.cleaned_data.get('company')
            user.profile.branch = form.cleaned_data.get('branch')
            user.profile.image_url = form.cleaned_data.get('image_url')
            user.profile.registration_no = form.cleaned_data.get('registration_no')
            user.profile.passing_year = form.cleaned_data.get('passing_year')
            user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            messages.success(request, f'Account created for {username}!')
            login(request, user)
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'mainapp/register.html', {'form': form, 'title': 'Register'})

@login_required
def createJob(request):
    if request.method == 'POST':
        form = JobCreateForm(request.POST)
        if form.is_valid():
            job = form.save()
            job.save()
            return redirect('home-page')

    else:
        form = JobCreateForm()
    return render(request, 'mainapp/createJob.html', {'form' : form, 'title' : 'Add a Job!'})

@login_required
def createEvent(request):
    if request.method == 'POST':
        form = EventCreateForm(request.POST)
        if form.is_valid():
            event = form.save()
            event.save()
            return redirect('home-page')

    else:
        form = EventCreateForm()
    return render(request, 'mainapp/createEvent.html', {'form' : form, 'title' : 'Add an Event!'})