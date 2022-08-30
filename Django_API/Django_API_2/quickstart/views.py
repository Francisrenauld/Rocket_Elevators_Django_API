from django.shortcuts import render
from DjangoSite.models import Employees
from rest_framework import viewsets
from rest_framework import permissions
from Django_API_2.quickstart.serializers import EmployeesSerializer

class EmployeesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer

    
class EmployeesByIdViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Employees.objects.filter()
    serializer_class = EmployeesSerializer
    
