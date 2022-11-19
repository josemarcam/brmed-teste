from unittest.mock import patch
from datetime import datetime, timedelta

from django.test import TestCase

from modules.rating.tests.mocks import requests_get_mock, cache_mock
from modules.rating.service import RatingService
from modules.rating.validator import RatingValidatorModel
# Create your tests here.



class RatingTestCase(TestCase):
    
    @patch("requests.get",side_effect=requests_get_mock)
    @patch("modules.rating.service.cache",side_effect=cache_mock)
    def test_get_quotation(self, requests_get_mock, cache_mock):
        valid_data = RatingValidatorModel(from_date='2018-05-04', to_date='2018-05-04')
        service = RatingService()
        api_data = service.get_quotation(valid_data)
        
        self.assertEqual(type(api_data), list)
        self.assertEqual(len(api_data), 1)

class RatingValidatorsTestCase(TestCase):
    
    def test_future_date_validator(self):
        with self.assertRaises(ValueError) as context:
            future_date = datetime.now() + timedelta(days=1)
            future_date_str = future_date.strftime('%Y-%m-%d')
            RatingValidatorModel(from_date=future_date_str, to_date=future_date_str)
    
    def test_from_date_higher_then_validator(self):
        with self.assertRaises(ValueError) as context:
            RatingValidatorModel(from_date='2018-05-04', to_date='2018-05-02')

    def test_max_period_validator(self):
        with self.assertRaises(ValueError) as context:
            
            RatingValidatorModel(from_date='2018-05-03', to_date='2018-05-13')

    def test_date_format_validator(self):
        with self.assertRaises(ValueError) as context:
            
            RatingValidatorModel(from_date='2018-05-03', to_date='2018-05-13')
        