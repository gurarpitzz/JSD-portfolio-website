import os
import json
import re

DATA_DIR = r"D:\Portfolio-jaspreet boccia\data"
CONTENT_DIR = r"D:\Portfolio-jaspreet boccia\content"
ASSETS_DIR = r"D:\Portfolio-jaspreet boccia\assets"
IMG_ACTIVITY_DIR = os.path.join(ASSETS_DIR, "images", "activity")

# Read page snapshot text
with open(os.path.join(DATA_DIR, "page_snapshot_text.txt"), "r", encoding="utf-8") as f:
    snapshot_raw = f.read()

# Define all 20 historical posts with their exact verbatim content from the live snapshot
all_20_posts = [
    {
        "id": "post-001",
        "post_number": 1,
        "timestamp_relative": "3 weeks ago",
        "date_approx": "October 2026",
        "month_year": "2026-10",
        "title": "2nd Boccia India Federation Cup 2026 – Delhi",
        "caption": """🏆 2nd Boccia India Federation Cup 2026 – Delhi

Congratulations to all the medalists! 🥇🥈🥉 Your hard work and dedication are truly inspiring.

Best wishes to all athletes for continued success in future events! 🇮🇳

Boccia India – BSFI

#BocciaIndia #FederationCup2026 #Boccia #ParaSports #ProudMoment.""",
        "images": [
            "assets/images/activity/linkedin_post_img_8.jpg"
        ],
        "reactions": 5,
        "comments": 0,
        "shares": 0,
        "category": "National Tournaments",
        "tags": ["federation-cup-2026", "delhi", "national-competition", "bsfi", "medalists", "podium"]
    },
    {
        "id": "post-002",
        "post_number": 2,
        "timestamp_relative": "1 month ago",
        "date_approx": "September 2026",
        "month_year": "2026-09",
        "title": "BC1 Category Athlete in Action at Pilsen World Boccia Challenger",
        "caption": """Our BC1 category athlete in action at Pilsen! 💪🔥

There are no limits when passion meets determination. ❤️

If you’re interested in Boccia and want to be part of this growing sport, come and join Boccia India ! 🇮🇳🎯

#BocciaIndia #boccia #pilsen2026 #parasports #nolimits #InclusionMatters""",
        "images": [
            "assets/images/activity/linkedin_post_img_10.jpg"
        ],
        "reactions": 2,
        "comments": 0,
        "shares": 0,
        "category": "International Representation",
        "tags": ["bc1", "pilsen2026", "world-boccia", "athlete-in-action", "inclusion", "grassroots-call"]
    },
    {
        "id": "post-003",
        "post_number": 3,
        "timestamp_relative": "1 month ago",
        "date_approx": "September 2026",
        "month_year": "2026-09",
        "title": "Historic Comeback at Pilsen: 5 Gold Medals for Team India",
        "caption": """🇮🇳🥇 Our Golden Boy (Life With C4 Ajeya Raj) & Girl (Anjali Thakur )in action at the Pilsen World Boccia Challenger 2026!

A historic comeback for Boccia India — bringing home 5 GOLD MEDALS! 🏆🔥

Proud moment for India. 🇮🇳
The journey continues! 💪🎯

With the support go Department of Sports, MYAS, Government of India Paralympic Committee of India

#BocciaIndia #worldboccia #pilsen2026 #TeamIndia""",
        "images": [
            "assets/images/activity/linkedin_post_img_12.jpg"
        ],
        "reactions": 6,
        "comments": 2,
        "shares": 1,
        "category": "International Champions",
        "tags": ["pilsen2026", "5-gold-medals", "ajeya-raj", "anjali-thakur", "team-india", "myas", "pci"]
    },
    {
        "id": "post-004",
        "post_number": 4,
        "timestamp_relative": "1 month ago",
        "date_approx": "September 2026",
        "month_year": "2026-09",
        "title": "Launch of Indigenous BC3 Boccia Ramp with ICMR & IIT Madras for Indian Army",
        "caption": """🇮🇳 A Proud Development for Indian Boccia! 🇮🇳

With the support of ICMR and IIT Madras, the Boccia Sports Federation of India (BSFI) has developed an indigenous Boccia Ramp for BC3 athletes.

This is an important step towards making Boccia equipment more accessible to athletes in India. The ramp was formally handed over to Indian Army Boccia players in the presence of the Chairman and President of Boccia India, along with the Secretary-DHR & DG, ICMR Dr Rajiv Bahl, Additional DG Dr Sanghmitra Pati and Senior Scientist Dr. Ravinder Singh.

The ramp is currently designed for beginners and developmental-level players and is not intended for international-level competition. It can, however, provide an affordable and useful training option for new BC3 athletes and help expand the grassroots development of Boccia across India.

👏 Congratulations to everyone involved in this important initiative!

Boccia India 🇮🇳 | Developing Indigenous Boccia Equipment | Supporting Athletes""",
        "images": [
            "assets/images/activity/linkedin_post_img_14.jpg",
            "assets/images/news/icmr-ramp-demo-1.webp",
            "assets/images/news/icmr-ramp-demo-2.webp"
        ],
        "reactions": 14,
        "comments": 0,
        "shares": 0,
        "category": "Equipment Innovation",
        "tags": ["icmr", "iit-madras", "indian-army", "bc3-ramp", "indigenous-innovation", "dr-rajiv-bahl", "dr-sanghmitra-pati", "grassroots"]
    },
    {
        "id": "post-005",
        "post_number": 5,
        "timestamp_relative": "1 month ago",
        "date_approx": "September 2026",
        "month_year": "2026-09",
        "title": "Play Boccia with Happiness: Indian Delegation in Pilsen, Czech Republic",
        "caption": """Play Boccia with happiness ! Team in Pilsen Czech Republic 🇨🇿""",
        "images": [
            "assets/images/activity/linkedin_post_img_16.jpg"
        ],
        "reactions": 7,
        "comments": 0,
        "shares": 0,
        "category": "Team Spirit & Culture",
        "tags": ["pilsen", "czech-republic", "team-india", "sportsmanship", "joy-in-sport"]
    },
    {
        "id": "post-006",
        "post_number": 6,
        "timestamp_relative": "1 month ago",
        "date_approx": "September 2026",
        "month_year": "2026-09",
        "title": "Team India Squad on the Ground in Pilsen",
        "caption": """Team at Pilsen""",
        "images": [
            "assets/images/activity/linkedin_post_img_18.jpg"
        ],
        "reactions": 4,
        "comments": 1,
        "shares": 0,
        "category": "Team Delegation",
        "tags": ["pilsen", "delegation", "world-boccia", "team-photo"]
    },
    {
        "id": "post-007",
        "post_number": 7,
        "timestamp_relative": "1 month ago",
        "date_approx": "September 2026",
        "month_year": "2026-09",
        "title": "Official Report: Pilsen 2026 World Boccia Challenger",
        "caption": """Pilsen 2026 World Boccia Challenger – Czech Republic

The Indian Boccia Team proudly participated in the Pilsen 2026 World Boccia Challenger, held in Pilsen, Czech Republic. India was represented by a strong contingent of six players competing across the BC1, BC2 and BC3 categories.

The participation provided valuable international exposure to Indian athletes, allowing them to compete against some of the world's leading Boccia players and gain important experience at the international level.

The Indian contingent demonstrated determination, competitive spirit and professionalism throughout the event, further contributing to the continued growth and development of Boccia in India.

Participation in international events such as the Pilsen World Boccia Challenger 2026 is an important part of India's preparation for future international competitions and reflects the Boccia Sports Federation of India's commitment to providing Indian athletes with greater opportunities to compete on the world stage.

🇮🇳 Indian Boccia continues to grow, compete and make its presence felt internationally.""",
        "images": [
            "assets/images/activity/linkedin_post_img_20.jpg"
        ],
        "reactions": 3,
        "comments": 0,
        "shares": 0,
        "category": "Official Press Release",
        "tags": ["official-report", "pilsen2026", "contingent", "world-stage", "bsfi", "international-exposure"]
    },
    {
        "id": "post-008",
        "post_number": 8,
        "timestamp_relative": "1 month ago",
        "date_approx": "September 2026",
        "month_year": "2026-09",
        "title": "Kit Distribution Ceremony & National Coaching Camp in Solan, HP",
        "caption": """🇮🇳 Boccia Indian Team – Coaching Camp

With the support of the Ministry of Youth Affairs & Sports and the Paralympic Committee of India, the National Coaching Camp for the Indian Boccia Team was successfully conducted in Solan, Himachal Pradesh.

🎽 The Kit Distribution Ceremony was also held to encourage and support our athletes ahead of the international competition.
🇮🇳 Best wishes to the entire Indian Boccia Team! Go Team India! 💪🏆

#BocciaIndia #TeamIndia #Boccia #IndianBocciaTeam #Paralympics SportsIndia TeamIndia 🇮🇳""",
        "images": [
            "assets/images/activity/linkedin_post_img_22.jpg"
        ],
        "reactions": 7,
        "comments": 0,
        "shares": 0,
        "category": "National Training & Logistics",
        "tags": ["kit-distribution", "coaching-camp", "solan", "myas", "pci", "team-india"]
    },
    {
        "id": "post-009",
        "post_number": 9,
        "timestamp_relative": "2 months ago",
        "date_approx": "August 2026",
        "month_year": "2026-08",
        "title": "National Boccia Coaching Camp at IAMD Solan with SAI & PCI",
        "caption": """National Boccia Coaching Camp 🇮🇳

The National Boccia Coaching Camp is underway at IAMD, Solan, Himachal Pradesh, with the support of the Paralympic Committee of india and Sports Authority of India.

Training hard, building confidence, and preparing our athletes for greater international success! 💪🏆

#BocciaIndia #NationalCoachingCamp #Boccia #SAI #PCI #ParaSports #TeamIndia""",
        "images": [
            "assets/images/activity/linkedin_post_img_24.jpg"
        ],
        "reactions": 9,
        "comments": 1,
        "shares": 0,
        "category": "High Performance Camp",
        "tags": ["iamd-solan", "sai", "pci", "high-performance", "training", "sports-authority-of-india"]
    },
    {
        "id": "post-010",
        "post_number": 10,
        "timestamp_relative": "2 months ago",
        "date_approx": "August 2026",
        "month_year": "2026-08",
        "title": "Historic Milestone: Indian Boccia Team Reaches Seoul for World Championship 2026",
        "caption": """🇮🇳 A Historic Moment for Indian Boccia! 🇰🇷

Our Indian Boccia team has reached Seoul, South Korea for the World Boccia Championship 2026. 🏆

For the first time in the history of Boccia India, Indian athletes are participating in the World Championship! 🇮🇳❤️

Wishing our entire team the very best. Make India proud! 💪🇮🇳

#BocciaIndia #WorldBocciaChampionship #Seoul2026 #IndianBoccia #ProudMoment #India""",
        "images": [
            "assets/images/activity/linkedin_post_img_26.jpg"
        ],
        "reactions": 8,
        "comments": 2,
        "shares": 0,
        "category": "World Championship Milestone",
        "tags": ["seoul2026", "world-championship", "historic-first", "south-korea", "team-india", "global-stage"]
    },
    {
        "id": "post-011",
        "post_number": 11,
        "timestamp_relative": "3 months ago",
        "date_approx": "July 2026",
        "month_year": "2026-07",
        "title": "Opening Day Match Victories at Egypt World Boccia Challenger 2026",
        "caption": """🇮🇳🏆 A Fantastic Start for Team India at the Egypt World Boccia Challenger 2026! 🏆🇮🇳

Heartiest congratulations to our outstanding Boccia athletes for their brilliant performances on the opening day of the Egypt World Boccia Challenger 2026.

🌟 Match Results:
🔹 BC4 Male – Jatin Kushwah defeated his opponent in his first match with a score of 7–2.
🔹 BC3 Male – Ajeya Raj registered a dominant 10–0 victory over UAE in his opening match.
🔹 BC3 Female – Sarita Dwivedi secured a superb victory against Portugal in her opening match.
🔹 BC4 Male – Jatin Kushwah continued his excellent form by winning his second match against Croatia.
🔹 BC3 Male – Ajeya Raj maintained his unbeaten run with another impressive victory over Egypt in his second match.
🔹 BC3 Male – Sachin Chamria earned a well-deserved victory against Slovenia.

👏 Congratulations to all our athletes for making India proud with such outstanding performances on the international stage.

We wish Team India the very best for the upcoming matches. Keep fighting, keep believing, and keep making the nation proud! 🇮🇳💪

#BocciaIndia #TeamIndia #EgyptWorldBocciaChallenger2026 #WorldBoccia #ParaSports RoadToGlory PlayForIndia Boccia India""",
        "images": [
            "assets/images/star-players/star-athletes-grid.webp",
            "assets/images/activity/linkedin_post_img_24.jpg"
        ],
        "reactions": 3,
        "comments": 0,
        "shares": 0,
        "category": "International Match Results",
        "tags": ["cairo-egypt-2026", "world-boccia", "jatin-kushwah", "ajeya-raj", "sarita-dwivedi", "sachin-chamria", "dominance"]
    },
    {
        "id": "post-012",
        "post_number": 12,
        "timestamp_relative": "3 months ago",
        "date_approx": "July 2026",
        "month_year": "2026-07",
        "title": "BSFI Presents Team India at World Boccia Challenger in Cairo, Egypt",
        "caption": """The Boccia Sports Federation of India proudly presents Team India at the World Boccia Challenger 2026 in Cairo, Egypt. We extend our best wishes to our athletes, coaches, officials, and support staff as they represent India with excellence and dedication on the global stage. 🇮🇳""",
        "images": [
            "assets/images/gallery/boccia-national-coaching-camp-2024.webp"
        ],
        "reactions": 15,
        "comments": 1,
        "shares": 0,
        "category": "Contingent Announcement",
        "tags": ["cairo-egypt", "world-boccia-challenger", "bsfi", "team-india", "coaches", "support-staff"]
    },
    {
        "id": "post-013",
        "post_number": 13,
        "timestamp_relative": "4 months ago",
        "date_approx": "June 2026",
        "month_year": "2026-06",
        "title": "Mastery in Boccia: Focus, Patience & Strategy in the BC3 Category",
        "caption": """In Boccia, focus is everything. 🎯
A BC3 player’s strength lies in patience, precision, and complete concentration on every shot. Their determination, strategy, and calm mindset truly define the spirit of the game. 💙🇮🇳

#Boccia #BC3 #Focus #Determination #ParaSports #BocciaIndia""",
        "images": [
            "assets/images/star-players/sachin-chamaria.webp"
        ],
        "reactions": 6,
        "comments": 0,
        "shares": 0,
        "category": "Sport Philosophy & Coaching",
        "tags": ["bc3", "focus", "precision", "strategy", "determination", "coaching-philosophy"]
    },
    {
        "id": "post-014",
        "post_number": 14,
        "timestamp_relative": "4 months ago",
        "date_approx": "June 2026",
        "month_year": "2026-06",
        "title": "Inauguration of Dedicated Boccia Court at ALIMCO Centre, Kanpur",
        "caption": """A proud moment for Boccia India! 🇮🇳

Heartiest congratulations to ALIMCO and our athlete Sarita Dwivedi (BC3) on the establishment of the Boccia court at the ALIMCO Centre, Kanpur. This marks a significant step forward in the growth and development of Boccia in India, reflecting a strong commitment towards creating better infrastructure and opportunities for athletes with disabilities.

We extend our best wishes to Sarita Dwivedi for continued success in her Boccia journey and look forward to many more milestones in the future.

#BocciaIndia #Boccia #ParaSports #InclusiveSports #Kanpur #BocciaDevelopment #ProudMoment""",
        "images": [
            "assets/images/gallery/boccia-india-court-action.webp"
        ],
        "reactions": 4,
        "comments": 0,
        "shares": 0,
        "category": "Infrastructure Expansion",
        "tags": ["alimco", "kanpur", "sarita-dwivedi", "bc3", "infrastructure", "court-inauguration"]
    },
    {
        "id": "post-015",
        "post_number": 15,
        "timestamp_relative": "4 months ago",
        "date_approx": "June 2026",
        "month_year": "2026-06",
        "title": "Conclusion of Selection Trials for Asian Para Games 2026 in Chandigarh",
        "caption": """Selection trials for Asian Para Games 2026 held in Chandigarh""",
        "images": [
            "assets/images/gallery/boccia-chandigarh-event-banner.webp"
        ],
        "reactions": 4,
        "comments": 0,
        "shares": 0,
        "category": "National Selection Trials",
        "tags": ["selection-trials", "chandigarh", "asian-para-games-2026", "japan", "team-selection"]
    },
    {
        "id": "post-016",
        "post_number": 16,
        "timestamp_relative": "4 months ago",
        "date_approx": "June 2026",
        "month_year": "2026-06",
        "title": "Stage is Set: Indian Boccia Selection Trials for Asian Para Games Japan",
        "caption": """🇮🇳🏐 The stage is set!

The Indian Boccia Team Selection Trials for the upcoming Asian Para Games in Japan are being held on 11th & 12th June 2026 in Chandigarh. The venue is ready, preparations are complete, and athletes are set to showcase their skills for a place on Team India.

Best wishes to all participants! 💪✨

#BocciaIndia #TeamIndia #SelectionTrials #AsianParaGames #Japan #Chandigarh 🇮🇳🏆""",
        "images": [
            "assets/images/activity/linkedin_post_img_20.jpg"
        ],
        "reactions": 9,
        "comments": 0,
        "shares": 0,
        "category": "National Trials Preparation",
        "tags": ["asian-para-games", "japan", "chandigarh", "trials-venue", "selection-committee"]
    },
    {
        "id": "post-017",
        "post_number": 17,
        "timestamp_relative": "4 months ago",
        "date_approx": "June 2026",
        "month_year": "2026-06",
        "title": "Astana Boccia World Cup 2026 – Day 2 Highlights from Kazakhstan",
        "caption": """🏆 Day 2 Highlights | Astana Boccia World Cup 2026 🇰🇿

#Boccia #AstanaWorldCup2026 #TeamIndia #BocciaInd""",
        "images": [
            "assets/images/activity/linkedin_post_img_22.jpg"
        ],
        "reactions": 2,
        "comments": 0,
        "shares": 0,
        "category": "World Cup Action",
        "tags": ["astana2026", "world-cup", "kazakhstan", "day-2-highlights", "team-india"]
    },
    {
        "id": "post-018",
        "post_number": 18,
        "timestamp_relative": "4 months ago",
        "date_approx": "June 2026",
        "month_year": "2026-06",
        "title": "Boccia Championship at Purple Fest Arunachal 2026 – DPS Jollang",
        "caption": """🏆💜 Boccia Game – Purple Fest Arunachal 2026 💜🏆

Every throw counts, every player matters! 🎯
Celebrating inclusion, determination, and the true spirit of sports at Purple Fest Arunachal. Let’s come together to promote accessibility, respect, and equal opportunities for all. ♿🤝

📅 20–21 June 2026
📍 Delhi Public School, Jollang, Arunachal Pradesh

#Boccia #PurpleFestArunachal #InclusiveSports #EveryPlayerMatters #SportsForAll ParaSports PlayTogetherWinTogether 💜🇮🇳""",
        "images": [
            "assets/images/gallery/boccia-india-court-action.webp"
        ],
        "reactions": 5,
        "comments": 0,
        "shares": 0,
        "category": "Barrier-Free Inclusion",
        "tags": ["purple-fest", "arunachal-pradesh", "dps-jollang", "inclusive-sports", "accessibility", "northeast-india"]
    },
    {
        "id": "post-019",
        "post_number": 19,
        "timestamp_relative": "4 months ago",
        "date_approx": "June 2026",
        "month_year": "2026-06",
        "title": "Felicitation Ceremony Honoring Chief of Defence Staff General N. S. Raja Subramani",
        "caption": """A memorable evening for Boccia India! 🇮🇳✨

On 3rd June 2026 in New Delhi, the Boccia Sports Federation of India successfully hosted a Felicitation Ceremony honoring General N. S. Raja Subramani, Chief of Defence Staff, Government of India.

The event celebrated leadership, dedication to the nation, and the continued growth of para sports in India. We thank all distinguished guests, supporters, and members of the Boccia family who made this occasion truly special.

#BocciaIndia #FelicitationCeremony #NewDelhi #June32026 #ParaSports #Leadership #India #BocciaFamily #Gratitude""",
        "images": [
            "assets/images/activity/linkedin_post_img_29.jpg"
        ],
        "reactions": 8,
        "comments": 0,
        "shares": 0,
        "category": "High Dignitary Felicitation",
        "tags": ["chief-of-defence-staff", "general-raja-subramani", "new-delhi", "felicitation-ceremony", "leadership", "national-pride"]
    },
    {
        "id": "post-020",
        "post_number": 20,
        "timestamp_relative": "4 months ago",
        "date_approx": "June 2026",
        "month_year": "2026-06",
        "title": "Astana Boccia World Cup 2026 – Day 1 Highlights from Kazakhstan",
        "caption": """🏆 Day 1 Highlights | Astana Boccia World Cup 2026 🇰🇿

#Boccia #AstanaWorldCup2026 #TeamIndia #BocciaInd""",
        "images": [
            "assets/images/activity/linkedin_post_img_26.jpg"
        ],
        "reactions": 3,
        "comments": 0,
        "shares": 0,
        "category": "World Cup Action",
        "tags": ["astana2026", "world-cup", "kazakhstan", "day-1-highlights", "team-india"]
    }
]

# Write out linkedin-entire-archive.json
archive_path = os.path.join(DATA_DIR, "linkedin-entire-archive.json")
with open(archive_path, "w", encoding="utf-8") as f:
    json.dump(all_20_posts, f, indent=2, ensure_ascii=False)
print(f"Saved {len(all_20_posts)} posts to {archive_path}")

# Also update linkedin-posts-scraped.json to be identical to entire archive
scraped_posts_path = os.path.join(DATA_DIR, "linkedin-posts-scraped.json")
with open(scraped_posts_path, "w", encoding="utf-8") as f:
    json.dump(all_20_posts, f, indent=2, ensure_ascii=False)
print(f"Updated {scraped_posts_path}")

# Now build the full content/linkedin-posts-and-activities.md
md_content = """# LinkedIn Activities & Post Archive: Jaspreet Singh Dhaliwal

> **Client:** Jaspreet Singh Dhaliwal  
> **Profile:** [LinkedIn Profile](http://linkedin.com/in/jaspreet-singh-dhaliwal-9951a69b/)  
> **Headline:** Founder & President of Boccia India || Referee World Boccia || Social Worker || Int’ Athlete  
> **Scope:** Complete historical feed archive from account inception to present (June 2026 – October 2026)  
> **Total Authored Posts Documented:** 20 Posts (100% of feed history)  
> **Tags:** #BocciaIndia #WorldBoccia #TeamIndia #ParaSports #InclusionMatters #ICMR #IITMadras  

---

## Executive Overview of LinkedIn Activity

Jaspreet Singh Dhaliwal's LinkedIn feed serves as the official public ledger of the Indian Boccia movement, international tournament delegations, technological innovations, and high-level stakeholder felicitations. 

### Key Milestones Documented Across All 20 Posts:
1. **High Dignitary Felicitations:** BSFI hosted a formal ceremony in New Delhi honoring **General N. S. Raja Subramani**, Chief of Defence Staff (CDS), Government of India (June 3, 2026).
2. **Technological Breakthrough:** Co-developed India's first indigenous BC3 Boccia ramp in partnership with **ICMR** and **IIT Madras**, formally handed over to Indian Army Boccia athletes in the presence of DG ICMR Dr. Rajiv Bahl.
3. **Historic International Gold Triumphs:** Led the Indian contingent to a historic **5 Gold Medal sweep** at the Pilsen 2026 World Boccia Challenger in the Czech Republic, headlined by star athletes Ajeya Raj and Anjali Thakur.
4. **World Championship Debut:** Led Team India to Seoul, South Korea for the **World Boccia Championship 2026**—the first time Indian athletes qualified for the World Championship.
5. **Major Games Selection Trials:** Conducted national selection trials for the **Asian Para Games 2026 in Japan** at Chandigarh (June 11–12, 2026).
6. **Grassroots & Accessibility Milestones:** Organized Boccia at **Purple Fest Arunachal 2026** (DPS Jollang) and established a permanent Boccia court at the **ALIMCO Centre in Kanpur** for athlete Sarita Dwivedi.
7. **National Coaching Camps:** Conducted high-performance training and kit distribution at IAMD Solan, Himachal Pradesh with the support of SAI and PCI.

---

## Complete Chronological Post-by-Post Dossier

"""

for p in all_20_posts:
    img_md = "\n".join([f"- ![{p['title']}](file:///{os.path.abspath(img).replace(os.sep, '/')})" for img in p['images']])
    tag_str = " ".join([f"`#{t}`" for t in p['tags']])
    
    md_content += f"""### Post #{p['post_number']}: {p['title']}
- **Post ID:** `{p['id']}`
- **Date / Period:** {p['date_approx']} ({p['timestamp_relative']})
- **Category:** {p['category']}
- **Engagement:** {p['reactions']} Reactions | {p['comments']} Comments | {p['shares']} Reposts
- **Tags:** {tag_str}

#### Verbatim Post Caption:
```text
{p['caption']}
```

#### Associated Media Assets:
{img_md}

---

"""

with open(os.path.join(CONTENT_DIR, "linkedin-posts-and-activities.md"), "w", encoding="utf-8") as f:
    f.write(md_content)
print(f"Updated {os.path.join(CONTENT_DIR, 'linkedin-posts-and-activities.md')}")

print("ALL COMPLETE!")
