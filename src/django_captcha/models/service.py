# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from enum import unique

from django.db import models
from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _

from django_captcha.models.base_model import BaseModel


@unique
class Scope(TextChoices):
    GLOBAL = "global", _("Global")
    CHANNEL = "channel", _("Channel")


class Service(BaseModel):
    scope = models.CharField(max_length=256, choices=Scope.choices, default=Scope.GLOBAL)
    channel_idx = models.CharField(max_length=128, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    secret_key = models.CharField(max_length=256, blank=False, null=False)
    objects = models.Manager()
