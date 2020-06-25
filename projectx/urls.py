
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('postandcomment.urls')),
    path('', include('user_info.urls')),
]
