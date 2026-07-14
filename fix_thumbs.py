import re, glob, os

base = r'd:\VS KODI\Latseo Github'
for f in sorted(glob.glob(os.path.join(base, 'wattsan-*.html'))):
    with open(f, 'r', encoding='utf-8') as fh:
        html = fh.read()
    
    count = 0
    def fix_thumb(m):
        global count
        count += 1
        cls = 'gallery-thumb active' if count == 1 else 'gallery-thumb'
        return f'<img class="{cls}" src="{m.group(1)}" onclick="setGallery(this)" alt="{m.group(2)}">'
    
    html = re.sub(
        r'<img class="gallery-thumb(?:\s+active)?" src="([^"]+)" onclick="setGallery\(this\)" alt="([^"]+)">',
        fix_thumb,
        html
    )
    
    with open(f, 'w', encoding='utf-8') as fh:
        fh.write(html)
    print(f'Fixed: {os.path.basename(f)}')

print('DONE')
