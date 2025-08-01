import random
from datetime import datetime
import os
import re
import json

# Comprehensive list of VS Code extensions organized by categories
extensions_by_category = {
    "Code Quality & Formatting": [
        {
            "name": "Prettier - Code formatter",
            "id": "esbenp.prettier-vscode",
            "overview": "Prettier is an opinionated code formatter that enforces a consistent style by parsing your code and re-printing it with its own rules, supporting many languages and integrating with most editors.",
            "tags": ["formatter", "code-quality", "javascript", "typescript", "css", "html"]
        },
        {
            "name": "ESLint",
            "id": "dbaeumer.vscode-eslint",
            "overview": "ESLint is a popular linter for JavaScript and TypeScript that helps you find and fix problems in your code, enforcing coding standards and best practices.",
            "tags": ["linter", "javascript", "typescript", "code-quality"]
        },
        {
            "name": "SonarLint",
            "id": "SonarSource.sonarlint-vscode",
            "overview": "SonarLint helps you detect and fix quality issues as you write code. Like a spell checker, SonarLint squiggles quality issues and provides real-time feedback.",
            "tags": ["code-quality", "security", "bugs", "code-smells"]
        },
        {
            "name": "Code Spell Checker",
            "id": "streetsidesoftware.code-spell-checker",
            "overview": "Code Spell Checker is a basic spell checker that works well with code and documents, helping you catch common spelling errors in comments and strings.",
            "tags": ["spell-check", "documentation", "comments"]
        }
    ],
    
    "Git & Version Control": [
        {
            "name": "GitLens — Git supercharged",
            "id": "eamodio.gitlens",
            "overview": "GitLens supercharges the built-in VS Code Git capabilities, providing rich insights into code authorship, history, and more, right in your editor.",
            "tags": ["git", "version-control", "history", "blame"]
        },
        {
            "name": "Git Graph",
            "id": "mhutchie.git-graph",
            "overview": "Git Graph is a powerful extension that visualizes your Git repository with a beautiful graph, making it easy to understand your project's history.",
            "tags": ["git", "visualization", "history", "graph"]
        },
        {
            "name": "Git History",
            "id": "donjayamanne.githistory",
            "overview": "Git History allows you to view the git log, file history, compare branches or commits, and more, all within VS Code.",
            "tags": ["git", "history", "log", "compare"]
        }
    ],
    
    "Web Development": [
        {
            "name": "Live Server",
            "id": "ritwickdey.LiveServer",
            "overview": "Live Server launches a local development server with live reload for static and dynamic pages, making web development faster and easier.",
            "tags": ["web-development", "live-reload", "server", "html", "css"]
        },
        {
            "name": "Auto Rename Tag",
            "id": "formulahendry.auto-rename-tag",
            "overview": "Auto Rename Tag automatically renames paired HTML/XML tags, making it easier to edit markup without breaking tag pairs.",
            "tags": ["html", "xml", "web-development", "auto-rename"]
        },
        {
            "name": "CSS Peek",
            "id": "pranaygp.vscode-css-peek",
            "overview": "CSS Peek allows you to peek and go to CSS definitions directly from HTML files, making it easier to navigate between HTML and CSS.",
            "tags": ["css", "html", "web-development", "navigation"]
        },
        {
            "name": "HTML CSS Support",
            "id": "ecmel.vscode-html-css-support",
            "overview": "HTML CSS Support provides CSS class name completion for HTML documents based on definitions in your workspace.",
            "tags": ["html", "css", "autocomplete", "web-development"]
        }
    ],
    
    "JavaScript & TypeScript": [
        {
            "name": "JavaScript (ES6) code snippets",
            "id": "xabikos.JavaScriptSnippets",
            "overview": "This extension contains code snippets for JavaScript in ES6 syntax for VS Code editor.",
            "tags": ["javascript", "snippets", "es6", "productivity"]
        },
        {
            "name": "TypeScript Importer",
            "id": "pmneo.tsimporter",
            "overview": "TypeScript Importer automatically searches for TypeScript definitions in workspace files and provides all available imports.",
            "tags": ["typescript", "imports", "autocomplete", "productivity"]
        },
        {
            "name": "Import Cost",
            "id": "wix.vscode-import-cost",
            "overview": "Import Cost displays the size of the imported package above the import statement, helping you optimize your bundle size.",
            "tags": ["javascript", "typescript", "bundle-size", "optimization"]
        }
    ],
    
    "Python Development": [
        {
            "name": "Python",
            "id": "ms-python.python",
            "overview": "The Python extension provides rich support for the Python language, including features such as IntelliSense, linting, debugging, code navigation, code formatting, refactoring, variable explorer, test explorer, and more.",
            "tags": ["python", "intellisense", "debugging", "linting"]
        },
        {
            "name": "Pylance",
            "id": "ms-python.vscode-pylance",
            "overview": "Pylance is a fast, feature-rich language server for Python in VS Code, providing type checking, auto-imports, and more.",
            "tags": ["python", "type-checking", "language-server", "intellisense"]
        },
        {
            "name": "Python Docstring Generator",
            "id": "njpwerner.autodocstring",
            "overview": "Generates docstrings for Python functions automatically, supporting Google, NumPy, and Sphinx formats.",
            "tags": ["python", "documentation", "docstrings", "productivity"]
        }
    ],
    
    "Database & SQL": [
        {
            "name": "SQLTools",
            "id": "mtxr.sqltools",
            "overview": "SQLTools is a lightweight SQL client with a clean interface, supporting multiple databases and providing syntax highlighting and autocomplete.",
            "tags": ["sql", "database", "query", "client"]
        },
        {
            "name": "SQL Server (mssql)",
            "id": "ms-mssql.mssql",
            "overview": "Microsoft SQL Server extension for VS Code, providing IntelliSense, debugging, and query execution capabilities.",
            "tags": ["sql", "mssql", "database", "microsoft"]
        }
    ],
    
    "Productivity & Navigation": [
        {
            "name": "Path Intellisense",
            "id": "christian-kohler.path-intellisense",
            "overview": "Path Intellisense autocompletes filenames in your code, making it easier to import files and navigate your project.",
            "tags": ["navigation", "autocomplete", "file-paths", "productivity"]
        },
        {
            "name": "Auto Import",
            "id": "steoates.autoimport",
            "overview": "Auto Import automatically finds, parses and provides code actions for all available imports, making it easier to manage imports.",
            "tags": ["imports", "autocomplete", "productivity", "typescript"]
        },
        {
            "name": "Bookmarks",
            "id": "alefragnani.Bookmarks",
            "overview": "Bookmarks helps you navigate in your code, moving between important positions easily and quickly.",
            "tags": ["navigation", "bookmarks", "productivity", "code-navigation"]
        },
        {
            "name": "Bracket Pair Colorizer",
            "id": "CoenraadS.bracket-pair-colorizer",
            "overview": "Bracket Pair Colorizer allows matching brackets to be identified with colors, making it easier to read and debug code with nested structures.",
            "tags": ["brackets", "syntax-highlighting", "readability", "productivity"]
        }
    ],
    
    "Themes & Icons": [
        {
            "name": "Material Icon Theme",
            "id": "PKief.material-icon-theme",
            "overview": "Material Icon Theme provides beautiful icons for VS Code, making it easier to identify file types and navigate your project.",
            "tags": ["icons", "material-design", "file-explorer", "visual"]
        },
        {
            "name": "One Dark Pro",
            "id": "zhuangtongfa.Material-theme",
            "overview": "One Dark Pro is a beautiful dark theme for VS Code, inspired by Atom's One Dark theme.",
            "tags": ["theme", "dark", "one-dark", "visual"]
        },
        {
            "name": "Dracula Official",
            "id": "dracula-theme.theme-dracula",
            "overview": "Dracula is a dark theme for VS Code and many other applications, featuring a carefully selected color palette.",
            "tags": ["theme", "dark", "dracula", "visual"]
        }
    ],
    
    "Testing & Debugging": [
        {
            "name": "Debugger for Chrome",
            "id": "msjsdiag.debugger-for-chrome",
            "overview": "Debugger for Chrome enables you to debug your JavaScript code running in Google Chrome directly from VS Code.",
            "tags": ["debugging", "chrome", "javascript", "web-development"]
        },
        {
            "name": "Jest",
            "id": "Orta.vscode-jest",
            "overview": "Jest extension for VS Code provides a comprehensive testing experience with Jest, including test discovery, running, and debugging.",
            "tags": ["testing", "jest", "javascript", "unit-tests"]
        },
        {
            "name": "Thunder Client",
            "id": "rangav.vscode-thunder-client",
            "overview": "Thunder Client is a lightweight REST API client for VS Code, allowing you to test APIs directly from your editor.",
            "tags": ["api", "rest", "testing", "http-client"]
        }
    ],
    
    "Docker & DevOps": [
        {
            "name": "Docker",
            "id": "ms-azuretools.vscode-docker",
            "overview": "The Docker extension makes it easy to build, manage and deploy containerized applications from VS Code.",
            "tags": ["docker", "containers", "devops", "deployment"]
        },
        {
            "name": "Remote - SSH",
            "id": "ms-vscode-remote.remote-ssh",
            "overview": "Remote - SSH allows you to open a folder on a remote machine using SSH, making it easy to develop on remote servers.",
            "tags": ["ssh", "remote", "devops", "server"]
        },
        {
            "name": "YAML",
            "id": "redhat.vscode-yaml",
            "overview": "YAML language support for VS Code, providing syntax highlighting, validation, and formatting for YAML files.",
            "tags": ["yaml", "configuration", "devops", "kubernetes"]
        }
    ],
    
    "AI & Code Assistance": [
        {
            "name": "GitHub Copilot",
            "id": "GitHub.copilot",
            "overview": "GitHub Copilot is an AI-powered code completion tool that helps you write code faster by suggesting whole lines or blocks of code.",
            "tags": ["ai", "code-completion", "productivity", "github"]
        },
        {
            "name": "Tabnine AI Autocomplete",
            "id": "tabnine.tabnine-vscode",
            "overview": "Tabnine is an AI code completion tool that helps you code faster with intelligent suggestions based on your coding patterns.",
            "tags": ["ai", "autocomplete", "productivity", "code-completion"]
        },
        {
            "name": "IntelliCode",
            "id": "VisualStudioExptTeam.vscodeintellicode",
            "overview": "IntelliCode provides AI-assisted development features for Python, TypeScript/JavaScript and Java developers in Visual Studio Code.",
            "tags": ["ai", "intellisense", "productivity", "microsoft"]
        }
    ]
}

# Flatten all extensions into a single list
all_extensions = []
for category, extensions in extensions_by_category.items():
    for ext in extensions:
        ext["category"] = category
        all_extensions.append(ext)

today = datetime.now().strftime("%Y-%m-%d")
ext_dir = "extensions"
used_ids = set()

# Scan all markdown files in the extensions directory for used IDs
if os.path.exists(ext_dir):
    for fname in os.listdir(ext_dir):
        if fname.endswith(".md"):
            with open(os.path.join(ext_dir, fname), "r", encoding="utf-8") as f:
                for line in f:
                    match = re.match(r"\\*\\*ID:\\*\\* `([^`]+)`", line)
                    if match:
                        used_ids.add(match.group(1))

# Filter out used extensions
unused_extensions = [ext for ext in all_extensions if ext["id"] not in used_ids]

if not unused_extensions:
    print("All extensions have been used! No new extension to add.")
    exit(0)

chosen = random.choice(unused_extensions)
url = f"https://marketplace.visualstudio.com/items?itemName={chosen['id']}"

# Create SEO-friendly content with structured data
md = f"""# VS Code Extension of the Day - {today}

**Name:** {chosen['name']}  
**Category:** {chosen['category']}  
**Marketplace Link:** [View Extension]({url})  
**ID:** `{chosen['id']}`  
**Overview:** {chosen['overview']}  

## Tags
{', '.join([f'`{tag}`' for tag in chosen['tags']])}

## Why This Extension?

This extension is particularly useful for developers working with {', '.join(chosen['tags'][:3])}. It helps improve your development workflow by {chosen['overview'].lower().split('.')[0]}.

## Installation

1. Open VS Code
2. Press `Ctrl+Shift+X` to open the Extensions view
3. Search for "{chosen['name']}"
4. Click **Install**

## Related Extensions

Looking for more extensions in the **{chosen['category']}** category? Check out our other recommendations for similar tools and utilities.

---

*This extension was automatically selected from our curated list of the best VS Code extensions for developers. Each day, we feature a different extension to help you discover new tools that can improve your coding experience.*
"""

os.makedirs(ext_dir, exist_ok=True)
with open(f"{ext_dir}/{today}.md", "w", encoding="utf-8") as f:
    f.write(md)

print(f"Generated extension entry for {today}: {chosen['name']}")
print(f"Category: {chosen['category']}")
print(f"Tags: {', '.join(chosen['tags'])}")
