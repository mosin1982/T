# CI/CD Pipeline

T uses GitHub Actions for quality, security, and deployment readiness.

## Workflows

- `ci.yml`: lint, format, type check, tests, security scan, dependency audit
- `docker.yml`: validates Docker image build
- `release.yml`: creates release archive when version tags are pushed

## Local Quality Commands

```bash
ruff check .
black --check .
mypy .
pytest -q
bandit -r . -x tests
pip-audit
```

## Release

```bash
git tag v1.0.0
git push origin v1.0.0
```
