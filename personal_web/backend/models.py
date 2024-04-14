from django.db import models
category_choices={
    "python":"Python Projects",
    "web":"Web Development Projects",
}
subcategory_choices={
    "backend":"Back End",
    "frontend":"Front End",
    "full":"Full-stack",
    "arcade":"Arcade",
    "gui":"GUI",
    "python_script":"Python Scripting",
    "datascience":"Data Science",
    "other":"Other",
    "web":"Python Web",
}
# Create your models here.
class Project(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=500)
    category=models.CharField(max_length=50,choices=category_choices)
    subcategory=models.CharField(max_length=50,choices=subcategory_choices)
    example_link=models.URLField()
    github_link=models.URLField()
    picture=models.CharField(max_length=500)

    def __str__(self):
        return self.name