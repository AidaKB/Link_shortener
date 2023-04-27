from django.urls import path
from LinkShortener import views
from LinkShortener.views import ShortenerCreateApiView,ShortenerListApiView
from rest_framework.routers import DefaultRouter
# app_name='LinkShortener' ######mitone nayad
urlpatterns = [
    path('',ShortenerListApiView.as_view()),
    path('create/', ShortenerCreateApiView.as_view()),
]
