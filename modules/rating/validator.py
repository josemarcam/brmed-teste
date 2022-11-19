from pydantic import BaseModel, validator
from datetime import datetime, timedelta
from cotacao.settings import env
from typing import Optional

class RatingValidatorModel(BaseModel):

    from_date: datetime
    to_date: datetime

    @validator("*", pre=True)
    def format_validator(cls, v):
        try:
            transformed_v = datetime.strptime(v, '%Y-%m-%d') 
        except ValueError as e:
            raise ValueError("Formato da data invalido")
        return transformed_v
    
    @validator("*", pre=True)
    def future_date_validator(cls, v):
        if v > datetime.now():
            raise ValueError("Valor nao pode ser maior que a data atual")
        return v
    
    @validator("to_date")
    def to_date_validator(cls, v, values, **kwargs):
        if v < values['from_date']:
            raise ValueError("Data de inicio precisa ser menor que data final")

        date_diff = v - values['from_date'] + timedelta(days=1)

        if date_diff > timedelta(days=int(env("MAX_DAYS_PERIOD"))):
            raise ValueError("Periodo maximo excedido")
        
        return v
