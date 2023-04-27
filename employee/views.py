from django.shortcuts import render
from rest_framework.response import Response
from .serializers import EmployeeSerializers
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Employee
# Create your views here.

@api_view(["POST"])
def post_employee(request):
    data={"name":request.data["name"],
          "age":request.data["age"],
          "salary":request.data["salary"],
          "post":request.data["post"],}
    
    ser=EmployeeSerializers(data=data)
    if ser.is_valid():
        ser.save()
        return Response(ser.data,status=status.HTTP_201_CREATED)
    else:
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(["GET"])
def get_employees(request):
    emp=Employee.objects.all()
    ser=EmployeeSerializers(emp,many=True)
    return Response(ser.data,status=status.HTTP_200_OK)

@api_view(["POST","GET","DELETE","PUT"])
def get_update_delete_employee(request,pk):
    try:
        emp=Employee.objects.get(pk=pk)
    except:
        return Response({"error":"Not Found Your Obj!"},status=status.HTTP_400_BAD_REQUEST) 
    if request.method=="GET":
        ser=EmployeeSerializers(emp)
        return Response(ser.data,status=status.HTTP_200_OK)
    elif request.method=="PUT":
        ser=EmployeeSerializers(emp,data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data,status=status.HTTP_200_OK)
        else:
            return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=="DELETE":
        emp.delete()
        return Response({"message":"your obj was deleted!"},status=status.HTTP_204_NO_CONTENT)   


@api_view(["GET"])
def search_employee(request):
    emp=Employee.objects.filter(name=request.query_params["name"])
    if emp:
        ser=EmployeeSerializers(emp,many=True)
        return Response(ser.data,status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)