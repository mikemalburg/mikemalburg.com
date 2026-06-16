---
name: jekyll-migration
description: Migrate Jekyll sites between platforms. Use when changing hosting or updating gems.
---

# Jekyll Migration

Use this skill when:
- Moving site from GitHub Pages to another host
- Updating Gemfile for cross-platform compatibility

## Replace github-pages with Standalone Gems

See scripts/update_gemfile.py helper script.

## Add Linux Platform

bundle lock --add-platform x86_64-linux

## Verify Build

bundle install && bundle exec jekyll build
