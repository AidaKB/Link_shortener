from django.urls import path
from car import views
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register("person",views.PersonViewSet)
router.register("car",views.CarViewSet)


urlpatterns = [
    # path("get-post-person",views.person_view),
    #path("get-post-car",views.car_view)

]
urlpatterns+=router.urls
