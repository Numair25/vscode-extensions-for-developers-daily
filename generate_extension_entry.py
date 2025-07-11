import random
from datetime import datetime
import os
import re

extensions = [
    {
        "name": "Prettier",
        "id": "esbenp.prettier-vscode",
        "overview": "Prettier is an opinionated code formatter that enforces a consistent style by parsing your code and re-printing it with its own rules, supporting many languages and integrating with most editors."
    },
    {
        "name": "ESLint",
        "id": "dbaeumer.vscode-eslint",
        "overview": "ESLint is a popular linter for JavaScript and TypeScript that helps you find and fix problems in your code, enforcing coding standards and best practices."
    },
    {
        "name": "GitLens",
        "id": "eamodio.gitlens",
        "overview": "GitLens supercharges the built-in VS Code Git capabilities, providing rich insights into code authorship, history, and more, right in your editor."
    },
    {
        "name": "Live Server",
        "id": "ritwickdey.LiveServer",
        "overview": "Live Server launches a local development server with live reload for static and dynamic pages, making web development faster and easier."
    },
    {
        "name": "Path Intellisense",
        "id": "christian-kohler.path-intellisense",
        "overview": "Path Intellisense autocompletes filenames in your code, making it easier to import files and navigate your project."
    },
    {
        "name": "Code Spell Checker",
        "id": "streetsidesoftware.code-spell-checker",
        "overview": "Code Spell Checker is a basic spell checker that works well with code and documents, helping you catch common spelling errors."
    },
    {
        "name": "Bracket Pair Colorizer 2",
        "id": "CoenraadS.bracket-pair-colorizer-2",
        "overview": "Bracket Pair Colorizer 2 allows matching brackets to be identified with colors, making it easier to read and debug code with nested structures."
    },
    {
        "name": "Debugger for Chrome",
        "id": "msjsdiag.debugger-for-chrome",
        "overview": "Debugger for Chrome enables you to debug your JavaScript code running in Google Chrome directly from VS Code."
    },
]

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
unused_extensions = [ext for ext in extensions if ext["id"] not in used_ids]

if not unused_extensions:
    print("All extensions have been used! No new extension to add.")
    exit(0)

chosen = random.choice(unused_extensions)
url = f"https://marketplace.visualstudio.com/items?itemName={chosen['id']}"

md = f"""# VS Code Extension of the Day - {today}

**Name:** {chosen['name']}  
**Marketplace Link:** [View Extension]({url})  
**ID:** `{chosen['id']}`  
**Overview:** {chosen['overview']}  
"""

os.makedirs(ext_dir, exist_ok=True)
with open(f"{ext_dir}/{today}.md", "w", encoding="utf-8") as f:
    f.write(md)
