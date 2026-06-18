# Contributing to T

Thank you for considering contributing to T.

## Contribution Rules

1. Keep the project risk-first, not hype-first.
2. Do not add guaranteed-profit claims.
3. Add tests for new modules.
4. Keep secrets out of commits.
5. Keep modules explainable and observable.
6. Respect the T License v1.0.

## Development Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
pytest -q
```

## Pull Request Checklist

- [ ] Tests added or updated
- [ ] Documentation updated
- [ ] No secrets committed
- [ ] Security impact considered
- [ ] Financial-advice language avoided
- [ ] License headers preserved
