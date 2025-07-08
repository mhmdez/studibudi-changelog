#!/usr/bin/env python3
"""
Changelog Cleanup Script
Filters out technical noise and creates a clean, user-focused changelog
"""

import json
import re
from datetime import datetime
from typing import List, Dict, Any

def is_meaningless_commit(commit: Dict[str, Any]) -> bool:
    """
    Check if a commit is meaningless from an end user perspective
    """
    message = commit.get('message', '').lower()
    author_name = commit.get('author', {}).get('name', '').lower()
    
    # Filter out bot commits
    if 'bot' in author_name or 'gpt-engineer' in author_name:
        return True
    
    # Filter out merge commits
    if message.startswith('merge pull request') or message.startswith('merge branch'):
        return True
    
    # Filter out only the most technical noise - reduced list
    technical_keywords = [
        'lovable', 'code editor', 'edited ui in lovable',
        'code edited in lovable', 'lovable code editor',
        'vite.config', 'package.json', 'package-lock',
        'yarn.lock', 'bun.lockb', 'eslint', 'prettier',
        'github workflow', 'release drafter', 'ci/cd',
        'grant contents:write', 'disable pr trigger',
        'auto-generated', 'version bump', 'release notes',
        'pr title guide', 'setup documentation',
        '__pycache__', 'ignore list', 'binary file',
        'logging configuration', 'logging calls',
        'rls policies', 'database schema', 'instruction_cache',
        'build script', 'deployment', 'docker', 'kubernetes',
        'environment variable', 'env var', 'config var',
        'devlogger', 'console.log', 'debug log'
    ]
    
    for keyword in technical_keywords:
        if keyword in message:
            return True
    
    # Filter out very short messages only
    if len(message.strip()) < 8:
        return True
    
    # Filter out only the most generic file update patterns
    generic_patterns = [
        r'^update.*\.lock$',  # lock files
        r'^update.*\.json$',  # config files
        r'^update.*\.ya?ml$', # yaml files
        r'^add.*\.gitignore$', # gitignore
        r'^remove.*\.gitignore$', # gitignore
    ]
    
    for pattern in generic_patterns:
        if re.match(pattern, message.strip()):
            return True
    
    return False

def clean_commit_message(message: str) -> str:
    """
    Clean up commit message to be more user-friendly
    """
    # Remove merge commit prefixes
    message = re.sub(r'^Merge pull request #\d+ from [^\n]+\n+', '', message)
    
    # Remove conventional commit prefixes
    message = re.sub(r'^(feat|fix|chore|docs|style|refactor|test|build|ci|perf)(\([^)]*\))?\s*:\s*', '', message)
    
    # Remove PR numbers and links
    message = re.sub(r'\s*\(#\d+\)', '', message)
    message = re.sub(r'\s*closes?\s+#\d+', '', message, flags=re.IGNORECASE)
    message = re.sub(r'\s*fixes?\s+#\d+', '', message, flags=re.IGNORECASE)
    
    # Take only the first line (title) and split on semicolon to get main action
    message = message.split('\n')[0].split(';')[0].strip()
    
    # Clean up technical terms - more conservative
    replacements = {
        'component': 'interface',
        'components': 'interfaces',
        'api': 'service',
        'apis': 'services',
        'endpoint': 'feature',
        'endpoints': 'features',
        'auth': 'authentication',
        'ui': 'interface',
        'ux': 'user experience',
        'implement': 'add',
        'functionality': 'feature',
        'hook': 'feature',
        'hooks': 'features',
        'pdf': 'document',
        'pdfs': 'documents',
        'backend': 'service',
        'frontend': 'interface',
    }
    
    for old, new in replacements.items():
        message = re.sub(rf'\b{old}\b', new, message, flags=re.IGNORECASE)
    
    # Remove file extensions
    message = re.sub(r'\.(tsx?|jsx?|py|md|json|ya?ml|css|scss|html|sql)', '', message)
    
    # Remove file paths - be more conservative
    message = re.sub(r'\b(src|components|pages|hooks|lib|utils)/[^\s]*', '', message)
    
    # Remove only the most technical jargon
    message = re.sub(r'\b(RLS|SQL|HTTP|API|URL|URI|JSON|XML|HTML|CSS|JS|TS)\b', '', message)
    
    # Clean up extra spaces and punctuation
    message = re.sub(r'\s+', ' ', message)
    message = re.sub(r'[;,]\s*$', '', message)
    message = re.sub(r'^\s*[-\s]+', '', message)
    
    # Capitalize first letter and clean up
    message = message.strip()
    if message:
        message = message[0].upper() + message[1:]
    
    return message

def is_user_facing_feature(message: str) -> bool:
    """
    Check if a commit message represents a user-facing feature - more inclusive
    """
    message_lower = message.lower()
    
    # Automatically include anything that mentions user-facing concepts
    user_facing_keywords = [
        'voice', 'audio', 'chat', 'conversation', 'talk', 'speak',
        'tutor', 'ai', 'learning', 'study', 'education', 'student',
        'quiz', 'test', 'assessment', 'question', 'answer',
        'session', 'lesson', 'course', 'curriculum',
        'dashboard', 'profile', 'progress', 'tracking',
        'note', 'annotation', 'highlight', 'bookmark',
        'document', 'pdf', 'file', 'upload', 'download',
        'mobile', 'responsive', 'touch', 'gesture',
        'interface', 'design', 'layout', 'theme', 'style',
        'personalization', 'customization', 'preference',
        'notification', 'alert', 'reminder',
        'search', 'filter', 'sort', 'navigation',
        'login', 'authentication', 'account', 'user',
        'subscription', 'payment', 'billing', 'credit',
        'feedback', 'rating', 'review', 'comment',
        'share', 'collaborate', 'team', 'group',
        'export', 'import', 'sync', 'backup',
        'accessibility', 'language', 'translation',
        'speed', 'performance', 'loading', 'fast',
        'button', 'menu', 'sidebar', 'header', 'footer',
        'page', 'screen', 'view', 'display', 'show',
        'hide', 'toggle', 'switch', 'enable', 'disable',
        'add', 'remove', 'update', 'change', 'modify',
        'improve', 'enhance', 'better', 'fix', 'resolve',
        'create', 'build', 'make', 'develop', 'implement',
        'feature', 'functionality', 'capability', 'option',
        'setting', 'configuration', 'control', 'panel',
        'form', 'input', 'field', 'validation', 'error',
        'message', 'text', 'content', 'data', 'information',
        'icon', 'image', 'picture', 'graphic', 'visual',
        'color', 'font', 'size', 'spacing', 'margin',
        'animation', 'transition', 'effect', 'interaction',
        'click', 'hover', 'focus', 'scroll', 'swipe',
        'drag', 'drop', 'select', 'choose', 'pick',
        'connect', 'disconnect', 'sync', 'refresh', 'reload',
        'save', 'load', 'open', 'close', 'start', 'stop',
        'pause', 'resume', 'play', 'record', 'capture',
        'edit', 'delete', 'copy', 'paste', 'cut', 'undo',
        'redo', 'cancel', 'confirm', 'submit', 'send',
        'receive', 'get', 'fetch', 'retrieve', 'obtain'
    ]
    
    # Check if message contains any user-facing keywords
    if any(keyword in message_lower for keyword in user_facing_keywords):
        return True
    
    # Also include if it's categorized as a user-facing group
    return True  # Be inclusive - let categorization handle the rest

def categorize_commit(commit: Dict[str, Any]) -> str:
    """
    Categorize commits into user-friendly groups
    """
    message = commit.get('message', '').lower()
    group = commit.get('group', '').lower()
    
    # Check message content for better categorization
    if any(keyword in message for keyword in ['voice', 'audio', 'chat', 'tutor', 'ai', 'learning', 'study', 'quiz', 'session', 'dashboard', 'profile', 'add', 'create', 'new', 'implement', 'introduce']):
        return '🚀 New Features'
    
    if any(keyword in message for keyword in ['improve', 'enhance', 'better', 'update', 'redesign', 'mobile', 'responsive', 'optimize', 'change', 'modify', 'adjust']):
        return '✨ Improvements'
    
    if any(keyword in message for keyword in ['fix', 'resolve', 'correct', 'bug', 'issue', 'problem', 'error', 'solve']):
        return '🐛 Bug Fixes'
    
    if any(keyword in message for keyword in ['faster', 'speed', 'performance', 'quick', 'loading', 'optimize', 'efficient']):
        return '⚡ Performance'
    
    # Use existing group as fallback
    if 'feature' in group:
        return '🚀 New Features'
    elif 'improvement' in group:
        return '✨ Improvements'
    elif 'bug' in group or 'fix' in group:
        return '🐛 Bug Fixes'
    elif 'performance' in group:
        return '⚡ Performance'
    
    return '✨ Improvements'  # Default category

def process_changelog(json_file: str, output_file: str):
    """
    Process the JSON changelog and create a clean markdown file
    """
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            changelog_data = json.load(f)
    except FileNotFoundError:
        print(f"Error: File {json_file} not found")
        return
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in {json_file}")
        return
    
    # Group commits by category
    categories = {
        '🚀 New Features': [],
        '✨ Improvements': [],
        '🐛 Bug Fixes': [],
        '⚡ Performance': []
    }
    
    total_commits = 0
    filtered_commits = 0
    
    # Process each version
    for version_data in changelog_data:
        commits = version_data.get('commits', [])
        total_commits += len(commits)
        
        for commit in commits:
            if is_meaningless_commit(commit):
                filtered_commits += 1
                continue
            
            cleaned_message = clean_commit_message(commit.get('message', ''))
            
            # Skip if message becomes empty after cleaning
            if not cleaned_message or len(cleaned_message) < 5:
                filtered_commits += 1
                continue
            
            # More lenient user-facing check
            if not is_user_facing_feature(cleaned_message):
                filtered_commits += 1
                continue
            
            category = categorize_commit(commit)
            categories[category].append(cleaned_message)
    
    # Generate markdown
    markdown_content = generate_markdown(categories)
    
    # Write to file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(markdown_content)
    
    print(f"✅ Processed {total_commits} commits")
    print(f"🗑️  Filtered out {filtered_commits} meaningless commits")
    print(f"📝 Generated clean changelog: {output_file}")
    
    # Show category breakdown
    for category, items in categories.items():
        if items:
            print(f"{category}: {len(items)} items")

def generate_markdown(categories: Dict[str, List[str]]) -> str:
    """
    Generate clean markdown from categorized commits
    """
    content = []
    
    # Header
    content.append("# 📚 StudiBudi Product Updates")
    content.append("")
    content.append("*Your AI-powered study companion keeps getting better! Here's what's new for students and educators.*")
    content.append("")
    content.append("---")
    content.append("")
    content.append("## Recent Updates")
    content.append("")
    
    # Add categories with content
    for category, items in categories.items():
        if items:
            content.append(f"### {category}")
            content.append("")
            
            # Remove duplicates and sort
            unique_items = list(set(items))
            unique_items.sort()
            
            for item in unique_items:
                content.append(f"- {item}")
            content.append("")
    
    # Add message if no content
    if not any(categories.values()):
        content.append("### 📝 No Recent Updates")
        content.append("")
        content.append("*The changelog is being processed. Check back soon for the latest updates!*")
        content.append("")
    
    # Footer
    content.append("---")
    content.append("")
    content.append("### 🔗 Quick Links")
    content.append("- **📖 [User Guide](https://studibudi.com/docs)** - Learn how to use new features")
    content.append("- **💬 [Support](https://studibudi.com/support)** - Get help from our team")
    content.append("- **📧 [Feedback](mailto:feedback@studibudi.com)** - Tell us what you think")
    content.append("")
    content.append("---")
    content.append("")
    content.append(f"*Updated automatically • Last refresh: {datetime.now().strftime('%B %d, %Y')}*")
    
    return "\n".join(content)

if __name__ == "__main__":
    # Process the changelog
    process_changelog("CHANGELOG copy.json", "CHANGELOG_CLEAN.md") 