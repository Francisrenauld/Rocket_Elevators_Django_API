from django.shortcuts import render
from DjangoSite.models import Employees
from rest_framework import viewsets
from rest_framework import permissions
from Django_API_2.quickstart.serializers import EmployeesSerializer
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.response import Response
import face_recognition
import json

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

@api_view(['GET'])
def Register(request):
    
    if(request.method == 'GET'):
        try:
            queryset = Employees.objects.get(email=request.data['email'])
            employee = EmployeesSerializer(queryset, many=False)
            imageInDB = face_recognition.load_image_file(request.data['Insert Picture'])
            unknown_face_encoding = face_recognition.face_encodings(imageInDB)[0]

            known_faces = [
                employee.data['keypoints']
            ]

            results = face_recognition.compare_faces(known_faces, unknown_face_encoding)

            if(results == [True]):
                
                a = results

                return JsonResponse(employee.data)
            return Response("The image sent doesn't match!")
        except IndexError:
            quit()

    
        

@api_view(['PUT'])
def Update_Image(request):
    if request.method == 'PUT':
        imageInDB = face_recognition.load_image_file(request.data['Insert Picture'])
        new_face = face_recognition.face_encodings(imageInDB)[0]
        a = list(new_face)
        b = json.dumps(a)
        c = json.loads(b)
        Employees.objects.filter(email=request.data['email']).update(keypoints=c)
        return Response("Your picture had been updated successfully")


        





    
