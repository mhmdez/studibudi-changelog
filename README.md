# StudiBudi Combined Changelog

This repository automatically generates and maintains a unified changelog for both StudiBudi repositories:

- **Backend**: [github.com/mhmdez/studibudi](https://github.com/mhmdez/studibudi)
- **Frontend**: [github.com/mhmdez/studi-budi-ai-tutor](https://github.com/mhmdez/studi-budi-ai-tutor)

## 📋 View the Changelog

The changelog is automatically published via GitHub Pages:

**🔗 [View Live Changelog](https://mhmdez.github.io/studibudi-changelog/CHANGELOG.md)**

## 🤖 How It Works

This repository uses [git-cliff](https://git-cliff.org/) to automatically:

1. **Fetch** the complete git history from both repositories
2. **Parse** conventional commits (feat:, fix:, chore:, etc.)
3. **Generate** a unified changelog in reverse chronological order
4. **Update** the changelog twice daily via GitHub Actions

## ⚙️ Configuration

### Schedule
The changelog updates automatically every 12 hours (twice daily) via GitHub Actions.

### Commit Parsing
The configuration in `cliff.toml` categorizes commits into:

- 🚀 **Features** (`feat:`)
- 🐛 **Bug Fixes** (`fix:`) 
- 📚 **Documentation** (`doc:`)
- ⚡ **Performance** (`perf:`)
- �� **Refactor** (`refactor:`)
- 🎨 **Styling** (`style:`)
- 🧪 **Testing** (`test:`)
- ⚙️ **Miscellaneous Tasks** (`chore:`, `ci:`)
- 🛡️ **Security** (any commit mentioning security)
- ◀️ **Revert** (`revert:`)

## 🔧 Manual Operations

### Trigger Manual Update
1. Go to **Actions** → **combined-changelog**
2. Click **Run workflow**
3. The changelog will update within a few minutes

### Modify Update Schedule
Edit the cron expression in `.github/workflows/git-cliff.yml`:

```yaml
schedule:
  - cron: "0 */12 * * *"  # Current: every 12 hours
  # - cron: "0 6 * * *"   # Alternative: daily at 6 AM UTC
  # - cron: "0 */6 * * *"  # Alternative: every 6 hours
```

### Customize Commit Categories
Edit `cliff.toml` to modify how commits are categorized:

```toml
commit_parsers = [
    { message = "^feat", group = "<!-- 0 -->🚀 Features" },
    { message = "^fix", group = "<!-- 1 -->🐛 Bug Fixes" },
    # Add custom patterns here
]
```

## 🔑 Required Secrets

This repository requires a GitHub Personal Access Token with `repo:read` scope:

1. **Create Token**: GitHub Settings → Developer Settings → Personal Access Tokens → Tokens (classic)
2. **Permissions**: Select only `repo` scope
3. **Add Secret**: Repository Settings → Secrets and Variables → Actions → New repository secret
4. **Name**: `GH_TOKEN`

## 🚀 Zero Maintenance

Once set up, this system requires **no manual maintenance**:

- ✅ Automatically fetches new commits from both repositories
- ✅ Generates changelog in standardized format
- ✅ Updates GitHub Pages automatically
- ✅ Costs $0 to run
- ✅ Works with any number of repositories

## 🔍 Troubleshooting

### Changelog Not Updating
- Check that the GitHub Action is running successfully
- Verify the `GH_TOKEN` secret has proper permissions
- Ensure both source repositories are accessible

### Missing Commits
- Verify commits follow conventional commit format
- Check `cliff.toml` for filtering rules
- Ensure commits aren't being skipped by configuration

### GitHub Pages Not Working
- Verify Pages is enabled in repository Settings
- Check that the source is set to "Deploy from a branch: main / (root)"
- Ensure `CHANGELOG.md` exists in the repository root

---

*Last updated: Automatically via GitHub Actions*
