import os
import re
from collections import defaultdict

EXT_DIR = "extensions"
README = "README.md"
START_MARKER = "<!-- EXTENSIONS-LIST-START -->"
END_MARKER = "<!-- EXTENSIONS-LIST-END -->"

def parse_extension_file(filepath):
    with open(filepath, encoding="utf-8") as f:
        content = f.read()
    name = re.search(r"\*\*Name:\*\*\s*(.+)", content)
    category = re.search(r"\*\*Category:\*\*\s*(.+)", content)
    link = re.search(r"\*\*Marketplace Link:\*\*\s*\[View Extension\]\((.+?)\)", content)
    ext_id = re.search(r"\*\*ID:\*\*\s*`(.+?)`", content)
    overview = re.search(r"\*\*Overview:\*\*\s*(.+)", content)
    return {
        "name": name.group(1).strip() if name else None,
        "category": category.group(1).strip() if category else "Uncategorized",
        "link": link.group(1).strip() if link else None,
        "id": ext_id.group(1).strip() if ext_id else None,
        "overview": overview.group(1).strip() if overview else "",
    }

def collect_extensions():
    extensions = defaultdict(list)
    for fname in os.listdir(EXT_DIR):
        if fname.endswith(".md"):
            ext = parse_extension_file(os.path.join(EXT_DIR, fname))
            if ext["name"]:
                extensions[ext["category"]].append(ext)
    return extensions

def make_category_anchor(category):
    # GitHub markdown anchor format
    return category.lower().replace(" ", "-")

def generate_extensions_section(extensions):
    lines = []
    lines.append(START_MARKER)
    lines.append("\n## 📂 Categories\n")
    for cat in sorted(extensions):
        anchor = make_category_anchor(cat)
        lines.append(f"- [{cat}](#{anchor})")
    lines.append("\n---\n")
    for cat in sorted(extensions):
        anchor = make_category_anchor(cat)
        lines.append(f"\n## {cat}\n")
        lines.append("| Name | Marketplace Link | ID | Overview |\n|------|------------------|----|----------|")
        for ext in extensions[cat]:
            name = f"**{ext['name']}**"
            link = f"[View Extension]({ext['link']})" if ext['link'] else ""
            ext_id = f"`{ext['id']}`" if ext['id'] else ""
            overview = ext['overview'] if ext['overview'] else ""
            lines.append(f"| {name} | {link} | {ext_id} | {overview} |")
    lines.append("\n---")
    lines.append(END_MARKER)
    lines.append("\n_This section is automatically generated. Do not edit manually._\n")
    return "\n".join(lines)

def update_readme(extensions):
    if os.path.exists(README):
        with open(README, encoding="utf-8") as f:
            content = f.read()
        start = content.find(START_MARKER)
        end = content.find(END_MARKER)
        new_section = generate_extensions_section(extensions)
        if start != -1 and end != -1:
            end += len(END_MARKER)
            updated = content[:start] + new_section + content[end:]
        else:
            # Markers not found, append at the end
            if not content.endswith("\n"):
                content += "\n"
            updated = content + "\n" + new_section
    else:
        updated = generate_extensions_section(extensions)
    with open(README, "w", encoding="utf-8") as f:
        f.write(updated)

if __name__ == "__main__":
    extensions = collect_extensions()
    update_readme(extensions) 