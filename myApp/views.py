from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import CalSerializer
@api_view()
def hello_world(request):
    return Response({"message":"Hello World!"})


@api_view(['GET','POST'])
def hello(request):
    if request.method=="GET":
        return Response({"message":"Hello World!"})
    else:
        return Response({"message":"Hello {}!".format(request.data["name"])})


# @api_view(['POST'])
# def calculator(request):
#     try:
#         num1=request.data["num1"]
#         num2=request.data["num2"]
#         opr=request.data["opr"]
#     except:
#         return Response({"error":"you didn't send num1 or num2 or operator"},status=status.HTTP_400_BAD_REQUEST)     
#     else:
#         if isinstance(num1,int) and isinstance(num2,int):
#             if opr=="add":
#                 return Response({"result":num1+num2},status=status.HTTP_200_OK)
#             elif opr=="sub":
#                 return Response({"result":num1-num2},status=status.HTTP_200_OK)
#             elif opr=="multi":
#                 return Response({"result":num1*num2},status=status.HTTP_200_OK)
#             elif opr=="div":
#                 return Response({"result":num1/num2},status=status.HTTP_200_OK)
#             else:
#                 return Response({"error":"send a valid operator"},status=status.HTTP_400_BAD_REQUEST) 
#         else:
#             return Response({"error":"you didn't send int!"},status=status.HTTP_400_BAD_REQUEST)     
        
         

@api_view(['POST'])
def calculator(request):
    ser=CalSerializer(data=request.data)

    if ser.is_valid():
        num1=ser.data["num1"]
        num2=ser.data["num2"]
        opr=ser.data["opr"]
        if opr=="add":
            return Response({"result":num1+num2},status=status.HTTP_200_OK)
        elif opr=="sub":
            return Response({"result":num1-num2},status=status.HTTP_200_OK)
        elif opr=="multi":
            return Response({"result":num1*num2},status=status.HTTP_200_OK)
        elif opr=="div":
            return Response({"result":num1/num2},status=status.HTTP_200_OK)
        else:
            return Response({"error":"send a valid operator"},status=status.HTTP_400_BAD_REQUEST)    
    else:
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)   
    

# Create your views here.
