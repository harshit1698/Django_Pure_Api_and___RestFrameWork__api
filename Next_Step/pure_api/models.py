from django.db import models
from django.forms import ModelForm


# Create your models here.


class RK(models.Model):
    name = models.CharField(max_length=20)
    rship = models.IntegerField()

    def __str__(self):
        return self.name


class RKModelForm(ModelForm):
    class Meta:
        model = RK
        fields = ['name', 'rship']
