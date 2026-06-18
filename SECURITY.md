# Security Policy

## Supported Versions

Public GitHub releases are experimental until v1.0.0.

## Reporting Vulnerabilities

Please report vulnerabilities privately to the maintainers before public disclosure.

Do not open public issues containing:
- API keys
- Telegram bot tokens
- Exchange secrets
- Wallet private keys
- User credentials
- Exploit details that can harm users

## Secret Handling

Never commit secrets. Use:

- `.env` locally
- GitHub Actions Secrets for CI/CD
- Cloud secret managers for production

## Public Repo Safety Rules

- `.env` must remain ignored
- `.env.example` must contain placeholders only
- No real API key must be used in tests
- Donation wallet addresses are public donation identifiers only
- Private keys must never be stored in the repository
