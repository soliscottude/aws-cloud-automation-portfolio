# CI/CD Demo – GitHub Actions

This folder contains an example **GitHub Actions workflow** used during my learning journey.

The goal of this workflow is to show that I can:

- Use **GitHub Actions** to run automation on every push
- Install Python and project dependencies
- Run my AWS automation script in **simulation mode**
- (Optionally) deploy or upload artefacts to AWS

## Workflow file

- `aws_automation_ci.yaml` – example CI pipeline (copied from my original learning repo)

Example structure:

- Trigger on `push` to `main`
- Use `actions/checkout` to pull the repo
- Use `actions/setup-python` to install Python
- Install dependencies from `automation_manager/requirements.txt`
- Run:

```
python -m automation_manager.main
```

Why this matters
- This CI/CD demo shows that I understand:
- How to configure workflow triggers
- How to use GitHub-hosted runners
- How to integrate my Python automation project into a CI pipeline
- How to keep the workflow safe by running in simulation mode (no real AWS changes)