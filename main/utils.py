from django.conf import settings
import requests
from .models import DetailModel, WeightModel


def get_model_object(json_data, vin_id):
    detail = DetailModel.objects.create(
        vin_id=vin_id,
        year=json_data.get('year'),
        make=json_data.get('make'),
        model=json_data.get('model'),
        color=json_data.get('color'),
        dimensions=json_data.get('dimensions')
    )

    json_weight = json_data.get('weight')

    if isinstance(json_weight, list):
        for weight_objects_on_dict in json_weight:
            WeightModel.objects.create(
                weight_type=weight_objects_on_dict.get('type'),
                unit=weight_objects_on_dict.get('unit'),
                value=weight_objects_on_dict.get('value'),
                detail=detail
            )

    else:
        WeightModel.objects.create(
            weight_type=json_weight.get('type'),
            unit=json_weight.get('unit'),
            value=json_weight.get('value'),
            detail=detail
        )

    return detail


def get_detail_from_vin(vin_id):
    try:
        obj = DetailModel.objects.get(vin_id=vin_id)
    except DetailModel.DoesNotExist:
        r = requests.get(str(settings.VIN_DECODER_URL) + vin_id + '/')
        json_list = r.json()
        decode = json_list.get('decode')
        if decode.get('status') == 'SUCCESS':
            vehicles = decode.get('vehicle')
            obj = get_model_object(vehicles[0], vin_id)
        else:
            return False
    return obj
