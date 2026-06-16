# Mike Malburg
## Website

This is the personal website repository for Mike Malburg.

### Tech Stack
- **Jekyll** - Static site generator
- **GitHub Pages** - Hosting
- **Markdown** - Content authoring

### Color Palette
- Primary: OpenCode Blue (#2b5a8e)
- Secondary: Grey (#6c757d)
- Accent: Orange (#fd7e14)

### Getting Started
1. Clone the repository
2. Run `bundle install`
3. Run `jekyll serve`
4. Visit `http://localhost:4000`

### Structure
- `_posts/` - Blog posts (markdown)
- `_pages/` - Static pages (markdown)
- `_includes/` - Reusable HTML components
- `_layouts/` - Page templates
- `assets/` - Images, CSS, JS

### Deployment

**GitHub Pages** (Automatic)
```
git push origin main
```

**AWS S3** (Manual)
1. Install AWS CLI and configure: `aws configure`
2. Run: `bash deploy.sh` (Linux/Mac) or `./deploy.sh`
   - On Windows: install WSL or use PowerShell equivalent commands

Site URL after deploy: `http://mikemalburg.com.s3-website-us-east-1.amazonaws.com`

To add a custom domain, point your DNS to the S3 bucket endpoint.
