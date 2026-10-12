# entirius-django-captcha

A Django module for reCAPTCHA verification in Entirius, the open-source modular ecommerce platform. It provides a
view decorator that checks the token of a request against the Google reCAPTCHA API, with one configuration per sales
channel.

[![PyPI](https://img.shields.io/pypi/v/entirius-django-captcha.svg)](https://pypi.org/project/entirius-django-captcha/)
[![Python](https://img.shields.io/pypi/pyversions/entirius-django-captcha.svg)](https://pypi.org/project/entirius-django-captcha/)
[![License: MPL-2.0](https://img.shields.io/badge/license-MPL--2.0-blue.svg)](https://github.com/entirius/entirius-django-captcha/blob/develop/LICENSE)

## What it does

- Protects any Django view with the `verify_recaptcha` decorator.
- Stores reCAPTCHA configuration as `Service` records: global or per sales channel, with a secret key and an active
  flag.
- Picks the active service of the request's channel first and falls back to the global one.
- Lets requests through when no active service is configured, so the check can be switched on per environment.

## Installation

```shell
uv add entirius-django-captcha
pip install entirius-django-captcha
```

```python
INSTALLED_APPS = [
    ...
    "django_utils",
    "django_captcha",
]

# urls.py
urlpatterns = [
    path("", include("django_captcha.urls")),
]
```

Optional settings: `CAPTCHA_TOKEN_HEADER_NAME` (default `X-Recaptcha-Token`), `CAPTCHA_URL` (default: the Google
siteverify endpoint), `API_BASE_URL` (default `api`); reference in
https://github.com/entirius/entirius-django-captcha/blob/develop/AGENTS.md (section Architecture).

## Quick start

```python
from django_captcha.output.decorators import verify_recaptcha


@verify_recaptcha
def my_view(request):
    ...
```

The decorator reads the token from the `X-Recaptcha-Token` request header and raises a validation error when the
token is missing or rejected. Create a `Service` record with the secret key in the Django admin to switch it on.

## Requirements

- Python 3.11 or newer, Django 4.0 or newer.
- Entirius packages pulled in: `entirius-django-utils`.

## Documentation

- Entirius documentation: https://docs.entirius.com/
- Releases: https://github.com/entirius/entirius-django-captcha/releases

## Part of Entirius

This module runs inside the Entirius backend service (Volkanos), where public endpoints of other modules use it.

- Backend service: https://github.com/entirius/entirius-service-volkanos
- Docker harness: https://github.com/entirius/entirius-zeno
- Sibling modules: https://github.com/entirius/entirius-django-utils,
  https://github.com/entirius/entirius-django-accounts

## Development

```shell
make install     # sync dependencies (uv)
make check       # lint + format check (ruff)
make test        # test suite (pytest + pytest-django)
```

Development and agent instructions: https://github.com/entirius/entirius-django-captcha/blob/develop/AGENTS.md

## License

Mozilla Public License 2.0 (MPL-2.0) — see https://github.com/entirius/entirius-django-captcha/blob/develop/LICENSE.
