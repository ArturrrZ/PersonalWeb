from . import views
from django.urls import path

urlpatterns = [
    path("",views.index,name="index"),
    path('projects_python',views.projects_python,name="projects_python"),
    path('projects_web',views.projects_web,name="projects_web")
]