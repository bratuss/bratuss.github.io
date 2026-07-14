import os, re, glob

base = r'd:\VS KODI\Latseo Github'
files = glob.glob(os.path.join(base, 'wattsan-*.html'))

# Product descriptions for the heading subtitle line
subtitles = {
    '0404': 'Galda / Hobijiem',
    '0609': 'Kompakta / Mazai ražošanai',
    'A1 6090': '3 Asis / Ekonomiska',
    'M1 6090': '3 Asis / Pastiprināta',
    'A1 1313': 'Koka frēze / Budžeta',
    'M1 1313': 'Koka frēze / Profesionāla',
    '1313': 'Populārākais / 4.5 kW',
    'A1 1325': 'Pilna izmēra / 3 kW',
    '1325': 'Pilna izmēra / 4.5 kW',
    'M1 1325 RD': '4 Asis / Rotācija',
    'M3 1325': 'Industriāla / NC Studio 8',
    'A1 1616': 'Kvadrātveida / Budžeta',
    'M1 1616': 'Kvadrātveida / 4.5 kW',
    '1616': 'M2 Sērija / 1130 kg',
    'M1 S2 X': '2× Vārpsta / Dubultā jauda',
    '2030': 'Lielformāta / 6 kW',
    '2040': 'Maksimālā / 6 kW',
}

for f in sorted(files):
    fn = os.path.basename(f)
    with open(f, 'r', encoding='utf-8') as fh:
        html = fh.read()
    
    # Extract model slug from filename
    m = re.search(r'wattsan-(.+)\.html', fn)
    slug = m.group(1) if m else ''
    
    # Build clean model display name
    model_parts = slug.replace('-', ' ').upper()
    
    # Get subtitle - try exact match first, then partial
    sub = subtitles.get(model_parts, '')
    if not sub:
        for k, v in subtitles.items():
            if k.replace(' ', '') == model_parts.replace(' ', ''):
                sub = v
                break
    if not sub:
        sub = 'CNC Frēze'
    
    # Build clean heading
    new_h1 = f'<h1 class="product-title">Wattsan <strong>{model_parts}</strong><br><em>{sub}</em></h1>'
    
    # Replace the old messy heading
    old_pattern = r'<h1 class="product-title">Wattsan .*?</h1>'
    html = re.sub(old_pattern, new_h1, html)
    
    # Fix SVG icons - add proper width/height
    html = html.replace(
        '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">',
        '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">'
    )
    
    # Fix feature-card-icon SVG size
    html = html.replace(
        '.feature-card-icon svg{width:14px;height:14px;color:var(--accent)}',
        '.feature-card-icon svg{width:18px;height:18px;color:var(--accent)}'
    )
    
    # Better align product-hero
    html = html.replace(
        'align-items:start}',
        'align-items:center}'
    )
    
    # Limit key-specs to 4 items
    def limit_specs(m):
        content = m.group(2)
        specs = re.findall(r'<div class="key-spec">.*?</div>\s*', content, re.DOTALL)
        if len(specs) > 4:
            return m.group(1) + ''.join(specs[:4]) + m.group(3)
        return m.group(0)
    
    html = re.sub(
        r'(<div class="key-specs">)(.*?)(</div>)',
        limit_specs,
        html,
        flags=re.DOTALL
    )
    
    # Add some padding to gallery main
    html = html.replace(
        '.gallery-main{width:100%;aspect-ratio:4/3;object-fit:contain;background:var(--bg2);border:1px solid var(--border)}',
        '.gallery-main{width:100%;aspect-ratio:4/3;object-fit:contain;background:var(--bg2);border:1px solid var(--border);padding:24px}'
    )
    
    with open(f, 'w', encoding='utf-8') as fh:
        fh.write(html)
    
    print(f'Fixed: {fn} => Wattsan {model_parts}')

print('\nALL DONE!')
