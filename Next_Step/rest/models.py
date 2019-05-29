# from django.conf import settings
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
import os
from django.forms import ModelForm, forms


# Create your models here.
# from Next_Step import settings


def upload_img(instance,filename):
    return "rest/Upload/{filename}".format(filename=filename)


class Ap(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    image= models.ImageField(upload_to=upload_img,null=True,blank=True)

    def __str__(self):
        return self.name

    def open(self):
        img=os.path.join(os.getcwd()+"/"+str(self.image))
        return img


class ApForm(ModelForm):
    class Meta:
        model=Ap
        fields=['name','age']

    def clean(self):
        if self.cleaned_data["name"] is None or self.cleaned_data["age"] is None:
            raise forms.ValidationError("Either Name Or Age Is Required")
        if self.cleaned_data["age"] < 18:
            raise forms.ValidationError("Not Adult Bro")




