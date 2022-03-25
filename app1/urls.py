from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .import views


router = DefaultRouter()
router.register("", views.CountryView, basename="countryData")

urlpatterns = [
    path("all/",views.GlobalView.as_view()),
    path("", include(router.urls)),
]