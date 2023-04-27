from django.shortcuts import render
from .models import Person,Car
from .serializers import PersonSerializers,CarSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status,viewsets,permissions

# @api_view(["GET","POST"])
# def person_view(request):
#     if request.method=="GET":
#         person=Person.objects.all()
#         return Response(PersonSerializers(person,many=True).data,status=status.HTTP_200_OK)
#     elif request.method=="POST":
#         ser=PersonSerializers(data=request.data)
#         if ser.is_valid():
#             ser.save()
#             return Response(ser.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
class PersonViewSet(viewsets.ModelViewSet): #be jaye func bala in 3 ta khat:/
    queryset=Person.objects.all()
    serializer_class=PersonSerializers
    http_method_names=["post","get","put","delete"] #hatman horoof bayad koochak bashand
    # search_fields=('name',)
    # ordering_fields="__all__"
    def list(self, request, *args, **kwargs): #when the get method is called
        obj= super().list(request, *args, **kwargs)
        print("------list------")
        return obj
    def create(self, request, *args, **kwargs):
        obj= super().create(request, *args, **kwargs)
        print("------create------")
        return obj 
    def update(self, request, *args, **kwargs):
        obj= super().update(request, *args, **kwargs)
        ins=self.get_object()
        print("------update: {}".format(ins.name))
        return obj
    def retrieve(self, request, *args, **kwargs): #when get is calling and except one record to be shown
        obj=super().retrieve(request, *args, **kwargs)
        ins=self.get_object()
        print("------retrive: {}".format(ins.name))
        return obj
    def destroy(self, request, *args, **kwargs):
        ins=self.get_object()
        print("------retrive: {}".format(ins.name))
        obj=super().destroy(request, *args, **kwargs)
        return obj

# @api_view(["GET","POST"])
# def car_view(request):
#     if request.method=="GET":
#         car=Car.objects.all()
#         return Response(CarSerializers(car,many=True).data,status=status.HTTP_200_OK)
#     elif request.method=="POST":
#         ser=CarSerializers(data=request.data)
#         if ser.is_valid():
#             ser.save()
#             return Response(ser.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)


# Create your views here.

class CarViewSet(viewsets.ModelViewSet):
    queryset=Car.objects.all()
    serializer_class=CarSerializers
    http_method_names=["post","get","put","delete"]