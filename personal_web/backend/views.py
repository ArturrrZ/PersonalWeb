from django.shortcuts import render
from .models import Project
# Create your views here.

def index(request):
    return render(request,"backend/index.html")
def projects_python(request):

    return render(request,"backend/projects_python.html",{
        "projects":Project.objects.all().filter(category="python"),
    })

def projects_web(request):
    return render(request,"backend/projects_web.html",{
        # "projects":Project.objects.all().filter(category="web").order_by("-subcategory"),
        "full":Project.objects.all().filter(subcategory="full").order_by("name"),
        "back": Project.objects.all().filter(subcategory="backend").order_by("name"),
        "front": Project.objects.all().filter(subcategory="frontend").order_by("-name"),

    })