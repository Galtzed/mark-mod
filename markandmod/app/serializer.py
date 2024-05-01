from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

#user info no password
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['pk','username','email','first_name','last_name']

class ProjectManageSerializer(serializers.ModelSerializer):
    academic = UserSerializer()
    class Meta:
        model = ProjectManagement
        fields = ['pk','project','academic',"personal_mark"]

class ProjectSerialzer(serializers.ModelSerializer):
    management = ProjectManageSerializer(many=True)
    student = UserSerializer()
    class Meta:
        model = Project
        fields = ['pk','name','final_mark','student','management']