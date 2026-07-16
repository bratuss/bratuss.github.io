#!/usr/bin/env python3
"""Add galleries, features, and rich content to all CNC router product pages."""
import os, re, glob

BASE = r'd:\VS KODI\Latseo Github'

# Gallery images for each model (from wattsan.com product pages)
GALLERY = {
    'wattsan-0404.html': [
        'https://wattsan.com/wp-content/uploads/titul-0404-mini-zip.png',
        'https://wattsan.com/wp-content/uploads/0404-mini-milling-machine-masonry-gallery-1-result.webp',
        'https://wattsan.com/wp-content/uploads/0404-mini-milling-machine-masonry-gallery-2-result.webp',
        'https://wattsan.com/wp-content/uploads/0404-mini-milling-machine-masonry-gallery-3-result.webp',
        'https://wattsan.com/wp-content/uploads/0404-mini-milling-machine-masonry-gallery-4-result.webp',
    ],
    'wattsan-0609.html': [
        'https://wattsan.com/wp-content/uploads/titul-0609-mini-zip.png',
        'https://wattsan.com/wp-content/uploads/0404-mini-milling-machine-masonry-gallery-1-result.webp',
        'https://wattsan.com/wp-content/uploads/0404-mini-milling-machine-masonry-gallery-2-result.webp',
        'https://wattsan.com/wp-content/uploads/0404-mini-milling-machine-masonry-gallery-3-result.webp',
        'https://wattsan.com/wp-content/uploads/0404-mini-milling-machine-masonry-gallery-6-result.webp',
    ],
    'wattsan-a1-6090.html': [
        'https://wattsan.com/wp-content/uploads/titul-0609-mini-zip.png',
        'https://wattsan.com/wp-content/uploads/6090-a1-milling-machine-mansonry-gallery-3-result.webp',
        'https://wattsan.com/wp-content/uploads/1313-a1-milling-machine-mansonry-gallery-1-result.webp',
        'https://wattsan.com/wp-content/uploads/0404-mini-milling-machine-masonry-gallery-3-result.webp',
    ],
    'wattsan-m1-6090.html': [
        'https://wattsan.com/wp-content/uploads/titul-0609-mini-zip.png',
        'https://wattsan.com/wp-content/uploads/6090-a1-milling-machine-mansonry-gallery-3-result.webp',
        'https://wattsan.com/wp-content/uploads/1313-a1-milling-machine-mansonry-gallery-1-result.webp',
        'https://wattsan.com/wp-content/uploads/0404-mini-milling-machine-masonry-gallery-6-result.webp',
    ],
    'wattsan-a1-1313.html': [
        'https://wattsan.com/wp-content/uploads/M1-1313-S4.png',
        'https://wattsan.com/wp-content/uploads/1313-a1-milling-machine-mansonry-gallery-1-result.webp',
        'https://wattsan.com/wp-content/uploads/6090-a1-milling-machine-mansonry-gallery-3-result.webp',
        'https://wattsan.com/wp-content/uploads/0404-mini-milling-machine-masonry-gallery-3-result.webp',
    ],
    'wattsan-m1-1313.html': [
        'https://wattsan.com/wp-content/uploads/M1-1313-S4.png',
        'https://wattsan.com/wp-content/uploads/1313-a1-milling-machine-mansonry-gallery-1-result.webp',
        'https://wattsan.com/wp-content/uploads/1325-m1-milling-machine-mansonry-gallery-1-result.webp',
        'https://wattsan.com/wp-content/uploads/1325-m1-milling-machine-mansonry-gallery-2-result.webp',
    ],
    'wattsan-1313.html': [
        'https://wattsan.com/wp-content/uploads/M1-1313-S4.png',
        'https://wattsan.com/wp-content/uploads/1313-a1-milling-machine-mansonry-gallery-1-result.webp',
        'https://wattsan.com/wp-content/uploads/1325-m1-milling-machine-mansonry-gallery-1-result.webp',
        'https://wattsan.com/wp-content/uploads/1325-m1-milling-machine-mansonry-gallery-2-result.webp',
        'https://wattsan.com/wp-content/uploads/1325-m1-milling-machine-mansonry-gallery-6-result.webp',
    ],
    'wattsan-a1-1325.html': [
        'https://wattsan.com/wp-content/uploads/M1-1325.png',
        'https://wattsan.com/wp-content/uploads/1325-m1-milling-machine-mansonry-gallery-1-result.webp',
        'https://wattsan.com/wp-content/uploads/1325-m1-milling-machine-mansonry-gallery-2-result.webp',
        'https://wattsan.com/wp-content/uploads/1325-m1-milling-machine-mansonry-gallery-6-result.webp',
    ],
    'wattsan-1325.html': [
        'https://wattsan.com/wp-content/uploads/M1-1325.png',
        'https://wattsan.com/wp-content/uploads/1325-m1-milling-machine-mansonry-gallery-1-result.webp',
        'https://wattsan.com/wp-content/uploads/1325-m1-milling-machine-mansonry-gallery-2-result.webp',
        'https://wattsan.com/wp-content/uploads/1325-m1-milling-machine-mansonry-gallery-6-result.webp',
        'https://wattsan.com/wp-content/uploads/router-masonry-gallery-1325-m1-3.webp',
        'https://wattsan.com/wp-content/uploads/router-masonry-gallery-1325-m1-4.webp',
    ],
    'wattsan-m1-1325-rd.html': [
        'https://wattsan.com/wp-content/uploads/M1-1325.png',
        'https://wattsan.com/wp-content/uploads/1325-m1-milling-machine-mansonry-gallery-1-result.webp',
        'https://wattsan.com/wp-content/uploads/1325-m1-milling-machine-mansonry-gallery-2-result.webp',
        'https://wattsan.com/wp-content/uploads/router-masonry-gallery-1325-m1-3.webp',
    ],
    'wattsan-m3-1325.html': [
        'https://wattsan.com/wp-content/uploads/M1-1325.png',
        'https://wattsan.com/wp-content/uploads/1325-m1-milling-machine-mansonry-gallery-1-result.webp',
        'https://wattsan.com/wp-content/uploads/1325-m1-milling-machine-mansonry-gallery-2-result.webp',
        'https://wattsan.com/wp-content/uploads/router-masonry-gallery-m3-5.webp',
        'https://wattsan.com/wp-content/uploads/router-masonry-gallery-1325-m1-5.webp',
    ],
    'wattsan-a1-1616.html': [
        'https://wattsan.com/wp-content/uploads/m2-1616-titul-result.webp',
        'https://wattsan.com/wp-content/uploads/cnc-router-wattsan-m2-1325-2.webp',
        'https://wattsan.com/wp-content/uploads/cnc-router-wattsan-m2-1325-3.webp',
        'https://wattsan.com/wp-content/uploads/cnc-router-wattsan-m2-1325-6.webp',
    ],
    'wattsan-m1-1616.html': [
        'https://wattsan.com/wp-content/uploads/m2-1616-titul-result.webp',
        'https://wattsan.com/wp-content/uploads/cnc-router-wattsan-m2-1325-2.webp',
        'https://wattsan.com/wp-content/uploads/cnc-router-wattsan-m2-1325-3.webp',
        'https://wattsan.com/wp-content/uploads/cnc-router-wattsan-m2-1325-4.webp',
        'https://wattsan.com/wp-content/uploads/cnc-router-wattsan-m2-1325-6.webp',
    ],
    'wattsan-1616.html': [
        'https://wattsan.com/wp-content/uploads/m2-1616-titul-result.webp',
        'https://wattsan.com/wp-content/uploads/cnc-router-wattsan-m2-1325-2.webp',
        'https://wattsan.com/wp-content/uploads/cnc-router-wattsan-m2-1325-3.webp',
        'https://wattsan.com/wp-content/uploads/cnc-router-wattsan-m2-1325-4.webp',
        'https://wattsan.com/wp-content/uploads/cnc-router-wattsan-m2-1325-6.webp',
        'https://wattsan.com/wp-content/uploads/cnc-router-wattsan-m2-1325-1.webp',
    ],
    'wattsan-m1-s2-x.html': [
        'https://wattsan.com/wp-content/uploads/m2-1616-titul-result.webp',
        'https://wattsan.com/wp-content/uploads/cnc-router-wattsan-m2-1325-2.webp',
        'https://wattsan.com/wp-content/uploads/cnc-router-wattsan-m2-1325-4.webp',
        'https://wattsan.com/wp-content/uploads/cnc-router-wattsan-m2-1325-6.webp',
    ],
    'wattsan-2030.html': [
        'https://wattsan.com/wp-content/uploads/m12030plus2-2.png',
        'https://wattsan.com/wp-content/uploads/2030-m1-milling-machine-mansonry-gallery-1-result.webp',
        'https://wattsan.com/wp-content/uploads/2030-m1-milling-machine-mansonry-gallery-2-result.webp',
        'https://wattsan.com/wp-content/uploads/2030-m1-milling-machine-mansonry-gallery-3-result-Copy.webp',
        'https://wattsan.com/wp-content/uploads/2030-m1-milling-machine-mansonry-gallery-6-result.webp',
        'https://wattsan.com/wp-content/uploads/router-masonry-gallery-2030-m1-4.webp',
        'https://wattsan.com/wp-content/uploads/router-masonry-gallery-2030-m1-5.webp',
    ],
    'wattsan-2040.html': [
        'https://wattsan.com/wp-content/uploads/20402-1-1-1-1.png',
        'https://wattsan.com/wp-content/uploads/2030-m1-milling-machine-mansonry-gallery-1-result.webp',
        'https://wattsan.com/wp-content/uploads/2030-m1-milling-machine-mansonry-gallery-2-result.webp',
        'https://wattsan.com/wp-content/uploads/2030-m1-milling-machine-mansonry-gallery-6-result.webp',
        'https://wattsan.com/wp-content/uploads/router-masonry-gallery-2030-m1-4.webp',
    ],
}

# Rich text sections for each product
DESCRIPTIONS = {
    '0404': 'Kompakta galda CNC frēze iesācējiem un hobijiem. Neskatoties uz nelielo izmēru, iekārta ir aprīkota ar jaudīgu 1.5 kW vārpstu un NcStudio kontrolieri, kas nodrošina izcilu apstrādes precizitāti. Ideāla izvēle suvenīru, mazu koka detaļu, 3D elementu un gravējumu ražošanai mājas darbnīcā vai mazā uzņēmumā. Pateicoties kompaktajiem izmēriem (810×890×710 mm), iekārta viegli iekļaujas jebkurā darba telpā.',
    '0609': 'Uzticama kompaktklases CNC frēze ar 900×600 mm darba laukumu. Aprīkota ar 2.2 kW vārpstu un profesionālu DSP A11 kontrolieri — lielisks vidusceļš starp hobija un industriālajām iekārtām. Ideāli piemērota reklāmas aģentūrām, mēbeļu detaļu un dažādu dekoratīvo elementu ražošanai. DSP A11 kontrolieris nodrošina ērtu darbu ar G-kodu un intuitīvu vadību caur rokas paneli.',
    '6090 A1': 'Profesionāla 3 asu CNC frēze ar 900×600 mm darba laukumu, 2.2 kW vārpstu un RichAuto A11 kontrolieri. A1 sērija piedāvā izcilu cenas un kvalitātes attiecību maziem un vidējiem uzņēmumiem. Iekārtas svars 400 kg nodrošina labu stabilitāti, bet profila gulta un stepper motori garantē uzticamu darbību ikdienas lietošanā.',
    '6090 M1': 'M1 sērijas pastiprināta 3 asu CNC frēze ar 900×600 mm darba laukumu. Salīdzinot ar A1 versiju, šai iekārtai ir smagāks rāmis (500 kg), kas nodrošina augstāku stabilitāti un precizitāti. RichAuto A11 kontrolieris ar pilnu G-koda atbalstu ļauj realizēt sarežģītus projektus ar augstu atkārtojamību.',
    '1313 A1': 'Ekonomiska A1 sērijas koka CNC frēze ar 1300×1300 mm darba laukumu. Ideāli piemērota standarta izmēru mēbeļu fasāžu, durvju un dekoratīvo paneļu ražošanai. 2.2 kW vārpsta un RichAuto A11 kontrolieris nodrošina visu nepieciešamo funkcionalitāti par pieejamu cenu. 540 kg svars garantē stabilu darbību.',
    '1313 M1': 'Profesionāla M1 sērijas koka CNC frēze ar 1300×1300 mm darba laukumu un 3.2 kW vārpstu. Pastiprinātais 650 kg rāmis absorbē vibrācijas un nodrošina tīrāku, precīzāku griezumu pat strādājot ar cietākiem materiāliem. Piemērota ikdienas nepārtrauktai ražošanai — mēbeļu darbnīcām, galdniecības uzņēmumiem.',
    '1313 M1 S4': 'Mūsu vispopulārākais modelis! Jaudīga CNC frēze ar 1300×1300 mm darba laukumu un 4.5 kW vārpstu. Čuguna gulta un 1000 kg masīvais rāmis nodrošina maksimālu stabilitāti un vibrāciju absorbciju. Lieliska izvēle profesionālai mēbeļu, durvju fasāžu un apjomīgu koka, kompozītu vai plastmasas projektu ražošanai.',
    '1325 A1': 'Ekonomiska pilna izmēra CNC frēze ar 1300×2500 mm darba laukumu — nozares standarta izmērs lokšņu materiālu apstrādei. 3 kW vārpsta un RichAuto A11 kontrolieris nodrošina visu nepieciešamo funkcionalitāti durvju, mēbeļu un lokšņu materiālu ražošanai. 720 kg rāmis garantē stabilu darbību.',
    '1325 M1': 'Profesionāla pilna izmēra CNC frēze ar 1300×2500 mm darba laukumu un 4.5 kW vārpstu. Nozares vispopulārākais izmērs — ideāli piemērots pilna izmēra saplākšņa, MDF un plastmasas loksnēm. 880 kg masīvais rāmis un RichAuto A11 kontrolieris nodrošina profesionālu precizitāti ilgstošā darbībā.',
    '1325 RD M1': 'Unikāla 4 asu CNC frēze ar rotācijas ierīci (Rotary Device) apaļu un cilindrisku detaļu apstrādei. 1300×2500 mm darba laukums apvienojumā ar 4.5 kW vārpstu un RichAuto A18 4 asu kontrolieri paver jaunas iespējas — balustri, kājas, kolonnas un citi apaļie elementi. 1550 kg smagais rāmis nodrošina stabilitāti visos 4 asu režīmos.',
    '1325 M3': 'Industriālas klases CNC frēze ar 1300×2500 mm darba laukumu un 4.5 kW vārpstu. Aprīkota ar NC Studio 8 profesionālo vadības programmatūru un Lambda4S servo sistēmu (PM95A-4A) augstākajai precizitātei un ātrumam. 1260 kg rāmis paredzēts nepārtrauktai 24/7 ražošanai — ideāli lieliem ražošanas uzņēmumiem.',
    '1616 A1': 'Ekonomiska A1 sērijas CNC frēze ar kvadrātveida 1600×1600 mm darba laukumu. Šis formāts ir īpaši ērts nestandarta un liela izmēra sagatavju apstrādei. 3.2 kW vārpsta un RichAuto A11 kontrolieris par pieejamu cenu. 620 kg konstrukcija piemērota maziem un vidējiem uzņēmumiem.',
    '1616 M1': 'Profesionāla M1 sērijas CNC frēze ar 1600×1600 mm kvadrātveida darba laukumu un 4.5 kW vārpstu. 730 kg rāmis nodrošina stabilitāti lielāku sagatavju precīzai apstrādei. Lieliski piemērota mēbeļu ražošanai, interjera elementiem un reklāmas konstrukcijām no koka, MDF un plastmasas.',
    '1616 M2': 'Universāla M2 sērijas CNC frēze — mūsu smagākā 1600×1600 mm klases iekārta! 1130 kg masīvā konstrukcija ar 4.5 kW vārpstu un RichAuto A11 kontrolieri nodrošina maksimālu stabilitāti un precizitāti jebkuram materiālam. Piemērota pat alumīnija apstrādei. Izvēle profesionāļiem, kas prasa labāko.',
    '1616 M1 S2 X': 'Revolucionāra CNC frēze ar DIVĀM neatkarīgām 4.5 kW vārpstām! Vienlaicīga divu identisku detaļu izgatavošana — divkārša produktivitāte, nemainot darba laukumu. RichAuto F7324 kontrolieris nodrošina abu vārpstu sinhronu vadību. 840 kg rāmis un 1600×1600 mm darba laukums. Ideāli sērijveida ražošanai!',
    '2030 M1': 'Industriāla lielformāta CNC frēze ar iespaidīgu 2000×3000 mm darba laukumu. 6 kW jaudīgā vārpsta ļauj apstrādāt lielākās loksnes bez savienojumiem — ideāli reklāmas konstrukcijām, liela izmēra mēbelēm un būvniecības elementiem. 1140 kg konstrukcija ar ātrumu līdz 15 000 mm/min nodrošina maksimālu produktivitāti.',
    '2040 M1': 'Mūsu lielākā standarta CNC frēze ar gigantisku 2000×4000 mm darba laukumu! 6 kW vārpsta un 1370 kg masīvais rāmis — maksimālā veiktspēja vislielākajiem projektiem. Paredzēta masveida lokšņu materiālu griešanai, lielformāta reklāmai, fasādēm un smagai industriālai ražošanai. Ātrums līdz 15 000 mm/min.',
}

# Features unique to each category
FEATURES_BY_CAT = {
    'mini': [
        ('Kompakts dizains', 'Ideāli piemērots mazām darbnīcām un hobiju projektiem. Viegli iekļaujas jebkurā telpā.'),
        ('Vienkārša lietošana', 'Piemērota iesācējiem — ātra uzstādīšana un intuitīva vadība caur kontrolieri.'),
        ('Zems trokšņa līmenis', 'Klusa darbība ļauj strādāt pat dzīvojamās telpās bez traucējumiem.'),
        ('T-Slot galds', 'Alumīnija T-slot galds ar spīlēm — ideāli piemērots nestandarta formas sagatavēm.'),
    ],
    '6090': [
        ('RichAuto A11 kontrolieris', 'Profesionāls DSP kontrolleris ar intuitīvu saskarni un pilnu G-koda atbalstu.'),
        ('Stabila konstrukcija', 'Pastiprināts profila rāmis nodrošina precizitāti un ilgmūžību ikdienas darbā.'),
        ('Daudzpusīgs pielietojums', 'Piemērots kokam, saplāksnim, MDF, akrilam un plastmasai.'),
        ('Viegla apkope', 'Modulāra konstrukcija atvieglo piekļuvi komponentēm un tehnisko apkopi.'),
    ],
    '1313': [
        ('Kvadrātveida darba zona', '1300×1300 mm — ideāls izmērs mēbeļu fasādēm, durvīm un dekoratīviem paneļiem.'),
        ('Čuguna / profila gulta', 'Izturīga gulta ar termisko apstrādi — saglabā precizitāti gadiem ilgi.'),
        ('Jaudīga vārpsta', 'Līdz 4.5 kW jauda ļauj strādāt ar cietiem materiāliem un dziļiem griezumiem.'),
        ('Profesionāla precizitāte', 'Lāzera kalibrētas sliedes un spirālveida zobratu sistēma.'),
    ],
    '1325': [
        ('Lokšņu formāts', '1300×2500 mm — standarta lokšņu izmērs, ideāls mēbeļu un durvju ražošanai.'),
        ('Siksnas reduktors', 'Optimāls risinājums mīkstiem metāliem, kokam un plastmasai — precizitāte par pieejamu cenu.'),
        ('Biezsienu metāls', 'Visas Wattsan iekārtas izgatavotas no biezsienu metāla — uzlabo vibrāciju izturību.'),
        ('Termiski apstrādāts rāmis', 'Rāmja termiskā apstrāde noņem metāla spriegumus — garantē ilgstošu precizitāti.'),
    ],
    '1616': [
        ('Kvadrātveida zona', '1600×1600 mm — ērts lielu un nestandarta izmēru sagatavju apstrādei.'),
        ('Masīva konstrukcija', 'Līdz 1130 kg smags rāmis absorbē vibrācijas — tīrāks griezums.'),
        ('Universāls pielietojums', 'No koka līdz alumīnijam — piemērots jebkuram materiālam un projektam.'),
        ('Rūpnieciskas klases komponentes', 'Kvalitatīvas sliedes, zobrati un gultņi no pasaules vadošajiem ražotājiem.'),
    ],
    '2030': [
        ('Milzīgs darba laukums', '2000×3000 mm — apstrādājiet lielākās loksnes bez savienojumiem.'),
        ('6 kW jauda', 'Jaudīgākā vārpsta sērijā — griež visu, sākot no saplākšņa līdz alumīnijam.'),
        ('Ātrums līdz 15 m/min', 'Augsts darba ātrums palielina produktivitāti liela mēroga ražošanā.'),
        ('1140 kg stabilitāte', 'Stabila platforma, kas iztur intensīvu ikdienas noslodzi.'),
    ],
    '2040': [
        ('Maksimālais izmērs', '2000×4000 mm — lielākais standarta CNC frēzes izmērs tirgū.'),
        ('6 kW industriālā vārpsta', 'Maksimāla jauda vislielākajiem un sarežģītākajiem projektiem.'),
        ('1370 kg — smagākais rāmis', 'Vislielākais un stabilākais rāmis visā sērijā — nulles vibrācijas.'),
        ('Ātrums līdz 15 m/min', 'Neskatoties uz izmēru, saglabā augstu darba ātrumu un precizitāti.'),
    ],
}

# Technical specs sections
TECH_SPECS = {
    'mini': [
        ('Iekārtas svars', '92-135 kg'),
        ('Gulta', 'Alumīnija T-slot / profils'),
        ('Piedziņa', 'Stepper motors'),
        ('Maks. ātrums', '7000 mm/min'),
        ('Vārpstas dzesēšana', 'Gaisa'),
        ('Barošana', '220V / 50Hz'),
        ('Programmatūra', 'NcStudio / DSP A11'),
        ('Apstrādājamie materiāli', 'Koks, saplāksnis, MDF, akrils, plastmasa'),
    ],
    '6090': [
        ('Iekārtas svars', '400-500 kg'),
        ('Gulta', 'Profils'),
        ('Piedziņa', 'Stepper motors (closed-loop optional)'),
        ('Maks. ātrums', '7000 mm/min'),
        ('Vārpstas dzesēšana', 'Gaisa'),
        ('Barošana', '220V / 50Hz'),
        ('Programmatūra', 'RichAuto A11'),
        ('Apstrādājamie materiāli', 'Koks, saplāksnis, MDF, akrils, plastmasa'),
    ],
    '1313': [
        ('Iekārtas svars', '540-1000 kg'),
        ('Gulta', 'Profils / Čuguns'),
        ('Piedziņa', 'Stepper motors'),
        ('Maks. ātrums', '7000 mm/min'),
        ('Vārpstas dzesēšana', 'Gaisa'),
        ('Barošana', '220V / 380V'),
        ('Programmatūra', 'RichAuto A11 / DSP A11'),
        ('Apstrādājamie materiāli', 'Koks, ozols, saplāksnis, MDF, akrils, kompozīti'),
    ],
    '1325': [
        ('Iekārtas svars', '720-1550 kg'),
        ('Gulta', 'Profils / Čuguns'),
        ('Piedziņa', 'Stepper motors / Servo (M3)'),
        ('Maks. ātrums', '7000-15000 mm/min'),
        ('Vārpstas dzesēšana', 'Gaisa'),
        ('Barošana', '220V / 380V'),
        ('Programmatūra', 'RichAuto A11/A18 / NC Studio 8'),
        ('Apstrādājamie materiāli', 'Koks, ozols, saplāksnis, MDF, akrils, alumīnijs, kompozīti'),
    ],
    '1616': [
        ('Iekārtas svars', '620-1130 kg'),
        ('Gulta', 'Profils'),
        ('Piedziņa', 'Stepper motors'),
        ('Maks. ātrums', '7000-10000 mm/min'),
        ('Vārpstas dzesēšana', 'Gaisa'),
        ('Barošana', '220V / 380V'),
        ('Programmatūra', 'RichAuto A11 / F7324'),
        ('Apstrādājamie materiāli', 'Koks, ozols, saplāksnis, MDF, akrils, alumīnijs'),
    ],
    '2030': [
        ('Iekārtas svars', '1140 kg'),
        ('Gulta', 'Profils'),
        ('Piedziņa', 'Stepper motors'),
        ('Maks. ātrums', '15000 mm/min'),
        ('Vārpstas dzesēšana', 'Gaisa'),
        ('Barošana', '380V'),
        ('Programmatūra', 'RichAuto A11'),
        ('Apstrādājamie materiāli', 'Koks, saplāksnis, MDF, akrils, alumīnijs, lielas loksnes'),
    ],
    '2040': [
        ('Iekārtas svars', '1370 kg'),
        ('Gulta', 'Profils'),
        ('Piedziņa', 'Stepper motors'),
        ('Maks. ātrums', '15000 mm/min'),
        ('Vārpstas dzesēšana', 'Gaisa'),
        ('Barošana', '380V'),
        ('Programmatūra', 'RichAuto A11'),
        ('Apstrādājamie materiāli', 'Koks, saplāksnis, MDF, akrils, alumīnijs, maksimālas loksnes'),
    ],
}

CATEGORY_MAP = {
    '0404': 'mini', '0609': 'mini',
    'A1 6090': '6090', 'M1 6090': '6090',
    'A1 1313': '1313', 'M1 1313': '1313', '1313': '1313',
    'A1 1325': '1325', '1325': '1325', 'M1 1325 RD': '1325', 'M3 1325': '1325',
    'A1 1616': '1616', 'M1 1616': '1616', '1616': '1616', 'M1 S2 X': '1616',
    '2030': '2030', '2040': '2040',
}

CSS = '''
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{font-family:'Inter',sans-serif;background:#fff;color:#1a1a1a;overflow-x:hidden;-webkit-font-smoothing:antialiased}
a{text-decoration:none;color:inherit}
img{display:block;max-width:100%}
:root{--bg:#fff;--bg2:#f5f5f5;--bg3:#eee;--ink:#1a1a1a;--ink2:#555;--ink3:#999;--accent:#E63C32;--border:rgba(0,0,0,.09);--border2:rgba(0,0,0,.15);--max:1280px;--ease:cubic-bezier(.22,1,.36,1);--gutter:clamp(20px,5vw,64px)}
.nav{position:fixed;top:0;left:0;right:0;z-index:300;height:64px;display:flex;align-items:center;justify-content:space-between;padding:0 var(--gutter);background:rgba(255,255,255,.96);backdrop-filter:blur(20px);border-bottom:1px solid var(--border)}
.nav-logo{display:flex;align-items:center;gap:14px}
.nav-logo img{height:22px;width:auto}
.nav-logo-sep{width:1px;height:18px;background:var(--border2)}
.nav-logo-lv{font-family:'Plus Jakarta Sans',sans-serif;font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;color:var(--ink2);font-weight:400}
.nav-logo-lv em{font-style:normal;color:var(--accent)}
.nav-links{display:flex;align-items:center;gap:28px}
.nav-links a{font-size:.73rem;letter-spacing:.08em;text-transform:uppercase;color:var(--ink2);transition:color .2s;font-weight:400}
.nav-links a:hover,.nav-links a.active{color:var(--accent)}
.nav-cta{display:flex;align-items:center;gap:10px}
.btn-ghost{padding:8px 18px;font-size:.7rem;letter-spacing:.08em;text-transform:uppercase;border:1px solid var(--border2);color:var(--ink2);transition:all .2s;font-weight:400;white-space:nowrap}
.btn-ghost:hover{border-color:var(--ink);color:var(--ink)}
.btn-accent{padding:9px 20px;font-size:.7rem;letter-spacing:.08em;text-transform:uppercase;background:var(--accent);color:#fff;font-weight:500;transition:background .2s;white-space:nowrap}
.btn-accent:hover{background:#c42e25}
@media(max-width:860px){.nav-links{display:none}}
.nav-sub{background:var(--bg2);border-bottom:1px solid var(--border);padding:8px 0;margin-top:64px;overflow-x:auto;-webkit-overflow-scrolling:touch;scrollbar-width:none}
.nav-sub::-webkit-scrollbar{display:none}
.nav-sub-inner{max-width:var(--max);margin:0 auto;padding:0 var(--gutter);display:flex;gap:6px;align-items:center}
.nav-sub span{font-size:.56rem;letter-spacing:.12em;text-transform:uppercase;color:var(--ink3);white-space:nowrap;margin-right:8px}
.nav-sub a{font-size:.62rem;padding:5px 10px;border:1px solid var(--border);color:var(--ink2);white-space:nowrap;transition:all .15s;letter-spacing:.04em;flex-shrink:0}
.nav-sub a:hover,.nav-sub a.active{border-color:var(--accent);color:var(--accent);background:rgba(230,60,50,.04)}
.breadcrumb{padding:0 var(--gutter);max-width:var(--max);margin:0 auto}
.breadcrumb-inner{display:flex;align-items:center;gap:8px;font-size:.62rem;letter-spacing:.08em;text-transform:uppercase;color:var(--ink3);padding:12px 0;border-bottom:1px solid var(--border);flex-wrap:wrap}
.breadcrumb-inner a{color:var(--ink3);transition:color .2s;white-space:nowrap}
.breadcrumb-inner a:hover{color:var(--accent)}
.breadcrumb-current{color:var(--ink);font-weight:500}
.product-hero{max-width:var(--max);margin:0 auto;padding:32px var(--gutter);display:grid;grid-template-columns:1.2fr 1fr;gap:48px;align-items:center}
@media(max-width:860px){.product-hero{grid-template-columns:1fr;gap:28px}}
.product-gallery{position:relative;user-select:none;-webkit-user-select:none}
.gallery-stage{position:relative;overflow:hidden;background:var(--bg2);border:1px solid var(--border);touch-action:pan-y pinch-zoom}
.gallery-track{display:flex;transition:transform .4s var(--ease);will-change:transform}
.gallery-slide{flex:0 0 100%;min-width:100%;aspect-ratio:4/3;object-fit:contain;padding:24px;background:var(--bg2)}
.gallery-arrow{position:absolute;top:50%;transform:translateY(-50%);z-index:10;width:40px;height:40px;border-radius:50%;background:#fff;border:1px solid var(--border);display:flex;align-items:center;justify-content:center;cursor:pointer;box-shadow:0 2px 12px rgba(0,0,0,.08);transition:all .2s;opacity:.85}
.gallery-arrow:hover{opacity:1;border-color:var(--accent);box-shadow:0 4px 20px rgba(230,60,50,.15)}
.gallery-arrow svg{width:16px;height:16px;color:var(--ink)}
.gallery-arrow.prev{left:12px}.gallery-arrow.next{right:12px}
.gallery-dots{display:flex;justify-content:center;gap:8px;margin-top:12px}
.gallery-dot{width:8px;height:8px;border-radius:50%;background:var(--border);border:none;cursor:pointer;transition:all .25s;padding:0}
.gallery-dot.active{background:var(--accent);transform:scale(1.3)}
.gallery-thumbs{display:flex;gap:8px;margin-top:10px;overflow-x:auto;padding-bottom:4px;scrollbar-width:none}
.gallery-thumbs::-webkit-scrollbar{display:none}
.gallery-thumb{width:72px;height:54px;object-fit:cover;border:1px solid var(--border);cursor:pointer;opacity:.55;transition:all .2s;flex-shrink:0}
.gallery-thumb:hover,.gallery-thumb.active{opacity:1;border-color:var(--accent)}
@media(max-width:700px){.gallery-arrow{display:none}.gallery-slide{padding:12px}}
.product-info{display:flex;flex-direction:column;gap:16px}
.product-badge{display:inline-flex;align-items:center;gap:7px;background:rgba(230,60,50,.1);border:1px solid rgba(230,60,50,.25);padding:5px 12px;font-size:.6rem;letter-spacing:.12em;text-transform:uppercase;color:var(--accent);font-weight:600;width:fit-content}
.product-badge-dot{width:5px;height:5px;border-radius:50%;background:var(--accent);animation:pulse 2s ease infinite}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.35}}
.product-title{font-family:'Plus Jakarta Sans',sans-serif;font-size:clamp(1.8rem,3.2vw,2.8rem);font-weight:300;letter-spacing:-.03em;line-height:1.08}
.product-title strong{font-weight:700}
.product-title em{font-style:italic;color:var(--ink2);font-size:.75em;display:block;margin-top:4px}
.product-subtitle{font-size:.85rem;color:var(--ink2);line-height:1.65;font-weight:300}
.key-specs{display:grid;grid-template-columns:1fr 1fr;gap:1px;background:var(--border);border:1px solid var(--border)}
.key-spec{display:flex;flex-direction:column;gap:2px;padding:12px 14px;background:var(--bg2)}
.key-spec-l{font-size:.6rem;letter-spacing:.1em;text-transform:uppercase;color:var(--ink3);font-weight:500}
.key-spec-v{font-size:.9rem;font-weight:400;color:var(--ink)}
.product-cta{display:flex;gap:10px;flex-wrap:wrap}
.btn-primary{padding:13px 28px;background:var(--accent);color:#fff;font-size:.75rem;letter-spacing:.06em;text-transform:uppercase;font-weight:500;transition:background .2s;white-space:nowrap}
.btn-primary:hover{background:#c42e25}
.btn-outline{padding:13px 28px;border:1px solid var(--border2);color:var(--ink2);font-size:.72rem;letter-spacing:.06em;text-transform:uppercase;font-weight:400;transition:all .2s;white-space:nowrap}
.btn-outline:hover{border-color:var(--accent);color:var(--accent)}
.section{padding:clamp(40px,6vw,72px) var(--gutter)}
.section-max{max-width:var(--max);margin:0 auto}
.section-title{font-family:'Plus Jakarta Sans',sans-serif;font-size:clamp(1.6rem,3vw,2.2rem);font-weight:300;letter-spacing:-.03em;line-height:1.1;color:var(--ink);margin-bottom:10px}
.section-title strong{font-weight:700}
.eyebrow{display:inline-flex;align-items:center;gap:10px;font-size:.6rem;letter-spacing:.2em;text-transform:uppercase;color:var(--ink3);margin-bottom:14px}
.eyebrow::before{content:'';width:20px;height:1px;background:var(--accent);display:block}
.specs-grid{display:grid;grid-template-columns:1fr 1fr;gap:32px}
@media(max-width:700px){.specs-grid{grid-template-columns:1fr}}
.specs-block h3{font-family:'Plus Jakarta Sans',sans-serif;font-size:.8rem;font-weight:600;letter-spacing:.05em;text-transform:uppercase;color:var(--ink);margin-bottom:14px;padding-bottom:8px;border-bottom:2px solid var(--accent);display:inline-block}
.specs-row{display:flex;justify-content:space-between;padding:10px 0;border-bottom:1px solid var(--border);font-size:.82rem}
.specs-row-l{color:var(--ink2);font-weight:300}
.specs-row-v{color:var(--ink);font-weight:400;text-align:right}
.features-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:16px}
.feature-card{padding:20px;background:var(--bg2);border:1px solid var(--border);transition:border-color .2s}
.feature-card:hover{border-color:rgba(230,60,50,.25)}
.feature-card-icon{width:28px;height:28px;display:flex;align-items:center;justify-content:center;background:rgba(230,60,50,.1);margin-bottom:10px}
.feature-card-icon svg{width:18px;height:18px;color:var(--accent)}
.feature-card h4{font-family:'Plus Jakarta Sans',sans-serif;font-size:.88rem;font-weight:500;color:var(--ink);margin-bottom:5px}
.feature-card p{font-size:.74rem;color:var(--ink2);line-height:1.55;font-weight:300}
.materials-slider{position:relative;display:flex;align-items:center;gap:0;max-width:100%}
.materials-arrow{flex-shrink:0;width:36px;height:36px;border-radius:50%;background:#fff;border:1px solid var(--border);display:flex;align-items:center;justify-content:center;cursor:pointer;transition:all .2s;color:var(--ink);font-size:1.2rem;line-height:1;z-index:2}
.materials-arrow:hover{border-color:var(--accent);color:var(--accent);box-shadow:0 2px 12px rgba(230,60,50,.15)}
.materials-arrow svg{width:14px;height:14px}
.materials-track-wrap{overflow:hidden;flex:1;margin:0 4px}
.materials-track{display:flex;gap:20px;transition:transform .4s var(--ease);padding:8px 4px;will-change:transform}
.material-card{flex-shrink:0;display:flex;flex-direction:column;align-items:center;gap:10px;width:100px;cursor:default}
.material-img{width:80px;height:80px;border-radius:50%;object-fit:cover;border:2px solid var(--border);background:var(--bg2);transition:all .25s}
.material-card:hover .material-img{border-color:var(--accent);transform:scale(1.08)}
.material-name{font-size:.62rem;letter-spacing:.04em;text-transform:uppercase;color:var(--ink2);font-weight:500;text-align:center}
@media(max-width:600px){.material-card{width:80px}.material-img{width:64px;height:64px}.materials-track{gap:14px}}
.desc-text{font-size:.88rem;color:var(--ink2);line-height:1.8;font-weight:300;max-width:780px}
footer{background:var(--ink);color:#fff;padding:0}
.footer-main{max-width:var(--max);margin:0 auto;padding:60px var(--gutter) 40px;display:grid;grid-template-columns:2fr 1fr 1fr 1fr;gap:40px}
.footer-col h4{font-family:'Plus Jakarta Sans',sans-serif;font-size:0.95rem;font-weight:500;margin-bottom:18px;color:#fff;letter-spacing:-0.01em}
.footer-col p{font-size:0.85rem;color:rgba(255,255,255,.4);line-height:1.7;margin-bottom:12px}
.footer-col ul{list-style:none;display:flex;flex-direction:column;gap:10px}
.footer-col ul li{font-size:0.84rem}
.footer-col ul li a{color:rgba(255,255,255,.45);transition:color .2s}
.footer-col ul li a:hover{color:var(--accent)}
.footer-col .c-row{display:flex;align-items:flex-start;gap:10px;font-size:0.84rem;color:rgba(255,255,255,.55);margin-bottom:9px;line-height:1.5}
.footer-col .c-row svg{width:15px;height:15px;color:var(--accent);flex-shrink:0;margin-top:3px}
.footer-col .c-row a{color:#fff;font-weight:500;transition:color .2s}
.footer-col .c-row a:hover{color:var(--accent)}
.footer-bottom{border-top:1px solid rgba(255,255,255,.06);padding:20px var(--gutter);text-align:center;font-size:0.75rem;color:rgba(255,255,255,.3);display:flex;flex-direction:column;gap:4px}
.footer-bottom a{color:rgba(255,255,255,.45);transition:color .2s}
.footer-bottom a:hover{color:var(--accent)}
@media(max-width:1100px){.footer-main{grid-template-columns:1fr 1fr;gap:36px}}
@media(max-width:600px){.footer-main{grid-template-columns:1fr}}
.sr{opacity:0;transform:translateY(20px);transition:opacity .65s var(--ease),transform .65s var(--ease)}
.sr.in{opacity:1;transform:translateY(0)}
.d1{transition-delay:.08s}.d2{transition-delay:.16s}.d3{transition-delay:.24s}
'''

NAV = '''<nav class="nav"><div class="nav-logo"><a href="index.html"><img src="https://wattsan.com/wp-content/uploads/wattsan_logo-1.svg" alt="Wattsan"></a><div class="nav-logo-sep"></div><div class="nav-logo-lv">Latvija <em>·</em> LV</div></div><div class="nav-links"><a href="index.html#katalogs">CNC Frēzes</a><a href="index.html#prieksrocibas">Priekšrocības</a><a href="index.html#info">Par CNC</a><a href="https://bratus.lv/" target="_blank">bratus.lv ↗</a></div><div class="nav-cta"><a href="https://bratus.lv/" target="_blank" class="btn-ghost">Oficiālais pārstāvis ↗</a><a href="#kontakti" class="btn-accent">Pieteikt</a><div class="lang-switcher" role="group" aria-label="Language selector"><a href="#" data-lang="lv" class="active" data-i18n="common.lang_lv">LV</a><a href="#" data-lang="en" data-i18n="common.lang_en">EN</a></div></div></nav>'''

SUBNAV = '<div class="nav-sub"><div class="nav-sub-inner"><span>CNC Frēzes:</span>' + ''.join([
    f'<a href="{f}">{f.replace("wattsan-","").replace(".html","").replace("-"," ").upper()}</a>'
    for f in sorted([os.path.basename(x) for x in glob.glob(os.path.join(BASE, 'wattsan-*.html'))])
]) + '</div></div>'

FOOTER = '''<footer role="contentinfo" aria-label="Kontaktu informācija"><div class="footer-main"><div class="footer-col"><h4>SIA Bratus — Oficiālais Wattsan Pārstāvis</h4><p>Oficiālais Wattsan iekārtu izplatītājs Latvijā. Piegādājam, uzstādām un nodrošinām tehnisko atbalstu un garantiju visā reģionā. Vienīgais sertificētais Wattsan partneris Baltijā.</p><p style="margin-top:8px"><strong style="color:rgba(255,255,255,.55)">Darba laiks:</strong> P.–Pk. 9:00–18:00</p></div><div class="footer-col"><h4>Ātrās Saites</h4><ul><li><a href="/#katalogs">CNC Frēžu Katalogs</a></li><li><a href="https://bratus.lv/pages/cnc-frezes" target="_blank" rel="noopener noreferrer">Pilnais Katalogs</a></li><li><a href="https://bratus.lv/pages/par-mums" target="_blank" rel="noopener noreferrer">Par Mums</a></li><li><a href="https://bratus.lv/policies/privacy-policy" target="_blank" rel="noopener noreferrer">Privātuma Politika</a></li><li><a href="https://wattsan.com/" target="_blank" rel="noopener noreferrer">Wattsan.com</a></li></ul></div><div class="footer-col"><h4>Kontakti</h4><div class="c-row"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6A2 2 0 0 1 2.11 4h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81A2 2 0 0 1 7.36 10.7L6.09 11.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg><a href="tel:+37124424434">+371 24 424 434</a></div><div class="c-row"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg><a href="mailto:sales@bratus.lv">sales@bratus.lv</a></div><div class="c-row"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg><span>Dārznieku iela 42, Ķekava, LV-2123</span></div><div class="c-row"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg><span>Reģ. nr. 40203628316</span></div><div class="c-row"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg><span>PVN Maksātājs</span></div></div><div class="footer-col"><h4>Informācija</h4><ul><li><a href="https://bratus.lv/pages/par-mums" target="_blank" rel="noopener noreferrer">Par Mums</a></li><li><a href="https://bratus.lv/pages/cnc-frezes" target="_blank" rel="noopener noreferrer">Pilnais Katalogs</a></li><li><a href="https://bratus.lv/policies/privacy-policy" target="_blank" rel="noopener noreferrer">Privātuma Politika</a></li><li><a href="https://bratus.lv/policies/terms-of-service" target="_blank" rel="noopener noreferrer">Lietošanas Noteikumi</a></li><li><a href="https://wattsan.com/" target="_blank" rel="noopener noreferrer">Wattsan.com</a></li></ul></div></div><div class="footer-bottom"><p>&copy; <span id="yr"></span> SIA Bratus (cncfrezes.lv). Visas tiesības aizsargātas.</p><p style="font-size:0.7rem;margin-top:2px;color:rgba(255,255,255,.2)">Mājaslapas izstrādi un SEO optimizāciju veica <a href="https://latseo.com" target="_blank" rel="noopener noreferrer" style="color:rgba(255,255,255,.35)">latseo.com</a></p></div></footer>'''

JS = '<script>document.getElementById("yr").textContent=new Date().getFullYear();const o=new IntersectionObserver(e=>{e.forEach(x=>{if(x.isIntersecting){x.target.classList.add("in");o.unobserve(x.target)}});},{threshold:.05});document.querySelectorAll(".sr").forEach(el=>o.observe(el));function initGallery(id){const track=document.getElementById(id);if(!track)return;const slides=track.children;const total=slides.length;let idx=0;const dots=document.querySelectorAll("#"+id.replace("track","dots")+" .gallery-dot");const thumbs=document.querySelectorAll("#"+id.replace("track","thumbs")+" .gallery-thumb");function go(n){idx=(n+total)%total;track.style.transform="translateX(-"+idx*100+"%)";dots.forEach((d,i)=>{d.classList.toggle("active",i===idx)});thumbs.forEach((t,i)=>{t.classList.toggle("active",i===idx);if(i===idx)t.scrollIntoView({behavior:"smooth",block:"nearest",inline:"center"})})}document.getElementById(id.replace("track","prev")).addEventListener("click",()=>go(idx-1));document.getElementById(id.replace("track","next")).addEventListener("click",()=>go(idx+1));dots.forEach((d,i)=>{d.addEventListener("click",()=>go(i))});thumbs.forEach((t,i)=>{t.addEventListener("click",()=>go(i))});let ts=0;track.parentElement.addEventListener("touchstart",e=>{ts=e.touches[0].clientX},{passive:true});track.parentElement.addEventListener("touchend",e=>{const d=ts-e.changedTouches[0].clientX;if(Math.abs(d)>50){d>0?go(idx+1):go(idx-1)}},{passive:true});document.addEventListener("keydown",e=>{const g=e.target.closest(".product-gallery");if(g&&g.contains(track)){if(e.key==="ArrowLeft")go(idx-1);if(e.key==="ArrowRight")go(idx+1)}})}document.querySelectorAll(".gallery-track").forEach(t=>initGallery(t.id));function initMatSlider(id){const track=document.getElementById(id);if(!track)return;const cards=track.children;const cardW=cards[0]?cards[0].offsetWidth+20:120;let pos=0;const maxScroll=track.scrollWidth-track.parentElement.offsetWidth;document.getElementById(id.replace("track","prev")).addEventListener("click",()=>{pos=Math.max(0,pos-cardW*3);track.style.transform="translateX(-"+pos+"px)"});document.getElementById(id.replace("track","next")).addEventListener("click",()=>{pos=Math.min(maxScroll,pos+cardW*3);track.style.transform="translateX(-"+pos+"px)"})}document.querySelectorAll(".materials-track").forEach(t=>initMatSlider(t.id))</script>'

SVG_ICONS = {
    'Kompakts dizains': '<path d="M3 7v10a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-1V5a2 2 0 00-2-2H8a2 2 0 00-2 2v2H3z"/>',
    'Vienkārša lietošana': '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
    'Zems trokšņa līmenis': '<path d="M11 5L6 9H2v6h4l5 4V5z"/><path d="M19.07 4.93a10 10 0 010 14.14"/><path d="M15.54 8.46a5 5 0 010 7.07"/>',
    'Stabila konstrukcija': '<path d="M12 2L2 7l10 5 10-5-10-5z"/><path d="M2 17l10 5 10-5"/><path d="M2 12l10 5 10-5"/>',
    'Daudzpusīgs pielietojums': '<rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/>',
    'Viegla apkope': '<circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 00.33 1.82l.06.06a2 2 0 010 2.83 2 2 0 01-2.83 0l-.06-.06a1.65 1.65 0 00-1.82-.33 1.65 1.65 0 00-1 1.51V21a2 2 0 01-4 0v-.09A1.65 1.65 0 009 19.4a1.65 1.65 0 00-1.82.33l-.06.06a2 2 0 01-2.83-2.83l.06-.06A1.65 1.65 0 004.68 15a1.65 1.65 0 00-1.51-1H3a2 2 0 010-4h.09A1.65 1.65 0 004.6 9a1.65 1.65 0 00-.33-1.82l-.06-.06a2 2 0 012.83-2.83l.06.06A1.65 1.65 0 009 4.68a1.65 1.65 0 001-1.51V3a2 2 0 014 0v.09a1.65 1.65 0 001 1.51 1.65 1.65 0 001.82-.33l.06-.06a2 2 0 012.83 2.83l-.06.06A1.65 1.65 0 0019.4 9a1.65 1.65 0 001.51 1H21a2 2 0 010 4h-.09a1.65 1.65 0 00-1.51 1z"/>',
    'Jaudīga vārpsta': '<polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/>',
    'Profesionāla precizitāte': '<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>',
    'Lokšņu formāts': '<rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><line x1="3" y1="9" x2="21" y2="9"/><line x1="9" y1="21" x2="9" y2="9"/>',
    'Siksnas reduktors': '<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/>',
    'Biezsienu metāls': '<path d="M12 22s-8-4.5-8-11.8V4l8-2 8 2v6.2c0 7.3-8 11.8-8 11.8z"/>',
    'Termiski apstrādāts rāmis': '<path d="M17.66 17.66l-2.83-2.83"/><circle cx="12" cy="12" r="10"/><path d="M6.34 6.34l2.83 2.83"/><path d="M12 2v4"/><path d="M2 12h4"/><path d="M20 12h-4"/><path d="M12 18v4"/>',
    'Milzīgs darba laukums': '<rect x="3" y="3" width="18" height="18" rx="2" ry="2"/>',
    '6 kW jauda': '<polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/>',
    'Maksimālais izmērs': '<polyline points="15 3 21 3 21 9"/><polyline points="9 21 3 21 3 15"/><line x1="21" y1="3" x2="14" y2="10"/><line x1="3" y1="21" x2="10" y2="14"/>',
    'Rūpnieciskas klases komponentes': '<rect x="2" y="7" width="20" height="10" rx="2" ry="2"/><path d="M16 7V5a2 2 0 00-2-2h-4a2 2 0 00-2 2v2"/>',
    'Masīva konstrukcija': '<rect x="2" y="3" width="20" height="14" rx="2" ry="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/>',
    'Universāls pielietojums': '<circle cx="12" cy="12" r="10"/><path d="M2 12h20"/><path d="M12 2a15.3 15.3 0 014 10 15.3 15.3 0 01-4 10"/><path d="M12 2a15.3 15.3 0 00-4 10 15.3 15.3 0 004 10"/>',
    'T-Slot galds': '<rect x="3" y="3" width="18" height="18" rx="2"/><line x1="3" y1="9" x2="21" y2="9"/><line x1="3" y1="15" x2="21" y2="15"/>',
    'Ātrums līdz 15 m/min': '<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>',
    'Čuguna / profila gulta': '<path d="M20 21v-2a4 4 0 00-4-4H8a4 4 0 00-4 4v2"/><circle cx="12" cy="7" r="4"/>',
    'Kvadrātveida darba zona': '<rect x="3" y="3" width="18" height="18" rx="2" ry="2"/>',
    'Kvadrātveida zona': '<rect x="3" y="3" width="18" height="18" rx="2" ry="2"/>',
    'default': '<polyline points="20 6 9 17 4 12"/>',
}

HEAD1 = '<!DOCTYPE html><html lang="lv"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">'
HEAD2 = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet"><style>'
HEAD3 = '</style></head><body>'
HTML_END = '</body></html>'


def model_key(fn):
    return fn.replace('wattsan-', '').replace('.html', '')


def get_cat(slug):
    for k, v in CATEGORY_MAP.items():
        if k.replace(' ', '') == slug.replace('-', '').upper():
            return v
    return '6090'


def make_page(fn, meta_title, meta_desc, canonical, model_name, badge, gallery_imgs, key_specs, desc_text, features, tech_specs, materials):
    """Generate complete HTML product page."""
    # Gallery - swipeable carousel with arrows + dots
    gallery_id = 'g_' + model_name.replace(' ','_').lower()
    slides = '\n'.join([f'<img class="gallery-slide" src="{img}" alt="Wattsan {model_name}">' for img in gallery_imgs])
    dots = '\n'.join([f'<button class="gallery-dot{" active" if i==0 else ""}" data-idx="{i}" aria-label="Bilde {i+1}"></button>' for i in range(len(gallery_imgs))])
    thumbs = '\n'.join([f'<img class="gallery-thumb{" active" if i==0 else ""}" src="{img}" data-idx="{i}" alt="Wattsan {model_name}">' for i, img in enumerate(gallery_imgs)])
    gallery_html = f'''<div class="product-gallery sr">
<div class="gallery-stage">
<div class="gallery-track" id="{gallery_id}_track">{slides}</div>
<button class="gallery-arrow prev" id="{gallery_id}_prev" aria-label="Iepriekšējā"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="15 18 9 12 15 6"/></svg></button>
<button class="gallery-arrow next" id="{gallery_id}_next" aria-label="Nākamā"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"/></svg></button>
</div>
<div class="gallery-dots" id="{gallery_id}_dots">{dots}</div>
<div class="gallery-thumbs" id="{gallery_id}_thumbs">{thumbs}</div>
</div>'''

    # Key specs
    spec_items = '\n'.join([
        f'<div class="key-spec"><div class="key-spec-l">{k}</div><div class="key-spec-v">{v}</div></div>'
        for k, v in key_specs
    ])
    specs_html = f'<div class="key-specs">{spec_items}</div>'

    # Features
    feat_cards = '\n'.join([
        f'<div class="feature-card sr"><div class="feature-card-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">{SVG_ICONS.get(f[0], SVG_ICONS["default"])}</svg></div><h4>{f[0]}</h4><p>{f[1]}</p></div>'
        for f in features
    ])

    # Materials section
    mat_cards = '\n'.join([f'<div class="material-card"><img class="material-img" src="{img}" alt="{name}" loading="lazy"><span class="material-name">{name}</span></div>' for name, img in MATERIALS.items()])
    mat_html = f'''<div class="materials-slider">
<button class="materials-arrow" id="{gallery_id}_mat_prev" aria-label="Iepriekš"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="15 18 9 12 15 6"/></svg></button>
<div class="materials-track-wrap"><div class="materials-track" id="{gallery_id}_mat_track">{mat_cards}</div></div>
<button class="materials-arrow" id="{gallery_id}_mat_next" aria-label="Tālāk"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"/></svg></button>
</div>'''

    # Tech specs
    tech_rows = '\n'.join([
        f'<div class="specs-row"><div class="specs-row-l">{k}</div><div class="specs-row-v">{v}</div></div>'
        for k, v in tech_specs
    ])

    # Materials
    mat_tags = '\n'.join([f'<span class="material-tag">{m}</span>' for m in materials])

    body = f'''{NAV}
{SUBNAV}
<div class="breadcrumb"><div class="breadcrumb-inner"><a href="index.html">Sākums</a><span>/</span><a href="index.html#katalogs">CNC Frēzes</a><span>/</span><span class="breadcrumb-current">Wattsan {model_name}</span></div></div>
<section class="product-hero">
<img class="gallery-slide" src="{gallery_imgs[0]}" alt="Wattsan {model_name}" style="aspect-ratio:4/3;object-fit:contain;background:var(--bg2);border:1px solid var(--border);padding:24px">
<div class="product-info sr d1">
<div class="product-badge"><span class="product-badge-dot"></span>{badge}</div>
<h1 class="product-title">Wattsan <strong>{model_name}</strong></h1>
<p class="product-subtitle">{desc_text.split('.')[0]}.</p>
{specs_html}
<div class="product-cta"><a href="https://bratus.lv/pages/contact" class="btn-primary">Pieprasīt piedāvājumu</a><a href="https://bratus.lv/pages/cnc-frezes" target="_blank" class="btn-outline">Skatīt bratus.lv ↗</a></div>
</div>
</section>
<section class="section" style="background:var(--bg2);border-top:1px solid var(--border)">
<div class="section-max">
<div class="eyebrow sr">Apraksts</div>
<h2 class="section-title sr d1">Par <strong>Wattsan {model_name}</strong></h2>
<p class="desc-text sr d2" style="margin-top:16px">{desc_text}</p>
</div>
</section>
<section class="section" style="background:var(--bg);border-top:1px solid var(--border)">
<div class="section-max">
<div class="eyebrow sr">Galerija</div>
<h2 class="section-title sr d1">Attēlu <strong>galerija</strong></h2>
{gallery_html}
</div>
</section>
<section class="section" style="background:var(--bg2);border-top:1px solid var(--border)">
<div class="section-max">
<div class="eyebrow sr">Priekšrocības</div>
<h2 class="section-title sr d1">Kāpēc <strong>Wattsan {model_name}</strong>?</h2>
<div class="features-grid" style="margin-top:24px">{feat_cards}</div>
</div>
</section>
<section class="section" style="background:var(--bg);border-top:1px solid var(--border)">
<div class="section-max">
<div class="eyebrow sr">Tehniskie dati</div>
<h2 class="section-title sr d1">Specifikācijas</h2>
<div class="specs-grid" style="margin-top:24px">
<div class="specs-block">{tech_rows}</div>
<div class="specs-block">
<h3>Iekārtas klase</h3>
<div class="specs-row"><div class="specs-row-l">Sērija</div><div class="specs-row-v">{badge}</div></div>
<div class="specs-row"><div class="specs-row-l">Pielietojums</div><div class="specs-row-v">Koks, saplāksnis, MDF, akrils, plastmasa</div></div>
</div>
</div>
</div>
</section>
<section class="section" style="background:var(--bg2);border-top:1px solid var(--border)">
<div class="section-max">
<div class="eyebrow sr">Materiāli</div>
<h2 class="section-title sr d1">Apstrādā <strong>materiālus</strong></h2>
{mat_html}
</div>
</section>
{FOOTER}
{JS}'''

    meta = f'''{HEAD1}<title>{meta_title}</title><meta name="description" content="{meta_desc}"><link rel="canonical" href="{canonical}">{HEAD2}{CSS}{HEAD3}'''
    return meta + body + HTML_END


# Products data
# All materials with Wattsan images
MATERIALS = {
    'Koks': 'https://wattsan.com/wp-content/uploads/wood_wp.webp',
    'Saplāksnis': 'https://wattsan.com/wp-content/uploads/plywood_wp.webp',
    'MDF': 'https://wattsan.com/wp-content/uploads/mdf_wp.webp',
    'Akrils': 'https://wattsan.com/wp-content/uploads/Acrylic_plexiglass_wp.webp',
    'Plastmasa': 'https://wattsan.com/wp-content/uploads/Plastic_wp.webp',
    'Skaidu plāksne': 'https://wattsan.com/wp-content/uploads/%D0%A1hipboard_wp.webp',
    'Alumīnijs': 'https://wattsan.com/wp-content/uploads/aluminium_wp.webp',
    'Varš': 'https://wattsan.com/wp-content/uploads/Copper_wp.webp',
    'Gumija': 'https://wattsan.com/wp-content/uploads/rubber_wp.webp',
    'Paronīts': 'https://wattsan.com/wp-content/uploads/Paronite_wp.webp',
}

PRODUCTS = [
    {
        'fn': 'wattsan-0404.html',
        'meta_title': 'Wattsan 0404 MINI | Galda CNC Frēze | Bratus',
        'meta_desc': 'Wattsan 0404 MINI — kompakta galda CNC frēze ar 400×400 mm, 1.5 kW, NcStudio. Ideāla hobijiem un maziem uzņēmumiem. Oficiālais Wattsan pārstāvis Latvijā.',
        'canonical': 'https://cncfrezes.lv/0404.html',
        'model': '0404 MINI',
        'badge': 'Mini Sērija',
        'key_specs': [('Darba laukums', '400 × 400 mm'), ('Vārpsta', '1.5 kW'), ('Kontrolieris', 'NcStudio'), ('Svars', '92 kg')],
        'materials': ['Koks', 'Saplāksnis', 'Akrils', 'MDF', 'Plastmasa'],
    },
    {
        'fn': 'wattsan-0609.html',
        'meta_title': 'Wattsan 0609 MINI | Kompakta CNC Frēze | Bratus',
        'meta_desc': 'Wattsan 0609 MINI — kompakta CNC frēze ar 900×600 mm, 2.2 kW, DSP A11. Lieliski piemērota reklāmas aģentūrām un mazajai ražošanai.',
        'canonical': 'https://cncfrezes.lv/0609.html',
        'model': '0609 MINI',
        'badge': 'Mini Sērija',
        'key_specs': [('Darba laukums', '900 × 600 mm'), ('Vārpsta', '2.2 kW'), ('Kontrolieris', 'DSP A11'), ('Svars', '135 kg')],
        'materials': ['Koks', 'Saplāksnis', 'Akrils', 'MDF', 'Plastmasa'],
    },
    {
        'fn': 'wattsan-a1-6090.html',
        'meta_title': 'Wattsan 6090 A1 | 3 Asu CNC Frēze | Bratus',
        'meta_desc': 'Wattsan 6090 A1 — 3 asu CNC frēze ar 900×600 mm, 2.2 kW, RichAuto A11. Ekonomiska profesionāla iekārta.',
        'canonical': 'https://cncfrezes.lv/6090-a1.html',
        'model': 'A1 6090',
        'badge': 'A1 Sērija · 3 Asis',
        'key_specs': [('Darba laukums', '900 × 600 mm'), ('Vārpsta', '2.2 kW'), ('Kontrolieris', 'RichAuto A11'), ('Svars', '400 kg')],
        'materials': ['Koks', 'Saplāksnis', 'MDF', 'Akrils', 'Plastmasa'],
    },
    {
        'fn': 'wattsan-m1-6090.html',
        'meta_title': 'Wattsan 6090 M1 | Pastiprināta CNC Frēze | Bratus',
        'meta_desc': 'Wattsan 6090 M1 — pastiprināta 3 asu CNC frēze ar 900×600 mm, 2.2 kW, RichAuto A11, 500 kg.',
        'canonical': 'https://cncfrezes.lv/6090-m1.html',
        'model': 'M1 6090',
        'badge': 'M1 Sērija · Pastiprināta',
        'key_specs': [('Darba laukums', '900 × 600 mm'), ('Vārpsta', '2.2 kW'), ('Kontrolieris', 'RichAuto A11'), ('Svars', '500 kg')],
        'materials': ['Koks', 'Saplāksnis', 'MDF', 'Akrils', 'Alumīnijs'],
    },
    {
        'fn': 'wattsan-a1-1313.html',
        'meta_title': 'Wattsan 1313 A1 | Koka CNC Frēze | Bratus',
        'meta_desc': 'Wattsan 1313 A1 — koka CNC frēze ar 1300×1300 mm, 2.2 kW, RichAuto A11. Ekonomiska izvēle.',
        'canonical': 'https://cncfrezes.lv/1313-a1.html',
        'model': 'A1 1313',
        'badge': 'A1 Sērija · Ekonomiska',
        'key_specs': [('Darba laukums', '1300 × 1300 mm'), ('Vārpsta', '2.2 kW'), ('Kontrolieris', 'RichAuto A11'), ('Svars', '540 kg')],
        'materials': ['Koks', 'Saplāksnis', 'MDF', 'Akrils', 'Kompozīti'],
    },
    {
        'fn': 'wattsan-m1-1313.html',
        'meta_title': 'Wattsan 1313 M1 | Profesionāla CNC Frēze | Bratus',
        'meta_desc': 'Wattsan 1313 M1 — profesionāla koka CNC frēze ar 1300×1300 mm, 3.2 kW, RichAuto A11, 650 kg.',
        'canonical': 'https://cncfrezes.lv/1313-m1.html',
        'model': 'M1 1313',
        'badge': 'M1 Sērija · Profesionāla',
        'key_specs': [('Darba laukums', '1300 × 1300 mm'), ('Vārpsta', '3.2 kW'), ('Kontrolieris', 'RichAuto A11'), ('Svars', '650 kg')],
        'materials': ['Koks', 'Ozols', 'Saplāksnis', 'MDF', 'Akrils'],
    },
    {
        'fn': 'wattsan-1313.html',
        'meta_title': 'Wattsan 1313 M1 S4 | Populārākā CNC Frēze | Bratus',
        'meta_desc': 'Wattsan 1313 M1 S4 — populārākais modelis ar 1300×1300 mm, 4.5 kW, DSP A11, 1000 kg čuguna gultu.',
        'canonical': 'https://cncfrezes.lv/1313.html',
        'model': '1313 M1 S4',
        'badge': 'Populārākais · Best-seller',
        'key_specs': [('Darba laukums', '1300 × 1300 mm'), ('Vārpsta', '4.5 kW'), ('Kontrolieris', 'DSP A11'), ('Svars', '1000 kg')],
        'materials': ['Koks', 'Ozols', 'Saplāksnis', 'MDF', 'Akrils', 'Alumīnijs'],
    },
    {
        'fn': 'wattsan-a1-1325.html',
        'meta_title': 'Wattsan 1325 A1 | Pilna Izmēra CNC Frēze | Bratus',
        'meta_desc': 'Wattsan 1325 A1 — pilna izmēra CNC frēze ar 1300×2500 mm, 3 kW, RichAuto A11. Ideāla durvju un lokšņu apstrādei.',
        'canonical': 'https://cncfrezes.lv/1325-a1.html',
        'model': 'A1 1325',
        'badge': 'A1 Sērija · Pilna izmēra',
        'key_specs': [('Darba laukums', '1300 × 2500 mm'), ('Vārpsta', '3 kW'), ('Kontrolieris', 'RichAuto A11'), ('Svars', '720 kg')],
        'materials': ['Koks', 'Saplāksnis', 'MDF', 'Akrils', 'Lokšņu materiāli'],
    },
    {
        'fn': 'wattsan-1325.html',
        'meta_title': 'Wattsan 1325 M1 | Profesionāla CNC Frēze | Bratus',
        'meta_desc': 'Wattsan 1325 M1 — profesionāla pilna izmēra CNC frēze ar 1300×2500 mm, 4.5 kW, RichAuto A11. Nozares standarts.',
        'canonical': 'https://cncfrezes.lv/1325.html',
        'model': '1325 M1',
        'badge': 'M1 Sērija · Nozares standarts',
        'key_specs': [('Darba laukums', '1300 × 2500 mm'), ('Vārpsta', '4.5 kW'), ('Kontrolieris', 'RichAuto A11'), ('Svars', '880 kg')],
        'materials': ['Koks', 'Ozols', 'Saplāksnis', 'MDF', 'Akrils', 'Alumīnijs'],
    },
    {
        'fn': 'wattsan-m1-1325-rd.html',
        'meta_title': 'Wattsan 1325 RD M1 | 4 Asu CNC Frēze | Bratus',
        'meta_desc': 'Wattsan 1325 RD M1 — 4 asu CNC frēze ar rotācijas ierīci. 1300×2500 mm, 4.5 kW, RichAuto A18.',
        'canonical': 'https://cncfrezes.lv/1325-rd.html',
        'model': 'M1 1325 RD',
        'badge': '4 Asis · Rotācijas ierīce',
        'key_specs': [('Darba laukums', '1300 × 2500 mm'), ('Vārpsta', '4.5 kW'), ('Kontrolieris', 'RichAuto A18'), ('Svars', '1550 kg')],
        'materials': ['Koks', 'Ozols', 'Apaļkoki', 'Balustri', 'Kolonnas'],
    },
    {
        'fn': 'wattsan-m3-1325.html',
        'meta_title': 'Wattsan 1325 M3 | Industriāla CNC Frēze | Bratus',
        'meta_desc': 'Wattsan 1325 M3 — industriāla CNC frēze ar 1300×2500 mm, 4.5 kW, NC Studio 8, Lambda4S servo.',
        'canonical': 'https://cncfrezes.lv/1325-m3.html',
        'model': 'M3 1325',
        'badge': 'M3 Sērija · Industriāla',
        'key_specs': [('Darba laukums', '1300 × 2500 mm'), ('Vārpsta', '4.5 kW'), ('Kontrolieris', 'NC Studio 8'), ('Svars', '1260 kg')],
        'materials': ['Koks', 'Ozols', 'Saplāksnis', 'MDF', 'Akrils', 'Alumīnijs', 'Kompozīti'],
    },
    {
        'fn': 'wattsan-a1-1616.html',
        'meta_title': 'Wattsan 1616 A1 | Kvadrātveida CNC Frēze | Bratus',
        'meta_desc': 'Wattsan 1616 A1 — CNC frēze ar 1600×1600 mm, 3.2 kW, RichAuto A11. Ekonomiska lielu izmēru apstrādei.',
        'canonical': 'https://cncfrezes.lv/1616-a1.html',
        'model': 'A1 1616',
        'badge': 'A1 Sērija · Kvadrātveida',
        'key_specs': [('Darba laukums', '1600 × 1600 mm'), ('Vārpsta', '3.2 kW'), ('Kontrolieris', 'RichAuto A11'), ('Svars', '620 kg')],
        'materials': ['Koks', 'Saplāksnis', 'MDF', 'Akrils', 'Lielas sagataves'],
    },
    {
        'fn': 'wattsan-m1-1616.html',
        'meta_title': 'Wattsan 1616 M1 | Profesionāla CNC Frēze | Bratus',
        'meta_desc': 'Wattsan 1616 M1 — CNC frēze ar 1600×1600 mm, 4.5 kW, RichAuto A11, 730 kg.',
        'canonical': 'https://cncfrezes.lv/1616-m1.html',
        'model': 'M1 1616',
        'badge': 'M1 Sērija · Profesionāla',
        'key_specs': [('Darba laukums', '1600 × 1600 mm'), ('Vārpsta', '4.5 kW'), ('Kontrolieris', 'RichAuto A11'), ('Svars', '730 kg')],
        'materials': ['Koks', 'Ozols', 'Saplāksnis', 'MDF', 'Akrils', 'Alumīnijs'],
    },
    {
        'fn': 'wattsan-1616.html',
        'meta_title': 'Wattsan 1616 M2 | Universāla CNC Frēze | Bratus',
        'meta_desc': 'Wattsan 1616 M2 — M2 sērijas CNC frēze ar 1600×1600 mm, 4.5 kW, RichAuto A11, 1130 kg. Smagākā savā klasē.',
        'canonical': 'https://cncfrezes.lv/1616.html',
        'model': '1616 M2',
        'badge': 'M2 Sērija · Smagākā klasē',
        'key_specs': [('Darba laukums', '1600 × 1600 mm'), ('Vārpsta', '4.5 kW'), ('Kontrolieris', 'RichAuto A11'), ('Svars', '1130 kg')],
        'materials': ['Koks', 'Ozols', 'Saplāksnis', 'MDF', 'Akrils', 'Alumīnijs', 'Kompozīti'],
    },
    {
        'fn': 'wattsan-m1-s2-x.html',
        'meta_title': 'Wattsan 1616 M1 S2 X | Divu Vārpstu CNC | Bratus',
        'meta_desc': 'Wattsan 1616 M1 S2 X — CNC frēze ar DIVĀM 4.5 kW vārpstām. 1600×1600 mm, RichAuto F7324. Divkārša produktivitāte!',
        'canonical': 'https://cncfrezes.lv/1616-s2-x.html',
        'model': 'M1 S2 X',
        'badge': '2× Vārpsta · Dubultā jauda',
        'key_specs': [('Darba laukums', '1600 × 1600 mm'), ('Vārpstas', '2 × 4.5 kW'), ('Kontrolieris', 'RichAuto F7324'), ('Svars', '840 kg')],
        'materials': ['Koks', 'Saplāksnis', 'MDF', 'Akrils', 'Sērijveida ražošana'],
    },
    {
        'fn': 'wattsan-2030.html',
        'meta_title': 'Wattsan 2030 M1 | Lielformāta CNC Frēze | Bratus',
        'meta_desc': 'Wattsan 2030 M1 — industriāla lielformāta CNC frēze ar 2000×3000 mm, 6 kW, RichAuto A11.',
        'canonical': 'https://cncfrezes.lv/2030.html',
        'model': '2030 M1',
        'badge': 'Lielformāta · 6 kW',
        'key_specs': [('Darba laukums', '2000 × 3000 mm'), ('Vārpsta', '6 kW'), ('Kontrolieris', 'RichAuto A11'), ('Svars', '1140 kg')],
        'materials': ['Koks', 'Saplāksnis', 'MDF', 'Akrils', 'Alumīnijs', 'Lielas loksnes'],
    },
    {
        'fn': 'wattsan-2040.html',
        'meta_title': 'Wattsan 2040 M1 | Maksimālā CNC Frēze | Bratus',
        'meta_desc': 'Wattsan 2040 M1 — gigantiska CNC frēze ar 2000×4000 mm, 6 kW, RichAuto A11. Maksimālais izmērs.',
        'canonical': 'https://cncfrezes.lv/2040.html',
        'model': '2040 M1',
        'badge': 'Maksimālais izmērs',
        'key_specs': [('Darba laukums', '2000 × 4000 mm'), ('Vārpsta', '6 kW'), ('Kontrolieris', 'RichAuto A11'), ('Svars', '1370 kg')],
        'materials': ['Koks', 'Saplāksnis', 'MDF', 'Akrils', 'Alumīnijs', 'Maksimālas loksnes'],
    },
]

# Process all products
for p in PRODUCTS:
    fn = p['fn']
    model = p['model']
    slug = model_key(fn)
    cat = get_cat(slug)
    
    # Get gallery images
    gallery = GALLERY.get(fn, GALLERY.get('wattsan-0609.html', []))
    
    # Get description
    desc_key = model.split()[-1] if model.split()[-1] in DESCRIPTIONS else slug.split('-')[-1]
    if desc_key not in DESCRIPTIONS:
        for k in DESCRIPTIONS:
            if k in model:
                desc_key = k
                break
    desc = DESCRIPTIONS.get(desc_key, DESCRIPTIONS.get('0609', ''))
    
    # Get features
    features = FEATURES_BY_CAT.get(cat, FEATURES_BY_CAT['6090'])
    
    # Get tech specs
    tech_specs = TECH_SPECS.get(cat, TECH_SPECS['6090'])
    
    html = make_page(
        fn, p['meta_title'], p['meta_desc'], p['canonical'],
        model, p['badge'], gallery, p['key_specs'],
        desc, features, tech_specs, p['materials']
    )
    
    filepath = os.path.join(BASE, fn)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'Created: {fn} ({len(gallery)} images, {len(features)} features)')

print(f'\nALL {len(PRODUCTS)} pages created with rich content!')
