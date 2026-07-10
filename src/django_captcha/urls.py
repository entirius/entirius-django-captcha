# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from django.urls import include, path

from django_captcha import settings

api_paths = []
urlpatterns = [path(f"{settings.BASE_URL}/captcha/<str:version>/<str:channel_idx>/", include(api_paths))]
