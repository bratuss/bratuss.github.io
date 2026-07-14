#!/usr/bin/env python3
"""Create clean URLs without .html extensions on GitHub Pages."""
import os, re, glob, shutil

BASE = r'd:\VS KODI\Latseo Github'

# Step 1: Get all HTML files
html_files = glob.glob(os.path.join(BASE, '*.html'))

# Step 2: For each product page, create a folder and move the file as index.html
for f in sorted(html_files):
    fn = os.path.basename(f)
    name = fn.replace('.html', '')
    
    if name == 'index':
        # index.html stays at root
        print(f'Keeping: {fn} at root')
        continue
    
    # Create folder
    folder = os.path.join(BASE, name)
    os.makedirs(folder, exist_ok=True)
    
    # Copy file as index.html inside folder
    dest = os.path.join(folder, 'index.html')
    shutil.copy2(f, dest)
    print(f'Created: {name}/index.html')

# Step 3: Update all internal links in ALL HTML files
all_html = glob.glob(os.path.join(BASE, '*.html'))
all_html += glob.glob(os.path.join(BASE, '*', 'index.html'))

for f in sorted(all_html):
    with open(f, 'r', encoding='utf-8') as fh:
        content = fh.read()
    
    original = content
    
    # Replace links to product pages: href="wattsan-XXXX.html" -> href="/wattsan-XXXX/"
    # But NOT when followed by # (anchors on same page)
    content = re.sub(
        r'href="(wattsan-[a-zA-Z0-9-]+)\.html"',
        r'href="/\1/"',
        content
    )
    
    # Replace index.html links
    content = re.sub(
        r'href="index\.html#',
        r'href="/#',
        content
    )
    content = re.sub(
        r'href="index\.html"',
        r'href="/"',
        content
    )
    
    # Fix canonical URLs - change .html to /
    content = re.sub(
        r'(https://cncfrezes\.lv/[a-zA-Z0-9-]+)\.html',
        r'\1/',
        content
    )
    
    # Fix breadcrumb and nav links that use relative paths without leading /
    # These should stay relative since they're in subfolders now
    
    if content != original:
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(content)
        rel = os.path.relpath(f, BASE)
        print(f'Updated links in: {rel}')

# Step 4: Fix links in product pages (in subfolders) - need relative paths to work
for folder in sorted(glob.glob(os.path.join(BASE, 'wattsan-*'))):
    if not os.path.isdir(folder):
        continue
    idx = os.path.join(folder, 'index.html')
    if not os.path.exists(idx):
        continue
    
    with open(idx, 'r', encoding='utf-8') as fh:
        content = fh.read()
    
    # Fix subnav links - they use relative paths like "wattsan-0404.html"
    # Since we're in /wattsan-XXXX/index.html, relative links to /wattsan-YYYY/ should be ../wattsan-YYYY/
    content = content.replace('href="wattsan-', 'href="../wattsan-')
    
    # Fix: "../wattsan-XXXX.html" -> "../wattsan-XXXX/"
    content = re.sub(
        r'href="\.\./wattsan-([a-zA-Z0-9-]+)\.html"',
        r'href="../\1/"',
        content
    )
    
    # But we already changed .html to nothing above... let me check
    # The subnav HTML has: <a href="wattsan-0404.html">
    # After the replace above: <a href="../wattsan-0404.html">
    # We need: <a href="../wattsan-0404/">
    content = re.sub(
        r'href="\.\./(wattsan-[a-zA-Z0-9-]+)\.html"',
        r'href="../\1/"',
        content
    )
    
    # Fix breadcrumb: href="index.html" -> href="/"
    content = content.replace('href="index.html"', 'href="/"')
    content = content.replace('href="index.html#', 'href="/#')
    
    with open(idx, 'w', encoding='utf-8') as fh:
        fh.write(content)
    
    rel = os.path.relpath(idx, BASE)
    print(f'Fixed subfolder links: {rel}')

print('\nDONE! Clean URLs created.')
