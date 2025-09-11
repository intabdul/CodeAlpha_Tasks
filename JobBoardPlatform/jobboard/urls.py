from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to the Job Board Platform!</h1>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('jobs.urls')),  
    
    # Homepage will open directly at /
    path('', home, name='home'),
]
