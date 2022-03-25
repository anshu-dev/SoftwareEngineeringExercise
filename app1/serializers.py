from rest_framework import serializers
from .models import CountryData

class  CountryDataSerilizer(serializers.ModelSerializer):
    class Meta:
        model = CountryData
        fields = ["country",
                  "cases",
                  "todayCases",
                  "deaths",
                  "todayDeaths",
                  "recovered",
                  "active",
                  "critical",
                  "casesPerOneMillion",
                  "deathsPerOneMillion",
                  "totalTests",
                  "testsPerOneMillion"]
        