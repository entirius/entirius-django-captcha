# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

"""Smoke test: every public submodule imports cleanly under a configured Django."""

import importlib

import pytest

MODULES = [
    "django_captcha.apps",
    "django_captcha.admin",
    "django_captcha.settings",
    "django_captcha.urls",
    "django_captcha.models.base_model",
    "django_captcha.models.service",
    "django_captcha.output.decorators",
]


@pytest.mark.parametrize("module", MODULES)
def test_module_imports(module):
    importlib.import_module(module)
