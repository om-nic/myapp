from django.db import models

# Create your models here.

class Country(models.Model):
   c_name = models.CharField(max_length=40)
   
   def __str__(self):
        return self.c_name


class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    s_name = models.CharField(max_length=50)

    def __str__(self):
        return self.s_name

#Tiger Reserve name with Country and state
class TigerReserve(models.Model):
    tr_name = models.CharField(max_length = 100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    State = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.tr_name