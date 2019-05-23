from django.db import models
from django.forms import ModelForm

# Create your models here.


class Ap(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class ApForm(ModelForm):
    class Meta:
        model=Ap
        fields=['name','age']



