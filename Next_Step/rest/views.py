from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from .models import Ap
from .serializers.serializers import ApSerializer


# Create your views here.

class Create(ListAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Ap.objects.all()
    serializer_class = ApSerializer


class CBV_create(CreateAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Ap.objects.all()
    serializer_class = ApSerializer


class Del(DestroyAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Ap.objects.all()
    serializer_class = ApSerializer


class Up(UpdateAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Ap.objects.all()
    serializer_class = ApSerializer



