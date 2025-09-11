from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployerViewSet, CandidateViewSet, JobListingViewSet, ApplicationViewSet

router = DefaultRouter()
router.register("employers", EmployerViewSet)
router.register("candidates", CandidateViewSet)
router.register("jobs", JobListingViewSet)
router.register("applications", ApplicationViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
