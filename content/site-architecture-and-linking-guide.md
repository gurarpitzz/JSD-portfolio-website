# Portfolio Website Architecture & Data Linking Guide
**Master Blueprint for Jaspreet Singh Dhaliwal's Personal Portfolio**

---

## 1. Visual & Aesthetic Philosophy
In accordance with modern high-impact frontend design guidelines:
* **Typography:** Extreme display weight headers (800–900 Archivo / Syne / Plus Jakarta Sans) paired with clean, highly legible body typography (Inter / Geist).
* **Color Palette:**
  * Royal Paralympic Purple: `#4A154B` / `#2D082E` (Prestige, dignity, and the global purple movement for disability inclusion)
  * Gaekwad / Olympic Gold: `#D4AF37` / `#F3E5AB` (Championship medals, excellence, and celebration)
  * Crisp Contrast Slate / Charcoal: `#0F172A` / `#F8FAFC`
* **Depth Model (2.5D Architecture):**
  * `depth-0`: Atmospheric deep-space / abstract boccia court gradient canvas.
  * `depth-1`: Ambient floating gold & purple particle dust.
  * `depth-2`: Interactive 3D Boccia ball & ramp trajectory canvas (Three.js / WebGL).
  * `depth-3`: Structured content cards, glassmorphic timeline panels with GSAP ScrollTrigger pinning.
  * `depth-4`: High-resolution photo lightboxes and interactive athlete spotlights.
  * `depth-5`: Sticky navigation bar, accessibility controls (contrast toggle, motion reduction).

---

## 2. Directory Structure & Complete Asset Inventory

```
D:\Portfolio-jaspreet boccia\
├── assets\
│   ├── documents\
│   │   └── PCI_Official_Letter_Jaspreet_Singh.pdf  [Paralympic Committee of India Certified Letter]
│   └── images\
│       ├── activity\                               [Scraped LinkedIn Post & Event Photos - 12 files]
│       │   ├── linkedin_post_img_2.jpg             [Cover Photo Media]
│       │   ├── linkedin_post_img_8.jpg             [Federation Cup 2026 Delhi Podium]
│       │   ├── linkedin_post_img_10.jpg            [BC1 Athlete in Action Pilsen]
│       │   ├── linkedin_post_img_12.jpg            [Pilsen 5 Gold Medals Action]
│       │   ├── linkedin_post_img_14.jpg            [ICMR & IIT Madras Ramp Handover]
│       │   ├── linkedin_post_img_16.jpg            [Team India in Pilsen Czech Republic]
│       │   ├── linkedin_post_img_18.jpg            [Pilsen Squad Photo]
│       │   ├── linkedin_post_img_20.jpg            [Pilsen World Challenger Official Contingent]
│       │   ├── linkedin_post_img_22.jpg            [Kit Distribution Ceremony Solan]
│       │   ├── linkedin_post_img_24.jpg            [National Coaching Camp IAMD Solan]
│       │   ├── linkedin_post_img_26.jpg            [World Boccia Championship Seoul 2026 Squad]
│       │   └── linkedin_post_img_29.jpg            [At GoSports Foundation Event]
│       ├── gallery\                                [High-Res Press & Event Archive - 6 files]
│       │   ├── boccia-india-award-ceremony-2026.webp
│       │   ├── cairo-world-challenger-2026.webp
│       │   ├── icmr-iit-madras-bc3-ramp-launch.webp
│       │   ├── national-coaching-camp-solan-2026.webp
│       │   ├── pilsen-2026-world-challenger-team.webp
│       │   └── world-boccia-agm-seoul-2026.webp
│       ├── logos-affiliations\                     [Official Federations & Institutional Logos - 6 files]
│       │   ├── anti-doping-logo.jpg
│       │   ├── boccia-india-logo.webp
│       │   ├── icmr-logo.jpg
│       │   ├── myas-logo.svg
│       │   ├── paralympic-committee-india-logo.webp
│       │   └── world-boccia-logo.webp
│       ├── news\                                   [Press Releases & 4K DSLR Photos - 6 files]
│       │   ├── bahrain-6-medal-historic-victory.webp
│       │   ├── icmr-ramp-demo-1.webp               [4176x2784 Ultra HD DSLR]
│       │   ├── icmr-ramp-demo-2.webp               [4176x2784 Ultra HD DSLR]
│       │   ├── sandhya-gold-medal-celebration.webp
│       │   ├── sci-day-awareness-2026.webp
│       │   └── solan-national-camp-cover.webp
│       ├── profile\                                [Primary Identity & Headshots - 36 files]
│       │   ├── jaspreet_singh_dhaliwal_headshot.jpg [506x506 Primary Avatar]
│       │   ├── jaspreet_singh_linkedin_cover.jpg    [506x126 Banner]
│       │   └── (Additional high-resolution portraits & icons)
│       └── star-players\                           [Medalist Athlete Spotlights - 7 files]
│           ├── ajeya-raj-bc3.webp
│           ├── anjali-devi.webp
│           ├── jatin-kushwaha-bc4.webp
│           ├── pooja-gupta-bc4.webp
│           ├── sachin-chamaria-bc3-gold.webp
│           ├── sarita-athlete.webp
│           └── vyom-pawa.webp
├── content\                                        [Formatted, Tagged Markdown Dossiers]
│   ├── athletes-and-podium-legacy.md               [All Medalists & Tournament Campaign Details]
│   ├── biography.md                                [Full Life Narrative, Origin Story & Verified Roles]
│   ├── boccia-pioneer-journey.md                   [Federation Building & Nationwide Expansion]
│   ├── equipment-innovation-icmr-iit.md            [Indigenous BC3 Ramp Engineering]
│   ├── linkedin-posts-and-activities.md            [Complete 20-Post Verbatim Feed Archive]
│   ├── pci-official-record.md                      [PCI Certification & 9 Major LOC Roles]
│   └── site-architecture-and-linking-guide.md      [This Master Linking Guide]
└── data\                                           [Structured Machine-Readable JSON Datastores]
    ├── boccia-movement.json                        [Origins, Chronology, Star Athletes & Tech]
    ├── experience-loc.json                         [All 9 Major LOC Appointments & Duties]
    ├── image-manifest.json                         [Metadata Index of All 73 Image Assets]
    ├── linkedin-entire-archive.json                [Master Archive of All 20 Historical Posts]
    ├── linkedin-posts-scraped.json                 [Feed Posts with Tags, Metrics & Media Paths]
    └── profile.json                                [Complete Executive Profile & Tenures]
```

---

## 3. Data Linking & Integration Schema

### 1. Profile Hero & Identity Section
* **Data Sources:** [`data/profile.json`](file:///D:/Portfolio-jaspreet%20boccia/data/profile.json) -> `personal_info`
* **Visual Anchors:** 
  * Headshot: [`assets/images/profile/jaspreet_singh_dhaliwal_headshot.jpg`](file:///D:/Portfolio-jaspreet%20boccia/assets/images/profile/jaspreet_singh_dhaliwal_headshot.jpg)
  * Cover Banner: [`assets/images/profile/jaspreet_singh_linkedin_cover.jpg`](file:///D:/Portfolio-jaspreet%20boccia/assets/images/profile/jaspreet_singh_linkedin_cover.jpg)
  * Institutional Badges: [`assets/images/logos-affiliations/`](file:///D:/Portfolio-jaspreet%20boccia/assets/images/logos-affiliations/)
* **Narrative:** [`content/biography.md`](file:///D:/Portfolio-jaspreet%20boccia/content/biography.md)

### 2. Major Games LOC & Leadership Interactive Timeline
* **Data Source:** [`data/experience-loc.json`](file:///D:/Portfolio-jaspreet%20boccia/data/experience-loc.json) -> `events`
* **Filter Tags:** `loc-member`, `transportation-chairman`, `grand-prix`, `world-championships`, `asian-games`
* **Downloadable Credential:** [`assets/documents/PCI_Official_Letter_Jaspreet_Singh.pdf`](file:///D:/Portfolio-jaspreet%20boccia/assets/documents/PCI_Official_Letter_Jaspreet_Singh.pdf)
* **Detailed Record:** [`content/pci-official-record.md`](file:///D:/Portfolio-jaspreet%20boccia/content/pci-official-record.md)

### 3. The Indian Boccia Revolution (2014 – 2026)
* **Data Source:** [`data/boccia-movement.json`](file:///D:/Portfolio-jaspreet%20boccia/data/boccia-movement.json)
* **Key Visuals:**
  * Seoul AGM 2026: [`assets/images/gallery/world-boccia-agm-seoul-2026.webp`](file:///D:/Portfolio-jaspreet%20boccia/assets/images/gallery/world-boccia-agm-seoul-2026.webp)
  * Bahrain 6-Medal Historic Sweep: [`assets/images/news/bahrain-6-medal-historic-victory.webp`](file:///D:/Portfolio-jaspreet%20boccia/assets/images/news/bahrain-6-medal-historic-victory.webp)
  * Pilsen 2026 Squad: [`assets/images/gallery/pilsen-2026-world-challenger-team.webp`](file:///D:/Portfolio-jaspreet%20boccia/assets/images/gallery/pilsen-2026-world-challenger-team.webp)
* **Dossier:** [`content/boccia-pioneer-journey.md`](file:///D:/Portfolio-jaspreet%20boccia/content/boccia-pioneer-journey.md)

### 4. Assistive Technology Innovation: Indigenous BC3 Ramp
* **Data Source:** [`data/boccia-movement.json`](file:///D:/Portfolio-jaspreet%20boccia/data/boccia-movement.json) -> `technology_and_equipment_innovations`
* **Ultra-High-Res Showcase (4176x2784 DSLR):**
  * [`assets/images/news/icmr-ramp-demo-1.webp`](file:///D:/Portfolio-jaspreet%20boccia/assets/images/news/icmr-ramp-demo-1.webp)
  * [`assets/images/news/icmr-ramp-demo-2.webp`](file:///D:/Portfolio-jaspreet%20boccia/assets/images/news/icmr-ramp-demo-2.webp)
* **Dossier:** [`content/equipment-innovation-icmr-iit.md`](file:///D:/Portfolio-jaspreet%20boccia/content/equipment-innovation-icmr-iit.md)

### 5. Hall of Fame Athletes & Podium Legacy
* **Data Source:** [`data/boccia-movement.json`](file:///D:/Portfolio-jaspreet%20boccia/data/boccia-movement.json) -> `hall_of_fame_athletes`
* **Athlete Profiles:** Pooja Gupta (BC4), Sachin Chamaria (BC3), Ajeya Raj (BC3), Anjali Thakur (BC3), Jatin Kushwaha (BC4), Sarita Dwivedi (BC3), Sandhya Bhumij (BC1)
* **Visuals:** [`assets/images/star-players/`](file:///D:/Portfolio-jaspreet%20boccia/assets/images/star-players/)
* **Dossier:** [`content/athletes-and-podium-legacy.md`](file:///D:/Portfolio-jaspreet%20boccia/content/athletes-and-podium-legacy.md)

### 6. Live Activity & Social Archive (All 20 Posts)
* **Data Sources:** 
  * [`data/linkedin-entire-archive.json`](file:///D:/Portfolio-jaspreet%20boccia/data/linkedin-entire-archive.json)
  * [`data/linkedin-posts-scraped.json`](file:///D:/Portfolio-jaspreet%20boccia/data/linkedin-posts-scraped.json)
* **Full Formatted Dossier:** [`content/linkedin-posts-and-activities.md`](file:///D:/Portfolio-jaspreet%20boccia/content/linkedin-posts-and-activities.md)
* **Coverage:** Complete chronological archive from October 2026 back to June 2026 (100% of feed history)
* **Key Posts Highlighted:**
  * Post #19: Felicitation of Chief of Defence Staff General N. S. Raja Subramani in New Delhi (June 3, 2026)
  * Post #18: Purple Fest Arunachal 2026 (June 20–21, 2026 at DPS Jollang)
  * Post #14: ALIMCO Centre Kanpur dedicated Boccia court inauguration for Sarita Dwivedi
  * Post #11: Egypt World Boccia Challenger opening day sweep (Ajeya Raj 10-0 UAE, Jatin Kushwah 7-2)
  * Post #10: Historic team departure for World Boccia Championship in Seoul, South Korea
  * Post #4: Indigenous BC3 ramp handover to Indian Army athletes with DG ICMR Dr. Rajiv Bahl
  * Post #3: 5 Gold Medals historic sweep in Pilsen, Czech Republic
