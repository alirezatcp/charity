from django.urls import path

from about_us.views import about_us

urlpatterns = [
    path('', about_us),
]