from django.shortcuts import render
from rest_framework import generics
# Create your views here.

from .models import Employee, Department
from .serializers import EmployeeSerializer, DepartmentSerializer

class EmployeeList(generics.ListCreateAPIView):
    serializer_class = EmployeeSerializer
    
    def get_queryset(self):
        queryset = Employee.objects.all()
        department = self.request.query_params.get('department')
        if department is not None:
            queryset = queryset.filter(departmentLocation=department)
        return queryset

class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

class DepartmentList(generics.ListCreateAPIView):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()

class DepartmentDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()