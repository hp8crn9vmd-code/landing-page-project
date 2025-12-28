#!/usr/bin/env python3
"""
GitHub Publishing Automation for Kaggle Notebooks

This script securely publishes the landing page project to GitHub
using Kaggle Secrets for token storage and git commands for deployment.

Usage:
    python tools/publish.py --token-secret GITHUB_TOKEN --username yourusername --repo landing-page
"""

import os
import sys
import subprocess
import argparse
from pathlib import Path
import time

def run_command(cmd, cwd=None, capture_output=True):
    """Run a shell command safely."""
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            cwd=cwd,
            capture_output=capture_output,
            text=True,
            timeout=30
        )
        return result.returncode, result.stdout, result.stderr
    except subprocess.TimeoutExpired:
        return 1, "", f"Command timed out: {cmd}"
    except Exception as e:
        return 1, "", f"Error running command: {e}"

def check_git_installed():
    """Check if git is available in the system."""
    return_code, stdout, stderr = run_command("git --version")
    return return_code == 0

def setup_git_config(username, email=None):
    """Configure git with user information."""
    if not email:
        email = f"{username}@users.noreply.github.com"
    
    commands = [
        f"git config --global user.name '{username}'",
        f"git config --global user.email '{email}'",
        "git config --global init.defaultBranch main",
        "git config --global pull.rebase false"
    ]
    
    for cmd in commands:
        return_code, stdout, stderr = run_command(cmd)
        if return_code != 0:
            print(f"Warning: {cmd} failed: {stderr}")
    
    print("Git configuration set")

def initialize_git_repo(project_dir):
    """Initialize a new git repository."""
    print(f"Initializing git repository in: {project_dir}")
    
    if (project_dir / ".git").exists():
        print("Git repository already exists")
        return True
    
    return_code, stdout, stderr = run_command("git init", cwd=project_dir)
    if return_code == 0:
        print("Git repository initialized")
        return True
    else:
        print(f"Failed to initialize git: {stderr}")
        return False

def add_git_remote(project_dir, username, repo_name, token):
    """Add GitHub remote repository."""
    remote_url = f"https://{token}@github.com/{username}/{repo_name}.git"
    
    print(f"Adding remote: https://github.com/{username}/{repo_name}")
    
    return_code, stdout, stderr = run_command("git remote -v", cwd=project_dir)
    if "origin" in stdout:
        return_code, stdout, stderr = run_command(
            f"git remote set-url origin {remote_url}",
            cwd=project_dir
        )
    else:
        return_code, stdout, stderr = run_command(
            f"git remote add origin {remote_url}",
            cwd=project_dir
        )
    
    if return_code == 0:
        print("Remote repository configured")
        return True
    else:
        print(f"Failed to add remote: {stderr}")
        return False

def create_gitignore(project_dir):
    """Create .gitignore file for Kaggle environment."""
    gitignore_content = """
# Kaggle specific
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
.ipynb_checkpoints/
kaggle/
working/
input/
lib/

# Environment
.env
.env.local
.env.development.local
.env.test.local
.env.production.local

# Dependencies
node_modules/
.pnp
.pnp.js
yarn.lock
package-lock.json

# Production
build/
dist/
out/

# Development
.cache/
.tmp/
.temp/

# Logs
logs
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*
lerna-debug.log*

# Runtime data
pids
*.pid
*.seed
*.pid.lock

# Coverage
coverage/
*.lcov

# System
.DS_Store
Thumbs.db
desktop.ini

# IDE
.vscode/
.idea/
*.swp
*.swo
*~
"""
    
    gitignore_path = project_dir / ".gitignore"
    gitignore_path.write_text(gitignore_content.strip())
    print(".gitignore file created")

def stage_and_commit(project_dir, commit_message=None):
    """Stage all changes and create a commit."""
    if not commit_message:
        commit_message = f"Deploy landing page from Kaggle - {time.strftime('%Y-%m-%d %H:%M:%S')}"
    
    print("Staging files...")
    return_code, stdout, stderr = run_command("git add .", cwd=project_dir)
    if return_code != 0:
        print(f"Failed to stage files: {stderr}")
        return False
    
    print("Creating commit...")
    return_code, stdout, stderr = run_command(
        f'git commit -m "{commit_message}"',
        cwd=project_dir
    )
    
    if return_code == 0:
        print(f"Commit created: {commit_message}")
        return True
    elif "nothing to commit" in stderr.lower():
        print("No changes to commit")
        return True
    else:
        print(f"Failed to commit: {stderr}")
        return False

def push_to_github(project_dir, branch="main"):
    """Push changes to GitHub."""
    print(f"Pushing to GitHub (branch: {branch})...")
    
    print("Checking for remote changes...")
    return_code, stdout, stderr = run_command(
        f"git pull origin {branch} --allow-unrelated-histories",
        cwd=project_dir
    )
    
    return_code, stdout, stderr = run_command(
        f"git push -u origin {branch}",
        cwd=project_dir
    )
    
    if return_code == 0:
        print("Successfully pushed to GitHub!")
        return True
    else:
        print(f"Push failed: {stderr}")
        return False

def verify_deployment(username, repo_name):
    """Verify the deployment was successful."""
    import requests
    
    repo_url = f"https://github.com/{username}/{repo_name}"
    print(f"Verifying deployment: {repo_url}")
    
    try:
        response = requests.get(repo_url, timeout=10)
        if response.status_code == 200:
            print("Repository is accessible on GitHub")
            return True
        else:
            print(f"Repository returned status: {response.status_code}")
            return False
    except Exception as e:
        print(f"Could not verify deployment: {e}")
        return True

def main():
    parser = argparse.ArgumentParser(description="Publish project to GitHub from Kaggle")
    parser.add_argument("--token-secret", required=True, help="Kaggle Secret name for GitHub token")
    parser.add_argument("--username", required=True, help="GitHub username or organization")
    parser.add_argument("--repo", required=True, help="Repository name")
    parser.add_argument("--branch", default="main", help="Branch name (default: main)")
    parser.add_argument("--email", help="Git commit email (default: username@users.noreply.github.com)")
    parser.add_argument("--commit-message", help="Custom commit message")
    
    args = parser.parse_args()
    
    print("GitHub Publishing Automation")
    print("=" * 40)
    
    token = os.environ.get(args.token_secret)
    if not token:
        print(f"Error: Kaggle Secret '{args.token_secret}' not found")
        print("Make sure to add it in Kaggle Notebook: Add-ons -> Secrets")
        sys.exit(1)
    
    token_mask = f"{token[:4]}...{token[-4:]}" if len(token) > 8 else "***"
    print(f"GitHub token loaded: {token_mask}")
    
    if not check_git_installed():
        print("Git is not installed or not in PATH")
        print("In Kaggle, install git with: !apt-get update && apt-get install -y git")
        sys.exit(1)
    
    project_dir = Path(__file__).parent.parent
    
    setup_git_config(args.username, args.email)
    
    if not initialize_git_repo(project_dir):
        sys.exit(1)
    
    create_gitignore(project_dir)
    
    if not add_git_remote(project_dir, args.username, args.repo, token):
        sys.exit(1)
    
    if not stage_and_commit(project_dir, args.commit_message):
        sys.exit(1)
    
    if not push_to_github(project_dir, args.branch):
        sys.exit(1)
    
    verify_deployment(args.username, args.repo)
    
    print("Deployment complete!")
    print(f"Repository: https://github.com/{args.username}/{args.repo}")
    print(f"GitHub Pages (if enabled): https://{args.username}.github.io/{args.repo}")
    print("Next steps:")
    print("  1. Enable GitHub Pages in repository settings")
    print("  2. Configure custom domain if needed")
    print("  3. Set up GitHub Actions for automatic updates")

if __name__ == "__main__":
    main()
