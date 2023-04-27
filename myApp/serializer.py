from rest_framework import serializers

class CalSerializer(serializers.Serializer):
    num1=serializers.IntegerField(required=True)
    num2=serializers.IntegerField(required=True)
    opr=serializers.CharField(max_length=30,required=True)
