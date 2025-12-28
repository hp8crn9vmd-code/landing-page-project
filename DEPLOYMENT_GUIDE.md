# Deployment Guide: Kaggle to GitHub

This guide explains how to deploy your 2D motion landing page from Kaggle to GitHub Pages.

## Prerequisites

1. **GitHub Account** with repository creation permissions
2. **Kaggle Notebook** with internet enabled
3. **GitHub Personal Access Token** with `repo` scope

## Setting Up Kaggle Secrets

1. In your Kaggle notebook, click **"Add-ons"** -> **"Secrets"**
2. Add a new secret with:
   - **Name:** `GITHUB_TOKEN`
   - **Value:** Your GitHub Personal Access Token

## Automated Deployment

Run the deployment script from your Kaggle notebook:

```python
!cd /kaggle/working/landing-page-project && \
    python tools/publish.py \
    --token-secret GITHUB_TOKEN \
    --username YOUR_GITHUB_USERNAME \
    --repo YOUR_REPO_NAME \
    --branch main \
    --commit-message "Deploy from Kaggle"
```

**Parameters:**
- `--token-secret`: Kaggle Secret name (default: GITHUB_TOKEN)
- `--username`: Your GitHub username or organization
- `--repo`: Repository name (will be created if doesn't exist)
- `--branch`: Branch to deploy to (default: main)
- `--commit-message`: Custom commit message

## Manual Deployment Steps

If the automated script fails, follow these manual steps:

### 1. Initialize Git Repository
```bash
cd /kaggle/working/landing-page-project
git init
git config user.name "Your Name"
git config user.email "your-email@example.com"
```

### 2. Add GitHub Remote
```bash
git remote add origin https://YOUR_TOKEN@github.com/USERNAME/REPO.git
```

### 3. Commit and Push
```bash
git add .
git commit -m "Deploy from Kaggle"
git branch -M main
git push -u origin main
```

## Enabling GitHub Pages

After deployment:

1. Go to your GitHub repository -> **Settings** -> **Pages**
2. Under **Source**, select:
   - **Branch:** `main`
   - **Folder:** `/` (root)
3. Click **Save**

Your site will be available at:
- `https://USERNAME.github.io/REPO`
- Or custom domain if configured

## GitHub Actions (CI/CD)

The repository includes a GitHub Actions workflow that:
- Automatically deploys to GitHub Pages on push to `main`
- Can be triggered manually from the Actions tab
- Provides deployment status and logs

## Verification Checklist

After deployment, verify:

- [ ] Repository is public (or you have access)
- [ ] GitHub Pages is enabled and building
- [ ] Site is accessible at the provided URL
- [ ] All assets (CSS, JS, images) load correctly
- [ ] Mobile responsiveness works
- [ ] Animations function properly

## Troubleshooting

### "Permission denied" error
- Verify your GitHub token has `repo` scope
- Check token hasn't expired
- Ensure repository exists and you have write access

### Git not installed in Kaggle
```python
!apt-get update && apt-get install -y git
```

### "Repository not found"
- Create the repository on GitHub first
- Check username and repository name spelling

### GitHub Pages not updating
- Wait a few minutes for build to complete
- Check Actions tab for build errors
- Clear browser cache

## Support

For issues with deployment:
1. Check the [GitHub Status](https://www.githubstatus.com/)
2. Review GitHub Actions logs
3. Ensure Kaggle notebook has internet enabled

## Security Notes

- Never commit tokens or secrets to git
- Use Kaggle Secrets for secure storage
- GitHub tokens should have minimal required permissions
- Consider using GitHub Environments for production

---

*Deployment automation powered by Kaggle Notebooks*
