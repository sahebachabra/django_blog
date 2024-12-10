from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('djangoblogsaheba2005.urls')),  # Use the correct app name here
    path('admin/', admin.site.urls),
]
