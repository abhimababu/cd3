from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TaskSerializers
from .models import Task
from rest_framework.permissions import IsAuthenticatedAllowAny
from django.contrib.auth import get_user_model
from rest_framework.generic import createAPIView
from .serializers import UserSerializers


# Create your views here.
class TaskViewset(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-date_created')
    serializer_class = TaskSerializers


class DueTaskViewset(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-date _created').filter(completed=False)
    serializer_class = TaskSerializers


class CompletedTaskViewset(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-date _created').filter(completed=True)
    serializer_class = TaskSerializers


class TaskViewSet:
    permission_classes = (IsAuthenticated,)


class createUserView(createAPIView):
    model = get_user_model()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializers
