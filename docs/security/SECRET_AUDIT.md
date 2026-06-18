# Secret Audit Guide

Before pushing to GitHub:

```bash
git status
git diff --cached
grep -R "TELEGRAM_BOT_TOKEN=" . --exclude-dir=.git
grep -R "API_SECRET" . --exclude-dir=.git
grep -R "PRIVATE_KEY" . --exclude-dir=.git
```

Recommended tools:
- gitleaks
- trufflehog
- GitHub secret scanning

Never commit:
- API keys
- Exchange secrets
- Bot tokens
- Private keys
- Seed phrases
- Production database URLs
