from rest_framework import serializers
from .models import Employer, Candidate, JobListing, Application

class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = "__all__"

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = "__all__"

class JobListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobListing
        fields = "__all__"

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = "__all__"
