from datetime import datetime
import json

from pydantic import ValidationError

from django.views.generic.base import View
from django.shortcuts import render

from modules.rating.validator import RatingValidatorModel
from modules.rating.service import RatingService


class RatingPageView(View):

    def get(self, request, *args, **kwargs):
        
        from_date_str = request.GET.get('from_date',datetime.now().strftime('%Y-%m-%d'))
        to_date_str = request.GET.get('to_date',datetime.now().strftime('%Y-%m-%d'))
        
        errors = []
        api_data = []

        try:
            validated_data = RatingValidatorModel(from_date = from_date_str, to_date = to_date_str)
        except ValidationError as e:
            error_messages = self._process_error_message(e.json())
            errors.append(*error_messages)
        
        if not errors:

            service = RatingService()

            api_data = service.get_quotation(valid_data=validated_data)

        return render(request=request, template_name="index.html", context={"api_data":json.dumps(api_data), "errors":json.dumps(errors) })

    def _process_error_message(self, errors):
        return [{"msg": error['msg']} for error in json.loads(errors)]
        
