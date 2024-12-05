from django.urls import path
from . import views


urlpatterns = [
    path('createjob/', views.create_job, name="create_job"),
]