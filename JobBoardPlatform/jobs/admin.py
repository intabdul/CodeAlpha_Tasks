from django.contrib import admin
from .models import Employer, Candidate, JobListing, Application

@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    list_display = ("company_name", "user", "website")

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ("user", "resume")

@admin.register(JobListing)
class JobListingAdmin(admin.ModelAdmin):
    list_display = ("title", "employer", "location", "created_at")
    search_fields = ("title", "location")

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("job", "candidate", "status", "applied_at")
    list_filter = ("status",)
    search_fields = ("job__title", "candidate__user__username")
