---
name: github-actions-jekyll-ci
description: Set up GitHub Actions CI/CD for Jekyll builds with AWS deployment.
---

# GitHub Actions Jekyll CI

Use this skill when:
- Creating deploy workflow in .github/workflows/

## Workflow Steps

1. Checkout code
2. Setup Ruby 3.2 with bundler-cache: true
3. Build site with bundle exec jekyll build
4. Deploy to S3

## Required Secrets

AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
