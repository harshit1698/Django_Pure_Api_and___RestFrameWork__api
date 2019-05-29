from django.core.serializers import serialize
from django.db import models
from django.forms import ModelForm, forms


# Create your models here.


class UpdateQuerSet(models.QuerySet):
    def serialize(self):
        qs=self
        return serialize("json",qs)


class RkManager(models.Manager):
    def get_queryset(self):
        return UpdateQuerSet(self.model,using=self._db)


class RK(models.Model):
    name = models.CharField(max_length=20)
    rship = models.IntegerField()

    objects=RkManager()

    def __str__(self):
        return self.name

    def serialize(self):
        return serialize("json",[self])


class RKModelForm(ModelForm):
    class Meta:
        model = RK
        fields = ['name', 'rship']

    def clean(self):
        if self.cleaned_data["name"] is None:
            raise forms.ValidationError("Name is required")

