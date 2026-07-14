#!/usr/bin/env python3
"""Add JSON-LD Schema.org structured data to all pages for SEO."""
import os, re, glob, json

BASE = r'd:\VS KODI\Latseo Github'

# ─── PRODUCT DATA for schemas ───
PRODUCTS = {
    'wattsan-0404': {
        'name': 'Wattsan 0404 MINI',
        'sku': '0404-MINI',
        'description': 'Kompakta galda CNC frēze ar 400×400 mm darba laukumu, 1.5 kW vārpstu un NcStudio kontrolieri. Ideāla hobijiem, suvenīru un mazu koka detaļu ražošanai.',
        'workArea': '400 × 400 mm',
        'spindlePower': '1.5 kW',
        'controller': 'NcStudio',
        'weight': '92 kg',
        'image': 'https://wattsan.com/wp-content/uploads/titul-0404-mini-zip.png',
        'category': 'Galda CNC Frēze',
        'price': 'Pieprasīt cenu',
        'availability': 'InStock',
    },
    'wattsan-0609': {
        'name': 'Wattsan 0609 MINI',
        'sku': '0609-MINI',
        'description': 'Kompakta CNC frēze ar 900×600 mm darba laukumu, 2.2 kW vārpstu un DSP A11 kontrolieri. Lieliski piemērota reklāmas aģentūrām un mazajai ražošanai.',
        'workArea': '900 × 600 mm',
        'spindlePower': '2.2 kW',
        'controller': 'DSP A11',
        'weight': '135 kg',
        'image': 'https://wattsan.com/wp-content/uploads/titul-0609-mini-zip.png',
        'category': 'Kompakta CNC Frēze',
        'price': 'Pieprasīt cenu',
        'availability': 'InStock',
    },
    'wattsan-a1-6090': {
        'name': 'Wattsan 6090 A1',
        'sku': '6090-A1',
        'description': 'Profesionāla 3 asu CNC frēze ar 900×600 mm darba laukumu, 2.2 kW vārpstu un RichAuto A11 kontrolieri. A1 sērija ar izcilu cenas/kvalitātes attiecību.',
        'workArea': '900 × 600 mm',
        'spindlePower': '2.2 kW',
        'controller': 'RichAuto A11',
        'weight': '400 kg',
        'image': 'https://wattsan.com/wp-content/uploads/titul-0609-mini-zip.png',
        'category': '3 Asu CNC Frēze',
        'price': 'Pieprasīt cenu',
        'availability': 'InStock',
    },
    'wattsan-m1-6090': {
        'name': 'Wattsan 6090 M1',
        'sku': '6090-M1',
        'description': 'Pastiprināta M1 sērijas 3 asu CNC frēze ar 900×600 mm, 2.2 kW un 500 kg rāmi.',
        'workArea': '900 × 600 mm',
        'spindlePower': '2.2 kW',
        'controller': 'RichAuto A11',
        'weight': '500 kg',
        'image': 'https://wattsan.com/wp-content/uploads/titul-0609-mini-zip.png',
        'category': 'Pastiprināta CNC Frēze',
        'price': 'Pieprasīt cenu',
        'availability': 'InStock',
    },
    'wattsan-a1-1313': {
        'name': 'Wattsan 1313 A1',
        'sku': '1313-A1',
        'description': 'Ekonomiska koka CNC frēze ar 1300×1300 mm darba laukumu un 2.2 kW vārpstu.',
        'workArea': '1300 × 1300 mm',
        'spindlePower': '2.2 kW',
        'controller': 'RichAuto A11',
        'weight': '540 kg',
        'image': 'https://wattsan.com/wp-content/uploads/M1-1313-S4.png',
        'category': 'Koka CNC Frēze',
        'price': 'Pieprasīt cenu',
        'availability': 'InStock',
    },
    'wattsan-m1-1313': {
        'name': 'Wattsan 1313 M1',
        'sku': '1313-M1',
        'description': 'Profesionāla koka CNC frēze ar 1300×1300 mm, 3.2 kW vārpstu un 650 kg rāmi.',
        'workArea': '1300 × 1300 mm',
        'spindlePower': '3.2 kW',
        'controller': 'RichAuto A11',
        'weight': '650 kg',
        'image': 'https://wattsan.com/wp-content/uploads/M1-1313-S4.png',
        'category': 'Profesionāla Koka CNC Frēze',
        'price': 'Pieprasīt cenu',
        'availability': 'InStock',
    },
    'wattsan-1313': {
        'name': 'Wattsan 1313 M1 S4',
        'sku': '1313-M1-S4',
        'description': 'Populārākais modelis — jaudīga CNC frēze ar 1300×1300 mm, 4.5 kW vārpstu, DSP A11 kontrolieri un 1000 kg čuguna gultu.',
        'workArea': '1300 × 1300 mm',
        'spindlePower': '4.5 kW',
        'controller': 'DSP A11',
        'weight': '1000 kg',
        'image': 'https://wattsan.com/wp-content/uploads/M1-1313-S4.png',
        'category': 'Populārākā CNC Frēze',
        'price': 'Pieprasīt cenu',
        'availability': 'InStock',
    },
    'wattsan-a1-1325': {
        'name': 'Wattsan 1325 A1',
        'sku': '1325-A1',
        'description': 'Pilna izmēra CNC frēze ar 1300×2500 mm darba laukumu un 3 kW vārpstu. Ideāla durvju un lokšņu apstrādei.',
        'workArea': '1300 × 2500 mm',
        'spindlePower': '3 kW',
        'controller': 'RichAuto A11',
        'weight': '720 kg',
        'image': 'https://wattsan.com/wp-content/uploads/M1-1325.png',
        'category': 'Pilna Izmēra CNC Frēze',
        'price': 'Pieprasīt cenu',
        'availability': 'InStock',
    },
    'wattsan-1325': {
        'name': 'Wattsan 1325 M1',
        'sku': '1325-M1',
        'description': 'Profesionāla pilna izmēra CNC frēze ar 1300×2500 mm, 4.5 kW, RichAuto A11. Nozares standarts lokšņu materiālu apstrādei.',
        'workArea': '1300 × 2500 mm',
        'spindlePower': '4.5 kW',
        'controller': 'RichAuto A11',
        'weight': '880 kg',
        'image': 'https://wattsan.com/wp-content/uploads/M1-1325.png',
        'category': 'Profesionāla Pilna Izmēra CNC Frēze',
        'price': 'Pieprasīt cenu',
        'availability': 'InStock',
    },
    'wattsan-m1-1325-rd': {
        'name': 'Wattsan 1325 RD M1',
        'sku': '1325-RD-M1',
        'description': '4 asu CNC frēze ar rotācijas ierīci apaļu detaļu apstrādei. 1300×2500 mm, 4.5 kW, RichAuto A18.',
        'workArea': '1300 × 2500 mm',
        'spindlePower': '4.5 kW',
        'controller': 'RichAuto A18',
        'weight': '1550 kg',
        'image': 'https://wattsan.com/wp-content/uploads/M1-1325.png',
        'category': '4 Asu CNC Frēze ar Rotāciju',
        'price': 'Pieprasīt cenu',
        'availability': 'InStock',
    },
    'wattsan-m3-1325': {
        'name': 'Wattsan 1325 M3',
        'sku': '1325-M3',
        'description': 'Industriāla CNC frēze ar 1300×2500 mm, 4.5 kW, NC Studio 8 un Lambda4S servo sistēmu.',
        'workArea': '1300 × 2500 mm',
        'spindlePower': '4.5 kW',
        'controller': 'NC Studio 8',
        'weight': '1260 kg',
        'image': 'https://wattsan.com/wp-content/uploads/M1-1325.png',
        'category': 'Industriāla CNC Frēze',
        'price': 'Pieprasīt cenu',
        'availability': 'InStock',
    },
    'wattsan-a1-1616': {
        'name': 'Wattsan 1616 A1',
        'sku': '1616-A1',
        'description': 'Kvadrātveida CNC frēze ar 1600×1600 mm darba laukumu un 3.2 kW vārpstu.',
        'workArea': '1600 × 1600 mm',
        'spindlePower': '3.2 kW',
        'controller': 'RichAuto A11',
        'weight': '620 kg',
        'image': 'https://wattsan.com/wp-content/uploads/m2-1616-titul-result.webp',
        'category': 'Kvadrātveida CNC Frēze',
        'price': 'Pieprasīt cenu',
        'availability': 'InStock',
    },
    'wattsan-m1-1616': {
        'name': 'Wattsan 1616 M1',
        'sku': '1616-M1',
        'description': 'Profesionāla CNC frēze ar 1600×1600 mm, 4.5 kW vārpstu un 730 kg rāmi.',
        'workArea': '1600 × 1600 mm',
        'spindlePower': '4.5 kW',
        'controller': 'RichAuto A11',
        'weight': '730 kg',
        'image': 'https://wattsan.com/wp-content/uploads/m2-1616-titul-result.webp',
        'category': 'Profesionāla Kvadrātveida CNC Frēze',
        'price': 'Pieprasīt cenu',
        'availability': 'InStock',
    },
    'wattsan-1616': {
        'name': 'Wattsan 1616 M2',
        'sku': '1616-M2',
        'description': 'Universāla M2 sērijas CNC frēze ar 1600×1600 mm, 4.5 kW un 1130 kg — smagākā savā klasē.',
        'workArea': '1600 × 1600 mm',
        'spindlePower': '4.5 kW',
        'controller': 'RichAuto A11',
        'weight': '1130 kg',
        'image': 'https://wattsan.com/wp-content/uploads/m2-1616-titul-result.webp',
        'category': 'Universāla M2 CNC Frēze',
        'price': 'Pieprasīt cenu',
        'availability': 'InStock',
    },
    'wattsan-m1-s2-x': {
        'name': 'Wattsan 1616 M1 S2 X',
        'sku': '1616-M1-S2-X',
        'description': 'CNC frēze ar DIVĀM 4.5 kW vārpstām — divkārša produktivitāte. 1600×1600 mm, RichAuto F7324.',
        'workArea': '1600 × 1600 mm',
        'spindlePower': '2 × 4.5 kW',
        'controller': 'RichAuto F7324',
        'weight': '840 kg',
        'image': 'https://wattsan.com/wp-content/uploads/m2-1616-titul-result.webp',
        'category': 'Divu Vārpstu CNC Frēze',
        'price': 'Pieprasīt cenu',
        'availability': 'InStock',
    },
    'wattsan-2030': {
        'name': 'Wattsan 2030 M1',
        'sku': '2030-M1',
        'description': 'Industriāla lielformāta CNC frēze ar 2000×3000 mm darba laukumu un 6 kW vārpstu.',
        'workArea': '2000 × 3000 mm',
        'spindlePower': '6 kW',
        'controller': 'RichAuto A11',
        'weight': '1140 kg',
        'image': 'https://wattsan.com/wp-content/uploads/m12030plus2-2.png',
        'category': 'Lielformāta CNC Frēze',
        'price': 'Pieprasīt cenu',
        'availability': 'InStock',
    },
    'wattsan-2040': {
        'name': 'Wattsan 2040 M1',
        'sku': '2040-M1',
        'description': 'Maksimālā izmēra CNC frēze ar 2000×4000 mm darba laukumu un 6 kW vārpstu. Lielākā standarta CNC frēze.',
        'workArea': '2000 × 4000 mm',
        'spindlePower': '6 kW',
        'controller': 'RichAuto A11',
        'weight': '1370 kg',
        'image': 'https://wattsan.com/wp-content/uploads/20402-1-1-1-1.png',
        'category': 'Maksimālā Izmēra CNC Frēze',
        'price': 'Pieprasīt cenu',
        'availability': 'InStock',
    },
}

# ─── HOMEPAGE SCHEMA ───
homepage_schema = {
    "@context": "https://schema.org",
    "@graph": [
        {
            "@type": "Organization",
            "@id": "https://cncfrezes.lv/#organization",
            "name": "SIA Bratus — Wattsan Oficiālais Pārstāvis Latvijā",
            "alternateName": ["Bratus", "Wattsan Latvia", "cncfrezes.lv"],
            "url": "https://cncfrezes.lv/",
            "logo": "https://wattsan.com/wp-content/uploads/wattsan_logo-1.svg",
            "description": "Oficiālais Wattsan CNC iekārtu izplatītājs Latvijā. Piegādājam, uzstādām un nodrošinām tehnisko atbalstu un garantiju — CNC frēzes, lāzera iekārtas kokam, saplāksnim, MDF un plastmasai.",
            "email": "sales@bratus.lv",
            "telephone": "+37124424434",
            "address": {
                "@type": "PostalAddress",
                "streetAddress": "Dārznieku iela 42",
                "addressLocality": "Ķekava",
                "postalCode": "LV-2123",
                "addressCountry": "LV"
            },
            "sameAs": [
                "https://bratus.lv/",
                "https://wattsan.com/"
            ],
            "vatID": "40203628316"
        },
        {
            "@type": "WebSite",
            "@id": "https://cncfrezes.lv/#website",
            "url": "https://cncfrezes.lv/",
            "name": "CNC Frēzes Latvijā — Wattsan Oficiālais Pārstāvis",
            "description": "Profesionālas Wattsan CNC frēzes kokam, saplāksnim, MDF un plastmasai. 17 modeļi — no kompaktām galda frēzēm līdz industriālām lielformāta iekārtām.",
            "publisher": {"@id": "https://cncfrezes.lv/#organization"},
            "inLanguage": "lv"
        },
        {
            "@type": "ItemList",
            "@id": "https://cncfrezes.lv/#katalogs",
            "name": "CNC Frēžu Katalogs",
            "description": "17 Wattsan CNC frēžu modeļi",
            "numberOfItems": 17,
            "itemListElement": [
                {"@type": "ListItem", "position": i+1, "url": f"https://cncfrezes.lv/{slug}/", "name": p['name']}
                for i, (slug, p) in enumerate(PRODUCTS.items())
            ]
        }
    ]
}

# ─── ADD SCHEMA TO HOMEPAGE ───
index_path = os.path.join(BASE, 'index.html')
with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

schema_json = json.dumps(homepage_schema, indent=2, ensure_ascii=False)
schema_tag = f'\n<script type="application/ld+json">\n{schema_json}\n</script>\n'

# Insert before </head>
html = html.replace('</head>', f'{schema_tag}</head>')

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(html)
print('Added Organization + WebSite + ItemList schema to index.html')

# ─── ADD PRODUCT SCHEMA TO EACH PRODUCT PAGE ───
for slug, p in PRODUCTS.items():
    folder = os.path.join(BASE, slug)
    idx_path = os.path.join(folder, 'index.html')
    if not os.path.exists(idx_path):
        # Also check root
        idx_path = os.path.join(BASE, f'{slug}.html')
    if not os.path.exists(idx_path):
        print(f'SKIP: {slug} — file not found')
        continue
    
    with open(idx_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    product_schema = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Product",
                "@id": f"https://cncfrezes.lv/{slug}/#product",
                "name": p['name'],
                "sku": p['sku'],
                "description": p['description'],
                "image": p['image'],
                "category": p['category'],
                "brand": {
                    "@type": "Brand",
                    "name": "Wattsan"
                },
                "manufacturer": {
                    "@type": "Organization",
                    "name": "Jinan Wattsan Technology Limited",
                    "url": "https://wattsan.com/"
                },
                "offers": {
                    "@type": "Offer",
                    "url": f"https://cncfrezes.lv/{slug}/",
                    "price": p['price'],
                    "priceCurrency": "EUR",
                    "availability": f"https://schema.org/{p['availability']}",
                    "seller": {"@id": "https://cncfrezes.lv/#organization"}
                },
                "additionalProperty": [
                    {"@type": "PropertyValue", "name": "Darba laukums", "value": p['workArea']},
                    {"@type": "PropertyValue", "name": "Vārpstas jauda", "value": p['spindlePower']},
                    {"@type": "PropertyValue", "name": "Kontrolieris", "value": p['controller']},
                    {"@type": "PropertyValue", "name": "Svars", "value": p['weight']},
                ],
                "url": f"https://cncfrezes.lv/{slug}/"
            },
            {
                "@type": "BreadcrumbList",
                "@id": f"https://cncfrezes.lv/{slug}/#breadcrumb",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Sākums", "item": "https://cncfrezes.lv/"},
                    {"@type": "ListItem", "position": 2, "name": "CNC Frēzes", "item": "https://cncfrezes.lv/#katalogs"},
                    {"@type": "ListItem", "position": 3, "name": p['name']},
                ]
            }
        ]
    }
    
    schema_json = json.dumps(product_schema, indent=2, ensure_ascii=False)
    schema_tag = f'\n<script type="application/ld+json">\n{schema_json}\n</script>\n'
    
    # Remove any existing schema (in case of re-run)
    html = re.sub(r'<script type="application/ld\+json">.*?</script>\s*', '', html, flags=re.DOTALL)
    
    # Insert before </head>
    html = html.replace('</head>', f'{schema_tag}</head>')
    
    with open(idx_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'Added Product + BreadcrumbList schema to {slug}/')

print('\nALL SCHEMAS ADDED!')
