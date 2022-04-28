from cProfile import Profile
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

DEPARTMENTS = (
    ("COMPS","COMPUTER ENGINEERING"),
    ("IT", "INFORMATION TECHNOLOGY ENGINEERING"),
    ("EXTC", "ELECTRONICS AND TELECOMMUNICATION ENGINEERING"),
    ("ETRX","ELECTRONICS ENGINEERING"),
    ("AIDS", "ARTIFICIAL INTELLIGENCE AND DATA SCIENCE ENGINEERING")
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=0)
    name = models.CharField(max_length=50, default="abc")
    registration_no = models.IntegerField(null=True, unique=True)
    passing_year = models.IntegerField(default=2000)
    phone = models.CharField(max_length=10)
    branch = models.CharField(choices=DEPARTMENTS, max_length=5)
    email_id = models.EmailField(null=True)
    company = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    image_url = models.URLField(max_length=500, default="")

    def __str__(self):
        return self.user.username

class Job(models.Model):
    company = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    ctc = models.IntegerField(null=True, default=0)
    description = models.TextField()
    mailto = models.EmailField(null=True)

    def __str__(self):
        return self.company

class Event(models.Model):
    name = models.CharField(max_length=500)
    schedule = models.DateTimeField()
    description = models.TextField()
    event_image = models.URLField(max_length=500)

    def __str__(self):
        return self.name


@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()