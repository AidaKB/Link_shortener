from django.shortcuts import render,redirect
from rest_framework.generics import ListAPIView,CreateAPIView
from django.conf import settings
from .seralizers import LinkSerializer
from .models import Link
from django.views import View
class ShortenerListApiView(ListAPIView):
    queryset=Link.objects.all()
    serializer_class=LinkSerializer



class ShortenerCreateApiView(CreateAPIView):
    serializer_class=LinkSerializer
class Redirectot(View):
    def get(self,request,shortener_link,*args,**kwargs):
        shortener_link=settings.HOST_URL+"/"+self.kwargs["shortener_link"]
        redirect_link=Link.objects.filter(shortened_link=shortener_link).first().original_link
        return redirect(redirect_link)


# Create your views here.
