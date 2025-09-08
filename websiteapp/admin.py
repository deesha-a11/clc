from django.contrib import admin
from .models import Workshopattendees, SampleEntry, WorkshopEntry


@admin.register(Workshopattendees)
class WorkshopattendeesAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "email",
        "whatsapp",
        "workshop_date",
        "referral_source",
        "language",
        "background",
        "career_goal",
        "ai_experience",
        "consent",
        "submitted_at",
    )
    list_filter = ("workshop_date", "language", "referral_source", "consent")
    search_fields = ("full_name", "email", "whatsapp", "background", "career_goal")
    ordering = ("-submitted_at",)


@admin.register(SampleEntry)
class SampleEntryAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")


@admin.register(WorkshopEntry)
class WorkshopEntryAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "email",
        "whatsapp",
        "workshop_date",
        "referral_source",
        "language",
        "background",
        "career_goal",
        "ai_experience",
        "consent",
        "submitted_at",
    )
    list_filter = ("workshop_date", "language", "referral_source", "consent")
    search_fields = ("full_name", "email", "whatsapp", "background", "career_goal")
    ordering = ("-submitted_at",)
