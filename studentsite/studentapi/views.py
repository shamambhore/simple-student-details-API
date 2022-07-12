from django.shortcuts import render
from rest_framework.response import Response
from studentapi.models import Student
from .serializers import studentserializer
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET'])
def index(request):
    students = Student.objects.all()
    studentsers = studentserializer(students, many=True)
    return Response(studentsers.data)

@api_view(['GET'])
def studentview(request, pk):
    student = Student.objects.get(id=pk)
    studenser = studentserializer(student, many=False)
    return Response(studenser.data)

@api_view(['POST'])
def addstudent(request):
    serialstudentadd = studentserializer(data=request.data)
    if serialstudentadd.is_valid():
        serialstudentadd.save()
        
    return Response(serialstudentadd.data)
        
@api_view(['POST'])
def updatestudent(request,pk):
    updstudent = Student.objects.get(id=pk)
    updstudentserial = studentserializer(instance=updstudent, data=request.data)
    
    if updstudentserial.is_valid():
        updstudentserial.save()
        
    return Response(updstudentserial.data)

@api_view(['DELETE'])
def deletestudent(request, pk):
    delstudent = Student.objects.get(id=pk)
    delstudent.delete()
    
    students = Student.objects.all()
    studentsers = studentserializer(students, many=True)
    return Response(studentsers.data)
    
    