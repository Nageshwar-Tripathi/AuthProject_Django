
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Auth Project"
admin.site.site_title = "Auth Project"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]
