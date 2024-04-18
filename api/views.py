# from argparse import Action
from rest_framework.decorators import action
from django.shortcuts import render
from rest_framework import viewsets

from api.models import Company, Employee
from api.serializers import CompanySerializer, EmployeeSerializer
from rest_framework.response import Response
# Create your views here.

class ComampanyViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer

# companies/{comapnee_id}/employees
    @action(detail=True, methods=['get'])
    def employees(self, request,pk=None):
        print("get employee of ", pk, "company")
        company=Company.objects.get(pk=pk)
        emps= Employee.objects.filter(company=company)
        emps_serializer=EmployeeSerializer(emps,many=True,context={'request':request})
        return Response(emps_serializer)


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer