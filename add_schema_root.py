#!/usr/bin/env python3
"""Add JSON-LD Schema.org to root .html files for backward compatibility."""
import os, re, json, glob

BASE = r'd:\VS KODI\Latseo Github'

products = {
    'wattsan-0404': {'name':'Wattsan 0404 MINI','sku':'0404-MINI','desc':'Kompakta galda CNC frēze ar 400×400 mm, 1.5 kW, NcStudio.','img':'https://wattsan.com/wp-content/uploads/titul-0404-mini-zip.png'},
    'wattsan-0609': {'name':'Wattsan 0609 MINI','sku':'0609-MINI','desc':'Kompakta CNC frēze ar 900×600 mm, 2.2 kW, DSP A11.','img':'https://wattsan.com/wp-content/uploads/titul-0609-mini-zip.png'},
    'wattsan-a1-6090': {'name':'Wattsan 6090 A1','sku':'6090-A1','desc':'3 asu CNC frēze ar 900×600 mm, 2.2 kW, RichAuto A11.','img':'https://wattsan.com/wp-content/uploads/titul-0609-mini-zip.png'},
    'wattsan-m1-6090': {'name':'Wattsan 6090 M1','sku':'6090-M1','desc':'Pastiprināta 3 asu CNC frēze ar 900×600 mm, 2.2 kW, 500 kg.','img':'https://wattsan.com/wp-content/uploads/titul-0609-mini-zip.png'},
    'wattsan-a1-1313': {'name':'Wattsan 1313 A1','sku':'1313-A1','desc':'Koka CNC frēze ar 1300×1300 mm, 2.2 kW, RichAuto A11.','img':'https://wattsan.com/wp-content/uploads/M1-1313-S4.png'},
    'wattsan-m1-1313': {'name':'Wattsan 1313 M1','sku':'1313-M1','desc':'Profesionāla koka frēze ar 1300×1300 mm, 3.2 kW, 650 kg.','img':'https://wattsan.com/wp-content/uploads/M1-1313-S4.png'},
    'wattsan-1313': {'name':'Wattsan 1313 M1 S4','sku':'1313-M1-S4','desc':'Populārākais — 1300×1300 mm, 4.5 kW, DSP A11, 1000 kg.','img':'https://wattsan.com/wp-content/uploads/M1-1313-S4.png'},
    'wattsan-a1-1325': {'name':'Wattsan 1325 A1','sku':'1325-A1','desc':'Pilna izmēra CNC frēze ar 1300×2500 mm, 3 kW.','img':'https://wattsan.com/wp-content/uploads/M1-1325.png'},
    'wattsan-1325': {'name':'Wattsan 1325 M1','sku':'1325-M1','desc':'Profesionāla pilna izmēra CNC frēze ar 1300×2500 mm, 4.5 kW.','img':'https://wattsan.com/wp-content/uploads/M1-1325.png'},
    'wattsan-m1-1325-rd': {'name':'Wattsan 1325 RD M1','sku':'1325-RD-M1','desc':'4 asu CNC frēze ar rotāciju, 1300×2500 mm, 4.5 kW.','img':'https://wattsan.com/wp-content/uploads/M1-1325.png'},
    'wattsan-m3-1325': {'name':'Wattsan 1325 M3','sku':'1325-M3','desc':'Industriāla CNC frēze ar 1300×2500 mm, NC Studio 8, servo.','img':'https://wattsan.com/wp-content/uploads/M1-1325.png'},
    'wattsan-a1-1616': {'name':'Wattsan 1616 A1','sku':'1616-A1','desc':'Kvadrātveida CNC frēze ar 1600×1600 mm, 3.2 kW.','img':'https://wattsan.com/wp-content/uploads/m2-1616-titul-result.webp'},
    'wattsan-m1-1616': {'name':'Wattsan 1616 M1','sku':'1616-M1','desc':'Profesionāla CNC frēze ar 1600×1600 mm, 4.5 kW, 730 kg.','img':'https://wattsan.com/wp-content/uploads/m2-1616-titul-result.webp'},
    'wattsan-1616': {'name':'Wattsan 1616 M2','sku':'1616-M2','desc':'M2 sērijas CNC frēze ar 1600×1600 mm, 4.5 kW, 1130 kg.','img':'https://wattsan.com/wp-content/uploads/m2-1616-titul-result.webp'},
    'wattsan-m1-s2-x': {'name':'Wattsan 1616 M1 S2 X','sku':'1616-M1-S2-X','desc':'CNC frēze ar DIVĀM 4.5 kW vārpstām, 1600×1600 mm.','img':'https://wattsan.com/wp-content/uploads/m2-1616-titul-result.webp'},
    'wattsan-2030': {'name':'Wattsan 2030 M1','sku':'2030-M1','desc':'Lielformāta CNC frēze ar 2000×3000 mm, 6 kW.','img':'https://wattsan.com/wp-content/uploads/m12030plus2-2.png'},
    'wattsan-2040': {'name':'Wattsan 2040 M1','sku':'2040-M1','desc':'Maksimālā CNC frēze ar 2000×4000 mm, 6 kW.','img':'https://wattsan.com/wp-content/uploads/20402-1-1-1-1.png'},
}

root_files = glob.glob(os.path.join(BASE, 'wattsan-*.html'))
for f in root_files:
    fn = os.path.basename(f)
    slug = fn.replace('.html', '')
    
    with open(f, 'r', encoding='utf-8') as fh:
        html = fh.read()
    
    # Remove any existing schema
    html = re.sub(r'<script type="application/ld\+json">.*?</script>\s*', '', html, flags=re.DOTALL)
    
    p = products.get(slug)
    if not p:
        print(f'SKIP {fn}')
        continue
    
    product_schema = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Product",
                "@id": f"https://cncfrezes.lv/{slug}/#product",
                "name": p['name'],
                "sku": p['sku'],
                "description": p['desc'],
                "image": p['img'],
                "brand": {"@type": "Brand", "name": "Wattsan"},
                "manufacturer": {"@type": "Organization", "name": "Jinan Wattsan Technology Limited", "url": "https://wattsan.com/"},
                "offers": {
                    "@type": "Offer",
                    "url": f"https://cncfrezes.lv/{slug}/",
                    "price": "Pieprasīt cenu",
                    "priceCurrency": "EUR",
                    "availability": "https://schema.org/InStock",
                    "seller": {"@id": "https://cncfrezes.lv/#organization"}
                },
                "url": f"https://cncfrezes.lv/{slug}/"
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Sākums", "item": "https://cncfrezes.lv/"},
                    {"@type": "ListItem", "position": 2, "name": "CNC Frēzes", "item": "https://cncfrezes.lv/#katalogs"},
                    {"@type": "ListItem", "position": 3, "name": p['name']},
                ]
            }
        ]
    }
    
    schema_json = json.dumps(product_schema, indent=2, ensure_ascii=False)
    schema_tag = '\n<script type="application/ld+json">\n' + schema_json + '\n</script>\n'
    html = html.replace('</head>', schema_tag + '</head>')
    
    with open(f, 'w', encoding='utf-8') as fh:
        fh.write(html)
    print(f'OK: {fn}')

print('DONE')
