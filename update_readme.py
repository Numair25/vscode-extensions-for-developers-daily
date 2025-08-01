import os
import re
from datetime import datetime
from collections import defaultdict

def extract_extension_info(md_content):
    """Extract extension information from markdown content."""
    name_match = re.search(r'\*\*Name:\*\* (.+)', md_content)
    category_match = re.search(r'\*\*Category:\*\* (.+)', md_content)
    url_match = re.search(r'\[View Extension\]\((https://marketplace\.visualstudio\.com/items\?itemName=[^)]+)\)', md_content)
    id_match = re.search(r'\*\*ID:\*\* `([^`]+)`', md_content)
    overview_match = re.search(r'\*\*Overview:\*\* (.+)', md_content)
    
    if all([name_match, url_match, id_match, overview_match]):
        return {
            'name': name_match.group(1).strip(),
            'category': category_match.group(1).strip() if category_match else 'Uncategorized',
            'url': url_match.group(1),
            'id': id_match.group(1),
            'overview': overview_match.group(1).strip()
        }
    return None

def generate_readme_content(extensions_by_category):
    """Generate the README content with extensions organized by category."""
    
    # Read the existing README to get the header and footer
    with open('README.md', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the section between the markers
    start_marker = '<!-- EXTENSIONS-LIST-START -->'
    end_marker = '<!-- EXTENSIONS-LIST-END -->'
    
    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker)
    
    if start_idx == -1 or end_idx == -1:
        print("Could not find extension list markers in README.md")
        return
    
    # Generate the new extensions list
    extensions_content = []
    
    for category, extensions in extensions_by_category.items():
        if not extensions:
            continue
            
        extensions_content.append(f"## {category}")
        extensions_content.append("")
        extensions_content.append("| Name | Marketplace Link | ID | Overview |")
        extensions_content.append("|------|------------------|----|----------|")
        
        for ext in extensions:
            extensions_content.append(
                f"| **{ext['name']}** | [View Extension]({ext['url']}) | `{ext['id']}` | {ext['overview']} |"
            )
        
        extensions_content.append("")
    
    # Replace the content between markers
    new_content = (
        content[:start_idx + len(start_marker)] + 
        "\n\n" + 
        "\n".join(extensions_content) + 
        "\n\n---\n\n" +
        content[end_idx:]
    )
    
    # Write the updated README
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Updated README.md with {sum(len(exts) for exts in extensions_by_category.values())} extensions across {len(extensions_by_category)} categories")

def main():
    """Main function to update README with latest extensions."""
    extensions_dir = "extensions"
    extensions_by_category = defaultdict(list)
    seen_ids = set()
    
    if not os.path.exists(extensions_dir):
        print(f"Extensions directory '{extensions_dir}' not found")
        return
    
    # Read all markdown files in the extensions directory
    for filename in sorted(os.listdir(extensions_dir), reverse=True):
        if not filename.endswith('.md'):
            continue
            
        filepath = os.path.join(extensions_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        ext_info = extract_extension_info(content)
        if ext_info and ext_info['id'] not in seen_ids:
            extensions_by_category[ext_info['category']].append(ext_info)
            seen_ids.add(ext_info['id'])
    
    # Sort categories and extensions within each category
    sorted_categories = dict(sorted(extensions_by_category.items()))
    for category in sorted_categories:
        sorted_categories[category] = sorted(
            sorted_categories[category], 
            key=lambda x: x['name']
        )
    
    # Generate the updated README
    generate_readme_content(sorted_categories)
    
    print(f"Processed {len(seen_ids)} unique extensions")
    for category, exts in sorted_categories.items():
        print(f"  {category}: {len(exts)} extensions")

if __name__ == "__main__":
    main() 