from django.db import models


class Student(models.Model):
    first_name=models.CharField( max_length=50)
    last_name=models.CharField(max_length=50)
    std_num=models.IntegerField()
    Teacher=(("beheshti","Beheshti"),("karimi","Karimi"),("taheri","Taheri"))
    teacher=models.CharField(max_length=9,choices=Teacher)


# Create your models here.
