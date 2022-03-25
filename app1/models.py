from django.db import models

# Create your models here.
class CountryData(models.Model):
    country = models.CharField(max_length=255, null=True, blank=True)
    cases = models.FloatField(default=0, null=False, blank=False, help_text="Number of cases")
    todayCases = models.FloatField(default=0, null=False, blank=False, help_text="Number of Today cases")
    deaths = models.FloatField(default=0, null=False, blank=False, help_text="Number of deaths")
    todayDeaths = models.FloatField(default=0, null=False, blank=False, help_text="Number of Today Deths")
    recovered = models.FloatField(default=0, null=False, blank=False, help_text="Number of recovery cases")
    active = models.FloatField(default=0, null=False, blank=False, help_text="Number of active cases")
    critical = models.FloatField(default=0, null=False, blank=False, help_text="Number of criticle cases")
    casesPerOneMillion = models.FloatField(default=0, null=False, blank=False)
    deathsPerOneMillion = models.FloatField(default=0, null=False, blank=False)
    totalTests = models.FloatField(default=0, null=False, blank=False, help_text="Number of total test")
    testsPerOneMillion = models.FloatField(default=0, null=False, blank=False)
        
    def __str__(self) -> str:
        return self.country
    
    
