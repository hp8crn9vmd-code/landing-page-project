# 2D Motion Landing Page (Kaggle to GitHub)

A production-grade, fully 2D animated landing page built entirely inside a Kaggle Notebook and published to GitHub via Kaggle Secrets.

## Project Structure

/kaggle/working/landing-page-project/
├── index.html
├── styles/main.css
├── scripts/main.js
├── assets/favicon.svg
├── tools/preview.py
└── README.md

## Quick Preview

```python
%cd /kaggle/working/landing-page-project
!python tools/preview.py --port 8080
```

Then:
1. Enable Internet in Add-ons
2. Copy notebook URL from ... menu -> Copy Host URL
3. Append :8080
4. Open in new tab

## Features

- Pure HTML/CSS/JS - No frameworks
- 2D Motion System - CSS animations & SVG
- Mobile-First Responsive
- Accessibility First
- Kaggle-Native
- GitHub-Ready

## Development Status

- [x] Project structure & baseline files
- [x] Design system
- [x] Core components
- [ ] 2D animations
- [ ] Scroll-triggered effects
- [ ] Performance optimization
- [ ] GitHub publishing
## Deployment to GitHub

### Quick Deployment from Kaggle
```python
# Run in Kaggle notebook (with internet enabled)
!cd /kaggle/working/landing-page-project && \
    python tools/publish.py \
    --token-secret GITHUB_TOKEN \
    --username your-username \
    --repo landing-page \
    --commit-message "Deploy from Kaggle"
```

### Prerequisites
1. GitHub Personal Access Token with `repo` scope
2. Kaggle Secret named `GITHUB_TOKEN` containing the token
3. Internet enabled in Kaggle notebook

### Steps
1. Add GitHub token to Kaggle Secrets
2. Run the deployment script
3. Enable GitHub Pages in repository settings
4. Access at: `https://your-username.github.io/landing-page`

### GitHub Actions CI/CD
The project includes GitHub Actions workflow that automatically deploys to GitHub Pages on every push to the main branch.

For detailed instructions, see [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md).


---

Built with Kaggle-first constraints in mind.