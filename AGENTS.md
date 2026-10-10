# AGENTS.md

reCAPTCHA verification Django module — distribution `entirius-django-captcha`, Django app `django_captcha`.

## Commands

| Command | Meaning |
|---|---|
| `make install` | sync dependencies (uv, incl. extras) |
| `make check` | lint + format-check (ruff) |
| `make fix` | auto-fix lint + format |
| `make test` | test suite (pytest + pytest-django) |

## Conventions

- English only: code, docs, commits, branches, PRs.
- MPL-2.0: every non-trivial source file carries the license header (pre-commit inserts it).
- Toolchain: uv + ruff + hatchling + pytest; all config in `pyproject.toml`; `uv.lock` committed.
- Git flow: `master` (production) + `develop` (integration); changes land via PR; semver tag on `master`.
- Never rename the package / Django app_label / DB table prefix `django_captcha` — it is a schema contract.
- Migrations are part of the public contract — never edit an already released migration.
- Default: do not commit — git is the user's call.
- No AI attribution in commits or PR descriptions.

## Architecture

- `models/` — `Service`: reCAPTCHA configuration per scope (`global` / `channel` with `channel_idx`),
  secret key, active flag.
- `output/decorators.py` — `verify_recaptcha` view decorator: reads the token header, resolves the
  active `Service` (channel first, global fallback), verifies against the Google siteverify API;
  no active service configured = pass-through.
- `settings.py` — host-project overrides with defaults: `CAPTCHA_TOKEN_HEADER_NAME`
  (`X-Recaptcha-Token`), `CAPTCHA_URL` (Google siteverify), `API_BASE_URL`.
- `urls.py` — mounts an empty route list under `{API_BASE_URL}/captcha/<version>/<channel_idx>/`; the module
  exposes no endpoint of its own.

| Topic | Where |
|---|---|
| Decorator and service lookup | `src/django_captcha/output/decorators.py` |
| `Service` model and scopes | `src/django_captcha/models/service.py` |
| Settings and defaults | `src/django_captcha/settings.py` |
