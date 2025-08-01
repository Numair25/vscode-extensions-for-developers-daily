import os
import json
from datetime import datetime
from collections import defaultdict

def generate_seo_meta():
    """Generate SEO-friendly meta information and structured data."""
    
    # Read all extension files to gather data
    extensions_dir = "extensions"
    extensions_data = []
    categories = defaultdict(list)
    
    if os.path.exists(extensions_dir):
        for filename in os.listdir(extensions_dir):
            if filename.endswith('.md'):
                filepath = os.path.join(extensions_dir, filename)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Extract extension info
                name_match = re.search(r'\*\*Name:\*\* (.+)', content)
                category_match = re.search(r'\*\*Category:\*\* (.+)', content)
                url_match = re.search(r'\[View Extension\]\((https://marketplace\.visualstudio\.com/items\?itemName=[^)]+)\)', content)
                id_match = re.search(r'\*\*ID:\*\* `([^`]+)`', content)
                overview_match = re.search(r'\*\*Overview:\*\* (.+)', content)
                
                if all([name_match, category_match, url_match, id_match, overview_match]):
                    ext_info = {
                        'name': name_match.group(1).strip(),
                        'category': category_match.group(1).strip(),
                        'url': url_match.group(1),
                        'id': id_match.group(1),
                        'overview': overview_match.group(1).strip(),
                        'date': filename.replace('.md', '')
                    }
                    extensions_data.append(ext_info)
                    categories[ext_info['category']].append(ext_info)
    
    # Generate structured data for search engines
    structured_data = {
        "@context": "https://schema.org",
        "@type": "WebPage",
        "name": "Best VS Code Extensions for Developers - Daily Recommendations",
        "description": "Discover the most useful Visual Studio Code extensions for developers, updated daily with curated recommendations to boost your productivity and code quality.",
        "url": "https://github.com/Numair25/daily-vscode-extensions-for-developers",
        "mainEntity": {
            "@type": "ItemList",
            "name": "VS Code Extensions",
            "numberOfItems": len(extensions_data),
            "itemListElement": []
        }
    }
    
    # Add each extension to structured data
    for i, ext in enumerate(extensions_data, 1):
        structured_data["mainEntity"]["itemListElement"].append({
            "@type": "ListItem",
            "position": i,
            "item": {
                "@type": "SoftwareApplication",
                "name": ext['name'],
                "description": ext['overview'],
                "url": ext['url'],
                "applicationCategory": ext['category'],
                "operatingSystem": "Windows, macOS, Linux",
                "softwareVersion": "Latest"
            }
        })
    
    # Generate meta tags for HTML
    meta_tags = f"""<!-- SEO Meta Tags -->
<meta name="description" content="Discover the most useful Visual Studio Code extensions for developers, updated daily with curated recommendations to boost your productivity and code quality.">
<meta name="keywords" content="VS Code extensions, Visual Studio Code, developer tools, code editor, productivity, programming, development">
<meta name="author" content="VS Code Extensions Daily">
<meta name="robots" content="index, follow">
<meta property="og:title" content="Best VS Code Extensions for Developers - Daily Recommendations">
<meta property="og:description" content="Discover the most useful Visual Studio Code extensions for developers, updated daily with curated recommendations.">
<meta property="og:type" content="website">
<meta property="og:url" content="https://github.com/Numair25/daily-vscode-extensions-for-developers">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Best VS Code Extensions for Developers">
<meta name="twitter:description" content="Daily curated VS Code extensions for developers">

<!-- Structured Data -->
<script type="application/ld+json">
{json.dumps(structured_data, indent=2)}
</script>
"""
    
    # Generate sitemap data
    sitemap_data = {
        "lastmod": datetime.now().isoformat(),
        "total_extensions": len(extensions_data),
        "categories": len(categories),
        "extensions_by_category": {cat: len(exts) for cat, exts in categories.items()}
    }
    
    # Write meta tags to file
    with open('seo_meta.html', 'w', encoding='utf-8') as f:
        f.write(meta_tags)
    
    # Write structured data to JSON file
    with open('structured_data.json', 'w', encoding='utf-8') as f:
        json.dump(structured_data, f, indent=2)
    
    # Write sitemap data
    with open('sitemap_data.json', 'w', encoding='utf-8') as f:
        json.dump(sitemap_data, f, indent=2)
    
    print(f"Generated SEO meta information:")
    print(f"  - {len(extensions_data)} extensions processed")
    print(f"  - {len(categories)} categories found")
    print(f"  - SEO meta tags: seo_meta.html")
    print(f"  - Structured data: structured_data.json")
    print(f"  - Sitemap data: sitemap_data.json")
    
    # Print category summary
    print(f"\nExtensions by category:")
    for category, exts in sorted(categories.items()):
        print(f"  {category}: {len(exts)} extensions")

if __name__ == "__main__":
    import re
    generate_seo_meta() 