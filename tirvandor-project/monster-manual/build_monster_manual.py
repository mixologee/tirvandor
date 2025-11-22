#!/usr/bin/env python3
"""
Tirvandor Monster Manual PDF Builder
Creates a professional Monster Manual with cover, monster portraits, and battle maps
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Image, 
    Table, TableStyle, KeepTogether, Flowable
)
from reportlab.pdfgen import canvas
from PIL import Image as PILImage
import os
import re
from pathlib import Path

class NumberedCanvas(canvas.Canvas):
    """Custom canvas for page numbers"""
    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_page_number(self, page_count):
        page_num = self._pageNumber
        if page_num > 1:  # Skip page number on cover
            self.setFont("Helvetica", 9)
            self.drawRightString(7.5 * inch, 0.5 * inch, 
                                f"Page {page_num - 1} of {page_count - 1}")

class MonsterManualBuilder:
    def __init__(self):
        self.width, self.height = letter
        self.styles = getSampleStyleSheet()
        self.setup_custom_styles()
        self.story = []
        
        # Paths
        self.monster_dir = Path('markdown')
        self.assets_dir = Path('/home/claude/assets')
        self.portraits_dir = Path('images/portraits')
        self.output_dir = Path('/mnt/user-data/outputs')
        self.output_dir.mkdir(exist_ok=True)
        
    def setup_custom_styles(self):
        """Create custom paragraph styles"""
        # Title style
        self.styles.add(ParagraphStyle(
            name='MonsterTitle',
            parent=self.styles['Heading1'],
            fontSize=18,
            textColor=colors.HexColor('#8B0000'),
            spaceAfter=12,
            spaceBefore=12,
            fontName='Helvetica-Bold'
        ))
        
        # Monster stat block style
        self.styles.add(ParagraphStyle(
            name='StatBlock',
            parent=self.styles['Normal'],
            fontSize=10,
            fontName='Courier',
            leftIndent=20,
            spaceAfter=6
        ))
        
        # Section header
        self.styles.add(ParagraphStyle(
            name='SectionHeader',
            parent=self.styles['Heading1'],
            fontSize=24,
            textColor=colors.HexColor('#2C3E50'),
            spaceAfter=20,
            spaceBefore=30,
            alignment=TA_CENTER,
            fontName='Helvetica-Bold'
        ))
        
        # Chapter header
        self.styles.add(ParagraphStyle(
            name='ChapterHeader',
            parent=self.styles['Heading2'],
            fontSize=16,
            textColor=colors.HexColor('#34495E'),
            spaceAfter=12,
            spaceBefore=24,
            fontName='Helvetica-Bold'
        ))
        
        # Lore/description
        self.styles.add(ParagraphStyle(
            name='Lore',
            parent=self.styles['Normal'],
            fontSize=10,
            alignment=TA_JUSTIFY,
            spaceAfter=10,
            fontName='Helvetica-Oblique'
        ))

    def find_monster_portrait(self, monster_name):
        """Find portrait image for a monster"""
        # Clean monster name for matching
        clean_name = monster_name.lower().replace("'", "").replace(" ", "-")
        
        # Search patterns
        patterns = [
            f"*{clean_name}*.jpg",
            f"*monster*{clean_name}*.jpg",
            f"*{clean_name.replace('-', '')}*.jpg"
        ]
        
        # Search in portraits directory
        for pattern in patterns:
            matches = list(self.portraits_dir.glob(pattern))
            if matches:
                return str(matches[0])
        
        # Search in assets
        for pattern in patterns:
            matches = list(self.assets_dir.rglob(pattern))
            if matches:
                return str(matches[0])
        
        return None

    def add_cover(self):
        """Add cover page"""
        cover_path = Path('images/tirvandor-cover-monster-manual.png')
        if cover_path.exists():
            # Cover image scaled to fit page with margins
            img = Image(str(cover_path), width=6.5*inch, height=8.5*inch)
            self.story.append(Spacer(1, 0.25*inch))
            self.story.append(img)
            self.story.append(PageBreak())
        else:
            # Fallback text cover
            title = Paragraph("TIRVANDOR", self.styles['Title'])
            subtitle = Paragraph("Monster Manual", self.styles['Heading1'])
            self.story.extend([Spacer(1, 2*inch), title, Spacer(1, 0.5*inch), 
                             subtitle, PageBreak()])

    def add_toc(self):
        """Add table of contents"""
        self.story.append(Paragraph("TABLE OF CONTENTS", self.styles['SectionHeader']))
        self.story.append(Spacer(1, 0.3*inch))
        
        toc_entries = [
            ("Border Creatures", "10 monsters"),
            ("Thaldros Military", "10 monsters"),
            ("Aethoria Resistance", "8 monsters"),
            ("Iron Guild Mercenaries", "7 monsters"),
            ("Ascended-Touched", "8 monsters"),
            ("Ancient & Prophecy", "4 monsters"),
            ("Corrupted & Cursed", "3 monsters"),
            ("Battle Maps", "6 encounter maps")
        ]
        
        for entry, count in toc_entries:
            line = Paragraph(f"<b>{entry}</b> - {count}", self.styles['Normal'])
            self.story.append(line)
            self.story.append(Spacer(1, 6))
        
        self.story.append(PageBreak())

    def parse_monster_markdown(self, filepath):
        """Parse a monster from markdown"""
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Split into individual monsters
        monsters = []
        monster_sections = re.split(r'^## \d+\. ', content, flags=re.MULTILINE)
        
        for section in monster_sections[1:]:  # Skip header
            lines = section.split('\n')
            if not lines:
                continue
                
            monster = {
                'name': lines[0].strip().upper(),
                'content': section
            }
            monsters.append(monster)
        
        return monsters

    def add_monster(self, monster):
        """Add a single monster to the PDF"""
        elements = []
        
        # Monster name
        elements.append(Paragraph(monster['name'], self.styles['MonsterTitle']))
        
        # Find and add portrait if available
        portrait_path = self.find_monster_portrait(monster['name'])
        if portrait_path:
            try:
                # Verify image can be opened
                PILImage.open(portrait_path).verify()
                img = Image(portrait_path, width=2*inch, height=2*inch)
                elements.append(img)
                elements.append(Spacer(1, 0.2*inch))
            except Exception as e:
                print(f"  ⚠️  Skipping image for {monster['name']}: {e}")
        
        # Parse stat block
        lines = monster['content'].split('\n')
        in_stat_block = True
        in_actions = False
        in_reactions = False
        
        for line in lines[1:]:  # Skip name
            line = line.strip()
            if not line:
                continue
            
            # Section headers
            if line.startswith('### ACTIONS'):
                in_actions = True
                elements.append(Paragraph("<b>ACTIONS</b>", self.styles['Normal']))
                continue
            elif line.startswith('### REACTIONS'):
                in_reactions = True
                elements.append(Paragraph("<b>REACTIONS</b>", self.styles['Normal']))
                continue
            elif line.startswith('### LORE'):
                in_stat_block = False
                elements.append(Spacer(1, 0.2*inch))
                elements.append(Paragraph("<b>Lore</b>", self.styles['Normal']))
                continue
            elif line.startswith('### TACTICS'):
                elements.append(Spacer(1, 0.1*inch))
                elements.append(Paragraph("<b>Tactics</b>", self.styles['Normal']))
                continue
            elif line.startswith('### CAMPAIGN USE'):
                elements.append(Spacer(1, 0.1*inch))
                elements.append(Paragraph("<b>Campaign Use</b>", self.styles['Normal']))
                continue
            elif line.startswith('---'):
                continue
            
            # Format line
            if line.startswith('*Medium') or line.startswith('*Large') or line.startswith('*Small'):
                # Creature type line
                p = Paragraph(f"<i>{line.strip('*')}</i>", self.styles['Normal'])
            elif line.startswith('**') and line.endswith('**'):
                # Bold headers
                p = Paragraph(f"<b>{line.strip('*')}</b>", self.styles['Normal'])
            elif line.startswith('|'):
                # Skip table lines for now
                continue
            elif line.startswith('- '):
                # Bullet points
                p = Paragraph(line, self.styles['Normal'])
            else:
                # Regular text
                p = Paragraph(line, self.styles['Normal'])
            
            elements.append(p)
            elements.append(Spacer(1, 3))
        
        # Keep monster together on same page if possible
        self.story.append(KeepTogether(elements))
        self.story.append(Spacer(1, 0.3*inch))

    def add_monster_file(self, filepath, chapter_name):
        """Add all monsters from a file"""
        self.story.append(Paragraph(chapter_name, self.styles['ChapterHeader']))
        self.story.append(Spacer(1, 0.2*inch))
        
        monsters = self.parse_monster_markdown(filepath)
        for monster in monsters:
            self.add_monster(monster)
        
        self.story.append(PageBreak())

    def add_battle_maps(self):
        """Add battle maps section"""
        self.story.append(Paragraph("BATTLE MAPS", self.styles['SectionHeader']))
        self.story.append(Spacer(1, 0.3*inch))
        
        intro = Paragraph(
            "The following encounter maps provide tactical battlefields for the creatures "
            "in this manual. Each map is designed for standard 5-foot grid play and includes "
            "terrain features, hazards, and strategic elements.",
            self.styles['Normal']
        )
        self.story.append(intro)
        self.story.append(Spacer(1, 0.3*inch))
        
        maps_dir = self.assets_dir / 'maps' / 'battle-maps' / 'monster-encounters'
        
        if maps_dir.exists():
            map_files = sorted(maps_dir.glob('*.jpg'))
            
            for map_file in map_files:
                # Map name
                map_name = map_file.stem.replace('-', ' ').title()
                self.story.append(Paragraph(map_name, self.styles['Heading2']))
                self.story.append(Spacer(1, 0.2*inch))
                
                # Add map image (scaled to fit page)
                try:
                    # Verify image first
                    PILImage.open(map_file).verify()
                    img = Image(str(map_file), width=6.5*inch, height=6.5*inch)
                    self.story.append(img)
                    self.story.append(PageBreak())
                except Exception as e:
                    print(f"  ⚠️  Error adding map {map_file.name}: {e}")
                    self.story.append(Paragraph(f"[Map image unavailable]", self.styles['Normal']))
                    self.story.append(PageBreak())

    def build(self):
        """Build the complete Monster Manual PDF"""
        print("🏗️  Building Tirvandor Monster Manual...")
        
        # Add cover
        print("📘 Adding cover...")
        self.add_cover()
        
        # Add TOC
        print("📋 Adding table of contents...")
        self.add_toc()
        
        # Add introduction
        print("📖 Adding introduction...")
        intro_text = [
            Paragraph("INTRODUCTION", self.styles['SectionHeader']),
            Spacer(1, 0.3*inch),
            Paragraph(
                "Welcome to the Tirvandor Monster Manual, a comprehensive bestiary "
                "for the Realm of Deep Magic. This tome contains 50 unique creatures, "
                "each designed for use in D&D 5th Edition campaigns set in Tirvandor.",
                self.styles['Normal']
            ),
            Spacer(1, 0.2*inch),
            Paragraph(
                "The creatures within are organized by theme and region, reflecting "
                "the complex political landscape of a world divided by ancient catastrophe. "
                "From the contested Border lands to the military might of Thaldros and "
                "the revolutionary spirit of Aethoria, each monster tells a story of "
                "this fractured realm.",
                self.styles['Normal']
            ),
            Spacer(1, 0.2*inch),
            Paragraph(
                "<b>Using This Manual:</b> Each creature entry includes complete D&D 5e "
                "statistics, lore, tactical notes for DMs, and campaign integration "
                "suggestions. Many entries reference the Blood & Coin and Shattered Oaths "
                "campaigns, showing how these creatures fit into Tirvandor's ongoing conflicts.",
                self.styles['Normal']
            ),
            PageBreak()
        ]
        self.story.extend(intro_text)
        
        # Add monster chapters
        monster_files = [
            ('MONSTERS-BORDER.md', 'BORDER CREATURES'),
            ('MONSTERS-THALDROS.md', 'THALDROS MILITARY'),
            ('MONSTERS-AETHORIA-AND-IRON-GUILD.md', 'AETHORIA & IRON GUILD'),
            ('MONSTERS-FINAL-15-SPECIAL.md', 'ANCIENT, ASCENDED & CORRUPTED'),
        ]
        
        for filename, chapter in monster_files:
            filepath = self.monster_dir / filename
            if filepath.exists():
                print(f"📚 Adding {chapter}...")
                self.add_monster_file(filepath, chapter)
            else:
                print(f"⚠️  Warning: {filename} not found")
        
        # Add battle maps
        print("🗺️  Adding battle maps...")
        self.add_battle_maps()
        
        # Build PDF
        output_path = self.output_dir / 'Tirvandor-Monster-Manual.pdf'
        print(f"📄 Building PDF: {output_path}")
        
        doc = SimpleDocTemplate(
            str(output_path),
            pagesize=letter,
            rightMargin=0.75*inch,
            leftMargin=0.75*inch,
            topMargin=0.75*inch,
            bottomMargin=0.75*inch
        )
        
        doc.build(self.story, canvasmaker=NumberedCanvas)
        
        print(f"✅ Monster Manual complete: {output_path}")
        print(f"📊 File size: {output_path.stat().st_size / (1024*1024):.2f} MB")
        
        return output_path

if __name__ == '__main__':
    builder = MonsterManualBuilder()
    builder.build()
