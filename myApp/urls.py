from django.urls import path
from myApp import views

urlpatterns = [
    path("hello-world",views.hello_world),
    path("hello",views.hello),
    path("calculate",views.calculator)


]
