from unittest.util import _MAX_LENGTH
from django.db import models
from django.urls import reverse
from datetime import date


QUARTER = (
    ('W', 'Wet Cloth'),
    ('D', 'Dry Cloth'),
    ('M', 'MicroFiber'),
    ('F', 'Feather duster')
)

class Jewelry(models.Model):
    name = models.CharField(max_length=50)
    setting = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('jewelry_detail', kwargs={'pk': self.id})
    def __str__(self):
        return self.name

# Create your models here.
class Gem(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    uses = models.CharField(max_length=100)
    jewelry = models.ManyToManyField(Jewelry)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'gem_id': self.id})
    
    def clean_for_today(self):
        return self.cleaning_set.filter(date=date.today()).count()>= len(QUARTER)

class Cleaning(models.Model):
    date = models.DateField('cleaning date')
    cleaning = models.CharField(
        max_length=1,    
        choices=QUARTER,
        default=QUARTER[0][0]
    )

    gem=models.ForeignKey(Gem, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.get_cleaning_display()} on {self.date}"

    class Meta:
        ordering = ['-date']

    

