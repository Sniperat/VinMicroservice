from django.test import TestCase
from django.conf import settings
from django.db import connections, connection
from django.db.utils import OperationalError
from .models import DetailModel, WeightModel
import requests


class Test(TestCase):

    def test_model(self):

        d = DetailModel.objects.create(
            vin_id='ASD123ASD123ASD12',
            year='2000',
            make='make by test',
            model='test model',
            color='black',
            dimensions={'test': 'test'}
        )
        self.assertTrue(isinstance(d, DetailModel))

        w = WeightModel.objects.create(
            detail=d,
            _type='test',
            unit='uzs',
            value=2000
        )
        self.assertTrue(isinstance(w, WeightModel))

    def test_api(self):

        try:
            self.client.post('/ASD123ASD123ASD12/')
        except OperationalError as a:
            print(a)
