from DjangoSite.models import Employees
from rest_framework import serializers

class EmployeesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employees
        fields = ['id', 'first_name', 'last_name', 'email', 'keypoints']