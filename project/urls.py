# project/urls.py
from django.contrib import admin
from django.urls import path, include
import user.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user.views.login, name='login'),
    path('app/', include('app.urls')),
    path('user/', include('user.urls')),
]
