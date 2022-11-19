import requests
from datetime import timedelta, datetime

from django.core.cache import cache
from cotacao.settings import env

from modules.rating.validator import RatingValidatorModel



class RatingService:
    
    def __init__(self) -> None:
        self._date_format = '%Y-%m-%d'

    def get_quotation(self, valid_data: RatingValidatorModel):
        date_diff = valid_data.to_date - valid_data.from_date + timedelta(days=1)
        api_data = []
        for day in range(date_diff.days):
            
            search_date : datetime = valid_data.from_date + timedelta(days=day)
            
            if search_date.isoweekday() in [6,7]:
                continue 
            
            if cache.has_key(search_date.strftime(self._date_format)):
                redis_response = cache.get(search_date.strftime(self._date_format))
                api_data.append({ search_date.strftime(self._date_format) : redis_response })
                continue
            
            url_params = {
                "base": "USD",
                "date": search_date.date().strftime(self._date_format)
            }
            response = requests.get(env("VAT_API_BASE_URL"),params=url_params)
            response_json = response.json()
            api_data.append({ response_json.get("date") : response_json.get("rates") })
            cache.set(response_json.get("date"), response_json.get("rates"))
        
        return api_data