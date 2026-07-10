# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from functools import wraps

import requests
from django_utils.api.exceptions import ValidationError

from django_captcha.models.service import Scope, Service
from django_captcha.settings import CAPTCHA_TOKEN_HEADER_NAME, CAPTCHA_URL


def verify_recaptcha(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        captcha_token = request.headers.get(CAPTCHA_TOKEN_HEADER_NAME)

        service = Service.objects.filter(is_active=True, scope=Scope.GLOBAL).first()
        channel_idx = getattr(request, "channel", None)
        if not isinstance(channel_idx, str):
            channel_idx = getattr(channel_idx, "idx", None)
        if channel_idx:
            service_channel = Service.objects.filter(
                is_active=True, scope=Scope.CHANNEL, channel_idx=channel_idx
            ).first()
            if service_channel:
                service = service_channel
        if not service:
            return view_func(request, *args, **kwargs)

        if not captcha_token:
            raise ValidationError("Missing CAPTCHA token")

        data = {"secret": service.secret_key, "response": captcha_token}
        response = requests.post(CAPTCHA_URL, data=data)
        result = response.json()
        if not result.get("success"):
            raise ValidationError("Invalid CAPTCHA token")

        return view_func(request, *args, **kwargs)

    return _wrapped_view
