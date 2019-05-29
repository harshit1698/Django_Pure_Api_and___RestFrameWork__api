import datetime
from django.conf import settings
from django.utils import timezone

expiry=settings.JWT_AUTH['JWT_REFRESH_EXPIRATION_DELTA']


def jwt_response_payload_handler(token,user=None,request=None):
    return{'token':token,'user':user.username,'expiry':timezone.now()+expiry-datetime.timedelta(seconds=200)}