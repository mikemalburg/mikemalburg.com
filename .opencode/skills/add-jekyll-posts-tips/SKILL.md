# How to Add New Jekyll Posts

## File Naming Convention

Posts go in _posts/ folder:
YYYY-MM-DD-title.md

Examples: 2026-06-16-post-name.md, 2026-07-01-update.md

## Post Frontmatter

---
layout: post
title: Your Title
date: YYYY-MM-DD HH:MM:SS +0000
categories: tech
tags: tag1, tag2
---

Write markdown content after frontmatter.

## Testing Locally

bundle exec jekyll serve --future

## Push to GitHub

CI/CD builds and deploys to AWS S3 automatically.
