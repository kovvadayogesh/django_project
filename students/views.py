from django.shortcuts import render
from .models import Student
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializer import StudentSerializer
# Create your views here.

@api_view(['GET','POST','PUT','DELETE'])
def get_student_details(request, id=None):
    if request.method == 'GET':
        if id is not None:
            getStudentData = Student.objects.get(id=id)
            serializer = StudentSerializer(getStudentData)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            getStudentDetails = Student.objects.all()
            serializer = StudentSerializer(getStudentDetails, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        postData = StudentSerializer(data=request.data)
        if postData.is_valid():
            postData.save()
            return Response(postData.data, status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        studentID = Student.objects.get(id=id)
        updateData = StudentSerializer(studentID, data=request.data)
        if updateData.is_valid():
            updateData.save()
            return Response(updateData.data)
    
    if request.method == 'DELETE':
        studentID = Student.objects.get(id=id)
        studentID.delete()
        return Response(
            {"error":"Data has been deleted"}, status=status.HTTP_204_NO_CONTENT
        )

