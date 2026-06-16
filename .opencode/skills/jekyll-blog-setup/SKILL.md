---
name: jekyll-blog-setup
description: Convert static Jekyll pages to blog with posts collection. Use when adding blogging functionality.
---

# Jekyll Blog Setup

Use this skill when:
- Converting static site to blog (Home = blog index)
- Adding posts collection

## Steps

1. Create _posts/ directory with YYYY-MM-DD-title.md files
2. Create _layouts/post.html for individual posts
3. Update index.html to list site.posts
4. Add jekyll-feed plugin

## Python Helper Scripts

scripts/create_post.py - Generate post file with frontmatter
scripts/update_index.py - Update home page with recent posts
