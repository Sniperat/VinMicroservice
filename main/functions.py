from django.conf import settings
import requests
from .models import DetailModel, WeightModel


def get_model_object(json_data, vin_id):
    detail = DetailModel.objects.create(
        vin_id=vin_id,
        year=json_data['year'],
        make=json_data['make'],
        model=json_data['model'],
        color=json_data['color'],
        dimensions=json_data['dimensions']
    )

    json_weight = json_data['weight']

    if isinstance(json_weight, list):
        for i in json_weight:
            WeightModel.objects.create(
                _type=i['type'],
                unit=i['unit'],
                value=i['value'],
                detail=detail
            )

    else:
        WeightModel.objects.create(
            _type=json_weight['type'],
            unit=json_weight['unit'],
            value=json_weight['value'],
            detail=detail
        )

    return detail


def get_detail_from_vin(vin_id):
    try:
        obj = DetailModel.objects.get(vin_id=vin_id)
    except:
        r = requests.get(str(settings.VIN_DECODER_URL) + vin_id + '/')
        json_list = r.json()
        if json_list['decode']['status'] == 'SUCCESS':
            obj = get_model_object(json_list['decode']['vehicle'][0], vin_id)
        else:
            return False
    return obj
