#!/usr/bin/env python3
"""
Tirvandor FGU Module - Complete Final Version
Fixed: Portrait matching, 2024 ruleset, proper names
"""

import os, re, zipfile, glob
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom
import html

class FGUMonster:
    def __init__(self):
        self.monsters_dir = '/home/claude/monsters'
        self.portraits_dir = '/home/claude/portraits-converted'
        self.output_dir = '/mnt/user-data/outputs'
    
    def strip_md(self, text):
        if not text:
            return ''
        text = re.sub(r'\*\*([^\*]+)\*\*', r'\1', text)
        text = re.sub(r'\*([^\*]+)\*', r'\1', text)
        text = re.sub(r'`([^`]+)`', r'\1', text)
        text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
        text = text.replace('*', '').replace('_', '')
        text = re.sub(r'\s+', ' ', text)
        return text.strip()
    
    def title_case(self, text):
        """Convert ALL CAPS to proper Title Case"""
        text = text.strip()
        if text.isupper() or text.count(' ') > 0:
            result = text.title()
            result = re.sub(r"'S\b", "'s", result)
            return result
        return text
    
    def find_portrait(self, monster_name):
        """Find portrait file with multiple search patterns"""
        # Create search base
        base = monster_name.lower().replace(' ', '-').replace("'", '').replace('(', '').replace(')', '')
        
        # Try multiple patterns
        patterns = [
            f'tirvandor-monster-{base}.png',
            f'{base}.png',
            f'tirvandor-monster-{base}-*.png',  # Wildcard for extra suffixes
        ]
        
        # Also try without possessive 's'
        if 's' in base:
            base_no_s = base.replace('s-', '-')
            patterns.extend([
                f'tirvandor-monster-{base_no_s}.png',
                f'{base_no_s}.png',
            ])
        
        for pattern in patterns:
            matches = glob.glob(os.path.join(self.portraits_dir, pattern))
            if matches:
                return matches[0]  # Return first match
        
        return None
    
    def parse_stat(self, text):
        text = self.strip_md(text)
        m = re.search(r'(\d+)\s*\(([+-]\d+)\)', text)
        if m:
            return int(m.group(1)), int(m.group(2).replace('+', ''))
        m = re.search(r'(\d+)', text)
        if m:
            score = int(m.group(1))
            return score, (score - 10) // 2
        return 10, 0
    
    def parse_file(self, path):
        with open(path, 'r') as f:
            content = f.read()
        monsters = re.split(r'^(?:##|###)\s+\d+\.\s+', content, flags=re.MULTILINE)
        result = []
        for m in monsters[1:]:
            if m.strip():
                parsed = self.parse_monster(m)
                if parsed:
                    result.append(parsed)
        return result
    
    def parse_monster(self, text):
        lines = text.split('\n')
        raw_name = self.strip_md(lines[0].strip())
        
        m = {
            'name': self.title_case(raw_name),
            'type': '', 'size': 'Medium', 'alignment': 'unaligned',
            'ac': '', 'actext': '', 'hp': '', 'hd': '', 'speed': '',
            'str': 10, 'dex': 10, 'con': 10, 'int': 10, 'wis': 10, 'cha': 10,
            'str_b': 0, 'dex_b': 0, 'con_b': 0, 'int_b': 0, 'wis_b': 0, 'cha_b': 0,
            'saves': '', 'skills': '', 'senses': '', 'languages': '', 'cr': '', 'xp': 0,
            'traits': [], 'actions': [], 'reactions': [],
            'lore': '', 'tactics': '', 'campaign': ''
        }
        
        section = 'stats'
        
        for line in lines[1:]:
            s = line.strip()
            
            if s.startswith('### ACTIONS') or s == '**ACTIONS**':
                section = 'actions'
            elif s.startswith('### REACTIONS'):
                section = 'reactions'
            elif s.startswith('### LORE'):
                section = 'lore'
            elif s.startswith('### TACTICS'):
                section = 'tactics'
            elif s.startswith('### CAMPAIGN'):
                section = 'campaign'
            elif not s or s.startswith('---'):
                continue
            else:
                if section == 'stats':
                    if s.startswith('*') and any(t in s.lower() for t in ['humanoid', 'undead', 'construct', 'elemental', 'aberration', 'fiend', 'dragon', 'beast', 'monstrosity', 'plant', 'ooze', 'giant', 'fey', 'celestial']):
                        m['type'] = self.strip_md(s)
                        for sz in ['Tiny', 'Small', 'Medium', 'Large', 'Huge', 'Gargantuan']:
                            if sz in m['type']:
                                m['size'] = sz
                        for al in ['lawful good', 'neutral good', 'chaotic good', 'lawful neutral', 'neutral', 'chaotic neutral', 'lawful evil', 'neutral evil', 'chaotic evil', 'unaligned']:
                            if al in m['type'].lower():
                                m['alignment'] = al
                    elif 'Armor Class' in s or s.startswith('**AC**'):
                        ac = self.strip_md(re.sub(r'Armor Class|AC', '', s))
                        match = re.match(r'(\d+)\s*(.*)', ac)
                        if match:
                            m['ac'], m['actext'] = match.group(1), match.group(2).strip('()')
                    elif 'Hit Points' in s or s.startswith('**HP**'):
                        hp = self.strip_md(re.sub(r'Hit Points|HP', '', s))
                        match = re.match(r'(\d+)\s*\((.*?)\)', hp)
                        if match:
                            m['hp'], m['hd'] = match.group(1), match.group(2)
                    elif 'Speed' in s and 'Armor' not in s:
                        m['speed'] = self.strip_md(re.sub(r'Speed', '', s))
                    elif re.match(r'^\|\s*\d+', s):
                        parts = [p.strip() for p in s.split('|') if p.strip()]
                        if len(parts) == 6:
                            m['str'], m['str_b'] = self.parse_stat(parts[0])
                            m['dex'], m['dex_b'] = self.parse_stat(parts[1])
                            m['con'], m['con_b'] = self.parse_stat(parts[2])
                            m['int'], m['int_b'] = self.parse_stat(parts[3])
                            m['wis'], m['wis_b'] = self.parse_stat(parts[4])
                            m['cha'], m['cha_b'] = self.parse_stat(parts[5])
                    elif 'Saving Throws' in s or s.startswith('**Saves**'):
                        m['saves'] = self.strip_md(re.sub(r'Saving Throws|Saves', '', s))
                    elif 'Skills' in s and 'Saving' not in s:
                        m['skills'] = self.strip_md(re.sub(r'Skills', '', s))
                    elif 'Senses' in s:
                        m['senses'] = self.strip_md(re.sub(r'Senses', '', s))
                    elif 'Languages' in s:
                        m['languages'] = self.strip_md(re.sub(r'Languages', '', s))
                    elif 'Challenge' in s:
                        cr = self.strip_md(re.sub(r'Challenge', '', s))
                        match = re.match(r'([0-9/]+)\s*\(([0-9,]+)', cr)
                        if match:
                            m['cr'], m['xp'] = match.group(1), int(match.group(2).replace(',', ''))
                    elif s.startswith('**') and not any(x in s for x in ['Armor', 'Hit', 'Speed', 'Saving', 'Skills', 'Senses', 'Languages', 'Challenge', 'AC', 'HP', 'Saves', 'CR']):
                        match = re.match(r'\*\*([^*]+)\*\*\.?\s*(.*)', s)
                        if match:
                            m['traits'].append({'name': self.strip_md(match.group(1)), 'desc': self.strip_md(match.group(2))})
                    elif m['traits'] and not s.startswith('|'):
                        m['traits'][-1]['desc'] += ' ' + self.strip_md(s)
                
                elif section == 'actions':
                    if s.startswith('**'):
                        match = re.match(r'\*\*([^*]+)\*\*\.?\s*(.*)', s)
                        if match:
                            m['actions'].append({'name': self.strip_md(match.group(1)), 'desc': self.strip_md(match.group(2))})
                    elif m['actions'] and not s.startswith('|'):
                        m['actions'][-1]['desc'] += ' ' + self.strip_md(s)
                
                elif section == 'reactions':
                    if s.startswith('**'):
                        match = re.match(r'\*\*([^*]+)\*\*\.?\s*(.*)', s)
                        if match:
                            m['reactions'].append({'name': self.strip_md(match.group(1)), 'desc': self.strip_md(match.group(2))})
                    elif m['reactions']:
                        m['reactions'][-1]['desc'] += ' ' + self.strip_md(s)
                
                elif section == 'lore':
                    m['lore'] += self.strip_md(s) + ' '
                elif section == 'tactics':
                    m['tactics'] += self.strip_md(s) + ' '
                elif section == 'campaign':
                    m['campaign'] += self.strip_md(s) + ' '
        
        return m
    
    def to_xml(self, m, parent, zf):
        mid = re.sub(r'[^a-z0-9]', '', m['name'].lower())
        elem = SubElement(parent, f'id-{mid}')
        
        SubElement(elem, 'locked', type='number').text = '1'
        SubElement(elem, 'name', type='string').text = m['name']
        SubElement(elem, 'size', type='string').text = m['size']
        SubElement(elem, 'type', type='string').text = m['type']
        SubElement(elem, 'alignment', type='string').text = m['alignment']
        
        if m['ac']:
            SubElement(elem, 'ac', type='number').text = str(m['ac'])
        if m['actext']:
            SubElement(elem, 'actext', type='string').text = f"({m['actext']})"
        if m['hp']:
            SubElement(elem, 'hp', type='number').text = str(m['hp'])
        if m['hd']:
            SubElement(elem, 'hd', type='string').text = m['hd']
        if m['speed']:
            SubElement(elem, 'speed', type='string').text = m['speed']
        
        abilities = SubElement(elem, 'abilities')
        for stat, name in [('str', 'strength'), ('dex', 'dexterity'), ('con', 'constitution'), 
                           ('int', 'intelligence'), ('wis', 'wisdom'), ('cha', 'charisma')]:
            s = SubElement(abilities, name)
            SubElement(s, 'score', type='number').text = str(m[stat])
            SubElement(s, 'bonus', type='number').text = str(m[f'{stat}_b'])
        
        if m['saves']:
            SubElement(elem, 'savingthrows', type='string').text = m['saves']
        if m['skills']:
            SubElement(elem, 'skills', type='string').text = m['skills']
        if m['senses']:
            SubElement(elem, 'senses', type='string').text = m['senses']
        if m['languages']:
            SubElement(elem, 'languages', type='string').text = m['languages']
        if m['cr']:
            SubElement(elem, 'cr', type='string').text = m['cr']
        if m['xp']:
            SubElement(elem, 'xp', type='number').text = str(m['xp'])
        
        if m['traits']:
            traits = SubElement(elem, 'traits')
            for i, t in enumerate(m['traits'], 1):
                te = SubElement(traits, f'id-{i:05d}')
                SubElement(te, 'name', type='string').text = t['name']
                SubElement(te, 'desc', type='string').text = t['desc'].strip()
        
        if m['actions']:
            actions = SubElement(elem, 'actions')
            for i, a in enumerate(m['actions'], 1):
                ae = SubElement(actions, f'id-{i:05d}')
                SubElement(ae, 'name', type='string').text = a['name']
                SubElement(ae, 'desc', type='string').text = a['desc'].strip()
        
        if m['reactions']:
            reactions = SubElement(elem, 'reactions')
            for i, r in enumerate(m['reactions'], 1):
                re_elem = SubElement(reactions, f'id-{i:05d}')
                SubElement(re_elem, 'name', type='string').text = r['name']
                SubElement(re_elem, 'desc', type='string').text = r['desc'].strip()
        
        notes_html = []
        if m['lore'].strip():
            notes_html.append(f"<h>Lore</h><p>{html.escape(m['lore'].strip())}</p>")
        if m['tactics'].strip():
            notes_html.append(f"<h>Tactics</h><p>{html.escape(m['tactics'].strip())}</p>")
        if m['campaign'].strip():
            notes_html.append(f"<h>Campaign Use</h><p>{html.escape(m['campaign'].strip())}</p>")
        
        if notes_html:
            SubElement(elem, 'text', type='formattedtext').text = ''.join(notes_html)
        
        # Find portrait with improved matching
        portrait = self.find_portrait(m['name'])
        if portrait:
            name_base = os.path.basename(portrait).replace('.png', '')
            zf.write(portrait, f'tokens/{name_base}.png')
            SubElement(elem, 'token', type='token').text = f'tokens/{name_base}.png'
            print(f"    ✓ {os.path.basename(portrait)}")
    
    def build(self):
        print("\n🏗️  Building Tirvandor Monster Manual (2024)...")
        
        definition = Element('root', version='3.1')
        SubElement(definition, 'n').text = 'TirvandorMonsterManual'
        SubElement(definition, 'author').text = 'Mixologee'
        SubElement(definition, 'ruleset').text = '2024'
        SubElement(definition, 'displayname').text = 'Tirvandor: Monster Manual'
        
        db = Element('root', version='3.1')
        npc = SubElement(db, 'npc')
        
        mod_path = os.path.join(self.output_dir, 'Tirvandor-Monster-Manual.mod')
        
        total = 0
        with zipfile.ZipFile(mod_path, 'w', zipfile.ZIP_DEFLATED) as zf:
            for fname in ['MONSTERS-BORDER.md', 'MONSTERS-THALDROS.md', 
                         'MONSTERS-AETHORIA-AND-IRON-GUILD.md', 'MONSTERS-FINAL-15-SPECIAL.md']:
                fpath = os.path.join(self.monsters_dir, fname)
                if os.path.exists(fpath):
                    print(f"\n📖 {fname}")
                    for monster in self.parse_file(fpath):
                        print(f"  {monster['name']}")
                        self.to_xml(monster, npc, zf)
                        total += 1
            
            print(f"\n✅ {total} monsters")
            
            rough = tostring(definition, 'utf-8')
            zf.writestr('definition.xml', minidom.parseString(rough).toprettyxml(indent="  ", encoding="ISO-8859-1"))
            
            rough = tostring(db, 'utf-8')
            zf.writestr('db.xml', minidom.parseString(rough).toprettyxml(indent="  ", encoding="ISO-8859-1"))
            
            thumb = '/home/claude/assets/covers/tirvandor-cover-monster-manual.png'
            if os.path.exists(thumb):
                zf.write(thumb, 'thumbnail.png')
        
        size = os.path.getsize(mod_path) / (1024 * 1024)
        print(f"\n✅ {mod_path} ({size:.2f} MB)")

FGUMonster().build()
