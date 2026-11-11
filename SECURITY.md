# Security Policy

## Reporting a vulnerability
Do not publish credentials, personal data, or exploitable vulnerability details in a public issue.

Use GitHub's private vulnerability reporting feature if enabled. Otherwise, contact the repository maintainer privately through GitHub. Include a concise description, affected component, potential impact, and safe reproduction steps. Do not include real secrets or sensitive personal information.

## Security practices
- Never commit API keys, tokens, passwords, private keys, or production data.
- Keep secrets in environment variables or an approved secret manager.
- Review dependencies and their provenance before adding them.
- Validate untrusted input and treat external data and model output as untrusted.
- If a secret is exposed, revoke or rotate it; deleting the file from Git history does not revoke it.

Security fixes are considered for the default branch while the project is actively maintained. No response-time guarantee is made.
