from django.urls import include, path
from rest_framework import routers
from vessel import views

router = routers.DefaultRouter()
router.register(r'vessels', views.VesselViewSet, basename='vessels')

urlpatterns = [
    path('', include(router.urls)),
]
