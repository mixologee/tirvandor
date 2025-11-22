# 🎯 DM TOOLKIT - PROJECT STRUCTURE

## Overview

The DM Toolkit consists of 4 products, each with its own directory containing:
- `markdown/` - Source markdown files (EDIT THESE)
- `build_*.py` - Python script to generate DOCX
- Generated DOCX files go to `/mnt/user-data/outputs/`

---

## 📁 Directory Structure

```
tirvandor-project/
├── dm-toolkit-encounters/
│   ├── markdown/
│   │   └── RANDOM-ENCOUNTER-TABLES.md    ← EDIT THIS
│   └── build_encounters.py               ← RUN THIS
│
├── dm-toolkit-npc-cards/
│   ├── markdown/
│   │   └── NPC-QUICK-CARDS-TOP-20.md     ← EDIT THIS
│   └── build_npc_cards.py                ← RUN THIS
│
├── dm-toolkit-magic-items/
│   ├── markdown/
│   │   ├── MAGIC-ITEM-CARDS.md           ← EDIT THIS
│   │   └── LOOT-TABLES-BY-LEVEL.md       ← EDIT THIS
│   └── build_magic_items.py              ← RUN THIS
│
└── dm-toolkit-reference/
    ├── markdown/
    │   ├── SESSION-TRACKING-SHEETS.md    ← EDIT THESE
    │   ├── CAMPAIGN-DASHBOARD.md
    │   ├── LOCATION-QUICK-REFERENCE.md
    │   ├── MONSTER-STATS-CONDENSED.md
    │   ├── FACTION-RELATIONSHIP-MAP.md
    │   ├── MUSIC-AND-ATMOSPHERE-GUIDE.md
    │   ├── SESSION-ZERO-MATERIALS.md
    │   ├── SKILL-CHALLENGE-TEMPLATES.md
    │   ├── DM-QUICK-REFERENCE.md
    │   └── TIMELINE-VISUAL.md
    └── build_reference.py                ← RUN THIS
```

---

## ✏️ How to Edit

### 1. Edit the Markdown Files

Navigate to the appropriate `markdown/` directory and edit the files:

```bash
# Example: Edit random encounters
cd /home/claude/tirvandor-project/dm-toolkit-encounters/markdown
nano RANDOM-ENCOUNTER-TABLES.md
```

### 2. Rebuild the DOCX

After editing, run the build script:

```bash
# Random Encounters
cd /home/claude/tirvandor-project/dm-toolkit-encounters
python3 build_encounters.py

# NPC Cards
cd /home/claude/tirvandor-project/dm-toolkit-npc-cards
python3 build_npc_cards.py

# Magic Items
cd /home/claude/tirvandor-project/dm-toolkit-magic-items
python3 build_magic_items.py

# Reference Tools
cd /home/claude/tirvandor-project/dm-toolkit-reference
python3 build_reference.py
```

### 3. Get Your DOCX

Output files are created in: `/mnt/user-data/outputs/`

---

## 📝 Markdown Formatting Notes

### Random Encounters
- **Tables:** Use markdown table format with `|` separators
- **Headers:** Use `##` for sections, `###` for subsections
- **NPC Generator:** Tables must have proper `| header |` format

### NPC Cards
- **Headers:** Use `## NPC Name` (no "CARD X:")
- **Italics:** Use `*text*` for italic text
- **Bold:** Use `**text**` for bold text
- **Images:** Reference as `**Portrait:** \`filename.png\``

### Magic Items
- **Content in Boxes:** Everything inside ``` code blocks with box characters
- **Properties:** Use `•` bullet points
- **Quotes:** Use `"text"` for flavor text
- **Attribution:** `Campaign:` and `NPC:` lines

### Reference Tools
- **Tables:** Use markdown table format
- **Code Blocks:** Use ``` for form templates
- **Lists:** Use `-` or `*` for bullet lists

---

## 🖼️ Images

All images are stored in:
- `/home/claude/tirvandor-project/npc-portraits/` (342 images)

Includes both NPC portraits and magic item artwork.

---

## 🎨 Cover Image

Shared cover used by all products:
- `/home/claude/tirvandor-project/tirvandor-cover-dm-toolkit-converted.png`

---

## 🔄 Quick Rebuild All

```bash
#!/bin/bash
cd /home/claude/tirvandor-project/dm-toolkit-encounters && python3 build_encounters.py
cd /home/claude/tirvandor-project/dm-toolkit-npc-cards && python3 build_npc_cards.py
cd /home/claude/tirvandor-project/dm-toolkit-magic-items && python3 build_magic_items.py
cd /home/claude/tirvandor-project/dm-toolkit-reference && python3 build_reference.py
echo "✅ All DM Toolkit products rebuilt!"
```

---

## ✅ Current Status

All 4 products complete:
1. ✅ Random Encounters (2.6 MB)
2. ✅ NPC Quick Cards (13 MB)
3. ✅ Magic Items (22 MB)
4. ✅ Reference Tools (2.6 MB)

Total: ~40 MB across 4 professional DOCX files

---

## 📍 Output Location

All generated DOCX files: `/mnt/user-data/outputs/DM-Toolkit-*.docx`

Ready for download and distribution!
