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
            d1 = serialize("json", o2)
            # d2=json.dumps(d1)
            return JsonResponse(d1, safe=False)
        else:
            o2 = RK.objects.get(id=id)
            d1 = serialize("json", [o2, ])
            return JsonResponse(d1, safe=False)

    def post(self, request, *args, **kwargs):
        f = RKModelForm(request.POST)
        if f.is_valid():
            obj = f.save(commit=True)
        d = serialize("json", [obj, ])
        return JsonResponse(d, safe=False)

    def delete(self, request, id, *args, **kwargs):
        if id is not None:
            o = get_object_or_404(RK, id=id)
            o.delete()
            return JsonResponse({"deletee": "Yo"})


    def put(self, request, id, *args, **kwargs):
        print(request.body)
        o1 = RK.objects.get(id=id)
        old = json.loads(serialize("json", [o1,]))
        # new = json.loads(request.body)
        j=BytesIO(request.body)
        new=JSONParser().parse(j)
        for key, value in new.items():
            old[key] = value
        form = RKModelForm(new, instance=o1)
        obj = form.save(commit=True)
        d1 = json.dumps(obj)
        return JsonResponse(d1)
