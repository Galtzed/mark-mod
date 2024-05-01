from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from .models import *
from .serializer import *
from rest_framework import status
from rest_framework.response import Response
# Create your views here.

##convener views
class UserListView(APIView):
    serializer_class = UserSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    #view db convener only
    def get(self,request):
        try:
            users = User.objects.all()
        except User.DoesNotExist:
            return Response({"message":"User Not Found"},status=status.HTTP_204_NO_CONTENT)
        output = [(UserSerializer(output).data) for output in users]
        return Response(output)
    
    #add to db convener only
    def post(self,request):
        serialiser = UserSerializer(data=request.data)
        if serialiser.is_valid(raise_exception=True):
            serialiser.save()
            return Response(serialiser.data)
            
class UserView(APIView):
    serializer_class = UserSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    #view record all => themselves + converner
    def get(self,request,pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({"message":"User Not Found"},status=status.HTTP_204_NO_CONTENT)
        serialiser = UserSerializer(user)
        return Response(serialiser.data)
    
    #delete record converner only
    def delete(self,request,pk):
        try:
            user = User.objects.get(pk=pk)
            user.delete()
        except User.DoesNotExist:
            return Response({"message":"User Not Found"},status=status.HTTP_204_NO_CONTENT)
            
    #update record all => themselves + convener
    def put(self,request,pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({"message":"User Not Found"},status=status.HTTP_204_NO_CONTENT)
        serialiser = UserSerializer(user,data=request.data)
        if serialiser.is_valid(raise_exception=True):
            serialiser.save()
            return Response(serialiser.data)
        return Response(serialiser.errors,status=status.HTTP_400_BAD_REQUEST)

class ProjectListView(APIView):
    serializer_class = ProjectSerialzer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    #related only + conveners
    def get(self,request):
        try:
            projects = Project.objects.all()
        except Project.DoesNotExist:
            return Response({"message":"User Not Found"},status=status.HTTP_204_NO_CONTENT)
        output = [(ProjectSerialzer(output).data) for output in projects]
        return Response(output)
    def post(self,request):
        serialiser = ProjectSerialzer(data=request.data)
        if serialiser.is_valid(raise_exception=True):
            serialiser.save()
            return Response(serialiser.data)

class ProjectView(APIView):
    serializer_class = ProjectSerialzer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    #view record all => themselves + converner
    def get(self,request,pk):
        try:
            project = Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            return Response({"message":"Project Not Found"},status=status.HTTP_204_NO_CONTENT)
        serialiser = Project(project)
        return Response(serialiser.data)
    
    #delete record converner only
    def delete(self,request,pk):
        try:
            project = Project.objects.get(pk=pk)
            project.delete()
        except Project.DoesNotExist:
            return Response({"message":"Project Not Found"},status=status.HTTP_204_NO_CONTENT)
            
    #update record all => themselves + convener
    def put(self,request,pk):
        try:
            project = Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            return Response({"message":"Project Not Found"},status=status.HTTP_204_NO_CONTENT)
        serialiser = ProjectSerialzer(project,data=request.data)
        if serialiser.is_valid(raise_exception=True):
            serialiser.save()
            return Response(serialiser.data)
        return Response(serialiser.errors,status=status.HTTP_400_BAD_REQUEST)

class ProjectManagementViewAll(APIView):
    serializer_class = ProjectManageSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self,request):#all allowed
        try:
            projectsm = ProjectManagement.objects.all()
        except ProjectManagement.DoesNotExist:
            return Response({"message":"User Not Found"},status=status.HTTP_204_NO_CONTENT)
        output = [(ProjectManageSerializer(output).data) for output in projectsm]
        return Response(output)
    def post(self,request):#only convener and academics=>(for owned)
        serialiser = ProjectManageSerializer(data=request.data)
        if serialiser.is_valid(raise_exception=True):
            serialiser.save()
            return Response(serialiser.data)
    
#academics 

class AcadProjectManageAll(APIView):
    serializer_class = ProjectManageSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):#all allowed

        try:
            projectsm = ProjectManagement.objects.all().filter(academic = request.user)
        except ProjectManagement.DoesNotExist:
            return Response({"message":"User Not Found"},status=status.HTTP_204_NO_CONTENT)
        output = [(ProjectManageSerializer(output).data) for output in projectsm]
        return Response(output)
        
class AcadProjectManage(APIView):
    serializer_class = ProjectManageSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self,request,pk):#all allowed
        try:
            projectsm = ProjectManagement.objects.all().filter(academic = request.user).filter(pk = pk)
        except ProjectManagement.DoesNotExist:
            return Response({"message":"User Not Found"},status=status.HTTP_204_NO_CONTENT)
        output = [(ProjectManageSerializer(output).data) for output in projectsm]
        return Response(output)
    def put(self,request,pk):#only convener and academics=>(for owned)try:
        try:
            projectm = ProjectManagement.objects.all().filter(academic = request.user).filter(pk = pk)
        except ProjectManagement.DoesNotExist:
            return Response({"message":"User Not Found"},status=status.HTTP_204_NO_CONTENT)
        serialiser = ProjectSerialzer(projectm,data=request.data)
        if serialiser.is_valid(raise_exception=True):
            serialiser.save()
            return Response(serialiser.data)
        return Response(serialiser.errors,status=status.HTTP_400_BAD_REQUEST)

class StuProjectViewAll(APIView):
    serializer_class = ProjectSerialzer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        try:
            projects = Project.objects.all().filter(student = request.user)
        except Project.DoesNotExist:
            return Response({"message":"User Not Found"},status=status.HTTP_204_NO_CONTENT)
        output = [(ProjectSerialzer(output).data) for output in projects]
        return Response(output)
    
class GetGroup(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        output = [{
            group : group.name
            } for group in request.user.groups.all()]
        return Response(output)