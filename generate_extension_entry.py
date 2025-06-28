import random
from datetime import datetime
import os

extensions = [
    {"name": "Prettier", "id": "esbenp.prettier-vscode"},
    {"name": "ESLint", "id": "dbaeumer.vscode-eslint"},
    {"name": "GitLens", "id": "eamodio.gitlens"},
    {"name": "Live Server", "id": "ritwickdey.LiveServer"},
    {"name": "Path Intellisense", "id": "christian-kohler.path-intellisense"},
    {"name": "Code Spell Checker", "id": "streetsidesoftware.code-spell-checker"},
    {"name": "Bracket Pair Colorizer 2", "id": "CoenraadS.bracket-pair-colorizer-2"},
    {"name": "Debugger for Chrome", "id": "msjsdiag.debugger-for-chrome"},
]

today = datetime.now().strftime("%Y-%m-%d")
chosen = random.choice(extensions)
url = f"https://marketplace.visualstudio.com/items?itemName={chosen['id']}"

md = f"""# VS Code Extension of the Day - {today}

**Name:** {chosen['name']}  
**Marketplace Link:** [View Extension]({url})  
**ID:** `{chosen['id']}`  
"""

os.makedirs("extensions", exist_ok=True)
with open(f"extensions/{today}.md", "w") as f:
    f.write(md)
