from django.shortcuts import render
from common.json import ModelEncoder
from .models import BinVO, Shoe
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
import json


class BinVOEncoder(ModelEncoder):
    model = BinVO
    properties = [
        'closet_name',
        'import_href',
    ]


class ShoeEncoder(ModelEncoder):
    model = Shoe
    properties = [
        'manufacturer',
        'model_name',
        'color',
        'picture_url',
        'id'
    ]


class ShoeDetailEncoder(ModelEncoder):
    model = Shoe
    properties = [
        "manufacturer",
        "model_name",
        "color",
        "picture_url",
        "bin",
    ]
    encoders = {
        "bin": BinVOEncoder()
    }


class ShoeListEncoder(ModelEncoder):
    model = Shoe
    properties = [
        "manufacturer",
        "model_name",
        "color",
        "picture_url",
        "id",
    ]
    def get_extra_data(self, o):
        return {"bin": o.bin.closet_name}

    encoders = {
        'bin': BinVOEncoder
    }


@require_http_methods({"GET", "POST"})
def api_list_shoes(requests, bin_vo_id=None):
    if requests.method == "GET":
        if bin_vo_id is not None:
            shoe = Shoe.objects.filter(bin=bin_vo_id)
        else:
            shoe = Shoe.objects.all()
        return JsonResponse(
            {"shoes": shoe},
            encoder=ShoeListEncoder,
        )
    else:
        content = json.loads(requests.body)
        try:
            bin_href = content["bin"]
            bin = BinVO.objects.get(import_href=bin_href)
            content["bin"] = bin
        except BinVO.DoesNotExist:
            return JsonResponse(
                {"message": "Invalid bin id"},
                status=400,
            )
        shoes = Shoe.objects.create(**content)
        return JsonResponse(
            shoes,
            encoder=ShoeDetailEncoder,
            safe=False,
        )


@require_http_methods({"GET", "DELETE", "PUT"})
def api_show_shoe(requests, pk):
    if requests.method == "GET":
        try:
            shoe = Shoe.objects.get(id=pk)
            return JsonResponse(
                shoe,
                encoder=ShoeDetailEncoder,
                safe=False,
            )
        except Shoe.DoesNotExist:
            return JsonResponse(
                {"message": "invalid shoe id"},
                status=400,
            )
    elif requests.method == "DELETE":
        count, _ = Shoe.objects.filter(id=pk).delete()
        return JsonResponse(
            {"GoodBye!": count > 0}
        )
    else:
        content = json.loads(requests.body)
        Shoe.objects.filter(id=pk).update(**content)
        shoe = Shoe.objects.get(id=pk)
        return JsonResponse(
            shoe,
            encoder=ShoeDetailEncoder,
            safe=False,
        )
