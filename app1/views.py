from re import T
from django.http import JsonResponse
from rest_framework import generics
import requests 
from rest_framework.response import Response
from . import models
from . import serializers
from rest_framework import status,viewsets


def country_data(country="India"):
    """
    Args:
        country (str, optional): The Function Take country name as a parameter. Defaults to "India".

    Returns:
         _type_:
        "country": "India",
        "cases": 43016372,
        "todayCases": 0,
        "deaths": 516785,
        "todayDeaths": 0,
        "recovered": 42478087,
        "active": 21500,
        "critical": 8944,
        "casesPerOneMillion": 30652,
        "deathsPerOneMillion": 368,
        "totalTests": 785644225,
        "testsPerOneMillion": 559821

    """
    url = "https://coronavirus-19-api.herokuapp.com/countries"
    data = requests.get(url)
    try :
        data = data.json()
    except :
        return Response({"error":"Please Visit after some time"})
    for x in data:
        print(type(country),country,"-----------------------")
        if x.get("country").lower()==country.lower():
            DataIndia = x
            break
        else :
            DataIndia="null"
            continue
    if DataIndia == "null" :
        return Response({"error":"Please Provide Valid Country Name"})
    return DataIndia

def global_data():
    """ This function request the herokuapp.com API for taking
        worldwide corona cases details
    """
    url = "https://coronavirus-19-api.herokuapp.com/countries"
    data = requests.get(url)
    try :
        data = data.json()
    except :
        return Response({"error":"Please Visit after some time"})
    return data


class CountryView(viewsets.ModelViewSet):
    queryset = models.CountryData.objects.all()
    serializer_class = serializers.CountryDataSerilizer
    
    def get_queryset(self):
        return super().get_queryset()
    
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    def create(self,request):
        countrydata = country_data(request.data.get("country", None))
        serilizer = serializers.CountryDataSerilizer(data=countrydata)
        serilizer.is_valid(raise_exception=True)
        self.perform_create(serilizer)
        headers = self.get_success_headers(serilizer.data)
        return Response(data=serilizer.data, status= status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        self.perform_destroy(instance=instance)
        return Response(data=data, status=status.HTTP_200_OK)

    
class GlobalView(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        data = {"Success" : global_data()}
        return JsonResponse(data, safe=False)
