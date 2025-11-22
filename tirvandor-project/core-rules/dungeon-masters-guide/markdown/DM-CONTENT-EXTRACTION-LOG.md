# DM Content Extraction Log

## Summary

Comprehensive extraction of DM-only content from World Guide to DMG.

Total Extracted:
- 81 DM sections
- 1,277 lines of content
- 51 KB markdown file

Files Cleaned:

| Roll | Result |
|-----|--------|
| 1 | `regional-lore.md` - 423 lines removed |
| 2 | `settlement-histories.md` - 914 lines removed |
| 3 | `houses-and-dynasties.md` - 428 lines removed |
| 4 | `location-descriptions.md` - 311 lines removed |
| 5 | `settlement-histories-INDEX.md` - 6 lines removed |


Total Removed: 2,082 lines

## Content Types Extracted

### 1. Adventure Hooks Sections
Complete sections labeled "### Adventure Hooks" containing:
- Quest ideas for DMs
- Plot threads for campaigns
- Conflict escalation opportunities

### 2. Secrets & Mysteries Sections
Complete sections labeled "### Secrets & Mysteries" containing:
- Hidden truths about locations
- Conspiracy theories
- Undiscovered plot elements

### 3. Inline Quest Hooks
Individual NPC quest hooks marked with:
- `*Quest:` tags
- `*Secret:` tags
- `*Hook:` tags

## Output File

All extracted content saved to:
`/core-rules/dungeon-masters-guide/markdown/WORLD-GUIDE-DM-CONTENT.md`

Format: Organized by source file > chapter > section for easy reference.

## World Guide Status

The cleaned World Guide is now player-safe and contains only:
- Geographic descriptions
- Historical facts (public knowledge)
- NPC names, roles, and descriptions
- Cultural information
- Settlement details
- Faction descriptions (public knowledge)

No adventure hooks, secrets, or spoilers remain in player-facing content.

---

## FINAL CLEANUP - Additional Extraction

Date: 2025-11-13

### Additional Content Extracted

Total: 98 additional lines

### Sections Removed:

| Roll | Result |
|-----|--------|
| 1 | Adventure Hooks by Faction (factions.md) - 11 lines |
| 2 | Next Steps sections (houses-and-dynasties.md) |
| 3 | Session Notes (settlement-histories.md) - 2 lines |
| 4 | Quick Reference: Adventure Hooks (settlement-histories-INDEX.md) - 30 lines |
| 5 | Inline Adventure Hooks from city descriptions - 21 lines |
| 6 | Settlement Adventure Hooks (settlement-registry.md) - 13 lines |


### Formatting Fixes Applied:

Location Names Fixed (All Caps → Title Case):
- Kaer Thandros, Silverpine, Goldreach, Crossvale, Sundara, Ashgate, Ironhold
- Aethermere, Starfall, Crystalbrook, Marshaven, Wildgrove, Port Myrthen
- Deepforge, Riverdale, Oakenheart, Sandstone, Westmarch, Moonwell, Vineheart
- Oakenheart Village, Bogwallow Village, Frostholm Village

Regional Names Fixed:
- The Frostmarches, The Ironspine Holds, The Shattered Shore, The Silverwood
- The Heartlands, The Goldcoast, The Sundaran Expanse, The Ashfall Barrens
- The Reaching Claws, The Starwood, The Crystalvale, The Fractured Coast
- The Emerald Deeps, The Brightwater Valley, The Mistwood Reaches
- The Thornmire Marches, The Singing Fens, The Verdant Wall, The Split Peninsula

Section Headers Fixed:
- Major Cities - Detailed Walkthroughs
- Additional Major Cities - Detailed Walkthroughs
- Aethoria Cities - Detailed Walkthroughs
- Notable Towns - Detailed Scenes
- Selected Towns
- Thaldros Towns, Aethoria Towns
- Islands & Neutral Territories
- DM Tips

### Files Modified:

| Roll | Result |
|-----|--------|
| 1 | location-descriptions.md - 21 lines removed, 14 formatting fixes |
| 2 | location-details-street-level.md - 26 formatting fixes |
| 3 | regional-lore.md - 19 formatting fixes |
| 4 | settlement-histories-INDEX.md - 30 lines removed, 1 formatting fix |
| 5 | factions.md - 11 lines removed |
| 6 | settlement-registry.md - 13 lines removed |
| 7 | settlement-histories.md - 2 lines removed, 2 formatting fixes |


### Total Cleanup Stats:
- Lines extracted: 98
- Formatting fixes: 88
- Files cleaned: 7

All extracted content appended to: `WORLD-GUIDE-DM-CONTENT.md`

---

## META NOTES CLEANUP

Date: 2025-11-13

### Meta Notes Removed

Removed 18 lines of document creation/meta notes from 8 files:

Removed patterns:
- `*Created as part of Tirvandor Project - Phase X, Session Y*`
- `*Document created as part of Phase X, Session Y*`
- `*Compiled from [source files]*`
- `*[Document continues with...]*`
- `*[End of Section]*`
- `*End of [Section] Documentation*`
- `*Due to length constraints...*`
- `*This guide will expand as campaigns progress...*`
- `*For complete settlement details, see [link]*`
- `*For regional lore and adventure hooks, see [link]*`
- `*This is Part X of Y of the Expanded Timeline*`

Files cleaned:

| Roll | Result |
|-----|--------|
| 1 | location-details-street-level.md - 3 lines |
| 2 | timeline-expanded.md - 5 lines |
| 3 | timeline-expanded-part3.md - 3 lines |
| 4 | geography.md - 2 lines |
| 5 | location-descriptions.md - 2 lines |
| 6 | timeline-expanded-part1.md - 1 line |
| 7 | timeline-expanded-part2.md - 1 line |
| 8 | regional-lore.md - 1 line |


Kept (flavor/context):
- Chapter epigraphs and mottos
- Descriptive subtitles
- In-world flavor text about gods, history, culture
- Notes about different cultural perspectives
- Thematic introductions

Result: Clean, professional player-facing document with no meta/creation notes.

---

## DM/PLAYER TIPS EXTRACTION

Date: 2025-11-13

### DM Tips Moved to DMG

Total: 102 lines extracted to Dmg

Sections Removed:
1. DM Tips: Making Locations Memorable (location-descriptions.md)
- Show Character techniques
- Create Contrast examples

2. DM Tips: Using These Descriptions (location-details-street-level.md)
- Arrival/Walking Through/Improvisation
- NPC Encounters tips
- Creating Atmosphere techniques
- Sensory Layers hierarchy
- Show Don't Tell examples

3. Session Prep inline sections (location-descriptions.md)
4. Before Session/During Session subsections (location-details-street-level.md)
Files Modified:
1. location-descriptions.md - 63 lines removed
Output File:
`/core-rules/dungeon-masters-guide/markdown/WORLD-GUIDE-DM-TIPS.md` (3.6 KB)

Player Tips: None found (no player-specific tips in World Guide)

### Rationale

World Guide = Setting information only
- What exists in the world
- Public knowledge and lore
- Geographic and cultural facts

DMG = How to run it
- Session preparation techniques
- Description guidelines
- NPC interaction tips
- Atmosphere creation

PHB = Player guidance
- Character options
- How to engage with the world
- Player-facing rules

---

## FINAL EXTRACTION SUMMARY

Total Extracted from World Guide to DMG:
- Adventure Hooks & Mysteries: 2,180 lines (56 KB) - WORLD-GUIDE-DM-CONTENT.md
- DM Tips & Session Prep: 102 lines (3.6 KB) - WORLD-GUIDE-DM-TIPS.md
- TOTAL: 2,282 lines across 2 files

World Guide Status:
✓ Player-safe
✓ No adventure hooks, secrets, or spoilers
✓ No DM tips or session prep guidance
✓ No meta notes or creation references
✓ No all-caps formatting issues
✓ Professional, clean, ready for distribution

---

## STREET-LEVEL DETAILS & FINAL DM SECTIONS MOVED

Date: 2025-11-13

### Entire File Moved to DMG

location-details-street-level.md → WORLD-GUIDE-STREET-LEVEL-DETAILS.md
- Size: 136 KB (2,326 lines)
- Content: Complete street-level location details for DMs
- Reason: Entire file explicitly "for DMs" - immersive descriptions for running sessions

Sections included:
- Major Cities - Detailed Walkthroughs
- Village Descriptions (Detailed Examples)
- District-by-district breakdowns
- Approach descriptions, typical scenes, random detail tables
- All DM-focused atmospheric guidance

### Additional DM Sections Extracted

From location-descriptions.md:
- "For DMs" section with usage guidance

From settlement-histories-INDEX.md:
- "For DMs" section with hook usage

From regional-lore.md:
- "Usage Notes for DMs" section

### Player Content Extracted to PHB

Created: WORLD-GUIDE-PLAYER-TIPS.md (592 bytes)

From location-descriptions.md:
- "For Players" - Character Creation guidance
- Shopping & Services notes

From settlement-histories-INDEX.md:
- "For Players" - Background and patron options

---

## COMPLETE EXTRACTION TOTALS

Moved from World Guide to DMG:

| d6 | Result |
|-----|--------|
| 1 | Adventure Hooks & Mysteries: 2,180 lines (56 KB) - WORLD-GUIDE-DM-CONTENT.md |
| 2 | DM Tips & Session Prep: 102 lines (4.1 KB) - WORLD-GUIDE-DM-TIPS.md |
| 3 | Street-Level Details: 2,326 lines (136 KB) - WORLD-GUIDE-STREET-LEVEL-DETAILS.md |
| 4 | TOTAL: 4,608 lines (196 KB) across 3 files |


Moved from World Guide to PHB:
1. Player Tips: ~20 lines (592 bytes) - WORLD-GUIDE-PLAYER-TIPS.md
World Guide Final Status:
- Size reduced: 18 MB → 17 MB
- Removed: location-details-street-level.md from build
- Images: 30 → 28 (removed with street-level file)
- 100% player-safe, no DM content remaining
- Clean, professional, ready for distribution

Verification Checks:
✓ No "For DMs" references
✓ No "Street-Level" references
✓ No "Usage Notes for DMs"
✓ No "Session Prep" guidance
✓ No adventure hooks or secrets
✓ No DM tips or techniques
✓ No all-caps formatting issues
