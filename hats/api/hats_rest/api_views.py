from django.shortcuts import render
from .models import Hat
from django.views.decorators.http import require_http_methods
import json
from django.http import JsonResponse
from common.json import ModelEncoder

class HatListEncoder(ModelEncoder):
    model = Hat
    properties = [
        "fabric",
        "style_name"
    ]

class HatDetailEncoder(ModelEncoder):
    model = Hat
    properties = [
        "fabric",
        "style_name",
        "color",
        "picture_url",
        "location",
    ]

@require_http_methods(["GET", "POST"])
def api_list_hats(request):

    if request.method == "GET":
        hats = Hat.objects.all()
        return JsonResponse(
            {"hats": hats},
            encoder=HatListEncoder,
            safe=False,
        )
    else:
        content = json.loads(request.body)
        hat = Hat.objects.create(**content)
        return JsonResponse(
            hat,
            encoder=HatDetailEncoder,
            safe=False,
        )
