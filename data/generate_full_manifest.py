import os
import json

WORKSPACE = r"D:\Portfolio-jaspreet boccia"
ASSETS_DIR = os.path.join(WORKSPACE, "assets")
DATA_DIR = os.path.join(WORKSPACE, "data")

manifest = []

for root, dirs, files in os.walk(ASSETS_DIR):
    for f in sorted(files):
        full_path = os.path.join(root, f)
        rel_path = os.path.relpath(full_path, WORKSPACE).replace(os.sep, "/")
        file_size = os.path.getsize(full_path)
        ext = os.path.splitext(f)[1].lower()
        subfolder = os.path.basename(root)
        parent_folder = os.path.basename(os.path.dirname(root))

        category = subfolder
        suggested_usage = "General"
        alt = f.replace("-", " ").replace("_", " ").replace(ext, "").title()

        if subfolder == "profile":
            suggested_usage = "Hero / Profile Card / Header Identity"
        elif subfolder == "activity":
            suggested_usage = "LinkedIn Activity Feed / Tournament Grid"
        elif subfolder == "gallery":
            suggested_usage = "Championships & Milestones Gallery"
        elif subfolder == "news":
            suggested_usage = "News Showcase / Technology Feature"
        elif subfolder == "star-players":
            suggested_usage = "Athlete Spotlight & Hall of Fame Grid"
        elif subfolder == "logos-affiliations":
            suggested_usage = "Affiliations Ribbon & Trust Badges"
        elif subfolder == "documents":
            suggested_usage = "Official Credentials & Downloads Modal"

        manifest.append({
            "id": f"asset-{len(manifest) + 1:03d}",
            "filename": f,
            "path": rel_path,
            "category": category,
            "filesize_bytes": file_size,
            "extension": ext,
            "alt_text": alt,
            "suggested_component_usage": suggested_usage
        })

manifest_path = os.path.join(DATA_DIR, "image-manifest.json")
with open(manifest_path, "w", encoding="utf-8") as f:
    json.dump(manifest, f, indent=2)

print(f"Generated comprehensive manifest with {len(manifest)} assets at {manifest_path}")
