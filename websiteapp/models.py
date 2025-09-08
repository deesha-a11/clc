from django.db import models

# Create your models here.
from django.db import models

class WorkshopEntry(models.Model):   # changed name
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    whatsapp = models.CharField(max_length=20)
    referral_source = models.CharField(max_length=50, blank=True, null=True)
    language = models.CharField(max_length=50, blank=True, null=True)
    background = models.CharField(max_length=200)
    workshop_date = models.CharField(max_length=100)
    career_goal = models.CharField(max_length=100, blank=True, null=True)
    ai_experience = models.CharField(max_length=10, blank=True, null=True)
    consent = models.BooleanField(default=False)
    submitted_at = models.DateTimeField(auto_now_add=True)
    workshop_attended=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.full_name} - {self.workshop_date}"




class SampleEntry(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    








class Workshopattendees(models.Model):   # changed name
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    whatsapp = models.CharField(max_length=20)
    referral_source = models.CharField(max_length=50, blank=True, null=True)
    language = models.CharField(max_length=50, blank=True, null=True)
    background = models.CharField(max_length=200)
    workshop_date = models.CharField(max_length=100)
    career_goal = models.CharField(max_length=100, blank=True, null=True)
    ai_experience = models.CharField(max_length=10, blank=True, null=True)
    consent = models.BooleanField(default=False)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.workshop_date}"
