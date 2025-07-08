# 📚 StudiBudi Product Changelog

This repository automatically generates a **professional product changelog** for StudiBudi's AI-powered learning platform, combining updates from both repositories:

- **Backend**: [github.com/mhmdez/studibudi](https://github.com/mhmdez/studibudi)
- **Frontend**: [github.com/mhmdez/studi-budi-ai-tutor](https://github.com/mhmdez/studi-budi-ai-tutor)

## 📋 View the Live Changelog

**🔗 [StudiBudi Product Updates](https://mhmdez.github.io/studibudi-changelog/CHANGELOG.md)**

*Professional changelog designed for students, educators, and stakeholders*

## 🎯 What Makes This Special

### Ultra-Selective Content
Only **major user-facing updates** are included:

- 🚀 **Major New Features** - Core functionality like voice chat, AI tutoring, personalized learning
- ✨ **Notable Improvements** - UI/UX enhancements, better navigation, mobile optimization  
- ⚡ **Performance Enhancements** - Speed improvements users actually notice

### Professional Presentation
- **User-friendly descriptions** instead of technical commit messages
- **Product marketing language** that explains benefits to users
- **Clean formatting** with emojis and proper categorization
- **Quick links** to documentation and support

## 🚫 What's Filtered Out

Technical noise is completely removed:
- ❌ Bug fixes and minor tweaks
- ❌ Code refactoring and internal changes
- ❌ Developer tooling and build processes
- ❌ Documentation and testing updates
- ❌ File names, technical jargon, and commit hashes
- ❌ Administrative and configuration changes

## 🔄 Automated Transformation

The system intelligently transforms technical commits into user-friendly descriptions:

**Before:**
```
feat: implement voice interaction with AI tutor using WebRTC
```

**After:**
```
🎙️ Voice Chat with AI Tutor - Have natural conversations while studying
```

## ⚙️ How It Works

1. **Scans** both repositories every 12 hours
2. **Filters** for only major user-facing features
3. **Transforms** commit messages into product descriptions
4. **Publishes** to GitHub Pages automatically
5. **Limits** to ~15 most important recent updates

## 🔧 Configuration

### Ultra-Selective Filtering
The `cliff.toml` configuration targets specific keywords:
- Voice, audio, chat, tutor, AI capabilities
- Learning, study, personalization features  
- Dashboard, progress, quiz functionality
- Major UI, interface, and design updates
- Performance improvements users notice

### Professional Descriptions
The workflow transforms technical terms:
- `component` → `feature`
- `API` → `service` 
- `database` → `data`
- Removes file extensions and technical paths
- Adds emoji and professional language

## 🎨 Example Output

```markdown
# 📚 StudiBudi Product Updates

## 🚀 Major New Features
- 🎙️ **Voice Chat with AI Tutor** - Have natural conversations while studying
- 📊 **Progress Tracking** - See your learning journey and achievements

## ✨ Notable Improvements  
- 📱 **Mobile Optimization** - Perfect experience on any device
- 🧭 **Easier Navigation** - Find what you need faster

## ⚡ Performance Enhancements
- ⚡ **Faster Performance** - Everything loads and responds quicker
```

## 🚀 Benefits for Different Audiences

### For Students & Educators
- Clear understanding of new features
- No technical complexity
- Focus on learning benefits

### For Product Teams
- Professional changelog for stakeholders
- Marketing-ready descriptions
- Automated maintenance

### For Investors & Partners
- Clean overview of product evolution
- Professional presentation
- Evidence of continuous improvement

## 🔑 Setup Requirements

Requires a GitHub Personal Access Token with `repo:read` scope:
1. Create token with `repo` permissions only
2. Add as `GH_TOKEN` secret in repository settings
3. Workflow runs automatically every 12 hours

## 🔍 Manual Control

- **Trigger manually**: Actions → combined-changelog → Run workflow
- **Adjust frequency**: Edit cron schedule in workflow file
- **Modify filtering**: Update keyword patterns in `cliff.toml`
- **Change descriptions**: Edit transformation rules in workflow

---

*Professional product changelog • Updated automatically • Zero maintenance* 