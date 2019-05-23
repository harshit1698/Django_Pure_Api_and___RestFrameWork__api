from rest_framework.serializers import ModelSerializer
from rest.models import Ap


class ApSerializer(ModelSerializer):
    class Meta:
        model = Ap
        fields = ['name','age']