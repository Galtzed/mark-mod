from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Real Models

#model
class Project(models.Model):
    name = models.CharField(max_length = 100)
    final_mark = models.DecimalField(decimal_places = 3,max_digits = 10, blank = True, null = True)
    student = models.ForeignKey(User, on_delete = models.CASCADE,null = True)

class ProjectManagement(models.Model):
    project = models.ForeignKey(Project, related_name='management', on_delete = models.CASCADE,null = True)
    academic = models.ForeignKey(User, on_delete = models.CASCADE,null = True)
    personal_mark = models.DecimalField(decimal_places = 3,max_digits = 10, blank = True, null = True)