from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from runningTime import views

urlpatterns = [
    path('running_time/', views.get_running_time),
]

urlpatterns = format_suffix_patterns(urlpatterns)
