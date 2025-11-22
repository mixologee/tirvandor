<style>
  /* === TIRVANDOR MONSTER MANUAL THEME === */
  
  /* Main page background - aged parchment */
  .phb {
    background-color: #f5f2e8;
    font-family: 'Crimson Text', serif;
  }
  
  /* Headers - deep forest green with bronze accents */
  .phb h1 {
    color: #1b4332;
    border-bottom: 3px solid #8b6914;
    font-family: 'Spectral SC', serif;
  }
  
  .phb h2 {
    color: #2c5f2d;
    font-family: 'Spectral SC', serif;
  }
  
  .phb h3, .phb h4 {
    color: #40513b;
  }
  
  /* Stat blocks - subtle green with bronze border */
  .phb blockquote {
    border-left: 5px solid #8b6914;
    background-color: #f0f7f0;
    box-shadow: 0 0 5px rgba(43, 95, 45, 0.1);
  }
  
  /* Monster names in stat blocks */
  .phb blockquote h2 {
    color: #1b4332;
    border-bottom: 2px solid #8b6914;
    font-family: 'Spectral SC', serif;
  }
  
  /* Horizontal rules */
  .phb hr {
    background-image: linear-gradient(to right, 
      transparent, 
      #2c5f2d 10%, 
      #8b6914 50%, 
      #2c5f2d 90%, 
      transparent);
  }
  
  /* Page numbers and footers */
  .phb .pageNumber {
    color: #8b6914;
    font-family: 'Spectral SC', serif;
  }
  
  /* Footer text alternating pages */
  .phb:nth-child(odd):after {
    content: 'TIRVANDOR: MONSTER MANUAL';
    font-family: 'Spectral SC', serif;
    font-size: 0.8em;
    color: #2c5f2d;
  }
  
  .phb:nth-child(even):after {
    content: 'CREATURES OF THE SUNDERING';
    font-family: 'Spectral SC', serif;
    font-size: 0.8em;
    color: #2c5f2d;
  }
  
  /* Tables - match the theme */
  .phb table thead {
    background-color: #2c5f2d;
    color: #f5f2e8;
  }
  
  
  .phb#p1:after {
    display: none;
  }
  
  .phb#p1::before {
    display: none;
  }
  
  /* Table of Contents - no decorative letter, bigger font */
  .phb#p2 h1:first-letter {
    font-size: inherit;
    float: none;
    line-height: inherit;
    color: inherit;
  }
  
  .phb#p2 {
    font-size: 1.1em;
  }
</style>

![monster_manual_cover](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/tirvandor-project/monster-manual-cover.png) {position:absolute,top:0px,left:0px,width:820px}
\page
# Chapter 1
# Border Creatures

The contested lands between Thaldros and Aethoria are a lawless frontier where desperate souls eke out survival among ancient ruins and war-scarred terrain.

:::::::::::::

{{monster,frame,wide
## BORDER BANDIT
*Medium humanoid (any race), any non-lawful alignment*
___
**Armor Class** :: 12 (leather armor)
**Hit Points** :: 11 (2d8 + 2)
**Speed** :: 30 ft.![border bandit](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-border-bandit.jpg) {width:325px,mix-blend-mode:multiply}
___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|11 (+0) | 14 (+2) | 12 (+1) | 10 (+0) | 10 (+0) | 10 (+0)|
___
**Skills** Stealth +4, Deception +2
**Senses** passive Perception 10
**Languages** Common
**Challenge** 1/2 (100 XP)
___
**Border Cunning.** The bandit has advantage on Stealth checks in the Border region's ruins and wilderness.

**Desperate Fighter.** When reduced to half hit points or less, the bandit's next attack deals an extra 1d6 damage.

___
### ACTIONS
**Scimitar.** *Melee Weapon Attack:* +4 to hit, reach 5 ft., one target. *Hit:* 5 (1d6 + 2) slashing damage.

**Light Crossbow.** *Ranged Weapon Attack:* +4 to hit, range 80/320 ft., one target. *Hit:* 6 (1d8 + 2) piercing damage.

### LORE
Border bandits are desperate refugees, deserters, or opportunists who prey on travelers in the contested lands. They know the terrain intimately and fight with the desperation of those with nothing left to lose.
### TACTICS
- Use terrain for ambushes
- Target weakest-looking party member
- Flee when outnumbered or badly wounded
- May surrender if offered mercy
}}

\page

{{monster,frame,wide
## SMUGGLER CAPTAIN
*Medium humanoid (any race), any alignment*
___
**Armor Class** :: 15 (studded leather)
**Hit Points** :: 58 (9d8 + 18)
**Speed** :: 30 ft.![smuggler captain](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-smuggler-captain.jpg) {width:325px,mix-blend-mode:multiply}
___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|12 (+1) | 16 (+3) | 14 (+2) | 14 (+2) | 12 (+1) | 14 (+2)|
___
**Saving Throws** Dexterity +5, Intelligence +4
**Skills** Deception +6, Insight +3, Persuasion +6, Stealth +5
**Senses** passive Perception 11
**Languages** Common, Thieves' Cant, plus two others
**Challenge** 3 (700 XP)
___
**Cunning Action.** On each of its turns, the captain can use a bonus action to take the Dash, Disengage, or Hide action.

**Border Network.** The captain knows safe routes through the Border and has contacts in most settlements. Can call for reinforcements (1d4 border bandits arrive in 1d4 rounds).

**Sneak Attack (1/Turn).** The captain deals an extra 10 (3d6) damage when hitting with a weapon attack and has advantage on the attack roll.

___
### ACTIONS
**Multiattack.** The captain makes two attacks with their rapier.

**Rapier.** *Melee Weapon Attack:* +5 to hit, reach 5 ft., one target. *Hit:* 7 (1d8 + 3) piercing damage.

**Hand Crossbow.** *Ranged Weapon Attack:* +5 to hit, range 30/120 ft., one target. *Hit:* 6 (1d6 + 3) piercing damage.

**Contract Offer (Recharge 5-6).** The captain offers a bargain. One humanoid within 30 feet that can hear the captain must make a DC 14 Wisdom saving throw. On a failure, the target is charmed for 1 minute or until the captain or their allies harm it. While charmed, the target is inclined to accept reasonable deals.

### REACTIONS
**Parry.** The captain adds 2 to their AC against one melee attack that would hit them. To do so, the captain must see the attacker and be wielding a melee weapon.

### LORE
Smuggler captains run illicit goods across the Border—weapons, refugees, contraband, and information. They're neutral parties in the conflict, caring only for profit, but their networks make them valuable allies or dangerous enemies.
### TACTICS
- Negotiate before fighting if possible
- Use Cunning Action to stay mobile
- Call for backup if losing
- Always have an escape route planned
}}

\page

{{monster,frame,wide
## WAR-SCARRED VETERAN
*Medium humanoid (any race), any alignment*
___
**Armor Class** :: 17 (half plate)
**Hit Points** :: 68 (8d8 + 32)
**Speed** :: 30 ft.![war-scarred veteran](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-war-scarred-veteran.jpg) {width:325px,mix-blend-mode:multiply}
___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|16 (+3) | 13 (+1) | 18 (+4) | 10 (+0) | 12 (+1) | 10 (+0)|
___
**Saving Throws** Strength +5, Constitution +6
**Skills** Athletics +5, Intimidation +2, Survival +3
**Senses** passive Perception 11
**Languages** Common
**Challenge** 4 (1,100 XP)
___
**Survivor.** The veteran has advantage on death saving throws.

**Seen It All.** The veteran is immune to being frightened and has advantage on saving throws against being charmed.

**Battle Scarred.** When the veteran takes damage that would reduce them to 0 hit points, they can make a DC 10 Constitution saving throw. On a success, they drop to 1 hit point instead. This DC increases by 5 each time this feature is used and resets after a long rest.

___
### ACTIONS
**Multiattack.** The veteran makes two longsword attacks or two longbow attacks.

**Longsword.** *Melee Weapon Attack:* +5 to hit, reach 5 ft., one target. *Hit:* 7 (1d8 + 3) slashing damage, or 8 (1d10 + 3) slashing damage if used with two hands.

**Longbow.** *Ranged Weapon Attack:* +3 to hit, range 150/600 ft., one target. *Hit:* 5 (1d8 + 1) piercing damage.

**Intimidating Presence (Recharge 5-6).** The veteran roars a challenge. Each enemy within 30 feet that can see or hear the veteran must make a DC 13 Wisdom saving throw or become frightened for 1 minute. A frightened creature can repeat the save at the end of each of its turns, ending the effect on a success.

### LORE
These veterans have fought in countless Border skirmishes for both sides, mercenary bands, or their own survival. They're hard as nails, cynical, and incredibly difficult to kill. Many become mercenaries, bandits, or hermits.
### TACTICS
- Fight defensively, conserving energy
- Use intimidation to avoid fights
- Know when to retreat (and how)
- Protect allies instinctively
}}

\page

{{monster,frame,wide
## BORDER WRAITH
*Medium undead, neutral evil*
___
**Armor Class** :: 13
**Hit Points** :: 67 (9d8 + 27)
**Speed** :: 0 ft., fly 60 ft. (hover)![border wraith](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-border-wraith.jpg) {width:325px,mix-blend-mode:multiply}
___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|6 (-2) | 16 (+3) | 16 (+3) | 12 (+1) | 14 (+2) | 15 (+2)|
___
**Senses** darkvision 60 ft., passive Perception 12
**Languages** the languages it knew in life
**Challenge** 5 (1,800 XP)
___
**Incorporeal Movement.** The wraith can move through other creatures and objects as if they were difficult terrain. It takes 5 (1d10) force damage if it ends its turn inside an object.

**Sunlight Sensitivity.** While in sunlight, the wraith has disadvantage on attack rolls and Wisdom (Perception) checks that rely on sight.

**Border-Bound.** The wraith is bound to the Border region where it died. If forced outside the Border, it takes 10 (3d6) psychic damage at the start of each of its turns.

**Echoes of War.** When the wraith first appears, each creature within 30 feet hears a snippet of the battle where it died (screams, clashing steel, etc.). The wraith can speak one phrase from its final moments.

___
### ACTIONS
**Life Drain.** *Melee Weapon Attack:* +6 to hit, reach 5 ft., one creature. *Hit:* 21 (4d8 + 3) necrotic damage. The target must succeed on a DC 14 Constitution saving throw or its hit point maximum is reduced by an amount equal to the damage taken. This reduction lasts until the target finishes a long rest. The target dies if this effect reduces its hit point maximum to 0.

**Create Specter.** The wraith targets a humanoid within 10 feet of it that died violently in the last minute. The target's spirit rises as a specter under the wraith's control. The wraith can have no more than three specters under its control at one time.

### LORE
Border wraiths are the spirits of soldiers and civilians who died in the countless conflicts in the Border region. They're drawn to battles, feeding on death and violence. Some retain fragments of their former identities and may be laid to rest if their remains are properly buried.
### TACTICS
- Ambush from walls/objects
- Target squishier party members
- Use Create Specter on fallen enemies
- Flee if seriously injured (unless enraged)
}}

\page

{{monster,frame,wide
## CONTESTED LAND ELEMENTAL
*Large elemental, neutral*
___
**Armor Class** :: 17 (natural armor)
**Hit Points** :: 126 (12d10 + 60)
**Speed** :: 30 ft., burrow 30 ft.![contested land elemental](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-contested-land-elemental.jpg) {width:325px,mix-blend-mode:multiply}
___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|20 (+5) | 8 (-1) | 20 (+5) | 5 (-3) | 10 (+0) | 5 (-3)|
___
**Senses** darkvision 60 ft., tremorsense 60 ft., passive Perception 10
**Languages** Terran
**Challenge** 6 (2,300 XP)
___
**Earth Glide.** The elemental can burrow through nonmagical, unworked earth and stone. While doing so, it doesn't disturb the material it moves through.

**Siege Monster.** The elemental deals double damage to objects and structures.

**Mixed Form.** The elemental's body contains earth from both Thaldros and Aethoria, making it unstable. When the elemental takes damage, roll 1d6. On a 5-6, it erupts, dealing 7 (2d6) bludgeoning damage to all creatures within 5 feet.

**Territorial Fury.** The elemental has advantage on attack rolls against creatures that have dealt damage to structures or the earth in the last minute.

___
### ACTIONS
**Multiattack.** The elemental makes two slam attacks.

**Slam.** *Melee Weapon Attack:* +8 to hit, reach 10 ft., one target. *Hit:* 14 (2d8 + 5) bludgeoning damage.

**Border Quake (Recharge 5-6).** The elemental strikes the ground, creating a localized earthquake. Each creature on the ground within 20 feet must make a DC 15 Strength saving throw. On a failure, a creature takes 18 (4d8) bludgeoning damage and is knocked prone. On a success, the creature takes half damage and isn't knocked prone. Additionally, the ground in that area becomes difficult terrain until cleared.

### LORE
These elementals form in the Border region, composed of earth from both nations. The constant conflict and bloodshed has made the land itself angry and unstable. They attack anyone who further damages the land but may ignore peaceful travelers.
### TACTICS
- Emerge from underground (surprise)
- Focus on those damaging terrain
- Use Border Quake to knock down groups
- Retreat underground if badly hurt
}}

\page

{{monster,frame,wide
## REFUGEE MOB
*Large swarm of Medium humanoids, any alignment*
___
**Armor Class** :: 10
**Hit Points** :: 39 (6d10 + 6)
**Speed** :: 30 ft.![refugee mob](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-refugee-mob.jpg) {width:325px,mix-blend-mode:multiply}
___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|10 (+0) | 10 (+0) | 12 (+1) | 10 (+0) | 10 (+0) | 8 (-1)|
___
**Senses** passive Perception 10
**Languages** Common
**Challenge** 1 (200 XP)
___
**Swarm.** The mob can occupy another creature's space and vice versa, and the mob can move through any opening large enough for a Medium humanoid. The mob can't regain hit points or gain temporary hit points.

**Desperate Horde.** The mob has advantage on attack rolls if it has half its hit points or more.

**Panicked.** The mob has disadvantage on Wisdom saving throws while below half hit points.

___
### ACTIONS
**Mob Violence.** *Melee Weapon Attack:* +2 to hit, reach 0 ft., one creature in the swarm's space. *Hit:* 14 (4d6) bludgeoning damage, or 7 (2d6) bludgeoning damage if the swarm has half its hit points or fewer.

### REACTIONS
**Stampede.** When the mob takes damage from an area effect, it can move up to its speed away from the source of danger. This movement doesn't provoke opportunity attacks.

### LORE
Desperate refugees sometimes form angry mobs, driven by fear, hunger, or manipulation. They're not evil—just desperate people in terrible circumstances. Most will flee or surrender if given the opportunity.
### TACTICS
- Overwhelm through numbers
- Target obvious threats
- Flee if leaders fall or hope is offered
- Can be calmed with Persuasion (DC 15)
}}

\page

{{monster,frame,wide
## SCAVENGER GHOUL
*Medium undead, chaotic evil*
___
**Armor Class** :: 12
**Hit Points** :: 22 (5d8)
**Speed** :: 30 ft.![scavenger ghoul](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-scavenger-ghoul.jpg) {width:325px,mix-blend-mode:multiply}
___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|13 (+1) | 15 (+2) | 10 (+0) | 7 (-2) | 10 (+0) | 6 (-2)|
___
**Senses** darkvision 60 ft., passive Perception 10
**Languages** Common
**Challenge** 1 (200 XP)
___
**Battlefield Scavenger.** The ghoul has advantage on Wisdom (Perception) checks to find corpses or wounded creatures.

**Pack Tactics.** The ghoul has advantage on attack rolls against a creature if at least one of the ghoul's allies is within 5 feet of the creature and the ally isn't incapacitated.

___
### ACTIONS
**Bite.** *Melee Weapon Attack:* +4 to hit, reach 5 ft., one creature. *Hit:* 9 (2d6 + 2) piercing damage.

**Claws.** *Melee Weapon Attack:* +4 to hit, reach 5 ft., one target. *Hit:* 7 (2d4 + 2) slashing damage. If the target is a creature other than an elf or undead, it must succeed on a DC 10 Constitution saving throw or be paralyzed for 1 minute. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success.

**Corpse Feast (Recharge 5-6).** If the ghoul is adjacent to a corpse or unconscious creature, it can spend its action feeding. It regains 10 (3d6) hit points.

### LORE
The Border's constant violence creates ample food for ghouls. These undead scavengers lurk near battlefields and ambush sites, waiting for fresh corpses—or making their own.
### TACTICS
- Hunt in packs (2-8 ghouls)
- Target wounded enemies
- Use paralysis on dangerous foes
- Feast mid-combat if possible
}}

\page

{{monster,frame,wide
## TERRITORIAL DRAKE
*Large dragon, unaligned*
___
**Armor Class** :: 14 (natural armor)
**Hit Points** :: 52 (7d10 + 14)
**Speed** :: 30 ft., climb 30 ft.![territorial drake](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-territorial-drake.jpg) {width:325px,mix-blend-mode:multiply}
___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|16 (+3) | 11 (+0) | 14 (+2) | 4 (-3) | 10 (+0) | 7 (-2)|
___
**Skills** Perception +2, Stealth +2
**Senses** darkvision 60 ft., passive Perception 12
**Languages** understands Draconic but can't speak
**Challenge** 2 (450 XP)
___
**Border Camouflage.** The drake has advantage on Dexterity (Stealth) checks in rocky or ruined terrain.

**Pack Tactics.** The drake has advantage on attack rolls against a creature if at least one of the drake's allies is within 5 feet of the creature and the ally isn't incapacitated.

___
### ACTIONS
**Multiattack.** The drake makes one bite attack and one tail attack.

**Bite.** *Melee Weapon Attack:* +5 to hit, reach 5 ft., one target. *Hit:* 7 (1d8 + 3) piercing damage.

**Tail.** *Melee Weapon Attack:* +5 to hit, reach 5 ft., one target. *Hit:* 6 (1d6 + 3) bludgeoning damage, and the target must succeed on a DC 13 Strength saving throw or be knocked prone.

**Warning Roar (Recharge 5-6).** The drake roars, alerting other drakes in a 1-mile radius. Allied drakes within 60 feet gain advantage on their next attack roll.

### LORE
These drakes have claimed territories in the Border's ruins and caves. They're aggressive toward intruders but intelligent enough to recognize when they're outmatched. Some mercenary bands have trained them as mounts or guards.
### TACTICS
- Ambush from high ground
- Work in pairs if possible
- Use tail to knock down enemies
- Flee to lair if seriously wounded
}}

\page

{{monster,frame,wide
## WAR BEAST
*Large beast, unaligned*
___
**Armor Class** :: 14 (natural armor)
**Hit Points** :: 45 (6d10 + 12)
**Speed** :: 50 ft.![war beast](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-war-beast.jpg) {width:325px,mix-blend-mode:multiply}
___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|17 (+3) | 15 (+2) | 15 (+2) | 3 (-4) | 12 (+1) | 7 (-2)|
___
**Skills** Perception +3, Stealth +4
**Senses** passive Perception 13
**Languages** —
**Challenge** 3 (700 XP)
___
**Keen Hearing and Smell.** The beast has advantage on Wisdom (Perception) checks that rely on hearing or smell.

**Pack Tactics.** The beast has advantage on attack rolls against a creature if at least one of the beast's allies is within 5 feet of the creature and the ally isn't incapacitated.

**Trained Killer.** The beast was trained for war. It has advantage on attack rolls against frightened creatures.

___
### ACTIONS
**Bite.** *Melee Weapon Attack:* +5 to hit, reach 5 ft., one target. *Hit:* 10 (2d6 + 3) piercing damage. If the target is a creature, it must succeed on a DC 13 Strength saving throw or be knocked prone.

**Pounce.** If the beast moves at least 20 feet straight toward a creature and then hits it with a bite attack on the same turn, that target must succeed on a DC 13 Strength saving throw or be knocked prone. If the target is prone, the beast can make one bite attack against it as a bonus action.

**Intimidating Howl (Recharge 5-6).** The beast howls. Each enemy within 30 feet that can hear it must succeed on a DC 11 Wisdom saving throw or become frightened for 1 minute. A frightened creature can repeat the save at the end of each of its turns, ending the effect on a success.

### LORE
Both armies use war beasts—massive wolves, war dogs, or other predators bred and trained for combat. Some have escaped and gone feral in the Border, becoming apex predators.
### TACTICS
- Hunt in packs (2-5 beasts)
- Use Pounce to knock down targets
- Focus on frightened enemies
- Protect handlers if trained
}}

\page

{{monster,frame,wide
## HAUNTED BATTLEFIELD
*Gargantuan hazard/swarm, chaotic neutral*
___
**Armor Class** :: 15
**Hit Points** :: 150 (12d20 + 24)
**Speed** :: 0 ft.![haunted battlefield](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-haunted-battlefield.jpg) {width:325px,mix-blend-mode:multiply}
___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|1 (-5) | 20 (+5) | 14 (+2) | 10 (+0) | 14 (+2) | 16 (+3)|
___
**Senses** blindsight 120 ft., passive Perception 12
**Languages** understands all languages but can't speak
**Challenge** 7 (2,900 XP)
___
**Immobile Hazard.** The battlefield doesn't move. It exists as a 120-foot radius area of lingering death magic and tortured spirits.

**Echo of Battle.** Any creature that enters the area for the first time on a turn or starts its turn there must make a DC 15 Wisdom saving throw or take 14 (4d6) psychic damage and have disadvantage on attack rolls until the start of its next turn as ghostly weapons strike and spectral screams assault it.

**Restless Dead.** At the start of each round, 1d4 spectral soldiers (use specter statblock) manifest within the area. They attack the nearest living creatures and disappear after 1 minute or when reduced to 0 hit points.

**Consecration Vulnerable.** If a cleric or paladin spends 10 minutes performing funeral rites within the area, the battlefield's power is suppressed for 24 hours in a 30-foot radius around the ritual site.

___
### ACTIONS
**Phantom Army (Recharge 5-6).** At initiative count 20, the battlefield can summon a phantom army. All creatures in the area see ghostly soldiers fighting and dying around them. Each creature must make a DC 15 Wisdom saving throw. On a failure, a creature takes 22 (4d10) psychic damage and is frightened until the end of its next turn. On a success, the creature takes half damage and isn't frightened.

### LORE
Some battlefields in the Border have seen so much death that the land itself became haunted. These cursed areas trap the spirits of fallen soldiers, endlessly reenacting their final battle. The only way to permanently end a haunted battlefield is to consecrate it with proper funeral rites—a dangerous undertaking.
### TACTICS
- Describe the horror and chaos
- Track who enters the area
- Roll for spectral spawns
- Allow creative solutions (not just combat)
}}

\page
# Chapter 2
# Thaldros Military

The iron fist of the Thaldros Empire—disciplined soldiers, ruthless inquisitors, and devastating war machines that enforce the Emperor's will.

:::::::::::::

{{monster,frame,wide
## THALDROS CONSCRIPT
*Medium humanoid (any race), lawful neutral*
___
**Armor Class** :: 10 (no armor)
**Hit Points** :: 4 (1d8)
**Speed** :: 30 ft.![thaldros conscript](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-thaldros-conscript.jpg) {width:325px,mix-blend-mode:multiply}
___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|10 (+0) | 10 (+0) | 10 (+0) | 9 (-1) | 10 (+0) | 9 (-1)|
___
**Senses** passive Perception 10
**Languages** Common
**Challenge** 1/8 (25 XP)
___
**Poorly Trained.** The conscript has disadvantage on attack rolls if an ally within 5 feet is reduced to 0 hit points since the end of the conscript's last turn.

**Reluctant Fighter.** The conscript has disadvantage on death saving throws.

___
### ACTIONS
**Spear.** *Melee or Ranged Weapon Attack:* +2 to hit, reach 5 ft. or range 20/60 ft., one target. *Hit:* 3 (1d6) piercing damage, or 4 (1d8) piercing damage if used with two hands for a melee attack.

### LORE
Most of Thaldros's army consists of conscripted farmers, laborers, and urban poor. They're given minimal training and thrown into battle. Many desert if given the chance. Conscripts often have families back home they're fighting to return to.
### TACTICS
- Fight in large groups (5-20)
- Flee if leaders fall
- May surrender if treated well
- Protect each other (poorly)
}}

\page

{{monster,frame,wide
## THALDROS SOLDIER
*Medium humanoid (any race), lawful neutral*
___
**Armor Class** :: 16 (chain shirt, shield)
**Hit Points** :: 11 (2d8 + 2)
**Speed** :: 30 ft.![thaldros soldier](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-thaldros-soldier.jpg) {width:325px,mix-blend-mode:multiply}
___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|13 (+1) | 12 (+1) | 12 (+1) | 10 (+0) | 11 (+0) | 10 (+0)|
___
**Skills** Athletics +3, Perception +2
**Senses** passive Perception 12
**Languages** Common
**Challenge** 1/2 (100 XP)
___
**Formation Fighter.** The soldier has advantage on saving throws against being frightened while within 5 feet of an ally.

**Imperial Discipline.** The soldier can reroll a failed saving throw once per short rest.

___
### ACTIONS
**Longsword.** *Melee Weapon Attack:* +3 to hit, reach 5 ft., one target. *Hit:* 5 (1d8 + 1) slashing damage, or 6 (1d10 + 1) slashing damage if used with two hands.

**Crossbow.** *Ranged Weapon Attack:* +3 to hit, range 80/320 ft., one target. *Hit:* 5 (1d8 + 1) piercing damage.

### REACTIONS
**Shield Wall.** When an ally within 5 feet is hit by an attack, the soldier can grant them +2 to AC against that attack.

### LORE
Professional soldiers of Thaldros are disciplined, well-equipped, and indoctrinated into loyalty to the empire. Unlike conscripts, they're career soldiers who believe in Thaldros's vision of order and stability.
### TACTICS
- Fight in formation (shield wall)
- Support allies
- Follow orders strictly
- Retreat only when commanded
}}

\page

{{monster,frame,wide
## IRON LEGION ENFORCER
*Medium humanoid (any race), lawful evil*
___
**Armor Class** :: 13 (leather armor)
**Hit Points** :: 32 (5d8 + 10)
**Speed** :: 30 ft.![iron legion enforcer](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-iron-legion-enforcer.jpg) {width:325px,mix-blend-mode:multiply}
___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|15 (+2) | 11 (+0) | 14 (+2) | 10 (+0) | 12 (+1) | 14 (+2)|
___
**Skills** Intimidation +4, Perception +3
**Senses** passive Perception 13
**Languages** Common
**Challenge** 2 (450 XP)
___
**Brutal.** The enforcer's melee weapon attacks deal one extra die of damage (included in the attacks).

**Pack Tactics.** The enforcer has advantage on attack rolls against a creature if at least one of the enforcer's allies is within 5 feet of the creature and the ally isn't incapacitated.

___
### ACTIONS
**Multiattack.** The enforcer makes two attacks with its mace.

**Mace.** *Melee Weapon Attack:* +4 to hit, reach 5 ft., one target. *Hit:* 9 (2d6 + 2) bludgeoning damage.

**Intimidate.** The enforcer targets one creature it can see within 30 feet. The target must succeed on a DC 12 Wisdom saving throw or become frightened for 1 minute. A frightened target can repeat the save at the end of each of its turns, ending the effect on a success.

### LORE
The Iron Legion are Thaldros's internal security force—brutal enforcers who maintain order through fear and violence. They're called when the regular army isn't cruel enough. Hated by commoners and feared even by soldiers.
### TACTICS
- Use intimidation liberally
- Beat down resisters
- Work in pairs or groups
- Make examples of defiers
}}

\page

{{monster,frame,wide
## ROYAL GUARD ELITE
*Medium humanoid (any race), lawful neutral*
___
**Armor Class** :: 18 (plate armor)
**Hit Points** :: 52 (8d8 + 16)
**Speed** :: 30 ft.![royal guard elite](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-royal-guard-elite.jpg) {width:325px,mix-blend-mode:multiply}
___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|16 (+3) | 11 (+0) | 14 (+2) | 11 (+0) | 11 (+0) | 15 (+2)|
___
**Saving Throws** Constitution +4, Wisdom +2
**Skills** Athletics +5, Intimidation +4, Perception +2
**Senses** passive Perception 12
**Languages** Common
**Challenge** 5 (1,800 XP)
___
**Brave.** The guard has advantage on saving throws against being frightened.

**Royal Authority.** Allied creatures within 10 feet gain advantage on saving throws against being frightened.

___
### ACTIONS
**Multiattack.** The guard makes two greatsword attacks.

**Greatsword.** *Melee Weapon Attack:* +5 to hit, reach 5 ft., one target. *Hit:* 10 (2d6 + 3) slashing damage.

**Heavy Crossbow.** *Ranged Weapon Attack:* +2 to hit, range 100/400 ft., one target. *Hit:* 5 (1d10) piercing damage.

**Leadership (Recharges after a Short or Long Rest).** For 1 minute, the guard can utter a command or warning whenever a nonhostile creature within 30 feet makes an attack roll or saving throw. That creature can add a d4 to its roll. A creature can benefit from only one Leadership die at a time.

### REACTIONS
**Parry.** The guard adds 2 to their AC against one melee attack that would hit them.

### LORE
The Royal Guard are the elite soldiers of Thaldros, sworn to protect nobility and enforce the king's will. They're highly trained, well-equipped, and fanatically loyal. Unlike Iron Legion thugs, Royal Guards are respected even by their enemies.
### TACTICS
- Protect VIPs at all costs
- Use Leadership to buff allies
- Fight honorably but effectively
- Coordinate attacks
}}

\page

{{monster,frame,wide
## STATE INQUISITOR
*Medium humanoid (any race), lawful evil*
___
**Armor Class** :: 15 (studded leather)
**Hit Points** :: 78 (12d8 + 24)
**Speed** :: 30 ft.![state inquisitor](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-state-inquisitor.jpg) {width:325px,mix-blend-mode:multiply}
___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|11 (+0) | 16 (+3) | 14 (+2) | 16 (+3) | 14 (+2) | 16 (+3)|
___
**Saving Throws** Dexterity +6, Intelligence +6, Wisdom +5
**Skills** Deception +6, Insight +5, Investigation +9, Perception +5, Stealth +6
**Senses** passive Perception 15
**Languages** Common, plus three others
**Challenge** 6 (2,300 XP)
___
**Cunning Action.** On each turn, the inquisitor can use a bonus action to Dash, Disengage, or Hide.

**Evasion.** If the inquisitor is subjected to an effect that allows them to make a Dexterity saving throw to take only half damage, they take no damage on a success and half damage on a failure.

**Sneak Attack (1/Turn).** The inquisitor deals an extra 14 (4d6) damage when hitting with a weapon attack and has advantage on the attack roll, or when the target is within 5 feet of an ally.

**Information Network.** The inquisitor can spend 1 hour in a settlement to learn one piece of useful information about a specific person or event.

___
### ACTIONS
**Multiattack.** The inquisitor makes two shortsword attacks.

**Shortsword.** *Melee Weapon Attack:* +6 to hit, reach 5 ft., one target. *Hit:* 6 (1d6 + 3) piercing damage, plus poison (see Poisoned Blade).

**Hand Crossbow.** *Ranged Weapon Attack:* +6 to hit, range 30/120 ft., one target. *Hit:* 6 (1d6 + 3) piercing damage, plus poison (see Poisoned Blade).

**Poisoned Blade.** The inquisitor's weapon is coated in a special poison. The target must make a DC 14 Constitution saving throw, taking 10 (3d6) poison damage on a failed save, or half as much on a success.

**Interrogate (3/Day).** The inquisitor targets one creature within 30 feet that can hear them. The target must make a DC 14 Wisdom saving throw. On a failure, the target is compelled to answer one question truthfully. This is a magical compulsion effect.

### REACTIONS
**Uncanny Dodge.** When an attacker the inquisitor can see hits them with an attack, they can halve the attack's damage.

### LORE
State Inquisitors are Thaldros's secret police—spies, assassins, and interrogators who root out dissent and eliminate threats to the empire. They're feared throughout Tirvandor and operate with complete authority.
### TACTICS
- Gather intelligence first
- Poisoned weapons on priority targets
- Use Interrogate to extract info
- Escape if discovered
}}

\page

{{monster,frame,wide
## WAR MAGE OF THALDROS
*Medium humanoid (any race), lawful neutral*
___
**Armor Class** :: 12 (15 with *mage armor*)
**Hit Points** :: 66 (12d8 + 12)
**Speed** :: 30 ft.![war mage of thaldros](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-war-mage-of-thaldros.jpg) {width:325px,mix-blend-mode:multiply}
___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|9 (-1) | 14 (+2) | 12 (+1) | 17 (+3) | 12 (+1) | 11 (+0)|
___
**Saving Throws** Intelligence +6, Wisdom +4
**Skills** Arcana +6, History +6
**Senses** passive Perception 11
**Languages** Common, plus three others
**Challenge** 7 (2,900 XP)
___
**Spellcasting.** The mage is a 9th-level spellcaster. Spellcasting ability is Intelligence (spell save DC 14, +6 to hit with spell attacks). The mage has the following wizard spells prepared:

**War Caster.** The mage has advantage on Constitution saving throws to maintain concentration on spells. When a hostile creature's movement provokes an opportunity attack, the mage can cast a spell at the creature rather than making an opportunity attack.

___
### ACTIONS
**Quarterstaff.** *Melee Weapon Attack:* +2 to hit, reach 5 ft., one target. *Hit:* 2 (1d6 - 1) bludgeoning damage, or 3 (1d8 - 1) if used with two hands.

### LORE
Thaldros trains battle mages specifically for military operations. Unlike academic wizards, War Mages focus on destructive evocation magic and battlefield control. They're attached to military units and respected (and feared) by soldiers.
### TACTICS
- Stay behind front line
- Use *fireball* and *lightning bolt* on groups
- *Counterspell* enemy magic
- *Misty step* away from danger
- Conserve 5th level slot for emergency
}}

\page

{{monster,frame,wide
## SIEGE GOLEM
*Large construct, unaligned*
___
**Armor Class** :: 17 (natural armor)
**Hit Points** :: 157 (15d10 + 75)
**Speed** :: 20 ft.![siege golem](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-siege-golem.jpg) {width:325px,mix-blend-mode:multiply}
___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|22 (+6) | 9 (-1) | 20 (+5) | 3 (-4) | 11 (+0) | 1 (-5)|
___
**Damage Immunities** poison, psychic; bludgeoning, piercing, and slashing from nonmagical attacks not made with adamantine weapons
**Condition Immunities** charmed, exhaustion, frightened, paralyzed, petrified, poisoned
**Senses** darkvision 120 ft., passive Perception 10
**Languages** understands the languages of its creator but can't speak
**Challenge** 8 (3,900 XP)
___
**Immutable Form.** The golem is immune to any spell or effect that would alter its form.

**Magic Resistance.** The golem has advantage on saving throws against spells and other magical effects.

**Siege Monster.** The golem deals double damage to objects and structures.

**Military Programming.** The golem follows tactical commands perfectly and can execute complex battle plans.

___
### ACTIONS
**Multiattack.** The golem makes two slam attacks.

**Slam.** *Melee Weapon Attack:* +10 to hit, reach 5 ft., one target. *Hit:* 19 (3d8 + 6) bludgeoning damage.

**Boulder Launch (Recharge 5-6).** *Ranged Weapon Attack:* +10 to hit, range 60/240 ft., one target. *Hit:* 32 (4d12 + 6) bludgeoning damage. If the target is a structure, it takes double damage.

**Siege Mode (1/Day).** For 1 minute, the golem becomes rooted in place (speed 0) but gains advantage on attack rolls and its attacks deal maximum damage to structures.

### LORE
Thaldros's military mages have created these massive constructs for sieges and large battles. They're slow but nearly unstoppable, designed to break through fortifications and scatter enemy formations.
### TACTICS
- Advance slowly and steadily
- Focus on structures in Siege Mode
- Target clustered enemies with Boulder Launch
- Ignore distractions
}}

\page

{{monster,frame,wide
## GENERAL'S CHAMPION
*Medium humanoid (any race), lawful neutral*
___
**Armor Class** :: 18 (plate armor)
**Hit Points** :: 143 (22d8 + 44)
**Speed** :: 30 ft.![general's champion](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-generals-champion.jpg) {width:325px,mix-blend-mode:multiply}
___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|20 (+5) | 15 (+2) | 14 (+2) | 10 (+0) | 14 (+2) | 12 (+1)|
___
**Saving Throws** Strength +9, Constitution +6
**Skills** Athletics +9, Intimidation +5, Perception +6
**Senses** passive Perception 16
**Languages** Common
**Challenge** 9 (5,000 XP)
___
**Indomitable (2/Day).** The champion can reroll a saving throw. They must use the new roll.

**Second Wind (Recharges after a Short or Long Rest).** As a bonus action, the champion can regain 20 hit points.

___
### ACTIONS
**Multiattack.** The champion makes three attacks with their greatsword or longbow.

**Greatsword.** *Melee Weapon Attack:* +9 to hit, reach 5 ft., one target. *Hit:* 12 (2d6 + 5) slashing damage.

**Longbow.** *Ranged Weapon Attack:* +6 to hit, range 150/600 ft., one target. *Hit:* 6 (1d8 + 2) piercing damage.

**Rally (Recharges after a Short or Long Rest).** The champion rallies their allies. Each ally within 30 feet regains 10 hit points and gains advantage on their next attack roll or saving throw.

### REACTIONS
**Parry.** The champion adds 4 to their AC against one melee attack that would hit them.

### LORE
Thaldros generals sometimes send their personal champions to deal with important threats or lead special missions. These warriors are the best of the best—veterans of countless battles, master tacticians, and nearly unbeatable in single combat.
### TACTICS
- Challenge the strongest enemy
- Use Rally to support troops
- Fight honorably but ruthlessly
- Never surrender
}}

\page

{{monster,frame,wide
## IRON CROWN KNIGHT
*Medium humanoid (any race), lawful evil*
___
**Armor Class** :: 20 (plate armor +2, shield)
**Hit Points** :: 153 (18d8 + 72)
**Speed** :: 30 ft.![iron crown knight](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-iron-crown-knight.jpg) {width:325px,mix-blend-mode:multiply}
___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|19 (+4) | 11 (+0) | 18 (+4) | 12 (+1) | 14 (+2) | 16 (+3)|
___
**Saving Throws** Constitution +8, Wisdom +6, Charisma +7
**Skills** Athletics +8, Intimidation +7, Religion +5
**Damage Resistances** necrotic
**Condition Immunities** frightened
**Senses** passive Perception 12
**Languages** Common
**Challenge** 10 (5,900 XP)
___
**Aura of Tyranny (10 ft.).** Allied creatures within 10 feet deal an extra 1d4 damage on weapon attacks. Enemy creatures have disadvantage on saving throws against being frightened.

**Iron Will.** The knight has advantage on saving throws against being charmed or frightened.

**Spellcasting.** The knight is a 12th-level spellcaster (Oath of the Iron Crown subclass). Spellcasting ability is Charisma (spell save DC 15, +7 to hit). Prepared spells:

___
### ACTIONS
**Multiattack.** The knight makes two longsword attacks.

**Longsword +2.** *Melee Weapon Attack:* +10 to hit, reach 5 ft., one target. *Hit:* 10 (1d8 + 6) slashing damage, or 11 (1d10 + 6) slashing damage if used with two hands.

**Channel Divinity: Iron Command (1/Day).** Each hostile creature within 30 feet must make a DC 15 Wisdom saving throw. On a failure, the creature is paralyzed until the end of the knight's next turn.

### REACTIONS
**Oath of Protection.** When a creature within 5 feet is hit by an attack, the knight can make that attack target them instead.

### LORE
The Iron Crown Knights are Thaldros's holy warriors, fanatically devoted to the concept of ordered civilization through strength. They're paladins who've sworn the Oath of the Iron Crown and serve as both warriors and enforcers of imperial law.
### TACTICS
- Use Aura of Tyranny to buff allies
- Command the battlefield
- Iron Command at start of combat
- Protect important allies
}}

\page

{{monster,frame,wide
## LORD COMMANDER VARIUS
*Medium humanoid (human), lawful neutral*
___
**Armor Class** :: 21 (plate armor +3, shield +1)
**Hit Points** :: 187 (22d8 + 88)
**Speed** :: 30 ft.![lord commander varius](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-lord-commander-varius-military-leader.jpg) {width:325px,mix-blend-mode:multiply}
___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|20 (+5) | 14 (+2) | 18 (+4) | 16 (+3) | 16 (+3) | 18 (+4)|
___
**Saving Throws** Strength +10, Constitution +9, Wisdom +8, Charisma +9
**Skills** Athletics +10, History +8, Insight +8, Intimidation +9, Perception +8
**Damage Resistances** all damage from spells
**Condition Immunities** frightened
**Senses** passive Perception 18
**Languages** Common, plus four others
**Challenge** 13 (10,000 XP)
___
**Legendary Resistance (3/Day).** If Varius fails a saving throw, he can choose to succeed instead.

**Supreme Commander.** Allied creatures within 60 feet have advantage on saving throws against being frightened and add 1d6 to damage rolls.

**Tactical Genius.** Varius can take a special reaction at initiative count 20 (losing ties) to command an ally within 60 feet to immediately take an action.

**Magic Resistance.** Varius has advantage on saving throws against spells and other magical effects.

___
### ACTIONS
**Multiattack.** Varius makes three longsword attacks.

**Longsword of Command +3.** *Melee Weapon Attack:* +13 to hit, reach 5 ft., one target. *Hit:* 12 (1d8 + 8) slashing damage, or 13 (1d10 + 8) slashing damage if used with two hands, plus 9 (2d8) radiant damage.

**Javelin of Lightning +2.** *Ranged Weapon Attack:* +9 to hit, range 30/120 ft., one target. *Hit:* 7 (1d6 + 4) piercing damage plus 9 (2d8) lightning damage.

**Commanding Shout (Recharge 5-6).** Varius issues a tactical command. Each ally within 60 feet can immediately move up to half their speed and make one weapon attack as a reaction.

### LEGENDARY ACTIONS
**Move.** Varius moves up to half his speed.

**Attack.** Varius makes one longsword attack.

**Rally (Costs 2 Actions).** Each ally within 30 feet regains 15 hit points and gains advantage on their next attack roll.

**Tactical Reposition (Costs 3 Actions).** Varius and up to four allies within 60 feet can move up to their speed without provoking opportunity attacks.

### LORE
Lord Commander Varius is Thaldros's supreme military leader—a brilliant tactician, legendary warrior, and unshakeable loyalist. He's not evil, but he genuinely believes in Thaldros's vision of ordered civilization. Many soldiers would die for him, and even his enemies respect him.

In **Blood & Coin**, he may hire the party for missions or become an honorable foe.  
In **Shattered Oaths**, he's a major antagonist—the final military obstacle before the true villain.
### TACTICS
- Command the battlefield
- Use Tactical Genius and Legendary Actions to control action economy
- Rally troops when needed
- Lead from the front but strategically
- Respect worthy opponents
}}

\page
# Chapter 3
# Aethoria & Iron Guild

Freedom fighters struggling against tyranny and professional mercenaries who serve only coin.
\column
## Aethoria Resistance

Brave souls fighting for liberation from Thaldros rule.
::::::

{{monster,frame,wide
## AETHORIAN MILITIA
*Medium humanoid, any alignment*
___
**Armor Class** :: 12 (leather armor)
**Hit Points** :: 9 (2d8)
**Speed** :: 30 ft.![aethorian militia](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-aethorian-militia.jpg) {width:325px,mix-blend-mode:multiply}
___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|11 (+0) | 14 (+2) | 10 (+0) | 10 (+0) | 12 (+1) | 11 (+0)|
___
**Skills** Stealth +4, Survival +3
**Languages** Common
**Challenge** 1/4 (50 XP)
___
**Guerrilla Fighter.** Advantage on attacks when hidden or unseen by target.

___
### ACTIONS
**Spear.** *Melee Weapon Attack:* +4 to hit, reach 5 ft., one target. *Hit:* 1d6+2 piercing damage

**Sling.** *Ranged Weapon Attack:* +4 to hit, range 30/120 ft., one target. *Hit:* 1d4+2 bludgeoning damage

### LORE
Untrained civilians who took up arms. Brave but inexperienced.
}}

\page

{{monster,frame,wide
## RESISTANCE FIGHTER
*Medium humanoid, any good alignment*
___
**Armor Class** :: 14 (leather armor)
**Hit Points** :: 16 (3d8 + 3)
**Speed** :: 30 ft.![resistance fighter](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-resistance-fighter.jpg) {width:325px,mix-blend-mode:multiply}
___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|12 (+1) | 15 (+2) | 12 (+1) | 11 (+0) | 13 (+1) | 12 (+1)|
___
**Skills** Stealth +4, Survival +3
**Languages** Common
**Challenge** 1 (200 XP)
___
**Freedom's Fury.** Extra 1d6 damage against Thaldros forces.

___
### ACTIONS
**Shortsword.** *Melee Weapon Attack:* +4 to hit, reach 5 ft., one target. *Hit:* 1d6+2 piercing damage

**Shortbow.** *Ranged Weapon Attack:* +4 to hit, range 80/320 ft., one target. *Hit:* 1d6+2 piercing damage

**Inspiring Cry (Recharge 5-6).** Allies within 30 ft gain advantage on next attack.

### LORE
More experienced than militia. Fighting for families and freedom.
}}

\page

{{monster,frame,wide
## PEOPLE'S CHAMPION
*Medium humanoid, chaotic good*
___
**Armor Class** :: 16 (chainmail)
**Hit Points** :: 58 (9d8 + 18)
**Speed** :: 30 ft.![people's champion](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-peoples-champion.jpg) {width:325px,mix-blend-mode:multiply}
___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|16 (+3) | 13 (+1) | 14 (+2) | 10 (+0) | 12 (+1) | 15 (+2)|
___
**Saving Throws** Strength +5, Constitution +4
**Skills** Athletics +5, Persuasion +4
**Languages** Common
**Challenge** 3 (700 XP)
___
**Defender of the Weak.** Advantage on attacks against enemies threatening civilians.

___
### ACTIONS
**Multiattack.** Two longsword attacks.

**Longsword.** *Melee Weapon Attack:* +5 to hit, reach 5 ft., one target. *Hit:* 1d8+3 slashing damage

**Rally the People (1/Day).** All allies within 30 ft gain 10 temp HP and advantage on saves vs fear.

### LORE
Local heroes who stood up to tyranny. Inspirational leaders.
}}

\page

{{monster,frame,wide
## REVOLUTIONARY MAGE
*Medium humanoid, chaotic good*
___
**Armor Class** :: 12 (15 with *mage armor*)
**Hit Points** :: 49 (11d8)
**Speed** :: 30 ft.![revolutionary mage](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-revolutionary-mage.jpg) {width:325px,mix-blend-mode:multiply}
___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|9 (-1) | 14 (+2) | 11 (+0) | 17 (+3) | 12 (+1) | 11 (+0)|
___
**Saving Throws** Intelligence +6, Wisdom +4
**Skills** Arcana +6, History +6
**Languages** Common +2 others
**Challenge** 5 (1,800 XP)
___
### LORE
Aethorian mages who use magic to free the oppressed.
}}

\page

{{monster,frame,wide
## CHAIN BREAKER MONK
*Medium humanoid, lawful good*
___
**Armor Class** :: 17
**Hit Points** :: 91 (14d8 + 28)
**Speed** :: 50 ft.![chain breaker monk](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-chain-breaker-monk.jpg) {width:325px,mix-blend-mode:multiply}
___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|11 (+0) | 18 (+4) | 14 (+2) | 13 (+1) | 17 (+3) | 12 (+1)|
___
**Saving Throws** Strength +3, Dexterity +7
**Skills** Acrobatics +7, Stealth +7
**Languages** Common
**Challenge** 6 (2,300 XP)
___
**Unarmored Defense.** AC = 10 + Dexterity + Wisdom

**Unarmored Movement.** +20 ft speed

**Ki (11 points).** Regain on short rest.

___
### ACTIONS
**Multiattack.** Four unarmed strikes.

**Unarmed Strike.** *Melee Weapon Attack:* +7 to hit, reach 5 ft., one target. *Hit:* 1d8+4 bludgeoning damage

**Shatter Bonds (3 ki).** Automatically break all restraints on touched creature. Can use on self.

**Stunning Strike (1 ki).** DC 15 Constitution save or stunned until end of your next turn.

### LORE
Former slaves who mastered martial arts. Dedicated to freeing others.
}}

\page

{{monster,frame,wide
## GUERRILLA COMMANDER
*Medium humanoid, chaotic good*
___
**Armor Class** :: 16 (studded leather +1)
**Hit Points** :: 117 (18d8 + 36)
**Speed** :: 30 ft.![guerrilla commander](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-guerrilla-commander.jpg) {width:325px,mix-blend-mode:multiply}
___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|14 (+2) | 18 (+4) | 14 (+2) | 15 (+2) | 16 (+3) | 17 (+3)|
___
**Saving Throws** Dexterity +7, Wisdom +6
**Skills** Stealth +10, Survival +6, Persuasion +6
**Languages** Common +2 others
**Challenge** 7 (2,900 XP)
___
**Tactical Mind.** Allies within 60 ft add +2 to initiative.

**Sneak Attack (1/turn).** +4d6 damage with advantage.

___
### ACTIONS
**Multiattack.** Three shortsword or shortbow attacks.

**Shortsword +2.** *Melee Weapon Attack:* +9 to hit, reach 5 ft., one target. *Hit:* 1d6+6 piercing damage

**Strategic Command (Recharge 5-6).** All allies within 60 ft can move half speed and make one attack as reaction.

### LORE
Brilliant guerrilla leader. Master of ambush and hit-and-run tactics.
}}

\page

{{monster,frame,wide
## THE LIBERATOR
*Medium humanoid, chaotic good*
___
**Armor Class** :: 19 (studded leather +3)
**Hit Points** :: 178 (21d8 + 84)
**Speed** :: 40 ft.![the liberator](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-the-liberator.jpg) {width:325px,mix-blend-mode:multiply}
___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|16 (+3) | 20 (+5) | 18 (+4) | 14 (+2) | 16 (+3) | 20 (+5)|
___
**Saving Throws** Dexterity +10, Wisdom +8, Charisma +10
**Skills** All +9 or higher
**Languages** All common
**Challenge** 11 (7,200 XP)
___
**Legendary Resistance (2/Day).** Can choose to succeed on failed save.

**Aura of Freedom (30 ft).** Allies have advantage vs charmed/frightened.

**Sneak Attack (1/turn).** +6d6 damage

___
### ACTIONS
**Multiattack.** Four rapier attacks.

**Freedom's Blade +3.** *Melee Weapon Attack:* +12 to hit, reach 5 ft., one target. *Hit:* 1d8+8 piercing damage + 2d8 radiant damage

**Break All Chains (1/Day).** All restraints/prisons within 60 ft shatter. All allies gain 30 temp HP.

**Move.** Half speed

**Attack.** One rapier attack

**Inspire (2 actions).** One ally makes attack or spell as reaction

### LORE
Legendary resistance leader. Symbol of hope for all oppressed people.
}}

\page

{{monster,frame,wide
## PROPHESIED HERO
*Medium humanoid, any good*
___
**Armor Class** :: 20 (plate +1, shield +1)
**Hit Points** :: 210 (20d8 + 120)
**Speed** :: 30 ft.![prophesied hero](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-prophesied-hero.jpg) {width:325px,mix-blend-mode:multiply}
___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|20 (+5) | 14 (+2) | 22 (+6) | 12 (+1) | 18 (+4) | 20 (+5)|
___
**Saving Throws** Strength +10, Constitution +11, Wisdom +9, Charisma +10 | **Condition Immunities** frightened
**Languages** Common +3 others
**Challenge** 12 (8,400 XP)
___
**Destiny's Chosen.** Advantage on all saves. Crits on 19-20.

**Aura of Destiny (30 ft).** Allies add +3 to all saves.

___
### ACTIONS
**Multiattack.** Three longsword attacks.

**Destiny's Blade +2.** *Melee Weapon Attack:* +12 to hit, reach 5 ft., one target. *Hit:* 1d8+7 slashing damage + 3d8 radiant damage

**Channel Divinity: Smite the Tyrant (3/Day).** Next attack deals +50 radiant damage vs evil targets.

### LORE
One of "the Seven" from prophecy. Destined hero.
}}

\page

## Iron Guild Mercenaries

Professional soldiers for hire—loyal only to the contract.
::::::

{{monster,frame,wide
## GUILD RECRUIT
*Medium humanoid, any*
___
**Armor Class** :: 14 (leather, shield)
**Hit Points** :: 16 (3d8 + 3)
**Speed** :: 30 ft.![guild recruit](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-guild-recruit.jpg) {width:325px,mix-blend-mode:multiply}
___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|13 (+1) | 12 (+1) | 12 (+1) | 10 (+0) | 11 (+0) | 10 (+0)|
___
**Skills** Athletics +3
**Languages** Common
**Challenge** 1/2 (100 XP)
___
**Professional Training.** Advantage on saves vs fear while within 10 ft of ally.

___
### ACTIONS
**Longsword.** *Melee Weapon Attack:* +3 to hit, reach 5 ft., one target. *Hit:* 1d8+1 slashing damage

**Crossbow.** *Ranged Weapon Attack:* +3 to hit, range 80/320 ft., one target. *Hit:* 1d8+1 piercing damage

### LORE
New mercenaries learning the trade. Disciplined and eager to prove themselves.
}}

\page

{{monster,frame,wide
## VETERAN MERCENARY
*Medium humanoid, any*
___
**Armor Class** :: 16 (chain shirt, shield)
**Hit Points** :: 45 (7d8 + 14)
**Speed** :: 30 ft.![veteran mercenary](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-veteran-mercenary.jpg) {width:325px,mix-blend-mode:multiply}
___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|15 (+2) | 13 (+1) | 14 (+2) | 11 (+0) | 12 (+1) | 11 (+0)|
___
**Skills** Athletics +4, Survival +3
**Languages** Common
**Challenge** 2 (450 XP)
___
**Combat Veteran.** Advantage on saves vs poison and disease.

___
### ACTIONS
**Multiattack.** Two longsword attacks.

**Longsword.** *Melee Weapon Attack:* +4 to hit, reach 5 ft., one target. *Hit:* 1d8+2 slashing damage

**Tactical Retreat.** Disengage as bonus action.

### LORE
Experienced fighters who've survived many contracts.
}}

\page

{{monster,frame,wide
## GUILD ENFORCER
*Medium humanoid, any*
___
**Armor Class** :: 17 (half plate)
**Hit Points** :: 68 (8d8 + 32)
**Speed** :: 30 ft.![guild enforcer](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-guild-enforcer.jpg) {width:325px,mix-blend-mode:multiply}
___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|17 (+3) | 14 (+2) | 18 (+4) | 11 (+0) | 13 (+1) | 12 (+1)|
___
**Skills** Athletics +5, Intimidation +3 | **Languages** Common
**Languages** Common
**Challenge** 4 (1,100 XP)
___
**Guild Authority.** Can call for backup (1d4 recruits arrive in 1d4 rounds).

___
### ACTIONS
**Multiattack.** Two greatsword attacks.

**Greatsword.** *Melee Weapon Attack:* +5 to hit, reach 5 ft., one target. *Hit:* 2d6+3 slashing damage

**Intimidating Presence (Recharge 5-6).** DC 13 Wisdom save or frightened 1 min.

### LORE
Enforce Guild rules and handle troublemakers.
}}

\page

{{monster,frame,wide
## CONTRACT KILLER
*Medium humanoid, any*
___
**Armor Class** :: 15 (studded leather)
**Hit Points** :: 78 (12d8 + 24)
**Speed** :: 30 ft.![contract killer](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-contract-killer.jpg) {width:325px,mix-blend-mode:multiply}
___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|11 (+0) | 16 (+3) | 14 (+2) | 13 (+1) | 11 (+0) | 10 (+0)|
___
**Saving Throws** Dexterity +6
**Skills** Stealth +9, Perception +3
**Languages** Common, Thieves' Cant
**Challenge** 5 (1,800 XP)
___
**Assassinate.** Advantage vs creatures that haven't acted. Crits on surprise hits.

**Sneak Attack (1/turn).** +3d6 damage with advantage.

___
### ACTIONS
**Multiattack.** Two shortsword attacks.

**Shortsword.** *Melee Weapon Attack:* +6 to hit, reach 5 ft., one target. *Hit:* 1d6+3 piercing damage

**Poisoned Dart.** *Ranged Weapon Attack:* +6 to hit, range 20/60 ft., one target. *Hit:* 1d4+3 piercing damage + DC 14 Constitution save or 3d6 poison damage

### LORE
Guild assassins for special contracts. Professional and ruthless.
}}

\page

{{monster,frame,wide
## IRON GUILD CAPTAIN
*Medium humanoid, any*
___
**Armor Class** :: 18 (plate)
**Hit Points** :: 135 (18d8 + 54)
**Speed** :: 30 ft.![iron guild captain](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-iron-guild-captain.jpg) {width:325px,mix-blend-mode:multiply}
___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|18 (+4) | 12 (+1) | 16 (+3) | 14 (+2) | 15 (+2) | 16 (+3)|
___
**Saving Throws** Strength +7, Constitution +6, Wisdom +5
**Skills** Athletics +7, Persuasion +6
**Languages** Common +2 others
**Challenge** 7 (2,900 XP)
___
**Tactical Leader.** Allies within 30 ft add +2 to attack rolls.

**Second Wind (1/Short Rest).** Bonus action to heal 20 HP.

___
### ACTIONS
**Multiattack.** Three longsword attacks.

**Longsword +1.** *Melee Weapon Attack:* +8 to hit, reach 5 ft., one target. *Hit:* 1d8+5 slashing damage

**Command Squad (Recharge 5-6).** All allies within 60 ft can attack as reaction.

### LORE
Lead mercenary squads. Respected tacticians and fighters.
}}

\page

{{monster,frame,wide
## GUILDMASTER'S ELITE
*Medium humanoid, any*
___
**Armor Class** :: 19 (plate +1)
**Hit Points** :: 165 (22d8 + 66)
**Speed** :: 30 ft.![guildmaster's elite](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-guildmasters-elite.jpg) {width:325px,mix-blend-mode:multiply}
___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|20 (+5) | 14 (+2) | 16 (+3) | 12 (+1) | 14 (+2) | 15 (+2)|
___
**Saving Throws** Strength +9, Constitution +7
**Skills** Athletics +9, Intimidation +6
**Languages** Common +2 others
**Challenge** 9 (5,000 XP)
___
**Indomitable (2/Day).** Reroll failed save.

**Mercenary's Pride.** Advantage vs fear and charm.

___
### ACTIONS
**Multiattack.** Three greatsword attacks.

**Greatsword +2.** *Melee Weapon Attack:* +11 to hit, reach 5 ft., one target. *Hit:* 2d6+7 slashing damage

**Commanding Strike (Recharge 5-6).** One ally makes attack with advantage.

### LORE
The Guildmaster's personal guard. Legendary mercenaries.
}}

\page

{{monster,frame,wide
## GARRICK IRONHEART
*Medium humanoid (dwarf), lawful neutral*
___
**Armor Class** :: 20 (plate +2, shield +1)
**Hit Points** :: 195 (23d8 + 92)
**Speed** :: 25 ft.![garrick ironheart](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-garrick-ironheart-guildmaster.jpg) {width:325px,mix-blend-mode:multiply}
___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|20 (+5) | 12 (+1) | 18 (+4) | 16 (+3) | 16 (+3) | 18 (+4)|
___
**Saving Throws** All +7 or higher
**Skills** Insight +11, Persuasion +12
**Languages** Common, Dwarvish +3
**Challenge** 11 (7,200 XP)
___
**Legendary Resistance (2/Day).** Choose to succeed on failed save.

**Guildmaster's Authority.** All Iron Guild members within 60 ft gain +3 to all rolls.

___
### ACTIONS
**Multiattack.** Three warhammer attacks.

**Iron Will +3.** *Melee Weapon Attack:* +12 to hit, reach 5 ft., one target. *Hit:* 1d8+8 bludgeoning damage + 2d8 force damage

**Honor Duel (1/Day).** Challenge one creature. Both have advantage vs each other, disadvantage vs others. Lasts 1 min.

**Attack.** One warhammer attack

**Tactical Order (2 actions).** One ally acts immediately

**Iron Defense (2 actions).** +5 AC until next turn

### LORE
Founded Iron Guild. Legendary warrior and fair leader. Respected even by enemies.
}}
\page
# Chapter 4
# Ascended & Ancient

Divine champions blessed by the Seven Ascended, ancient guardians from ages past, and corrupted creatures twisted by dark magic.
\column
## Ascended-Touched

Champions blessed by the gods.
:::::
{{monster,frame,wide
## BLESSED PALADIN
*Medium humanoid, lawful good*
___
**Armor Class** :: 18 (plate)
**Hit Points** :: 52 (8d8 + 16)
**Speed** :: 30 ft.![blessed paladin](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-blessed-paladin.jpg) {width:325px,mix-blend-mode:multiply}
___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|16 (+3) | 11 (+0) | 14 (+2) | 11 (+0) | 14 (+2) | 16 (+3)|
___
**Saving Throws** Wisdom +4, Charisma +5
**Skills** Religion +2
**Senses** passive Perception 12
**Languages** Common
**Challenge** 4 (1,100 XP)
___
### ACTIONS
**Multiattack.** Two longsword attacks.

**Longsword.** *Melee Weapon Attack:* +5 to hit, reach 5 ft., one target. *Hit:* 1d8+3 slashing damage

**Divine Smite (3/Day).** Add 2d8 radiant to hit.

### LORE
Paladins blessed by the Seven Ascended. Champions of good.
}}

\page

{{monster,frame,wide
## THANDROS'S JUSTICAR
*Medium humanoid, lawful neutral*
___
**Armor Class** :: 17 (chain mail, shield)
**Hit Points** :: 91 (14d8 + 28)
**Speed** :: 30 ft.![thandros's justicar](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-thandross-justicar.jpg) {width:325px,mix-blend-mode:multiply}
___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|16 (+3) | 10 (+0) | 14 (+2) | 14 (+2) | 16 (+3) | 14 (+2)|
___
**Saving Throws** Wisdom +6, Charisma +5
**Skills** Insight +6, Persuasion +5
**Languages** Common
**Challenge** 6 (2,300 XP)
___
### ACTIONS
**Multiattack.** Two mace attacks.

**Mace of Justice.** *Melee Weapon Attack:* +6 to hit, reach 5 ft., one target. *Hit:* 1d6+3 bludgeoning damage + 2d8 radiant damage vs evil

**Gavel Strike (Recharge 5-6).** DC 14 Wisdom save or stunned 1 round (symbol of law striking).

### LORE
Chosen enforcers of Thandros, god of law. Hunt criminals and maintain order.
}}

\page

{{monster,frame,wide
## AETHOR'S LIBERATOR
*Medium celestial, chaotic good*
___
**Armor Class** :: 17 (natural)
**Hit Points** :: 136 (16d8 + 64)
**Speed** :: 30 ft., fly 90 ft.![aethor's liberator](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-aethors-liberator.jpg) {width:325px,mix-blend-mode:multiply}
___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|18 (+4) | 18 (+4) | 18 (+4) | 17 (+3) | 20 (+5) | 20 (+5)|
___
**Saving Throws** Wisdom +8, Charisma +8
**Skills** Insight +8, Perception +8
**Damage Resistances** radiant; bludgeoning, piercing, slashing from nonmagical
**Condition Immunities** charmed, frightened | **Senses** darkvision 120 ft.
**Senses** darkvision 120 ft.
**Languages** all, telepathy 120 ft.
**Challenge** 7 (2,900 XP)
___
### ACTIONS
**Multiattack.** Two mace attacks.

**Freedom's Mace.** *Melee Weapon Attack:* +7 to hit, reach 5 ft., one target. *Hit:* 1d6+4 bludgeoning damage + 4d8 radiant damage

**Break All Bonds.** All restrained/paralyzed creatures within 30 ft freed automatically.

**Change Shape.** Can polymorph into humanoid or Medium beast.

### LORE
Divine servants of Aethor sent to break chains and free the oppressed.
}}

\page

{{monster,frame,wide
## MOIRA'S SEER
*Medium humanoid, any*
___
**Armor Class** :: 12 (15 with *mage armor*)
**Hit Points** :: 60 (11d8 + 11)
**Speed** :: 30 ft.![moira's seer](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-moira-seer.jpg) {width:325px,mix-blend-mode:multiply}
___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|9 (-1) | 14 (+2) | 12 (+1) | 18 (+4) | 20 (+5) | 14 (+2)|
___
**Saving Throws** Intelligence +7, Wisdom +8
**Skills** Arcana +7, History +7, Insight +11
**Languages** Common +4 others
**Challenge** 5 (1,800 XP)
___
### ACTIONS
**Quarterstaff.** *Melee Weapon Attack:* +2 to hit, reach 5 ft., one target. *Hit:* 1d6-1 bludgeoning

**Prophetic Vision (Recharge 5-6).** One creature within 60 ft sees possible futures. DC 16 Wisdom save or incapacitated 1 round (overwhelmed by visions).

**Weaver's Warning (1/Day).** Grant one creature reroll on any d20 within next hour.

### LORE
Priests of Moira who see threads of fate. Cryptic but helpful.
}}

\page

{{monster,frame,wide
## SYLVARA'S WILD HUNTER
*Medium fey, chaotic neutral*
___
**Armor Class** :: 16 (natural)
**Hit Points** :: 127 (15d8 + 60)
**Speed** :: 40 ft.![sylvara's wild hunter](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-sylvaras-wild-hunter.jpg) {width:325px,mix-blend-mode:multiply}
___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|18 (+4) | 19 (+4) | 18 (+4) | 14 (+2) | 17 (+3) | 16 (+3)|
___
**Saving Throws** Dexterity +7, Wisdom +6
**Skills** Nature +5, Perception +9, Stealth +10
**Damage Resistances** lightning, thunder | **Senses** darkvision 120 ft.
**Senses** darkvision 120 ft.
**Languages** Sylvan, Common
**Challenge** 8 (3,900 XP)
___
### ACTIONS
**Multiattack.** Three longbow attacks or two spear attacks.

**Spear.** *Melee Weapon Attack:* +7 to hit, reach 5 ft., one target. *Hit:* 1d6+4 piercing damage + 2d6 lightning damage

**Storm Bow.** *Ranged Weapon Attack:* +7 to hit, range 150/600 ft., one target. *Hit:* 1d8+4 piercing damage + 2d6 lightning damage

**Call the Wild (Recharge 5-6).** Summon 2d4 wolves (arrive next round, last 1 hour).

**Lightning Leap.** Teleport up to 60 ft as bonus action, leaving lightning in space (5d6 lightning, DC 15 Dexterity).

### LORE
Sylvara's chosen hunters. Defend wilderness, punish those who harm nature.
}}

\page

{{monster,frame,wide
## SERA'S MERCY
*Small celestial, neutral good*
___
**Armor Class** :: 14
**Hit Points** :: 45 (10d6 + 10)
**Speed** :: 30 ft., fly 60 ft.![sera's mercy](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-seras-mercy.jpg) {width:325px,mix-blend-mode:multiply}
___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|10 (+0) | 18 (+4) | 12 (+1) | 14 (+2) | 18 (+4) | 16 (+3)|
___
**Skills** Medicine +8, Insight +6
**Damage Resistances** radiant
**Condition Immunities** charmed, frightened | **Senses** darkvision 60 ft.
**Senses** darkvision 60 ft.
**Languages** all, telepathy 60 ft.
**Challenge** 3 (700 XP)
___
### ACTIONS
**Touch of Mercy.** *Melee Weapon Attack:* +6 to hit, reach 5 ft., one target. *Hit:* target healed for 2d8+4 HP or takes 2d8+4 radiant (undead only).

**Shield of Compassion (3/Day).** Grant one creature within 60 ft resistance to all damage until end of its next turn.

**Peaceful Presence (Recharge 6).** All creatures within 30 ft make DC 14 Wisdom save or can't attack for 1 minute (charmed effect).

### LORE
Sera's divine messengers. Heal wounded and offer mercy to repentant.
}}

\page

{{monster,frame,wide
## MORDAIN'S SENTINEL
*Medium undead, lawful neutral*
___
**Armor Class** :: 20 (plate, shield)
**Hit Points** :: 180 (19d8 + 95)
**Speed** :: 30 ft.![mordain's sentinel](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-mordains-sentinel.jpg) {width:325px,mix-blend-mode:multiply}
___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|20 (+5) | 11 (+0) | 20 (+5) | 12 (+1) | 16 (+3) | 18 (+4)|
___
**Saving Throws** Strength +9, Constitution +9, Wisdom +7 | **Damage Immunities** necrotic, poison
**Damage Immunities** necrotic, poison
**Condition Immunities** exhaustion, frightened, poisoned | **Senses** darkvision 120 ft.
**Senses** darkvision 120 ft.
**Languages** Common
**Challenge** 10 (5,900 XP)
___
### ACTIONS
**Multiattack.** Three longsword attacks.

**Longsword of Vigil.** *Melee Weapon Attack:* +9 to hit, reach 5 ft., one target. *Hit:* 1d8+5 slashing damage + 3d8 necrotic damage

**Sentinel's Command (Recharge 5-6).** All undead within 60 ft gain +2 AC and advantage on attacks for 1 min.

**Honor the Fallen (1/Day).** All dead within 30 ft rise as shadows under sentinel's control for 1 hour.

### LORE
Mordain's chosen guardians. Protect sacred sites and honor the dead.
}}

\page

{{monster,frame,wide
## FALLEN CHAMPION
*Medium undead, any evil*
___
**Armor Class** :: 18 (plate)
**Hit Points** :: 135 (18d8 + 54)
**Speed** :: 30 ft.![fallen champion](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-fallen-champion.jpg) {width:325px,mix-blend-mode:multiply}
___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|18 (+4) | 12 (+1) | 16 (+3) | 11 (+0) | 12 (+1) | 14 (+2)|
___
**Saving Throws** Strength +8, Constitution +7 | **Damage Immunities** poison
**Damage Immunities** poison
**Condition Immunities** exhaustion, poisoned | **Senses** darkvision 60 ft.
**Senses** darkvision 60 ft.
**Languages** Common
**Challenge** 9 (5,000 XP)
___
### ACTIONS
**Multiattack.** Three greatsword attacks.

**Cursed Greatsword.** *Melee Weapon Attack:* +8 to hit, reach 5 ft., one target. *Hit:* 2d6+4 slashing damage + 2d8 necrotic damage

**Aura of Despair (Recharge 5-6).** All creatures within 30 ft make DC 15 Wisdom save or frightened 1 min. Frightened creatures have speed 0.

**Corrupted Smite (3/Day).** Add 4d8 necrotic to attack.

### LORE
Heroes who broke their oaths or fell to corruption. Tragic enemies.
}}

\page

## Ancient & Prophecy

Timeless guardians and prophetic beings.
::::::
{{monster,frame,wide
## ANCIENT GUARDIAN
*Large construct, neutral*
___
**Armor Class** :: 17 (natural)
**Hit Points** :: 178 (17d10 + 85)
**Speed** :: 20 ft.![ancient guardian](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-ancient-guardian.jpg) {width:325px,mix-blend-mode:multiply}
___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|22 (+6) | 9 (-1) | 20 (+5) | 10 (+0) | 11 (+0) | 1 (-5)|
___
**Damage Immunities** poison, psychic; nonmagical weapons
**Condition Immunities** charmed, exhaustion, frightened, paralyzed, petrified, poisoned
**Senses** darkvision 120 ft., truesight 30 ft.
**Languages** understands Ancient tongue
**Challenge** 8 (3,900 XP)
___
### ACTIONS
**Multiattack.** Two slam attacks.

**Slam.** *Melee Weapon Attack:* +9 to hit, reach 10 ft., one target. *Hit:* 3d8+6 bludgeoning damage

**Time Ripple (Recharge 5-6).** All creatures in 20 ft radius make DC 16 Wisdom save. Failed save: sent forward in time 1 round (miss turn, reappear in same space). Success: take 4d10 psychic damage.

### LORE
Ancient constructs guarding prophetic sites. Test those who seek knowledge.
}}

\page

{{monster,frame,wide
## PROPHECY KEEPER
*Medium aberration, lawful neutral*
___
**Armor Class** :: 15 (natural)
**Hit Points** :: 142 (15d8 + 75)
**Speed** :: 0 ft., fly 40 ft. (hover)![prophecy keeper](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-prophecy-keeper.jpg) {width:325px,mix-blend-mode:multiply}
___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|10 (+0) | 20 (+5) | 20 (+5) | 22 (+6) | 22 (+6) | 18 (+4)|
___
**Saving Throws** Intelligence +10, Wisdom +10, Charisma +8
**Skills** Arcana +14, History +14
**Damage Resistances** psychic | **Senses** truesight 120 ft., passive Perception 16
**Senses** truesight 120 ft., passive Perception 16
**Languages** all, telepathy 120 ft.
**Challenge** 10 (5,900 XP)
___
### ACTIONS
**Multiattack.** Three psychic lance attacks.

**Psychic Lance.** *Ranged Weapon Attack:* +10 to hit, range 120 ft., one target. *Hit:* 3d10+5 psychic damage

**Reveal Fate (Recharge 5-6).** Show one creature their destined future. DC 18 Wisdom save or stunned 1d4 rounds (overwhelming vision). On success, gain advantage on next d20 roll.

**Alter Memory (3/Day).** As *modify memory* spell.

### LORE
Cosmic entities who record prophecies. Neutral—they just observe and remember.
}}

\page

{{monster,frame,wide
## FORGOTTEN KING
*Medium undead, neutral evil*
___
**Armor Class** :: 17 (natural)
**Hit Points** :: 135 (18d8 + 54)
**Speed** :: 30 ft.![forgotten king](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-forgotten-king.jpg) {width:325px,mix-blend-mode:multiply}
___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|11 (+0) | 16 (+3) | 16 (+3) | 20 (+5) | 14 (+2) | 16 (+3)|
___
**Saving Throws** Constitution +9, Intelligence +11, Wisdom +8
**Skills** Arcana +17, History +17
**Damage Resistances** cold, lightning, necrotic
**Damage Immunities** poison; nonmagical weapons
**Condition Immunities** charmed, exhaustion, frightened, paralyzed, poisoned
**Senses** truesight 120 ft.
**Languages** Common +10 others
**Challenge** 15 (13,000 XP)
___
### ACTIONS
**Touch of Death.** *Melee Weapon Attack:* +8 to hit, reach 5 ft., one target. *Hit:* 3d6 cold damage + 3d6 necrotic damage. DC 17 Constitution save or paralyzed 1 min.

**Crown of Forgotten Kings (Recharge 5-6).** All creatures within 60 ft make DC 19 Wisdom save or forget their purpose (confusion effect) for 1 min.

**Cantrip.** Cast a cantrip

**Move.** Fly up to half speed

**Cast Spell (2 actions).** Cast spell of 1st-3rd level

**Summon Undead (3 actions).** 1d6 wraiths appear

### LORE
Ancient king whose dynasty fell. Part of the original "Seven" who failed. His throne is prophesied to be reclaimed.
}}

\page

{{monster,frame,wide
## HERALD OF THE SEVEN
*Large celestial, lawful good*
___
**Armor Class** :: 19 (natural)
**Hit Points** :: 200 (16d10 + 112)
**Speed** :: 40 ft., fly 120 ft.![herald of the seven](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-herald-of-the-seven.jpg) {width:325px,mix-blend-mode:multiply}
___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|24 (+7) | 20 (+5) | 24 (+7) | 19 (+4) | 22 (+6) | 25 (+7)|
___
**Saving Throws** Constitution +12, Wisdom +11, Charisma +12
**Skills** Insight +11, Perception +11
**Damage Resistances** radiant; nonmagical weapons
**Condition Immunities** charmed, exhaustion, frightened | **Senses** truesight 120 ft.
**Senses** truesight 120 ft.
**Languages** all, telepathy 120 ft.
**Challenge** 12 (8,400 XP)
___
### ACTIONS
**Multiattack.** Two greatsword attacks.

**Greatsword of the Seven.** *Melee Weapon Attack:* +12 to hit, reach 5 ft., one target. *Hit:* 4d6+7 slashing damage + 5d8 radiant damage

**Ascended's Command (Recharge 5-6).** Issue divine command. All creatures within 60 ft must obey one-word command (as *command* spell) if they fail DC 20 Wisdom save.

**Healing Touch (4/Day).** Touch heals 6d8+7 HP and removes all conditions.

### LORE
Direct messenger of the Seven Ascended. Appears during pivotal moments.
}}

\page

## Corrupted & Cursed

Twisted by war and dark magic.

::::

{{monster,frame,wide
## CORRUPTION SPAWN
*Small aberration, chaotic evil*
___
**Armor Class** :: 9
**Hit Points** :: 67 (9d6 + 36)
**Speed** :: 10 ft., swim 10 ft.![corruption spawn](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-corruption-spawn.jpg) {width:325px,mix-blend-mode:multiply}
___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|10 (+0) | 8 (-1) | 18 (+4) | 3 (-4) | 10 (+0) | 6 (-2)|
___
**Condition Immunities** prone | **Senses** darkvision 60 ft.
**Senses** darkvision 60 ft.
**Languages** —
**Challenge** 4 (1,100 XP)
___
### ACTIONS
**Multiattack.** One bite, one spitting attack.

**Bites.** *Melee Weapon Attack:* +2 to hit, reach 5 ft., one target. *Hit:* 5d6 piercing damage

**Spit Corruption.** *Ranged Weapon Attack:* +2 to hit, range 15/30 ft., one target. *Hit:* 3d6 acid damage

**Blinding Spittle (Recharge 5-6).** Spit at point within 15 ft. 5-ft radius, DC 13 Dexterity save or blinded 1 min.

### LORE
Spawn of war magic gone wrong. Corrupted by dark energies. Mindless and hungry.
}}

\page

{{monster,frame,wide
## WAR-TWISTED SOLDIER
*Medium undead, neutral evil*
___
**Armor Class** :: 14 (armor scraps)
**Hit Points** :: 97 (13d8 + 39)
**Speed** :: 30 ft.![war-twisted soldier](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-war-twisted-soldier.jpg) {width:325px,mix-blend-mode:multiply}
___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|18 (+4) | 14 (+2) | 16 (+3) | 10 (+0) | 12 (+1) | 9 (-1)|
___
**Saving Throws** Constitution +6
**Skills** Perception +4, Stealth +5
**Damage Resistances** necrotic; bludgeoning, piercing, slashing from nonmagical
**Damage Immunities** poison | **Condition Immunities** exhaustion, poisoned
**Condition Immunities** exhaustion, poisoned
**Senses** darkvision 60 ft.
**Languages** Common
**Challenge** 6 (2,300 XP)
___
### ACTIONS
**Multiattack.** Two longsword attacks and one life drain.

**Longsword.** *Melee Weapon Attack:* +7 to hit, reach 5 ft., one target. *Hit:* 1d8+4 slashing damage

**Life Drain.** *Melee Weapon Attack:* +7 to hit, reach 5 ft., one target. *Hit:* 2d6+4 necrotic. Target max HP reduced by amount (until long rest). Dies if max HP reaches 0.

**Battle Cry (Recharge 6).** All war-twisted soldiers within 30 ft can attack as reaction.

### LORE
Soldiers who died violently and rose as undead, twisted by rage and trauma.
}}

\page

{{monster,frame,wide
## CURSE BEARER
*Large monstrosity, chaotic evil*
___
**Armor Class** :: 15 (natural)
**Hit Points** :: 126 (12d10 + 60)
**Speed** :: 40 ft., climb 40 ft.![curse bearer](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-curse-bearer.jpg) {width:325px,mix-blend-mode:multiply}
___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|19 (+4) | 16 (+3) | 20 (+5) | 8 (-1) | 14 (+2) | 10 (+0)|
___
**Saving Throws** Constitution +8, Wisdom +5
**Skills** Perception +5, Stealth +6
**Damage Resistances** necrotic | **Senses** darkvision 120 ft., blindsight 30 ft.
**Senses** darkvision 120 ft., blindsight 30 ft.
**Languages** understands Common but can't speak
**Challenge** 8 (3,900 XP)
___
### ACTIONS
**Multiattack.** Two claw attacks and one bite.

**Claw.** *Melee Weapon Attack:* +7 to hit, reach 10 ft., one target. *Hit:* 2d6+4 slashing damage

**Bite.** *Melee Weapon Attack:* +7 to hit, reach 5 ft., one target. *Hit:* 2d8+4 piercing damage + 2d8 necrotic damage

**Curse Touch (Recharge 5-6).** One creature within 5 ft makes DC 15 Wisdom save or cursed. Cursed creature has disadvantage on all d20 rolls for 1 hour. *Remove curse* ends it.

**Terrifying Howl (1/Day).** All creatures within 60 ft make DC 15 Wisdom save or frightened 1 min. Can repeat save each turn.

### LORE
Result of powerful curses or exposure to corrupted magic. Was once human or beast.
}}