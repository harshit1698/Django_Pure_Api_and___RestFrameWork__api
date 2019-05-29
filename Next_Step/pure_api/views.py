from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.http import JsonResponse
from django.http import HttpResponse
from django.core.serializers import serialize
from django.shortcuts import get_object_or_404
from .models import RK
from .models import RKModelForm
import json
from django.utils.six import BytesIO
from rest_framework.parsers import JSONParser


# Create your views here.


class Exemptmixin(object):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class CBV(Exemptmixin, View):
    def get(self, request, id=None, *args, **kwargs):
        if id is None:
            o2 = RK.objects.all()
            # d1 = serialize("json", o2)
            d1 = o2.serialize()
            # d2=json.dumps(d1)
            return JsonResponse(d1, safe=False)
        else:
            o2 = RK.objects.get(id=id)
            d1 = serialize("json", [o2, ])
            return JsonResponse(d1, safe=False)

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
             print(request.POST)
        else:
            print("Error")
        f = RKModelForm(request.POST)
        if f.is_valid():
            obj = f.save(commit=True)
            d = obj.serialize()
            return JsonResponse(d, safe=False)
        if f.errors:
            data=json.dumps(f.errors)
            return JsonResponse(data,safe=False)

    def delete(self, request, id, *args, **kwargs):
        if id is not None:
            o = get_object_or_404(RK, id=id)
            o.delete()
            res = json.dumps({"deletee": "Yo"})
            return JsonResponse(res, status=201,safe=False)
        else:
            res = json.dumps({"Delete": "Already deleted"})
            return JsonResponse(res, status=404 ,safe=False)

    def put(self, request, id, *args, **kwargs):
        print(request.body)
        # data=serialize("json",request.body)
        passed_data = json.loads(request.body)
        obj = RK.objects.filter(id=id)
        if obj is None:
            error_data = json.dumps({"Error": "Object Not Found"})
            return JsonResponse(error_data, status=404,safe=False)
        data = json.loads(obj.serialize())
        for key, value in passed_data.items():
            data[key] = value
        form = RKModelForm(data, instance=obj)
        if form.is_valid():
            obj = form.save(commit=True)
            d1 = json.dump(data)
            return JsonResponse(d1, status=201,safe=False)
        if form.errors:
            d1 = json.dumps(form.errors)
            return JsonResponse(d1, status=400,safe=False)
