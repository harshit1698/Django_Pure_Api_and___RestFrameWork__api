from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from rest_framework import permissions, pagination
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView, \
    RetrieveUpdateDestroyAPIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Ap, ApForm
from rest_framework.authentication import SessionAuthentication
from .serializers.serializers import ApSerializer, RegisterUserSerializer
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin


# Create your views here.
User=get_user_model()

class Create(CreateModelMixin, ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [SessionAuthentication]
    serializer_class = ApSerializer

    def get_queryset(self):
        qs = Ap.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(name__icontains=query)
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CBV_create(CreateAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Ap.objects.all()
    serializer_class = ApSerializer


class DstroyModelMixin(object):
    pass


class details(RetrieveUpdateDestroyAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Ap.objects.all()
    serializer_class = ApSerializer
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def patch(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)


class Del(DestroyAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Ap.objects.all()
    serializer_class = ApSerializer
    lookup_field = 'id'


class Up(UpdateAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Ap.objects.all()
    serializer_class = ApSerializer
    lookup_field = 'id'


class CustomPagination(pagination.PageNumberPagination):
    page_size = 4


class APIVieww(CreateModelMixin,UpdateModelMixin,DestroyModelMixin,ListAPIView,RetrieveModelMixin):
    # permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = [SessionAuthentication]
    serializer_class = ApSerializer
    queryset = Ap.objects.all()
    lookup_field = "id"
    pagination_class = CustomPagination

    def get_queryset(self):
        qs = Ap.objects.all()
        print(self.request.user)
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(name__icontains=query)
        return qs

    def get_object(self):
        p_id=self.request.GET.get("id",None)
        queryset = self.get_queryset()
        obj = None
        if p_id is not None:
            obj = get_object_or_404(queryset,id=p_id)
            self.check_object_permissions(self.request,obj)
        return obj

    def perform_destroy(self, instance):
        if instance is not None:
            return instance.delete()
        return None

    def get(self, request, *args, **kwargs):
        p_id=request.GET.get('id',None)
        if p_id is not None:
            return self.retrieve(request,*args,**kwargs)
        return super().get(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request,*args,**kwargs)

    def patch(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)


class Beginning(CreateAPIView,UpdateModelMixin):
    authentication_classes = [SessionAuthentication,JSONWebTokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ApSerializer
    queryset = Ap.objects.all()

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)


class List(ListView):
    template_name = 'show.html'
    queryset = Ap.objects.all()


class Ree(RetrieveAPIView):
    queryset = Ap.objects.all()
    serializer_class = ApSerializer
    permission_classes = []
    authentication_classes = []
    lookup_field = "id"


class YoBoy(CreateView):
    template_name = 'yo.html'
    model = Ap
    form_class = ApForm
    success_url = reverse_lazy("Rest:Ap")


# class Update(UpdateAPIView)
class RegisterView(CreateAPIView):
    queryset = User
    serializer_class = RegisterUserSerializer
    permission_classes = [permissions.AllowAny]





