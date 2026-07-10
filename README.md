# django-captcha

reCAPTCHA verification for Django — a `verify_recaptcha` view decorator backed by per-channel
`Service` configuration (site scope, secret key, active flag).

## Installation

```shell
pip install entirius-django-captcha
```

Add the app to your project:

```python
INSTALLED_APPS = [
    ...
    "django_captcha",
]
```

## Usage

```python
from django_captcha.output.decorators import verify_recaptcha

@verify_recaptcha
def my_view(request):
    ...
```

The decorator reads the token from the `X-Recaptcha-Token` request header (configurable via
`CAPTCHA_TOKEN_HEADER_NAME`) and validates it against the Google reCAPTCHA API.

## Development

```shell
make install     # sync dependencies (uv)
make check       # lint + format check (ruff)
make test        # test suite (pytest + pytest-django)
```

Development and agent instructions: [AGENTS.md](AGENTS.md).

## License

Mozilla Public License 2.0 — see [LICENSE](LICENSE).
