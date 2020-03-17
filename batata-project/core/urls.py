from django.urls import include, path
from core import views

urlpatterns = [
    path('persons/', views.snippet_list),
    path('persons/<int:pk>/', views.snippet_detail),
]