from django.shortcuts import render
from .models import Hat, LocationVO
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

class LocationVOEncoder(ModelEncoder):
    model = LocationVO
    properties = [
        "closet_name",
        "section_number",
        "shelf_number",
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

@require_http_methods(["GET", "PUT", "DELETE"])
def api_show_hats(request, pk):
    if request.method == "GET":
        hat = Hat.objects.get(id=pk)
        return JsonResponse(
            {"hat": hat},
            encoder=HatDetailEncoder,
        )
    elif request.method == "DELETE":
        count, _ = Hat.objects.filter(id=pk).delete()
        return JsonResponse({"deleted": count > 0})


@require_http_methods(["DELETE", "GET", "PUT"])
def api_show_location(request, pk):
    if request.method == "GET":
        location = LocationVO.objects.get(id=pk)
        return JsonResponse(
            location,
            encoder=LocationVOEncoder,
            safe=False,
        )
    elif request.method == "DELETE":
        count, _ = LocationVO.objects.filter(id=pk).delete()
        return JsonResponse({"deleted": count > 0})
    else:
        content = json.loads(request.body)
        LocationVO.objects.filter(id=pk).update(**content)
        location = LocationVO.objects.get(id=pk)
        return JsonResponse(
            location,
            encoder=LocationVOEncoder,
            safe=False,
        )
