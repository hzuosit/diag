from django.db import models
from datetime import date
from django.utils import timezone
# Create your models here.

class Ml(models.Model):
       class  Meta:
                 verbose_name_plural = 'Ml'
       e = models.EmailField(unique=True,null=False)
       def __unicode__(self):
                  return self.e


# Create your models here.
class Car_Data(models.Model):
   class Meta:
            verbose_name_plural = 'Driving data'

   UUID = models.CharField(max_length =20,primary_key=True,default=True)
   date_start = models.IntegerField(null=True)
   data_end=models.IntegerField(null=True)
   time_start = models.IntegerField(null=True)
   time_end=models.IntegerField(null=True)
   speed = models.IntegerField(null=True)
   rpm=models.IntegerField(null=True)
   instant_fuel=models.DecimalField(max_digits=5,decimal_places=2,null=True)
   average_fuel=models.DecimalField(max_digits=5,decimal_places=2,null=True)
   fuel_left=models.DecimalField(max_digits=5,decimal_places=2,null=True)
   duration=models.IntegerField(null=True)
   mileage=models.IntegerField(null=True)
   fuel_consump_thistime=models.IntegerField(null=True)
   hard_accel=models.IntegerField(null=True)
   hard_breaks=models.IntegerField(null=True)
   battery_v=models.DecimalField(max_digits=5,decimal_places=2,null=True)
   coolant_Temp=models.CharField(max_length=5, null=True)
   DTC=models.IntegerField(null=True,blank=True)
   throttle_position=models.DecimalField(max_digits=5,decimal_places=2,null=True)
   engine_load=models.DecimalField(max_digits=5,decimal_places=2,null=True)
   hotcar_du = models.IntegerField(null=True)
   idle_duration=models.DecimalField(max_digits=5,decimal_places=2,null=True)
   idle_fuel_consump=models.DecimalField(max_digits=5,decimal_places=2,null=True)
   max_rpm=models.IntegerField(null=True)
   max_speed=models.IntegerField(null=True)
