from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime


def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)


# Create your models here.
class Car(models.Model):

    class Meta:
        ordering = ['numberplate']

    numberplate = models.CharField(primary_key=True, max_length=8, unique=True, default='00-AA-AA')
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField(
        default=current_year(), validators=[MinValueValidator(1960), max_value_current_year])
    fuel_choices = [
        ('P', 'Petrol'),
        ('D', 'Diesel'),
        ('E', 'Electric'),
        ('H', 'Hybrid'),
        ('L', 'LPG'),
    ]
    fuel = models.CharField(max_length=10, choices=fuel_choices, default='P')
    engine = models.CharField(max_length=100)
    purchase_date = models.DateField(auto_now_add=False)
    sales_date = models.DateField(auto_now_add=False, null=True, blank=True)
    residual_value = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.numberplate


class MaintenceData(models.Model):

    class Meta:
        verbose_name_plural = 'Maintence Data'

    car = models.ForeignKey('Car', null=True, blank=True, on_delete=models.SET_NULL)
    oil_change_km = models.PositiveIntegerField()
    oil_change_date = models.DateField(auto_now_add=False)
    next_oil_change_km = models.PositiveIntegerField()
    distribution_set_km = models.PositiveIntegerField()
    distribution_set_date = models.DateField(auto_now_add=False)
    next_distribution_set_km = models.PositiveIntegerField()
