from django.test import TestCase
from django.conf import settings
from django.db import connections, connection
from django.db.utils import OperationalError
import requests

class TasksViewTest(TestCase):
    
    def test_database_url(self):
        
        connection.ensure_connection()

    # def test_vin_decoder(self):

    #     r = requests.get(settings.VIN_DECODER_URL+'SCBBR9ZA1AC063223kj/')
    #     json_list = r.json()
    #     # print(json_list)
    #     self.assertTrue(json_list['decode']['status'] == 'SUCCESS')
            # print('problem with VIN_DECODER_URL')



    def test_endpoint_url(self):
        self.client.post('/?vin=11111111111111111')


        