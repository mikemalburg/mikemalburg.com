---
name: aws-s3-cloudfront-deploy
description: Deploy Jekyll sites to AWS S3 with CloudFront HTTPS support. Use when migrating from GitHub Pages or setting up new hosting with custom domain and SSL.
---

# AWS S3 + CloudFront Deployment

Use this skill when:
- Migrating from GitHub Pages to AWS
- Need HTTPS with custom domain
- Setting up CI/CD for Jekyll builds
- CloudFront cache invalidation needed

## Prerequisites

1. **AWS Account** with ACM, S3, CloudFront, Route53 permissions
2. **IAM User** with these policies: AmazonS3FullAccess, AWSCloudFrontFullAccess, AWSCertificateManagerFullAccess, AmazonRoute53FullAccess
3. **AWS CLI configured**: aws configure

## Quick Deploy

`ash
bundle exec jekyll build
aws s3 sync _site/ s3://mikemalburg.com --delete
`

## Python Helper Scripts

See scripts/ directory for utilities to:
- Validate AWS credentials (scripts/check_aws.py)
- Check CloudFront status (scripts/check_cloudfront.py)
- Create invalidation (scripts/invalidate_cf.py)

## GitHub Actions Workflow

Use secrets: AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
