from django.shortcuts import render
from common.json import ModelEncoder
from .models import Bin, Shoe
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
import json


class BinEncoder(ModelEncoder):
    model = Bin
    properties = [
        'closet_name',
        'bin_size',
        'bin_number',
        'bin_href',
        'id'
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

    encoders = {
        'bin': BinEncoder
    }


@require_http_methods(['GET', 'POST'])
def api_list_shoe(request):
    if request.method == 'GET':
        shoes = Shoe.objects.all()
        return JsonResponse({'shoes':shoes}, encoder=ShoeEncoder, safe=False)
    else:
        content = json.loads(request.body)
        try:

            bin_href = content['bin_href']
            bin = Bin.objects.get(id = bin_href, safe=False)
            content['bin_href'] = bin

        except Bin.DoesNotExist:
            return JsonResponse({'message': 'Bin does not exist'}, status=400)
        shoe = Shoe.objects.create(**content)
        return JsonResponse(shoe, encoder=ShoeEncoder, safe=False)


@require_http_methods(['GET', 'PUT', 'DELETE'])
def api_show_shoe(request, pk):
    if request.method == 'DELETE':
        count, _ = Shoe.objects.filter(id=pk).delete()
        return JsonResponse({'deleted': count > 0})
    elif request.method == 'GET':
        shoe = Shoe.objects.get(id=pk)
        return JsonResponse(shoe, encoder=ShoeEncoder, safe=False)
    else:
        content = json.loads(request.body)
        try:
            if 'bin' in content:
                content['bin'] = Bin.objects.get(bin_number=content['bin'])
        except Bin.DoesNotExist:
            return JsonResponse({'message':'Invalid'}, status=400)

        Shoe.object.filter(id=pk).update(**content)
        shoe = Shoe.object.get(id=pk)
        return JsonResponse(shoe, encoder=ShoeEncoder, safe=False)
