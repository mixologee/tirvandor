<style>
  

/* UPDATED | KDP hardcover: 8.25" x 11" trim size, page extended to 9.25" x 11.75" so the
   printer treats the surrounding 0.625" (Spine Side) / 0.375" (top, bottom, outer edge) as bleed/margin.
   Margin and Padding values keep text + images well inside
   the trim, centered between left and right margins (no odd/even gutter).
   Bottom padding is larger to leave room for page number / footnote.
   Ref: https://kdp.amazon.com/en_US/help/topic/GVBQ3CMEQW3W2VL6 
   
   https://homebrewery.naturalcrit.com/new
   */



.page {
  width: 9.25in;                /*Print size 9.25in (.page+.page padding left and right)*/
  height: 12in;                 /*Print size 12in (.page height + padding top and bottom)*/
  background-size: 100% 100%;
  padding-top: 0.85in;         /*Bleed and Safe Margin + 0.35in */
  padding-bottom: 0.5in;      /*Bleed and Safe Margin + 0.1in */
}

/* Even Pages (Right Hand Side): Bleed is on the right (outside), gutter on the left (spine) */
.page:nth-of-type(odd) {  
   padding-left: 1.25in;        /* 0.625" Inside (Gutter Margin) + 0.27in */
   padding-right: 1in;       /* 0.125" Bleed + 0.25" Outside Margin + 0.5in   */
}

/* Odd Pages (Left Hand Side): Bleed is on the left (outside), gutter on the right (spine) */
.page:nth-of-type(even) {
   padding-right: 1.125in;        /* 0.625" Inside (Gutter Margin) + 0.27in */
   padding-left: 1in;       /* 0.125" Bleed + 0.25" Outside Margin + 0.5in   */   
}

.page .pageNumber,
.page .footnote {
    position: absolute;
    bottom: 0.75in;             
    left: 0.625in !important;   /* Position Left elements within page layout */
    right: 0.625in !important;  /* Position right elements within page layout */
    width: inherit !important;
    display: block;
}


/*Overrides for style.css*/

.page:after {
    bottom: 0.70in !important;    /*Adjusts footer graphic position from bottom*/
}

.columnWrapper {
    max-height:95% !important;
}

/* 2. Position the Footnote text slightly left of center */
.page .footnote {
    text-align: left;
    margin-left: 0.5in; /* Adjust this to push the text further left */
}

/* 3. Position the Page Number slightly right of center */
.page .pageNumber {
    text-align: right;
    padding-right: 0.5in; /* Adjust this to push the number further right */
    color: gol;         /* Fixed typo from 'gol' */
}

/* Constrain absolutely-positioned chapter-opener images to the safety margins.
   The cover image (filename contains "cover") is excluded so it can bleed to
   the page edge. Matches both with-space and no-space style serializations. */
.page img[style*="position:absolute"]:not([src*="cover"]),
.page img[style*="position: absolute"]:not([src*="cover"]) {
    /*top: 0 !important;
    left: 0 !important;
    right: 0 !important;
    object-fit: cover;
    margin-bottom: .5in !important;*/
}

/* Display settings for Chapter Cover Images */

.cvr-img-top img, .cvr-img-bottom img {            /*Chapter images*/
    position: absolute;
    width: 100%;
    object-fit: cover;
    left:0;
}

.cvr-img-top img {top:0;}       /*Chapter images pinned to top*/

.cvr-img-bottom img {bottom:0;}  /*Chapter images pinned to bottom*/

.col-img img {display: block; z-index:1; margin: 0 auto;} /*Characters and Creatures*/

.col-img-item img {display: block;  z-index:0; width: 50%; margin:1%;} /*Item images*/
  
</style>

{{insideCover}}

# Tirvandor
## Field Guide

#### Creatures of the Sundered Realms


{{padding-top:275px}}

<div style="text-align: center">

### Acknowledgements
:
</div>

<div style="font-family: Garamond;font-size: 18px">

{{frame,wide
I want to say a special thanks to my in-laws for helping me find the time to make this book and the world of Tirvandor a reality.
}}

</div>

{{padding-top:135px}}

#### Copyright & Attribution

**Tirvandor Field Guide** ::

Copyright © 2025 Jason "Mixologee" Scheponik. All rights reserved.

All original content including world lore, characters, locations, storylines, and artwork are the exclusive property of the author.

#### Attribution

This work includes material taken from the System Reference Document 5.1 (SRD 5.2) by Wizards of the Coast LLC and available at https://www.dndbeyond.com/srd.

The SRD 5.2 is licensed under the Creative Commons Attribution 4.0 International License available at https://creativecommons.org/licenses/by/4.0/legalcode.

#### Product Identity

The following are designated as Product Identity: Tirvandor, all proper names of characters, locations, organizations, and factions; all storylines, plots, and narrative elements; all original artwork and maps; the Seven Ascended concept; the Seven Bound Ancients concept; all original magic items; the Worldrend event and timeline; all campaign content.

{{skipCounting}}
\page
\page

{{toc,wide
# Contents

- ### [{{ Using This Bestiary}}{{ 3}}](#p5)
- ### [{{ Chapter 1 - Border Creatures}}{{ 5}}](#p7)
  - [{{ Border Bandit}}{{ 5}}](#p7)
  - [{{ Smuggler Captain}}{{ 6}}](#p8)
  - [{{ War-Scarred Veteran}}{{ 7}}](#p9)
  - [{{ Border Wraith}}{{ 8}}](#p10)
  - [{{ Contested Land Elemental}}{{ 10}}](#p12)
  - [{{ Refugee Mob}}{{ 11}}](#p13)
  - [{{ Scavenger Ghoul}}{{ 12}}](#p14)
  - [{{ Territorial Drake}}{{ 13}}](#p15)
  - [{{ War Beast}}{{ 14}}](#p16)
  - [{{ Haunted Battlefield}}{{ 16}}](#p18)
- ### [{{ Chapter 2 - Thaldros Military}}{{ 19}}](#p21)
  - [{{ Thaldros Conscript}}{{ 19}}](#p21)
  - [{{ Thaldros Soldier}}{{ 20}}](#p22)
  - [{{ Iron Legion Enforcer}}{{ 21}}](#p23)
  - [{{ Royal Guard Elite}}{{ 22}}](#p24)
  - [{{ State Inquisitor}}{{ 24}}](#p26)
  - [{{ War Mage of Thaldros}}{{ 25}}](#p27)
  - [{{ Siege Golem}}{{ 27}}](#p29)
  - [{{ General’s Champion}}{{ 28}}](#p30)
  - [{{ Iron Crown Knight}}{{ 29}}](#p31)
  - [{{ Lord Commander Varius}}{{ 31}}](#p33)
- ### [{{ Chapter 3 - Aethoria & Iron Guild}}{{ 33}}](#p35)
- #### [{{ Aethoria Resistance}}{{ 33}}](#p35)
  - [{{ Aethorian Militia}}{{ 33}}](#p35)
  - [{{ Resistance Fighter}}{{ 34}}](#p36)
  - [{{ People’s Champion}}{{ 35}}](#p37)
  - [{{ Revolutionary Mage}}{{ 36}}](#p38)
  - [{{ Chain Breaker Monk}}{{ 37}}](#p39)
  - [{{ Guerrilla Commander}}{{ 38}}](#p40)
  - [{{ The Liberator}}{{ 39}}](#p41)
  - [{{ Prophesied Hero}}{{ 41}}](#p43)
- #### [{{ Iron Guild Mercenaries}}{{ 42}}](#p44)
  - [{{ Guild Recruit}}{{ 42}}](#p44)
  - [{{ Veteran Mercenary}}{{ 43}}](#p45)
  - [{{ Guild Enforcer}}{{ 44}}](#p46)
  - [{{ Contract Killer}}{{ 45}}](#p47)
  - [{{ Iron Guild Captain}}{{ 46}}](#p48)
  - [{{ Guildmaster’s Elite}}{{ 47}}](#p49)
  - [{{ Garrick Ironheart}}{{ 49}}](#p51)
- ### [{{ Chapter 4 - Ascended & Ancient}}{{ 51}}](#p53)
- #### [{{ Ascended-Touched}}{{ 51}}](#p53)
  - [{{ Blessed Paladin}}{{ 51}}](#p53)
  - [{{ Thandros’s Justicar}}{{ 52}}](#p54)
  - [{{ Aethor’s Liberator}}{{ 53}}](#p55)
  - [{{ Moira’s Seer}}{{ 54}}](#p56)
  - [{{ Sylvara’s Wild Hunter}}{{ 55}}](#p57)
  - [{{ Sera’s Mercy}}{{ 57}}](#p59)
  - [{{ Mordain’s Sentinel}}{{ 58}}](#p60)
  - [{{ Fallen Champion}}{{ 59}}](#p61)
- #### [{{ Ancient & Prophecy}}{{ 60}}](#p62)
  - [{{ Ancient Guardian}}{{ 60}}](#p62)
  - [{{ Prophecy Keeper}}{{ 61}}](#p63)
  - [{{ Forgotten King}}{{ 63}}](#p65)
  - [{{ Herald of the Seven}}{{ 65}}](#p67)
- #### [{{ Corrupted & Cursed}}{{ 66}}](#p68)
  - [{{ Corruption Spawn}}{{ 66}}](#p68)
  - [{{ War-Twisted Soldier}}{{ 67}}](#p69)
  - [{{ Curse Bearer}}{{ 69}}](#p71)
- #### [{{ Appendix A: Encounter Tables by Region}}{{ 71}}](#p73)
- #### [{{ Appendix B: CR Quick Reference}}{{ 72}}](#p74)
- #### [{{ OPEN GAME LICENSE Version 1.0a}}{{ 73}}](#p75)
}}



{{skipCounting}}
\page
\page

# Using This Bestiary
:
Welcome to the Sundered Realms.

This Field Guide collects fifty creatures and characters drawn from the world of Tirvandor — soldiers, scavengers, divine messengers, and the things war leaves behind. Each entry is organized to read top to bottom: visual flavor first, then narrative context, then mechanics, then plot seeds. You can stop at any layer depending on how much you need.

### What's in Each Entry
- **Description** — what the creature looks like, moves like, smells of. Read aloud at the table when introducing the encounter.
- **Lore** — who they are, why they exist, and how they fit into the world.
- **Cultural Significance** — how Tirvandor's broader societies view and treat them. Useful for shaping NPC reactions.
- **Habitat & Ecology** — where they live, how they organize, what their lives look like between fights. Helpful for planning regions, lairs, and follow-up encounters.
- **Tactics** *(Chapters 1–2)* — how they fight at the table.
- **Story Hooks** — four plot seeds per monster, ready to drop into a session.
- **Stat Block** — a 5th-Edition-compatible game-ready statblock with traits, actions, and (for some) legendary actions.



### Reading the Regions
The chapters are organized geographically and politically rather than by monster type:

- **Chapter 1: Border Creatures** — The Contested Lands between the two nations. Bandits, smugglers, war-twisted wildlife, and the dead that don't stay dead. Best for war-themed campaigns or any party traveling near the front.
- **Chapter 2: Thaldros Military** — The disciplined iron fist of the empire. Conscripts to legendary commanders. Drop these into any encounter where lawful authority is asserting itself.
- **Chapter 3: Aethoria Resistance & Iron Guild** — Freedom fighters and professional mercenaries — two faces of organized armed force outside the Thaldros structure.
- **Chapter 4: Ascended & Ancient** — Divine champions, prophetic entities, and the corrupted things that haunt the deep places. Use sparingly; their presence signals that the stakes have escalated.

\column

### Suggested Encounter Groups
Here are a few pre-built compositions to drop into a session:

- **Border Patrol (CR 3)** — 1 War-Scarred Veteran + 4 Border Bandits
- **Smuggler's Caravan (CR 5)** — 1 Smuggler Captain + 2 Veteran Mercenaries + 4 Guild Recruits
- **Thaldros Strike Team (CR 7)** — 1 State Inquisitor + 2 Royal Guard Elites + 4 Thaldros Soldiers
- **Resistance Cell (CR 6)** — 1 Guerrilla Commander + 1 Revolutionary Mage + 4 Resistance Fighters
- **Ghoul Pack on a Battlefield (CR 4)** — 1 Border Wraith + 4 Scavenger Ghouls
- **Iron Crown Tribunal (CR 11)** — 1 Iron Crown Knight + 1 Thandros's Justicar + 2 Iron Legion Enforcers
- **Sentinel's Vigil (CR 12)** — 1 Mordain's Sentinel + 2 War-Twisted Soldiers + 1 Fallen Champion
- **Wild Hunt (CR 10)** — 1 Sylvara's Wild Hunter + 4 War Beasts + 2 Territorial Drakes
- **Final Stand (CR 15+)** — 1 Lord Commander Varius + 2 General's Champions + 4 Royal Guard Elites

{{footnote Using This Bestiary}}
{{pageNumber,auto}}
\page
\page

# Chapter 1 - Border Creatures
:
The Contested Lands — Thaldros's lawless frontier territories — are a dangerous expanse where desperate souls eke out survival among ancient ruins and war-scarred terrain.

## Border Bandit

<div class="col-img">![border bandit](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-border-bandit.jpg) {width:325px}</div>

### Description
Border bandits look like what they are: people at the end of their rope. Thin from irregular meals, scarred from old fights, wearing mismatched armor and patched clothing taken from whoever had it last. Their weapons are battered swords, rusted crossbows, improvised clubs — nothing matches, nothing ceremonial, everything purely functional. Their eyes carry the watchful gaze of prey animals that have learned to survive by becoming predators themselves.

### Lore
Border bandits are desperate refugees, deserters, and opportunists who prey on travelers in the Contested Lands. Most didn't choose this life — the war chose it for them. They know every cave, ruin, and hidden approach in their chosen territory, and that local knowledge is often their only advantage against better-equipped opponents. Despite their reputation, most prefer surrender to slaughter; dead victims can't be robbed twice, and killing merchants discourages future trade. A few have even become folk heroes among the dispossessed, sharing stolen wealth with starving villages.

### Cultural Significance
In Thaldros and Aethoria alike, "border bandit" is the convenient label slapped on anyone living in the Contested Lands outside official authority — an unfair smear that covers farmers, merchants, and tradespeople just as much as actual raiders. The stereotype persists because it's useful to the powers that abandoned the region.

### Habitat & Ecology
Bandits operate in small groups of five to fifteen for mutual protection, staking out territories along trade routes and ambushing travelers vulnerable enough to rob without excessive risk. They form loose hierarchies based on experience and success, following whoever keeps them alive and fed. Information passes quickly through bandit networks: which merchants carry valuable cargo, which patrols take which routes, which other groups are reliable allies or treacherous rivals. Some bands maintain codes of conduct — don't harm children, don't kill unless necessary, share equally; others have abandoned such niceties entirely.

{{monster,frame
## Border Bandit
*Medium humanoid (any race), any non-lawful alignment*
___
**Armor Class** :: 12 (leather armor)
**Hit Points** :: 11 (2d8 + 2)
**Speed** :: 30 ft.

___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|11 (+0) | 14 (+2) | 12 (+1) | 10 (+0) | 10 (+0) | 10 (+0)|
___
**Skills** :: Stealth +4, Deception +2
**Senses** :: passive Perception 10
**Languages** :: Common
**Challenge** :: 1/2 (100 XP)
___
**Border Cunning.** :: The bandit has advantage on Stealth checks in the Border region's ruins and wilderness.

**Desperate Fighter.** :: When reduced to half hit points or less, the bandit's next attack deals an extra 1d6 damage.

___
### Actions
**Scimitar.** :: *Melee Weapon Attack:* +4 to hit, reach 5 ft., one target. *Hit:* 5 (1d6 + 2) slashing damage.

**Light Crossbow.** :: *Ranged Weapon Attack:* +4 to hit, range 80/320 ft., one target. *Hit:* 6 (1d8 + 2) piercing damage.

}}


<div class='pageNumber auto'></div>
<div class='footnote'>Chapter 1 - Border Creatures</div>
\page

### Tactics
- Use terrain for ambushes
- Target weakest-looking party member
- Flee when outnumbered or badly wounded
- May surrender if offered mercy

### Story Hooks
- Ambushers turn out to be former soldiers waging a quiet guerrilla war against occupation.
- A bandit leader holds information vital to the party's mission, but won't share it without payment or service.
- The party must negotiate safe passage through bandit territory, playing rival groups against each other.
- A "random" raid reveals that someone powerful is secretly directing these attacks.
- 
## Smuggler Captain

<div class="col-img">![smuggler captain](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-smuggler-captain.jpg) {width:325px}</div>

### Description
Smuggler captains dress to impress and disarm — quality leather, sturdy boots, travel cloaks that conceal weapons while suggesting wealth. Their appearance says "successful merchant" rather than "criminal," which is exactly the point. They move with easy confidence, hands always visible, smiles ready. The best of them can convince border guards they're old friends, talk their way past checkpoints, and negotiate with anyone from desperate refugees to corrupt generals.

{{monster,frame
## Smuggler Captain
*Medium humanoid (any race), any alignment*
___
**Armor Class** :: 15 (studded leather)
**Hit Points** :: 58 (9d8 + 18)
**Speed** :: 30 ft.

___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|12 (+1) | 16 (+3) | 14 (+2) | 14 (+2) | 12 (+1) | 14 (+2)|
___
**Saving Throws** :: Dexterity +5, Intelligence +4
**Skills** :: Deception +6, Insight +3, Persuasion +6, Stealth +5
**Senses** :: passive Perception 11
**Languages** :: Common, Thieves' Cant, plus two others
**Challenge** :: 3 (700 XP)
___
**Cunning Action.** :: On each of its turns, the captain can use a bonus action to take the Dash, Disengage, or Hide action.

**Border Network.** :: The captain knows safe routes through the Border and has contacts in most settlements. Can call for reinforcements (1d4 border bandits arrive in 1d4 rounds).

**Sneak Attack (1/Turn).** :: The captain deals an extra 10 (3d6) damage when hitting with a weapon attack and has advantage on the attack roll.

___
### Actions
**Multiattack.** :: The captain makes two attacks with their rapier.

**Rapier.** :: *Melee Weapon Attack:* +5 to hit, reach 5 ft., one target. *Hit:* 7 (1d8 + 3) piercing damage.

**Hand Crossbow.** :: *Ranged Weapon Attack:* +5 to hit, range 30/120 ft., one target. *Hit:* 6 (1d6 + 3) piercing damage.

**Contract Offer (Recharge 5-6).** :: The captain offers a bargain. One humanoid within 30 feet that can hear the captain must make a DC 14 Wisdom saving throw. On a failure, the target is charmed for 1 minute or until the captain or their allies harm it. While charmed, the target is inclined to accept reasonable deals.

### Reactions
**Parry.** :: The captain adds 2 to their AC against one melee attack that would hit them. To do so, the captain must see the attacker and be wielding a melee weapon.
}}

### Lore
Smuggler captains move weapons, refugees, contraband, and information across a border that exists more on maps than in practice. They're genuinely neutral in the continental conflict — taking sides would cut off half their market — and both governments officially condemn smuggling while quietly relying on it. Captains favor practical but expensive clothing that says "merchant" rather than "criminal," move with easy confidence, and can talk past most checkpoints. Their true ability isn't combat, every fight they're in has already gone wrong. 

<div class='pageNumber auto'></div>
<div class='footnote'>Chapter 1 - Border Creatures</div>
\page

But their network, given time, a captain can arrange almost anything: safe passage, false documents, weapons, or the occasional disappearance.

### Cultural Significance
Among border dwellers, smugglers are often the only connection to goods unavailable through legal channels — bringing medicine, food, tools, and news in equal measure. This makes them important community figures regardless of their technical criminality, and a captain known for fair dealing is a fixture across a dozen villages no map will name.

### Habitat & Ecology
Captains run operations that move people, goods, and information across the border, maintaining networks of bribed officials, sympathetic innkeepers, reliable guides, and corrupt merchants who ask no questions. They work for anyone who pays — neutrality is both professional principle and practical necessity. They maintain loose professional networks among themselves, sharing information about dangerous routes, reliable contacts, and treacherous customers. Every captain keeps emergency plans: escape routes, hidden resources, false identities for when things go wrong. Paranoia isn't a flaw in this profession; it's a job requirement.

### Tactics
- Negotiate before fighting if possible
- Use Cunning Action to stay mobile
- Call for backup if losing
- Always have an escape route planned

### Story Hooks
- The party needs to cross the border discreetly — only a smuggler can get them through.
- A captain has intelligence on enemy movements, but wants something in return.
- The party's smuggler contact is quietly playing both sides of the conflict.
- A captain's apparent betrayal turns out to be coercion — they're being blackmailed.

## War-Scarred Veteran

### Description
Veterans wear their history on their bodies. Scars cover what skin shows — sword cuts, burn marks, wounds from weapons that shouldn't have been survivable. Many are missing fingers, eyes, limbs, or pieces of ears. Their joints ache; their sleep is haunted. But they move with deadly economy, never wasting motion, always balanced. Their armor is well-maintained but outdated, repaired and modified over years of use. Their weapons are similarly veteran: blade edges sharpened until the metal is noticeably thinner, hilts worn smooth by countless grips.

### Lore
The Contested Lands have seen fighting for over a century, and these veterans wear that history on their bodies: scars, missing fingers, joints that ache, sleep that's haunted. Some served formal armies before being discharged as "unfit"; some sold blades to whoever paid; most simply survived where they shouldn't have. They aren't special — they're just the ones who didn't die, and that perspective colors everything they do. Veterans recognize each other instantly, something in the eyes, the stance, the way they scan a room. In both nations they're respected in theory but avoided in practice — uncomfortable reminders that war breaks people even when they survive.

<div class="col-img">![war-scarred veteran](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-war-scarred-veteran.jpg) {width:325px}</div>

### Cultural Significance
Among soldiers, veterans are either revered or resented — some see them as fonts of hard-won wisdom, others as reminders of their own potential fate. A veteran's advice about survival is usually correct, but rarely welcome. Informal networks bind them together quietly across both nations: they remember names, debts, and where the bodies are buried.

### Habitat & Ecology
Veterans gravitate toward roles that use their skills without requiring the demands of active campaigning — mercenary instructors, hired muscle, caravan guards, or 

<div class='pageNumber auto'></div>
<div class='footnote'>Chapter 1 - Border Creatures</div>
\page

hermits in the border wilds. Some find peace; others never do, struggling with drink, nightmares, sudden rages, and an inability to feel safe. Years of survival have made them cunning and perceptive: they read battlefields instinctively, seeing cover, escape routes, and tactical advantages that civilians never notice. They understand violence in ways that ordinary people never will.

{{monster,frame
## War-Scarred Veteran
*Medium humanoid (any race), any alignment*
___
**Armor Class** :: 17 (half plate)
**Hit Points** :: 68 (8d8 + 32)
**Speed** :: 30 ft.
___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|16 (+3) | 13 (+1) | 18 (+4) | 10 (+0) | 12 (+1) | 10 (+0)|
___
**Saving Throws** :: Strength +5, Constitution +6
**Skills** :: Athletics +5, Intimidation +2, Survival +3
**Condition Immunities** :: frightened
**Senses** :: passive Perception 11
**Languages** :: Common
**Challenge** :: 4 (1,100 XP)
___
**Survivor.** :: The veteran has advantage on death saving throws.

**Seen It All.** :: The veteran is immune to being frightened and has advantage on saving throws against being charmed.

**Battle Scarred.** :: When the veteran takes damage that would reduce them to 0 hit points, they can make a DC 10 Constitution saving throw. On a success, they drop to 1 hit point instead. This DC increases by 5 each time this feature is used and resets after a long rest.

___
### Actions
**Multiattack.** :: The veteran makes two longsword attacks or two longbow attacks.

**Longsword.** :: *Melee Weapon Attack:* +5 to hit, reach 5 ft., one target. *Hit:* 7 (1d8 + 3) slashing damage, or 8 (1d10 + 3) slashing damage if used with two hands.

**Longbow.** :: *Ranged Weapon Attack:* +3 to hit, range 150/600 ft., one target. *Hit:* 5 (1d8 + 1) piercing damage.

**Intimidating Presence (Recharge 5-6).** :: The veteran roars a challenge. Each enemy within 30 feet that can see or hear the veteran must make a DC 13 Wisdom saving throw or become frightened for 1 minute. A frightened creature can repeat the save at the end of each of its turns, ending the effect on a success.
}}

### Tactics
- Fight defensively, conserving energy
- Use intimidation to avoid fights
- Know when to retreat (and how)
- Protect allies instinctively
\column
### Story Hooks
- A veteran holds crucial knowledge about an old battle or buried secret in the Contested Lands.
- The party needs a guide through dangerous territory — only a veteran knows the safe paths.
- A respected veteran is being hunted by both sides for something they witnessed.
- The party must convince a retired veteran to take up arms one final time.

## Border Wraith

<div class="col-img">![border wraith](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-border-wraith.jpg) {width:325px}</div>

### Description
Border wraiths are darkness given form, shadows that move against the light, cold spots in the air that speak of violent death. They retain vague humanoid shapes — echoes of the soldiers they were in life. When they manifest fully, witnesses report seeing ghostly armor, spectral weapons, faces frozen in final expressions of agony or rage. They carry the marks of their deaths: phantom wounds that weep shadow instead of blood, translucent forms pierced by arrows no longer there. Their presence chills the air noticeably — breath frosts, water freezes, living creatures feel a sudden dread their bodies recognize before their minds do.

<div class='pageNumber auto'></div>
<div class='footnote'>Chapter 1 - Border Creatures</div>
\page

### Lore
Centuries of bloodshed have saturated the Contested Lands with death energy, and where soldiers died violently — in great numbers, with unfinished business or overwhelming emotion — some did not pass on. Border wraiths are these trapped spirits, bound to the region where they fell, the battle that killed them playing on endless repeat in their shattered consciousness. They hunt at night, drawn to fresh violence the way sharks are drawn to blood, and when they first manifest they sometimes speak: a name, an order, a final phrase from their death. Most retain only fragments of intelligence, but a rare few remember enough of themselves to be reasoned with — or laid to rest by completing unfinished business. The Order of Moira considers wraith-laying sacred work.

### Cultural Significance
Both nations acknowledge wraiths as real threats but rarely discuss them openly. Military commanders factor wraith activity into campaign planning; smart officers avoid night battles in regions known for heavy historical casualties. Among border dwellers, wraiths are simply part of life — another danger to avoid, like bandits or bad weather.

### Habitat & Ecology
Wraiths cluster around the most saturated regions of the Contested Lands, forming loose collections that might resemble spectral units. They don't coordinate deliberately, but their shared patterns sometimes create the appearance of organized tactics. They're bound to the region where they died — force a wraith beyond these boundaries and it suffers increasing agony, eventually dissipating if kept away long enough. Those they kill violently might rise as lesser spirits under the wraith's instinctive control. A single wraith that finds victims can quickly become several.

### Tactics
- Ambush from walls/objects
- Target squishier party members
- Use Create Specter on fallen enemies
- Flee if seriously injured (unless enraged)

### Story Hooks
- A wraith retains crucial information about a historical event, but communicating with it is dangerous.
- The party must cross a haunted battlefield at night, avoiding or fighting the spectral army that manifests.
- Someone is deliberately creating conditions that produce new wraiths, weaponizing the dead.
- A wraith recognizes one of the party members as connected to its living past.

{{monster,frame
## Border Wraith
*Medium undead, neutral evil*
___
**Armor Class** :: 13
**Hit Points** :: 67 (9d8 + 27)
**Speed** :: 0 ft., fly 60 ft. (hover)
___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|6 (-2) | 16 (+3) | 16 (+3) | 12 (+1) | 14 (+2) | 15 (+2)|
___
**Damage Resistances** :: acid, cold, fire, lightning, thunder; bludgeoning, piercing, and slashing from nonmagical attacks
**Damage Immunities** :: necrotic, poison
**Condition Immunities** :: charmed, exhaustion, grappled, paralyzed, petrified, poisoned, prone, restrained
**Senses** :: darkvision 60 ft., passive Perception 12
**Languages** :: the languages it knew in life
**Challenge** :: 5 (1,800 XP)
___
**Incorporeal Movement.** :: The wraith can move through other creatures and objects as if they were difficult terrain. It takes 5 (1d10) force damage if it ends its turn inside an object.

**Sunlight Sensitivity.** :: While in sunlight, the wraith has disadvantage on attack rolls and Wisdom (Perception) checks that rely on sight.

**Border-Bound.** :: The wraith is bound to the Border region where it died. If forced outside the Border, it takes 10 (3d6) psychic damage at the start of each of its turns.

**Echoes of War.** :: When the wraith first appears, each creature within 30 feet hears a snippet of the battle where it died (screams, clashing steel, etc.). The wraith can speak one phrase from its final moments.

___
### Actions
**Life Drain.** :: *Melee Weapon Attack:* +6 to hit, reach 5 ft., one creature. *Hit:* 21 (4d8 + 3) necrotic damage. The target must succeed on a DC 14 Constitution saving throw or its hit point maximum is reduced by an amount equal to the damage taken. This reduction lasts until the target finishes a long rest. The target dies if this effect reduces its hit point maximum to 0.

**Create Specter.** :: The wraith targets a humanoid within 10 feet of it that died violently in the last minute. The target's spirit rises as a specter under the wraith's control. The wraith can have no more than three specters under its control at one time.

}}


<div class='pageNumber auto'></div>
<div class='footnote'>Chapter 1 - Border Creatures</div>
\page

## Contested Land Elemental

<div class="col-img">![contested land elemental](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-contested-land-elemental.jpg) {width:325px}</div>

### Description
These elementals embody the border's broken nature — massive humanoid forms averaging twelve feet tall, with bodies of earth and stone in chaotic composition. Layers of soil from both nations are visible like geological strata; minerals that shouldn't coexist are fused into unstable amalgams. Their features shift constantly as their substance reorganizes itself — one arm Thaldros granite, the other Aethorian sandstone, their eyes voids where the earth couldn't agree on what it should be. When they move, the ground trembles; their footsteps leave craters. They smell of freshly turned earth and ancient stone, and underneath, the copper tang of blood.

### Lore
Centuries of violence have poisoned the Contested Lands so deeply that the earth itself developed something like instinct, and these elementals are its immune response. Their bodies are chaotic amalgams — Thaldros granite fused with Aethorian sandstone, layers of soil from both nations visible like geological strata, minerals that were never meant to mix. They embody not a pure element but conflict itself, and their substance is inherently unstable, occasionally erupting when struck. Peaceful travelers may pass through unmolested, but anyone who digs trenches, builds fortifications, sets fires, or spills fresh blood on already-saturated ground draws the land's wrath. Some druids believe they represent the earth's attempt to make the war too costly to continue. If so, the land is losing.


{{monster,frame
## Contested Land Elemental
*Large elemental, neutral*
___
**Armor Class** :: 17 (natural armor)
**Hit Points** :: 126 (12d10 + 60)
**Speed** :: 30 ft., burrow 30 ft.
___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|20 (+5) | 8 (-1) | 20 (+5) | 5 (-3) | 10 (+0) | 5 (-3)|
___
**Damage Vulnerabilities** :: thunder
**Damage Resistances** :: bludgeoning, piercing, and slashing from nonmagical attacks
**Damage Immunities** :: poison
**Condition Immunities** :: exhaustion, paralyzed, petrified, poisoned, unconscious
**Senses** :: darkvision 60 ft., tremorsense 60 ft., passive Perception 10
**Languages** :: Terran
**Challenge** :: 6 (2,300 XP)
___
**Earth Glide.** :: The elemental can burrow through nonmagical, unworked earth and stone. While doing so, it doesn't disturb the material it moves through.

**Siege Monster.** :: The elemental deals double damage to objects and structures.

**Mixed Form.** :: The elemental's body contains earth from both Thaldros and Aethoria, making it unstable. When the elemental takes damage, roll 1d6. On a 5-6, it erupts, dealing 7 (2d6) bludgeoning damage to all creatures within 5 feet.

**Territorial Fury.** :: The elemental has advantage on attack rolls against creatures that have dealt damage to structures or the earth in the last minute.
___
### Actions
**Multiattack.** :: The elemental makes two slam attacks.

**Slam.** :: *Melee Weapon Attack:* +8 to hit, reach 10 ft., one target. *Hit:* 14 (2d8 + 5) bludgeoning damage.

**Border Quake (Recharge 5-6).** :: The elemental strikes the ground, creating a localized earthquake. Each creature on the ground within 20 feet must make a DC 15 Strength saving throw. On a failure, a creature takes 18 (4d8) bludgeoning damage and is knocked prone. On a success, the creature takes half damage and isn't knocked prone. Additionally, the ground in that area becomes difficult terrain until cleared.
}}

### Cultural Significance
Druids view these elementals with complicated reverence — they are natural spirits of a kind, but also aberrations, products of unnatural violence against the earth. Some druids work to heal the conditions that create them; others believe they should be left alone 

<div class='pageNumber auto'></div>
<div class='footnote'>Chapter 1 - Border Creatures</div>
\page

as guardians. Military commanders on both sides simply add elemental response to the cost column of any major engagement.

### Habitat & Ecology
Elementals form where the damage to the land is worst — old battlefields, ruined fortresses, mass graves — and remain solitary. A given area produces rarely more than one, and where territories overlap they simply ignore each other. They may lie dormant for years between provocations, only to rise when violence rekindles. Druids who have managed empathic contact report fragmented impressions: rage, protectiveness, exhaustion, grief — emotion rather than language. They do not communicate in any traditional sense, but they remember.

### Tactics
- Emerge from underground (surprise)
- Focus on those damaging terrain
- Use Border Quake to knock down groups
- Retreat underground if badly hurt

### Story Hooks
- The party must cross elemental territory without triggering a response.
- An elemental has awakened near a strategic location, threatening both armies equally.
- Someone has found a way to control or direct these elementals, and is using them as weapons.
- The elementals are guarding something buried deep underground — and they were placed there.


## Refugee Mob

<div class="col-img">![refugee mob](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-refugee-mob.jpg) {width:325px}</div>
\column
### Description
Individually, mob members are just people — families, workers, farmers displaced by war. Their clothes are worn, faces gaunt, eyes showing the empty exhaustion of those who've lost everything. Children cling to parents. Elderly struggle to keep up. The sick and injured are carried by those who can still walk. But when fear or rage ignites them, they become something else: a mass of reaching hands and screaming voices, individuals disappearing into the crowd.

### Lore
A refugee mob isn't truly a creature — it's desperation given collective form. Villages caught between armies are destroyed; cities change hands and populations flee; people who had homes, jobs, and lives become homeless wanderers with nothing but what they can carry. Most refugee columns remain peaceful, too exhausted for violence, but a spark — perceived injustice, denial of needed food, a demagogue's words — can ignite them into something else: a mass of reaching hands and screaming voices where individuals disappear into the crowd. Critically, mobs can be calmed. Offering food, safety, or genuine hope often defuses them, because the violence isn't natural — it's a response to unnatural conditions. After dispersing, participants often experience shame and horror at what they did. They were themselves; they also weren't.

### Cultural Significance
Both nations fear mob violence while doing little to address its root causes, treating refugees as problems to be contained rather than people to be helped — a self-fulfilling prophecy of further unrest. Priests and healers sometimes specialize in mob defusing, walking into crowds alone and trusting that genuine compassion can reach desperate people. This is heroically dangerous but sometimes works.

### Habitat & Ecology
Mobs are inherently unstable, forming quickly around triggering events and dissipating when the energy is spent or hope is offered. The same group might be a peaceful refugee column one hour and a violent mob the next, then peaceful again by evening. They follow whoever seems most confident in the moment and abandon leaders who show weakness. Individual mob members often have no idea what the group is doing until afterward — the crowd psychology takes over, and people do things they would never do alone. The experience is traumatic for everyone involved, victims and participants alike.

### Tactics
- Overwhelm through numbers
- Target obvious threats
- Flee if leaders fall or hope is offered
- Can be calmed with Persuasion (DC 15)

<div class='pageNumber auto'></div>
<div class='footnote'>Chapter 1 - Border Creatures</div>
\page

{{monster,frame
## Refugee Mob
*Large swarm of Medium humanoids, any alignment*
___
**Armor Class** :: 10
**Hit Points** :: 39 (6d10 + 6)
**Speed** :: 30 ft.

___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|10 (+0) | 10 (+0) | 12 (+1) | 10 (+0) | 10 (+0) | 8 (-1)|
___
**Condition Immunities** :: charmed, frightened, grappled, paralyzed, petrified, prone, restrained, stunned
**Senses** :: passive Perception 10
**Languages** :: Common
**Challenge** :: 1 (200 XP)
___
**Swarm.** :: The mob can occupy another creature's space and vice versa, and the mob can move through any opening large enough for a Medium humanoid. The mob can't regain hit points or gain temporary hit points.

**Desperate Horde.** :: The mob has advantage on attack rolls if it has half its hit points or more.

**Panicked.** :: The mob has disadvantage on Wisdom saving throws while below half hit points.

___
### Actions
**Mob Violence.** :: *Melee Weapon Attack:* +2 to hit, reach 0 ft., one creature in the swarm's space. *Hit:* 14 (4d6) bludgeoning damage, or 7 (2d6) bludgeoning damage if the swarm has half its hit points or fewer.

### Reactions
**Stampede.** :: When the mob takes damage from an area effect, it can move up to its speed away from the source of danger. This movement doesn't provoke opportunity attacks.
}}

### Story Hooks
- The party must calm a mob before soldiers arrive and massacre them.
- Someone is deliberately provoking mobs to destabilize the region.
- A mob is approaching a location the party must defend — how do they respond without bloodshed?
- The party discovers that what looked like a "mob attack" was actually something else entirely.
- 
## Scavenger Ghoul

### Description
Scavenger ghouls are gaunt, twisted things that were once humanoid but have been warped by undeath and constant corpse-feeding. Their skin is gray and tight over prominent bones; fingers have elongated into claws; teeth have multiplied and sharpened into rows of tearing fangs. They smell of death — old death, new death, every death in between — and their eyes carry a faint phosphorescent glow visible in darkness. They move in a hunched, scuttling manner, closer to animals than the people they once were. Most retain rotting scraps of the clothing they died in; some still wear armor rusted to their flesh.

<div class="col-img">![scavenger ghoul](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-scavenger-ghoul.jpg) {width:325px}</div>

### Lore
The Contested Lands are a ghoul paradise — constant violence produces constant corpses, and where there are corpses, ghouls thrive. These particular ghouls have specialized: gaunt, gray-skinned things with multiplied rows of tearing fangs and an enhanced ability to smell death from remarkable distances. They follow armies at a distance, hiding in ruins or underground for days until the fighting ends and the feasting begins. They prefer easy meals — corpses don't fight back — but isolated, wounded, or unarmed travelers are equally welcome food. Both armies treat ghoul infestations as a logistical problem requiring regular extermination, and proper burial is taken seriously in border country: bodies must be burned, buried deep, or consecrated, or new ghouls will rise.

### Cultural Significance
Among civilians, ghouls are just another horror the war has spawned. Parents use them to frighten children into obedience — "Stay inside after dark, or the ghouls will get you" — and the warnings aren't entirely fiction. 

<div class='pageNumber auto'></div>
<div class='footnote'>Chapter 1 - Border Creatures</div>
\page

Border villages maintain crude bone-pyres outside their walls for any unfortunate dead, lit weekly whether needed or not.

### Habitat & Ecology
Scavenger ghouls hunt in packs of four to twelve, following armies at a distance and lurking near battlefields. Pack hierarchies form around age and strength; older ghouls lead, younger ones follow, and disputes are settled through display rather than combat — ghouls don't waste food fighting each other. They're patient hunters, waiting days in ruins or underground until the living have left and the feasting can begin. They have no culture, no goals beyond hunger, and no existence beyond it. If the wars ever truly ended, scavenger ghouls would spread into other regions seeking food, or simply die out entirely.

{{monster,frame
## Scavenger Ghoul
*Medium undead, chaotic evil*
___
**Armor Class** :: 12
**Hit Points** :: 22 (5d8)
**Speed** :: 30 ft.

___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|13 (+1) | 15 (+2) | 10 (+0) | 7 (-2) | 10 (+0) | 6 (-2)|
___
**Damage Immunities** :: poison
**Condition Immunities** :: charmed, exhaustion, poisoned
**Senses** :: darkvision 60 ft., passive Perception 10
**Languages** :: Common
**Challenge** :: 1 (200 XP)
___
**Battlefield Scavenger.** :: The ghoul has advantage on Wisdom (Perception) checks to find corpses or wounded creatures.

**Pack Tactics.** :: The ghoul has advantage on attack rolls against a creature if at least one of the ghoul's allies is within 5 feet of the creature and the ally isn't incapacitated.

___
### Actions
**Bite.** :: *Melee Weapon Attack:* +4 to hit, reach 5 ft., one creature. *Hit:* 9 (2d6 + 2) piercing damage.

**Claws.** :: *Melee Weapon Attack:* +4 to hit, reach 5 ft., one target. *Hit:* 7 (2d4 + 2) slashing damage. If the target is a creature other than an elf or undead, it must succeed on a DC 10 Constitution saving throw or be paralyzed for 1 minute. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success.

**Corpse Feast (Recharge 5-6).** :: If the ghoul is adjacent to a corpse or unconscious creature, it can spend its action feeding. It regains 10 (3d6) hit points.
}}


### Tactics
- Hunt in packs (2-8 ghouls)
- Target wounded enemies
- Use paralysis on dangerous foes
- Feast mid-combat if possible

### Story Hooks
- A ghoul pack has grown large enough to threaten a settlement and tunnels beneath its walls.
- The party must recover something from a battlefield before scavengers arrive at dusk.
- Someone is deliberately feeding ghouls to build an undead army from the resulting kills.
- A pack's coordinated behavior suggests they're being directed by something intelligent.

## Territorial Drake

<div class="col-img">![territorial drake](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-territorial-drake.jpg) {width:325px}</div>

### Description
Territorial drakes are smaller cousins to true dragons — about the size of a large horse, with wingless serpentine bodies, powerful legs, and long whip-like tails. Their scales range from dusty brown to mottled gray, providing natural camouflage in the rocky ruins they prefer. Their heads are wedge-shaped with forward-facing eyes for ambush hunting, multiple rows of serrated teeth in jaws capable of crushing armor, and hooked claws built for climbing and grasping prey. Despite lacking wings, they scale vertical surfaces with ease and often attack from above.

<div class='pageNumber auto'></div>
<div class='footnote'>Chapter 1 - Border Creatures</div>
\page

### Lore
The Contested Lands' endless ruins make perfect drake habitat — elevated perches, protected dens, abundant prey both animal and humanoid. As war destroyed the human settlements that once stood here, territorial drakes claimed the empty spaces and thrived, growing more numerous and aggressive as they learned to hunt refugees, soldiers, and travelers. A single drake will fiercely defend several square miles of ruin, attacking from concealment with the camouflage their dusty scales provide. They're intelligent for animals — roughly wolf-level — and instinctively understand Draconic, which has not escaped the notice of certain mercenary bands who've successfully trained them as mounts. Drake-hide armor commands premium prices for those willing to risk the hunt.

### Cultural Significance
Drake-riders are an elite — expensive to maintain but devastatingly effective in rough terrain where conventional cavalry can't operate. Among border dwellers, drakes are simply dangerous wildlife to be avoided. Communities learn which ruins are drake territory and stay away. Those who don't aren't around to teach others.

### Habitat & Ecology
Drakes pair for life, with mated couples sharing a territory of several square miles and producing clutches of two to four eggs annually. Juveniles are driven out at maturity to find their own range or die trying. They hunt through ambush, dropping onto prey from above with devastating opening strikes, and they coordinate effectively with mates or pack-bonded siblings. Their territorial calls — long, layered roars — carry for miles, warning other drakes of claimed boundaries. Other drakes respect those calls, which is a kind of vocal heraldry, but lone drakes occasionally test borders during lean seasons.

### Tactics
- Ambush from high ground
- Work in pairs if possible
- Use tail to knock down enemies
- Flee to lair if seriously wounded

### Story Hooks
- Drake eggs are valuable; the party is hired to retrieve some — alive.
- A particularly large drake has claimed territory that blocks a critical trade route.
- Someone is training drakes for military use. Who, and for what purpose?
- The party discovers that drakes are far more intelligent than commonly believed.
  
{{monster,frame
## Territorial Drake
*Large dragon, unaligned*
___
**Armor Class** :: 14 (natural armor)
**Hit Points** :: 52 (7d10 + 14)
**Speed** :: 30 ft., climb 30 ft.

___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|16 (+3) | 11 (+0) | 14 (+2) | 4 (-3) | 10 (+0) | 7 (-2)|
___
**Skills** :: Perception +2, Stealth +2
**Senses** :: darkvision 60 ft., passive Perception 12
**Languages** :: understands Draconic but can't speak
**Challenge** :: 2 (450 XP)
___
**Border Camouflage.** :: The drake has advantage on Dexterity (Stealth) checks in rocky or ruined terrain.

**Pack Tactics.** :: The drake has advantage on attack rolls against a creature if at least one of the drake's allies is within 5 feet of the creature and the ally isn't incapacitated.

___
### Actions
**Multiattack.** :: The drake makes one bite attack and one tail attack.

**Bite.** :: *Melee Weapon Attack:* +5 to hit, reach 5 ft., one target. *Hit:* 7 (1d8 + 3) piercing damage.

**Tail.** :: *Melee Weapon Attack:* +5 to hit, reach 5 ft., one target. *Hit:* 6 (1d6 + 3) bludgeoning damage, and the target must succeed on a DC 13 Strength saving throw or be knocked prone.

**Warning Roar (Recharge 5-6).** :: The drake roars, alerting other drakes in a 1-mile radius. Allied drakes within 60 feet gain advantage on their next attack roll.
}}

## War Beast

<div class="col-img">![war beast](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-war-beast.jpg) {width:325px}</div>

<div class='pageNumber auto'></div>
<div class='footnote'>Chapter 1 - Border Creatures</div>
\page

### Description
War beasts are massive predators — wolves, hunting cats, or war dogs averaging six feet at the shoulder, with 
heavy muscle, powerful jaws, and coats ranging from dark gray to mottled brown depending on breeding lineage. Their eyes show unusual intelligence for animals — the product of generations of selective breeding. Scars from training and combat mark most specimens; their teeth and claws are larger than natural. Domesticated beasts wear barding and unit collars; feral ones have torn their gear away but often still bear harness marks faintly visible in their fur.

### Lore
Both Thaldros and Aethoria have run war-beast breeding programs for centuries, producing wolves, hunting cats, and war dogs that are larger, smarter, and more aggressive than their wild ancestors. Trained from birth to follow commands and form supernatural bonds with their handlers, domesticated war beasts are extensions of the soldiers who command them. But war is chaos — handlers die, units scatter, beasts escape or are abandoned. Feral war beasts retain their training while losing their restraint, and they hunt in packs using military tactics: flanking, ambush, coordinated strikes. They're more dangerous than wild predators because they think like soldiers. Their existence is a quiet scandal for both militaries; neither admits how many beasts have gone feral over the centuries.

### Cultural Significance
The bond between handler and beast is celebrated in military tradition — losing a war beast is considered equivalent to losing a comrade, and ceremonies are held for the dead. Feral beasts, by contrast, sit awkwardly in the cultural mind: they're dangerous pests, but they're also abandoned soldiers in their own right, and some people simply can't bring themselves to put them down.

### Habitat & Ecology
Feral war beasts establish territories throughout the Contested Lands, organizing in wolf-like packs of three to seven with dominant pairs leading. They hunt in coordinated formations using flanking, ambush, and signaled strikes — military tactics applied to prey. Packs from the same original unit sometimes recognize each other and reunite into larger groups. Inter-pack conflicts occur but rarely turn fatal; the animals seem to understand that killing each other wastes resources. They can be re-domesticated by handlers who know what they're doing, though the process is dangerous and time-consuming.
\column
### Tactics
- Hunt in packs (2-5 beasts)
- Use Pounce to knock down targets
- Focus on frightened enemies
- Protect handlers if trained

### Story Hooks
- A feral pack is threatening a settlement — can they be captured rather than killed?
- Someone is recapturing feral war beasts. Who, and for what purpose?
- A war beast recognizes a party member's military insignia and responds to old commands.
 
{{monster,frame
## War Beast
*Large beast, unaligned*
___
**Armor Class** :: 14 (natural armor)
**Hit Points** :: 45 (6d10 + 12)
**Speed** :: 50 ft.

___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|17 (+3) | 15 (+2) | 15 (+2) | 3 (-4) | 12 (+1) | 7 (-2)|
___
**Skills** :: Perception +3, Stealth +4
**Senses** :: passive Perception 13
**Languages** :: -
**Challenge** :: 3 (700 XP)
___
**Keen Hearing and Smell.** :: The beast has advantage on Wisdom (Perception) checks that rely on hearing or smell.

**Pack Tactics.** :: The beast has advantage on attack rolls against a creature if at least one of the beast's allies is within 5 feet of the creature and the ally isn't incapacitated.

**Trained Killer.** :: The beast was trained for war. It has advantage on attack rolls against frightened creatures.

___
### Actions
**Bite.** :: *Melee Weapon Attack:* +5 to hit, reach 5 ft., one target. *Hit:* 10 (2d6 + 3) piercing damage. If the target is a creature, it must succeed on a DC 13 Strength saving throw or be knocked prone.

**Pounce.** :: If the beast moves at least 20 feet straight toward a creature and then hits it with a bite attack on the same turn, that target must succeed on a DC 13 Strength saving throw or be knocked prone. If the target is prone, the beast can make one bite attack against it as a bonus action.

**Intimidating Howl (Recharge 5-6).** :: The beast howls. Each enemy within 30 feet that can hear it must succeed on a DC 11 Wisdom saving throw or become frightened for 1 minute. A frightened creature can repeat the save at the end of each of its turns, ending the effect on a success.

}}

<div class='pageNumber auto'></div>
<div class='footnote'>Chapter 1 - Border Creatures</div>
\page

## Haunted Battlefield

<div class="col-img">![haunted battlefield](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-haunted-battlefield.jpg) {width:325px}</div>
  
### Description
A haunted battlefield doesn't look particularly different from any other war-torn ground at first glance — churned earth, scattered debris, perhaps some remaining equipment and bones. The vegetation is often dead or stunted, but that's common in the Contested Lands. The difference becomes apparent at dusk, or by certain angles of light: ghostly figures flicker into view, phantom weapons clash, screams echo from nowhere. During full manifestation the entire battlefield comes alive — spectral armies clashing, phantom siege engines firing ethereal projectiles, the whole tragedy replaying for anyone unfortunate enough to witness it.

### Lore
When enough people die violently in one place — when their fear and rage and pain saturate the earth, when the final moment is so overwhelming that it leaves permanent impressions on reality — a haunted battlefield forms. These aren't locations with many ghosts; they are locations that have become ghosts, the land itself remembering trauma it cannot forget. By daylight, the ground looks merely war-torn; at dusk or by certain angles of light, the battle that happened here is still happening, spectral armies clashing, phantom siege engines firing, the whole tragedy replaying. The Contested Lands hold dozens of these sites, some centuries old. Consecration by clerics of Moira can suppress them temporarily, but some battlefields have been laid to rest repeatedly and always reawaken — too saturated with death to ever be truly cleansed.

### Cultural Significance
Both nations treat haunted battlefields as navigation hazards and campaign-planning constraints — fighting within one risks catastrophic supernatural casualties on top of the conventional kind. The Order of Moira considers battlefield consecration sacred work, sending teams of priests deep into the Contested Lands to perform comprehensive funeral rites while defending against the manifestations rising up to stop them.
\column
### Habitat & Ecology
Haunted battlefields are static; the horror doesn't spread or migrate, but within its boundaries it's lethal. Activation cycles are irregular though night is most common, with the area falling quiet for days or weeks between manifestations. New battlefields form periodically when particularly brutal engagements add to the region's collection of horrors. The spectral soldiers that manifest aren't intelligent undead — they're impressions, echoes, fragments of people who died there — but some battlefields appear to "remember" who fought whom, responding more violently to soldiers wearing specific insignia centuries after the fact.

{{monster,frame
## Haunted Battlefield
*Gargantuan hazard/swarm, chaotic neutral*
___
**Armor Class** :: 15
**Hit Points** :: 150 (12d20 + 24)
**Speed** :: 0 ft.

___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|1 (-5) | 20 (+5) | 14 (+2) | 10 (+0) | 14 (+2) | 16 (+3)|
___
**Damage Resistances** :: bludgeoning, piercing, slashing
**Damage Immunities** :: poison, psychic
**Condition Immunities** :: charmed, exhaustion, frightened, grappled, paralyzed, petrified, poisoned, prone, restrained, stunned, unconscious
**Senses** :: blindsight 120 ft., passive Perception 12
**Languages** :: understands all languages but can't speak
**Challenge** :: 7 (2,900 XP)
___
**Immobile Hazard.** :: The battlefield doesn't move. It exists as a 120-foot radius area of lingering death magic and tortured spirits.

**Echo of Battle.** :: Any creature that enters the area for the first time on a turn or starts its turn there must make a DC 15 Wisdom saving throw or take 14 (4d6) psychic damage and have disadvantage on attack rolls until the start of its next turn as ghostly weapons strike and spectral screams assault it.

**Restless Dead.** :: At the start of each round, 1d4 spectral soldiers (use specter statblock) manifest within the area. They attack the nearest living creatures and disappear after 1 minute or when reduced to 0 hit points.

**Consecration Vulnerable.** :: If a cleric or paladin spends 10 minutes performing funeral rites within the area, the battlefield's power is suppressed for 24 hours in a 30-foot radius around the ritual site.

___
### Actions
**Phantom Army (Recharge 5-6).** :: At initiative count 20, the battlefield can summon a phantom army. All creatures in the area see ghostly soldiers fighting and dying around them. Each creature must make a DC 15 Wisdom saving throw. On a failure, a creature takes 22 (4d10) psychic damage and is frightened until the end of its next turn. On a success, the creature takes half damage and isn't frightened.


}}

<div class='pageNumber auto'></div>
<div class='footnote'>Chapter 1 - Border Creatures</div>
\page

### Tactics
- Describe the horror and chaos
- Track who enters the area
- Roll for spectral spawns
- Allow creative solutions (not just combat)
\column
### Story Hooks
- The party must cross a haunted battlefield — what route minimizes exposure?
- A battlefield is growing, absorbing new deaths and expanding its boundaries each year.
- Someone wants to weaponize a haunted battlefield by drawing enemies into it deliberately.
- A battlefield contains something — an artifact, a body, a truth — that must be retrieved before it can ever be consecrated.


<div class='pageNumber auto'></div>
<div class='footnote'>Chapter 1 - Border Creatures</div>
\page

<div class='pageNumber auto'></div>
<div class='footnote'>Chapter 1 - Border Creatures</div>
\page

# Chapter 2 - Thaldros Military
:
The iron fist of the Thaldros Empire are disciplined soldiers, ruthless inquisitors, and devastating war machines that enforce the Emperor's will.

## Thaldros Conscript

<div class="col-img">![thaldros conscript](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-thaldros-conscript.jpg) {width:325px}</div>

### Description
Conscripts wear whatever they were given, usually ill-fitting leather armor that belonged to someone else before them, often someone who died wearing it. Their weapons are mass-produced spears designed for simplicity rather than quality. Most look exactly like what they are: farmers, laborers, and tradespeople thrust into uniforms and told to fight. Their faces tell their stories — exhaustion, fear, homesickness, the hollow look of people who didn't choose this life and don't expect to survive it.

### Lore
When volunteers aren't sufficient — and they rarely are — the Crown exercises its right of conscription. Quotas pass from provinces to towns to whoever can be spared, which in practice means the poor go to war while the wealthy buy exemptions. Conscripts are farmers, laborers, and tradespeople thrust into ill-fitting armor that often belonged to someone who died wearing it. They fight because deserters are executed, not because they believe in the cause, and most will break and run if their officers fall. They aren't cowards — they're ordinary people in extraordinary circumstances, and the only thing that makes their situation bearable is the fierce loyalty they develop for each other. Many soldiers who survive conscription remain bonded for life; just as many are mourned at the village reunions of those who came home without them.

### Cultural Significance
Conscription is one of the most contentious issues in Thaldros. Reformers argue it's a blood tax on the poor; traditionalists counter that the kingdom's defense requires sacrifice from all. Beneath both arguments simmers a quiet resentment of the professional soldiers, the officers, and the nobles who sent these farmers to die for an empire's vision they never shared.


{{monster,frame
## Thaldros Conscript
*Medium humanoid (any race), lawful neutral*
___
**Armor Class** :: 10 (no armor)
**Hit Points** :: 4 (1d8)
**Speed** :: 30 ft.

___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|10 (+0) | 10 (+0) | 10 (+0) | 9 (-1) | 10 (+0) | 9 (-1)|
___
**Senses** :: passive Perception 10
**Languages** :: Common
**Challenge** :: 1/8 (25 XP)
___
**Poorly Trained.** :: The conscript has disadvantage on attack rolls if an ally within 5 feet is reduced to 0 hit points since the end of the conscript's last turn.

**Reluctant Fighter.** :: The conscript has disadvantage on death saving throws.

___
### Actions
**Spear.** :: *Melee or Ranged Weapon Attack:* +2 to hit, reach 5 ft. or range 20/60 ft., one target. *Hit:* 3 (1d6) piercing damage, or 4 (1d8) piercing damage if used with two hands for a melee attack.
}}

### Habitat & Ecology
Conscripts are organized into mass-conscript companies under professional officers, sent to fill out the bulk of formation lines and absorb enemy attacks. They share food, cover for each other's lapses, and mourn together when comrades fall. They resent the professional soldiers who treat them as expendable, but the penalties for insubordination are severe enough that resentment rarely becomes action. In formation with 

<div class='pageNumber auto'></div>
<div class='footnote'>Chapter 2 - Thaldors Military</div>
\page

professionals, 
conscripts can hold a line adequately; alone or surprised, they panic. The army uses them as bulk — bodies to fill out formations, spears in the wall, labor for camp construction and supply movement.

### Tactics
- Fight in large groups (5-20)
- Flee if leaders fall
- May surrender if treated well
- Protect each other (poorly)

### Story Hooks
- The party encounters conscripts who beg for help deserting before the next engagement.
- A conscript unit holds crucial information about enemy movements they overheard.
- The party must convince conscripts to fight rather than flee a battle their officers have lost.
- A rescued conscript becomes a valuable ally — or a liability when their loyalty is tested.
- 
## Thaldros Soldier

<div class="col-img">![thaldros soldier](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-thaldros-soldier.jpg) {width:325px}</div>

### Description
Professional Thaldros soldiers wear standardized equipment — chain shirt, steel shield bearing the kingdom's iron crown emblem, longsword and crossbow — all well-maintained, as slovenliness is punished severely. They march in formation, respond to commands instantly, and carry themselves with trained discipline. They are physically fit, well-fed by military standards, and healthy. Most have served long enough to bear scars from training or combat, and their eyes hold the steady focus of people who have chosen military life and accepted its demands.

### Lore
Professional soldiers of Thaldros enlisted voluntarily — many from military families where service is tradition, others seeking escape from poverty or simple structure in chaotic lives. Six months to a year of rigorous training drills out the individual and drills in the formation: the shield wall, with interlocking shields creating a nearly impenetrable barrier while spears and swords strike from between gaps. Breaking a Thaldros formation requires either overwhelming force or exceptional tactics. They follow orders strictly — initiative is discouraged, and when orders conflict with reality, soldiers tend to follow orders anyway. The propaganda calls them defenders of order against chaos. The reality is more complex: some units have committed atrocities in the Contested Lands, hardened by years of conflict into something the recruitment posters do not show.
{{monster,frame

## Thaldros Soldier
*Medium humanoid (any race), lawful neutral*
___
**Armor Class** :: 16 (chain shirt, shield)
**Hit Points** :: 11 (2d8 + 2)
**Speed** :: 30 ft.

___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|13 (+1) | 12 (+1) | 12 (+1) | 10 (+0) | 11 (+0) | 10 (+0)|
___
**Skills** :: Athletics +3, Perception +2
**Senses** :: passive Perception 12
**Languages** :: Common
**Challenge** :: 1/2 (100 XP)
___
**Formation Fighter.** :: The soldier has advantage on saving throws against being frightened while within 5 feet of an ally.

**Imperial Discipline.** :: The soldier can reroll a failed saving throw once per short rest.

___
### Actions
**Longsword.** :: *Melee Weapon Attack:* +3 to hit, reach 5 ft., one target. *Hit:* 5 (1d8 + 1) slashing damage, or 6 (1d10 + 1) slashing damage if used with two hands.

**Crossbow.** :: *Ranged Weapon Attack:* +3 to hit, range 80/320 ft., one target. *Hit:* 5 (1d8 + 1) piercing damage.

### Reactions
**Shield Wall.** :: When an ally within 5 feet is hit by an attack, the soldier can grant them +2 to AC against that attack.

}}

<div class='pageNumber auto'></div>
<div class='footnote'>Chapter 2 - Thaldors Military</div>
\page

### Cultural Significance
Professional soldiers occupy a respected but complex social position — above common laborers, below even minor nobility. They have regular income but little freedom, are honored in abstract but often avoided in person. Veterans receive privileges and a small pension; civilians give them a wide berth.

### Habitat & Ecology
Soldiers sign contracts of typically five to ten years and serve in garrisons, frontier patrols, or campaign armies as needs dictate. Off-duty, they maintain barracks camaraderie — drinking, gambling, training, and complaining about officers. Military culture emphasizes loyalty to unit, respect for rank, and absolute obedience to orders. Individual initiative is discouraged; collective action is rewarded. This produces reliable soldiers but also limits adaptation when circumstances change. Most plan to complete their contracts and return to civilian life with veteran benefits; a few become career soldiers who know no other life.

### Tactics
- Fight in formation (shield wall)
- Support allies
- Follow orders strictly
- Retreat only when commanded

### Story Hooks
- A soldier patrol stops the party at a checkpoint with orders that have just changed.
- Soldiers offer information in exchange for help with a problem they can't bring to their officers.
- The party must penetrate or evade a Thaldros formation guarding a critical objective.
- A disillusioned soldier seeks to desert but needs help escaping the army's reach.
 

## Iron Legion Enforcer

### Description
Iron Legion enforcers dress for intimidation rather than protection — black leather armor, iron-studded gloves, heavy boots, and masks or helmets that conceal identity. They carry maces and clubs designed to break bones rather than kill quickly, though they are perfectly capable of killing when ordered. They are built for violence: large, muscular, with the scarred hands and confident movements of people experienced in hurting others. Their presence in a crowd creates immediate tension — people step aside, conversations fall silent.

### Lore
The Iron Legion is Thaldros's internal security force — police, secret police, and state enforcer combined — answering directly to the Crown rather than military command. Recruitment emphasizes loyalty and willingness to follow orders without question, drawing heavily from former criminals, failed soldiers, and those who simply enjoy power over others. Enforcers dress for intimidation rather than protection: black leather, iron-studded gloves, helmets that conceal identity, and maces designed to break bones rather than kill quickly. They prefer intimidation to outright violence — scared populations are easier to control than injured ones — and make public examples of a few to cow the many. Reformers consistently argue for the Legion's dissolution; the Crown consistently refuses. The Legion is too useful for maintaining power, and everyone involved knows it.

<div class="col-img">![iron legion enforcer](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-iron-legion-enforcer.jpg) {width:325px}</div>

### Cultural Significance
Legion members are socially isolated. Other soldiers distrust them, civilians fear them, and even their families often don't know the details of their work. This isolation creates intense internal loyalty — the Legion becomes the only community that accepts them — and senior enforcers have usually done things they can never acknowledge publicly.

### Habitat & Ecology
The Legion operates its own intelligence network separate from military intelligence, maintaining informant networks in every major city to track dissent, suspicious activity, and threats to state stability. 

<div class='pageNumber auto'></div>
<div class='footnote'>Chapter 2 - Thaldors Military</div>
\page

Enforcers work in pairs or groups, backing each other and coordinating to overwhelm targets. Off-duty, many struggle with the gap between their public role and private selves — some become the brutal thugs they pretend to be, while others maintain careful separation, treating enforcement as a job rather than an identity. Advancement requires demonstrated loyalty and effectiveness, and senior enforcers have usually done things they can never publicly acknowledge.

### Tactics
- Use intimidation liberally
- Beat down resisters
- Work in pairs or groups
- Make examples of defiers

### Story Hooks
- The party attracts Iron Legion attention for activities that could be interpreted as suspicious.
- An enforcer offers information in exchange for help with a personal problem.
- The party must evade or infiltrate a Legion operation that intersects with their goals.
- A former enforcer seeks redemption but is being hunted by former colleagues.
 
{{monster,frame
## Iron Legion Enforcer
*Medium humanoid (any race), lawful evil*
___
**Armor Class** :: 13 (leather armor)
**Hit Points** :: 32 (5d8 + 10)
**Speed** :: 30 ft.

___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|15 (+2) | 11 (+0) | 14 (+2) | 10 (+0) | 12 (+1) | 14 (+2)|
___
**Skills** :: Intimidation +4, Perception +3
**Senses** :: passive Perception 13
**Languages** :: Common
**Challenge** :: 2 (450 XP)
___
**Brutal.** :: The enforcer's melee weapon attacks deal one extra die of damage (included in the attacks).
**Pack Tactics.** :: The enforcer has advantage on attack rolls against a creature if at least one of the enforcer's allies is within 5 feet of the creature and the ally isn't incapacitated.
___
### Actions
**Multiattack.** :: The enforcer makes two attacks with its mace.
**Mace.** :: *Melee Weapon Attack:* +4 to hit, reach 5 ft., one target. *Hit:* 9 (2d6 + 2) bludgeoning damage.
**Intimidate.** :: The enforcer targets one creature it can see within 30 feet. The target must succeed on a DC 12 Wisdom saving throw or become frightened for 1 minute. A frightened target can repeat the save at the end of each of its turns, ending the effect on a success.

}}

\column

## Royal Guard Elite

<div class="col-img">![royal guard elite](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-royal-guard-elite.jpg) {width:325px}</div>

### Description
Royal Guard elites represent military excellence made visible. Their plate armor is functional but immaculately maintained, bearing personal heraldry alongside the iron crown. Their weapons are quality steel, often heirloom pieces passed down through military families, and they carry themselves with earned confidence. Their faces show intelligence and discipline; their movements are efficient — no wasted motion, no unnecessary display. They don't need to intimidate; their reputation precedes them.

### Lore
Selection for the Royal Guard is extraordinarily competitive — candidates must demonstrate exceptional combat skill, tactical intelligence, and character, with at least five years of distinguished service in regular units. Those who pass undergo additional training in close protection, noble custom, and court etiquette, and are thoroughly vetted for any compromising connection. The result is Thaldros's ideal soldier: skilled, disciplined, honorable, loyal. Crucially, their oath is to Thaldros and its legitimate government — not to whichever person currently wears the crown — a distinction that has mattered greatly during succession disputes. Unlike Iron Legion enforcers, Guard elites are

<div class='pageNumber auto'></div>
<div class='footnote'>Chapter 2 - Thaldors Military</div>
\page

respected by common soldiers and civilians alike. They are protectors, not oppressors, and their reputation is carefully cultivated and just as carefully earned.

### Cultural Significance
Guard membership confers significant social status — roughly equivalent to minor nobility — and many guards come from noble families to begin with. They form a tight community, often marry within guard families, and transition smoothly into comfortable retirement positions: security consulting, training roles, noble household service. They are the empire's polished face.

### Habitat & Ecology
Guards are assigned to protect royalty, secure important locations, and handle sensitive missions across the empire and abroad. They train together, socialize together, and form a tight intergenerational community. Their oath binds them to Thaldros as a concept rather than to whichever person currently wears the crown — a distinction that has mattered during succession disputes more than once. Retirement typically leads to comfortable positions: security consulting, training roles, noble household service. Arrogance is weeded out during selection; the Guard's reputation depends on its members remaining humble about their abilities.

### Tactics
- Protect VIPs at all costs
- Use Leadership to buff allies
- Fight honorably but effectively
- Coordinate attacks

### Story Hooks
- Guard elites are assigned to escort the party on a sensitive mission with restrictions they don't explain.
- The party must get past or through a Guard defensive position without bloodshed.
- A Guard elite has been given orders they're struggling to obey, and seeks outside counsel.
- Retirement from the Guard has left an elite directionless and seeking purpose — at any cost.

{{monster,frame
## Royal Guard Elite
*Medium humanoid (any race), lawful neutral*
___
**Armor Class** :: 18 (plate armor)
**Hit Points** :: 52 (8d8 + 16)
**Speed** :: 30 ft.

___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|16 (+3) | 11 (+0) | 14 (+2) | 11 (+0) | 11 (+0) | 15 (+2)|
___
**Saving Throws** :: Constitution +4, Wisdom +2
**Skills** :: Athletics +5, Intimidation +4, Perception +2
**Senses** :: passive Perception 12
**Languages** :: Common
**Challenge** :: 5 (1,800 XP)
___
**Brave.** :: The guard has advantage on saving throws against being frightened.

**Royal Authority.** :: Allied creatures within 10 feet gain advantage on saving throws against being frightened.

___
### Actions
**Multiattack.** :: The guard makes two greatsword attacks.

**Greatsword.** :: *Melee Weapon Attack:* +5 to hit, reach 5 ft., one target. *Hit:* 10 (2d6 + 3) slashing damage.

**Heavy Crossbow.** :: *Ranged Weapon Attack:* +2 to hit, range 100/400 ft., one target. *Hit:* 5 (1d10) piercing damage.

**Leadership (Recharges after a Short or Long Rest).** :: For 1 minute, the guard can utter a command or warning whenever a nonhostile creature within 30 feet makes an attack roll or saving throw. That creature can add a d4 to its roll. A creature can benefit from only one Leadership die at a time.

### Reactions
**Parry.** :: The guard adds 2 to their AC against one melee attack that would hit them.
}}

<div class='pageNumber auto'></div>
<div class='footnote'>Chapter 2 - Thaldors Military</div>
\page

## State Inquisitor

<div class="col-img">![state inquisitor](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-state-inquisitor.jpg) {width:325px}</div>

### Description
State Inquisitors dress to blend in, or to intimidate, depending on the current role. Undercover, they are indistinguishable from merchants, scholars, servants, or whatever cover serves the mission. When operating openly, they wear distinctive dark clothing with official insignia, carrying an immediate threat of state authority. They move quietly, observe constantly, and reveal nothing in their expressions. Years of intelligence work have taught them to control every tell — looking at an Inquisitor's face tells you exactly what they want you to know, and nothing more.

### Lore
The State Inquisition is officially denied and unofficially acknowledged — everyone knows Thaldros has spies; no one admits the details, and that ambiguity is itself a tool. Inquisitors are recruited from military intelligence, academia, criminal rehabilitation, and the streets, selected for aptitude, intelligence, discretion, and absolute loyalty to Thaldros's interests. Training covers infiltration, interrogation, surveillance, code-breaking, and assassination (never officially acknowledged). They operate with minimal oversight, trusted to make decisions in the field and held accountable for results rather than methods. Many live double lives, with families who believe them merchants or diplomats. 

{{monster,frame
## State Inquisitor
*Medium humanoid (any race), lawful evil*
___
**Armor Class** :: 15 (studded leather)
**Hit Points** :: 78 (12d8 + 24)
**Speed** :: 30 ft.

___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|11 (+0) | 16 (+3) | 14 (+2) | 16 (+3) | 14 (+2) | 16 (+3)|
___
**Saving Throws** :: Dexterity +6, Intelligence +6, Wisdom +5
**Skills** :: Deception +6, Insight +5, Investigation +9, Perception +5, Stealth +6
**Senses** :: passive Perception 15
**Languages** :: Common, plus three others
**Challenge** :: 6 (2,300 XP)
___
**Cunning Action.** :: On each turn, the inquisitor can use a bonus action to Dash, Disengage, or Hide.

**Evasion.** :: If the inquisitor is subjected to an effect that allows them to make a Dexterity saving throw to take only half damage, they take no damage on a success and half damage on a failure.

**Sneak Attack (1/Turn).** :: The inquisitor deals an extra 14 (4d6) damage when hitting with a weapon attack and has advantage on the attack roll, or when the target is within 5 feet of an ally.

**Information Network.** :: The inquisitor can spend 1 hour in a settlement to learn one piece of useful information about a specific person or event.

___
### Actions
**Multiattack.** :: The inquisitor makes two shortsword attacks.

**Shortsword.** :: *Melee Weapon Attack:* +6 to hit, reach 5 ft., one target. *Hit:* 6 (1d6 + 3) piercing damage, plus poison (see Poisoned Blade).

**Hand Crossbow.** :: *Ranged Weapon Attack:* +6 to hit, range 30/120 ft., one target. *Hit:* 6 (1d6 + 3) piercing damage, plus poison (see Poisoned Blade).

**Poisoned Blade.** :: The inquisitor's weapon is coated in a special poison. The target must make a DC 14 Constitution saving throw, taking 10 (3d6) poison damage on a failed save, or half as much on a success.

**Interrogate (3/Day).** :: The inquisitor targets one creature within 30 feet that can hear them. The target must make a DC 14 Wisdom saving throw. On a failure, the target is compelled to answer one question truthfully. This is a magical compulsion effect.

### Reactions
**Uncanny Dodge.** :: When an attacker the inquisitor can see hits them with an attack, they can halve the attack's damage.
}}

<div class='pageNumber auto'></div>
<div class='footnote'>Chapter 2 - Thaldors Military</div>
\page

Their information network is the most extensive in Tirvandor, embedded in Aethoria, the Contested Lands, criminal organizations, and even allied institutions. The fear of attracting their attention moderates public dissent across the empire — exactly as intended.

### Cultural Significance
The Inquisition's mere rumored presence is its primary weapon. People watch their words in taverns, in shops, even in their own homes — knowing that the wrong comment overheard by the wrong listener might bring scrutiny no one returns from cleanly. This chilling effect is deliberate and self-reinforcing; few citizens have ever met an Inquisitor, but everyone has been told by a friend who has.

### Habitat & Ecology
Inquisitors operate everywhere — embedded in Aethoria as merchants and diplomats, in the Contested Lands as informants and handlers, in criminal organizations as bought-off lieutenants, and even in allied institutions where their masters need eyes. They are patient, sometimes spending months or years developing a single operation. They answer to the Crown through a structure deliberately obscured from external view; even most government officials don't know the full extent of Inquisition operations. Some have no personal lives at all, consumed entirely by their work; others maintain elaborate covers and visit "families" who never learn what they actually do.

### Tactics
- Gather intelligence first
- Poisoned weapons on priority targets
- Use Interrogate to extract info
- Escape if discovered

### Story Hooks
- An Inquisitor approaches the party with an offer they can't quite refuse.
- The party discovers they're being surveilled by agents who know things they shouldn't.
- An Inquisitor's mission has gone catastrophically wrong and they need extraction.
- The party must counter an Inquisition operation without being identified — or remembered.

## War Mage of Thaldros

### Description
War mages wear military robes over light armor — practical rather than ostentatious. Their staves are reinforced for melee use if necessary, and they carry component pouches, scrolls, and backup wands with military efficiency. Nothing about their appearance is decorative. They stand apart from regular soldiers, occupying an uncomfortable middle ground between military hierarchy and magical tradition, and most show the strain of it — the discipline of a soldier combined with the independence of a mage, fully accepted by neither culture.

<div class="col-img">![war mage of thaldros](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-war-mage-of-thaldros.jpg) {width:325px}</div>

### Lore
Thaldros's military academies train mages specifically for battlefield application — evocation for destruction, abjuration for protection, minimal time wasted on impractical schools. Training emphasizes discipline and reliability over raw power; a war mage who consistently delivers effective results is more valuable than a genius who's unpredictable. They occupy an awkward social position: regular soldiers respect their power but distrust magic, commanders value their capabilities but rarely understand their limitations, and academic mages look down on their "crude" applications of magical theory. They stay behind the front line, conserving power for decisive applications, countering enemy magic, and timing fireballs to break formations rather than burn random skirmishers. The achievement Thaldros has made — successfully subordinating magical capability to military command — is viewed by independent mages as a kind of slavery, reducing magical potential to serve mundane wars.

<div class='pageNumber auto'></div>
<div class='footnote'>Chapter 2 - Thaldors Military</div>
\page

### Cultural Significance
Most war mages find community primarily with each other — the only people who understand their unique circumstances. They share tactical innovations, complain about commanders who can't tell *fireball* from *fire bolt*, and remember those who fell. A few rise to become trusted advisors to generals; the rest remain line soldiers with unusual capabilities and few peers.

### Habitat & Ecology
War mages are attached to specific military units rather than operating independently, answering to military commanders (who often don't understand magic) while maintaining standards set by the Magical Corps. They are trained to work within military structures, accept orders, and subordinate their magical instincts to tactical requirements. Communities of war mages exist within the Corps itself — small fraternities that meet between deployments to share innovations, complain about their commanders, and remember the ones who fell. Advancement depends partly on magical skill and partly on political navigation between the soldier and academic worlds, neither of which fully claims them.

### Tactics
- Stay behind front line
- Use *fireball* and *lightning bolt* on groups
- *Counterspell* enemy magic
- *Misty step* away from danger
- Conserve 5th level slot for emergency

### Story Hooks
- A war mage unit is the key to an enemy formation's strength — neutralize them and the line breaks.
- The party must recruit or eliminate war mages before a coming battle changes everything.
- A war mage's orders conflict with their understanding of magical ethics, and they want out.
- An encounter with academic mages creates tensions about what magic is *for*.

{{monster,frame
## War Mage of Thaldros
*Medium humanoid (any race), lawful neutral*
___
**Armor Class** :: 12 (15 with *mage armor*)
**Hit Points** :: 66 (12d8 + 12)
**Speed** :: 30 ft.
___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|9 (-1) | 14 (+2) | 12 (+1) | 17 (+3) | 12 (+1) | 11 (+0)|
___
**Saving Throws** :: Intelligence +6, Wisdom +4
**Skills** :: Arcana +6, History +6
**Senses** :: passive Perception 11
**Languages** :: Common, plus three others
**Challenge** :: 7 (2,900 XP)
___
**Spellcasting.** :: The mage is a 9th-level spellcaster. Spellcasting ability is Intelligence (spell save DC 14, +6 to hit with spell attacks). The mage has the following wizard spells prepared:

Cantrips (at will): *fire bolt, light, mage hand, prestidigitation* ::
1st level (4 slots): *detect magic, mage armor, magic missile, shield* ::
2nd level (3 slots): *misty step, scorching ray, suggestion* ::
3rd level (3 slots): *counterspell, fireball, lightning bolt* ::
4th level (3 slots): *greater invisibility, ice storm* ::
5th level (1 slot): *cone of cold, wall of force* ::

**War Caster.** :: The mage has advantage on Constitution saving throws to maintain concentration on spells. When a hostile creature's movement provokes an opportunity attack, the mage can cast a spell at the creature rather than making an opportunity attack.

___
### Actions
**Quarterstaff.** :: *Melee Weapon Attack:* +2 to hit, reach 5 ft., one target. *Hit:* 2 (1d6 - 1) bludgeoning damage, or 3 (1d8 - 1) if used with two hands.
}}

<div class='pageNumber auto'></div>
<div class='footnote'>Chapter 2 - Thaldors Military</div>
\page

## Siege Golem

<div class="col-img">![siege golem](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-siege-golem.jpg) {width:325px}</div>

### Description
Siege golems are massive constructs, twelve to fifteen feet tall, humanoid in general shape but built for destruction rather than imitation of life. Their bodies are reinforced stone and iron, designed to withstand the punishment of siege warfare. Their arms end in weapons rather than hands — battering rams, boulder launchers, or crushing implements depending on specific design. Their legs are thick columns providing stable platforms for their devastating attacks. Their "faces" are minimal: just enough features to suggest direction, with glowing eyes providing magical sight. They move slowly but inexorably, each step shaking the ground.

### Lore
Thaldros war mages created siege golems to solve a specific problem: fortifications. Conventional siege warfare is expensive, time-consuming, and costly in lives — golems provide an alternative that can breach walls, absorb defensive fire, and clear fortifications without risking irreplaceable soldiers. Twelve to fifteen feet tall, with arms ending in battering rams or boulder launchers rather than hands, they advance with each step shaking the ground and "faces" reduced to glowing eyes that provide magical sight. Each one represents months of work by skilled artificers, rare materials, and significant magical investment; despite being constructs, they aren't expendable. They follow tactical orders with perfect obedience and no initiative, executing complex battle plans flawlessly but unable to adapt when circumstances change. The materials and techniques for their creation are closely guarded state secrets that other nations have never replicated.

{{monster,frame
## Siege Golem
*Large construct, unaligned*
___
**Armor Class** :: 17 (natural armor)
**Hit Points** :: 157 (15d10 + 75)
**Speed** :: 20 ft.

___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|22 (+6) | 9 (-1) | 20 (+5) | 3 (-4) | 11 (+0) | 1 (-5)|
___
**Damage Immunities** poison, psychic; bludgeoning, piercing, and slashing from nonmagical attacks not made with adamantine weapons
**Condition Immunities** charmed, exhaustion, frightened, paralyzed, petrified, poisoned
**Senses** :: darkvision 120 ft., passive Perception 10
**Languages** :: understands the languages of its creator but can't speak
**Challenge** :: 8 (3,900 XP)
___
**Immutable Form.** :: The golem is immune to any spell or effect that would alter its form.

**Magic Resistance.** :: The golem has advantage on saving throws against spells and other magical effects.

**Siege Monster.** :: The golem deals double damage to objects and structures.

**Military Programming.** :: The golem follows tactical commands perfectly and can execute complex battle plans.

___
### Actions
**Multiattack.** :: The golem makes two slam attacks.

**Slam.** :: *Melee Weapon Attack:* +10 to hit, reach 5 ft., one target. *Hit:* 19 (3d8 + 6) bludgeoning damage.

**Boulder Launch (Recharge 5-6).** :: *Ranged Weapon Attack:* +10 to hit, range 60/240 ft., one target. *Hit:* 32 (4d12 + 6) bludgeoning damage. If the target is a structure, it takes double damage.

**Siege Mode (1/Day).** :: For 1 minute, the golem becomes rooted in place (speed 0) but gains advantage on attack rolls and its attacks deal maximum damage to structures.
}}

### Habitat & Ecology
Siege golems are stored in fortified workshops at major Thaldros garrisons, maintained between deployments by teams of artificers who know more about each individual unit than its commanding officers do. They have no intelligence beyond their programming — they don't think, feel, or choose; they execute commands until those commands are completed or 

<div class='pageNumber auto'></div>
<div class='footnote'>Chapter 2 - Thaldors Military</div>
\page

countermanded. They do have some problem-solving capability for navigating obstacles and identifying targets, but it's mechanical rather than cognitive, and they can be confused by circumstances their programming doesn't address. Damaged golems require expensive repairs that can take weeks; destroyed ones represent significant lost investment that bureaucrats remember long after the campaign ends.

### Cultural Significance
Siege golems represent Thaldros military-magical cooperation at its finest, a technological advantage other nations have failed for generations to copy. They are also controversial — some see them as appropriate military tools, others as monstrous perversions of the magical arts. Either way, their crawl across the horizon means a city's walls are no longer its protection.

### Tactics
- Advance slowly and steadily
- Focus on structures in Siege Mode
- Target clustered enemies with Boulder Launch
- Ignore distractions

### Story Hooks
- A siege golem is approaching a location the party must defend — and time is measured in days, not weeks.
- The party must disable a golem before it breaches critical defenses.
- Someone is trying to steal golem-creation secrets, and the artificer guild needs help.
- A golem's programming has been compromised — by accident, or sabotage — and it no longer answers to its commanders.

## General's Champion

### Description
Champions are physical specimens: tall, powerfully built, marked by years of intensive training and successful combat. Their armor is personalized, combining military functionality with individual distinction. Their weapons are masterwork quality, often magical, and always well-maintained. They carry themselves with earned confidence — not arrogance, but the certainty of people who have proven themselves against the best opponents available. Most bear extensive scarring from their careers, displayed with pride rather than concealed.

### Lore
When Thaldros generals face problems requiring individual 
excellence rather than unit strength, they send champions — warriors 
selected from the best soldiers across the military, then given 
advanced training, superior equipment, and the most challenging 
assignments. Champions serve individual generals rather than the 
military structure, which creates complicated loyalties: they're 
soldiers of Thaldros, but their immediate allegiance is to their 
patron. Smart generals earn genuine loyalty through fair treatment; 
others rely on contracts and ambition. Champions seek the strongest 
enemies and break formations through personal assault, fighting 
honorably by their own definition — which includes lethal efficiency 
and ruthless exploitation of any advantage. Their presence on a 
battlefield affects morale on both sides. A general with an exceptional 
champion gains reputation; losing one is a significant embarrassment 
that can damage careers.

<div class="col-img">![general's champion](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-generals-champion.jpg) {width:325px}</div>

### Habitat & Ecology
Champions serve as their generals' representatives off the battlefield as well as on — negotiating with allies, intimidating enemies, and handling situations requiring a personal touch backed by implicit violence. They form a loose community across general affiliations, sharing respect and rivalry; inter-champion competitions are legendary though rarely fatal, since killing a peer's champion creates political complications that ripple through the officer corps for years. A champion who ages out of prime capability faces an awkward adjustment — positions of lesser physical demand but continued relevance, such as training the next generation or advising at court.

<div class='pageNumber auto'></div>
<div class='footnote'>Chapter 2 - Thaldors Military</div>
\page

{{monster,frame
## General's Champion
*Medium humanoid (any race), lawful neutral*
___
**Armor Class** :: 18 (plate armor)
**Hit Points** :: 143 (22d8 + 44)
**Speed** :: 30 ft.

___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|20 (+5) | 15 (+2) | 14 (+2) | 10 (+0) | 14 (+2) | 12 (+1)|
___
**Saving Throws** :: Strength +9, Constitution +6
**Skills** :: Athletics +9, Intimidation +5, Perception +6
**Senses** :: passive Perception 16
**Languages** :: Common
**Challenge** :: 9 (5,000 XP)
___
**Indomitable (2/Day).** :: The champion can reroll a saving throw. They must use the new roll.

**Second Wind (Recharges after a Short or Long Rest).** :: As a bonus action, the champion can regain 20 hit points.

___
### Actions
**Multiattack.** :: The champion makes three attacks with their greatsword or longbow.

**Greatsword.** :: *Melee Weapon Attack:* +9 to hit, reach 5 ft., one target. *Hit:* 12 (2d6 + 5) slashing damage.

**Longbow.** :: *Ranged Weapon Attack:* +6 to hit, range 150/600 ft., one target. *Hit:* 6 (1d8 + 2) piercing damage.

**Rally (Recharges after a Short or Long Rest).** :: The champion rallies their allies. Each ally within 30 feet regains 10 hit points and gains advantage on their next attack roll or saving throw.

### Reactions
**Parry.** :: The champion adds 4 to their AC against one melee attack that would hit them.
}}

### Cultural Significance
Champions form a loose community across general affiliations, sharing respect and rivalry. Inter-champion competitions are legendary, though rarely fatal — killing a peer's champion creates political complications that ripple through the officer corps for years. The heroic ideal they represent inspires recruitment and training even as the realities of patron politics shape every move they make.

### Tactics
- Challenge the strongest enemy
- Use Rally to support troops
- Fight honorably but ruthlessly
- Never surrender

### Story Hooks
- A champion is sent to deal with the party as a special problem requiring personal attention.
- The party must challenge or defeat a champion to achieve a larger objective.
- A champion seeks worthy opponents — the party's growing reputation has drawn their notice.
- A retired champion offers training or assistance in exchange for suitable compensation — or a final mission.
- 
## Iron Crown Knight

<div class="col-img">![iron crown knight](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-iron-crown-knight.jpg) {width:325px}</div>

### Description
Iron Crown Knights wear their oath in their equipment: plate armor adorned with iron crown symbolism, shields bearing order insignia, weapons consecrated to their harsh philosophy. Their heraldry emphasizes authority and power — images of crowns, chains, and law. Their faces often reflect their philosophy's costs: hard eyes, grim expressions, the look of people who've made peace with doing unpleasant things for necessary reasons. They are not cruel by nature, but have grown comfortable with cruelty when they deem it necessary.

### Lore
The Iron Crown is a paladin order sworn to maintaining civilization 
through strength. Its knights believe that order is inherently good, 
that chaos leads to suffering, and that strong authority — even harsh 
authority — is preferable to the alternatives. Their powers come from 

<div class='pageNumber auto'></div>
<div class='footnote'>Chapter 2 - Thaldors Military</div>
\page

conviction rather than divine favor in the traditional sense; they 
believe they serve the gods of order, though whether those gods actually 
endorse their interpretation is theologically debated. 

Their armor and shields bear crowns, chains, and law, and their 
faces often show the philosophy's costs: hard eyes, grim expressions, 
the look of people who've made peace with doing unpleasant things for 
necessary reasons. Reformers view them as dangerous extremists; 
traditionalists see them as faithful guardians. Most people simply 
prefer not to think about them at all, and few are eager to test 
their Channel Divinity in person.

### Cultural Significance
The order maintains monasteries and chapter houses throughout Thaldros, serving as both military reserves and ideological centers. Knights regularly return for training, meditation, and reinforcement of their philosophy. They're politically connected but carefully nonpartisan, serving Thaldros rather than any faction — a neutrality that grants freedom of action while breeding suspicion from those who want specific loyalty.

### Habitat & Ecology
The order is organized into chapter houses, each led by a master who answers to the Grand Master at the central monastery in Kaer Thandros. Knights rotate between assignment (enforcement, escort, frontier duty) and retreat (training, meditation, philosophical study). Many people find Iron Crown Knights frightening even when they're theoretically allies — their certainty, their willingness to act on their philosophy, and their supernatural abilities create uncomfortable interactions. Among themselves, they speak of their oath as both burden and gift, and recruit carefully, knowing that any knight who breaks faith taints the entire order.

### Tactics
- Use Aura of Tyranny to buff allies
- Command the battlefield
- Iron Command at start of combat
- Protect important allies

### Story Hooks
- Iron Crown Knights are enforcing something the party morally opposes.
- A knight's faith is shaken by encountering something that doesn't fit their philosophy.
- The order has targeted the party or their allies as "agents of chaos" to be neutralized.
- A former knight seeks redemption for actions taken under the order's authority.

{{monster,frame
## Iron Crown Knight
*Medium humanoid (any race), lawful evil*
___
**Armor Class** :: 20 (plate armor +2, shield)
**Hit Points** :: 153 (18d8 + 72)
**Speed** :: 30 ft.

___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|19 (+4) | 11 (+0) | 18 (+4) | 12 (+1) | 14 (+2) | 16 (+3)|
___
**Saving Throws** :: Constitution +8, Wisdom +6, Charisma +7
**Skills** :: Athletics +8, Intimidation +7, Religion +5
**Damage Resistances** necrotic
**Condition Immunities** frightened
**Senses** :: passive Perception 12
**Languages** :: Common
**Challenge** :: 10 (5,900 XP)
___
**Aura of Tyranny (10 ft.).** :: Allied creatures within 10 feet deal an extra 1d4 damage on weapon attacks. Enemy creatures have disadvantage on saving throws against being frightened.

**Iron Will.** :: The knight has advantage on saving throws against being charmed or frightened.

**Spellcasting.** :: The knight is a 12th-level spellcaster (Oath of the Iron Crown subclass). Spellcasting ability is Charisma (spell save DC 15, +7 to hit). Prepared spells:

1st level (4 slots): *command, compelled duel, shield of faith* ::
2nd level (3 slots): *zone of truth, hold person* ::
3rd level (3 slots): *dispel magic, fear* ::

___
### Actions
**Multiattack.** :: The knight makes two longsword attacks.

**Longsword +2.** :: *Melee Weapon Attack:* +10 to hit, reach 5 ft., one target. *Hit:* 10 (1d8 + 6) slashing damage, or 11 (1d10 + 6) slashing damage if used with two hands.

**Channel Divinity: Iron Command (1/Day).** :: Each hostile creature within 30 feet must make a DC 15 Wisdom saving throw. On a failure, the creature is paralyzed until the end of the knight's next turn.

### Reactions
**Oath of Protection.** :: When a creature within 5 feet is hit by an attack, the knight can make that attack target them instead.
}}



<div class='pageNumber auto'></div>
<div class='footnote'>Chapter 2 - Thaldors Military</div>
\page
  
## Lord Commander Varius

<div class="col-img">![lord commander varius](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-lord-commander-varius-military-leader.jpg) {width:325px}</div>

### Description
Lord Commander Varius appears exactly as a supreme military commander should — tall, imposing, marked by decades of campaign experience without being weakened by it. His armor is masterwork quality bearing ancient military honors. His weapons are legendary items with their own histories. His face shows intelligence, determination, and the weight of countless decisions. He is older than he looks, somewhere past sixty, but maintains his condition through discipline and (rumors suggest) magical assistance. His eyes are his most notable feature: assessing, calculating, seeing tactical implications in everything.

### Lore
Varius rose from minor nobility through decades of service — winning battles considered unwinnable, salvaging campaigns others had abandoned, and developing tactical innovations that changed how Thaldros fights. Now somewhere past sixty (though maintained in fighting condition by discipline and, rumor suggests, magical assistance), he holds the position of Lord Commander, supreme military authority answering only to the Crown. He has served three monarchs in this role and provided continuity through their 
successions. His reputation crosses factional lines; even Aethorian commanders acknowledge his capabilities. His loyalty is to Thaldros as a concept rather than to individual monarchs, and his principled neutrality frustrates reformers who want him to 
take sides on controversial military policies. The military is his family; command is his purpose. He has outlived a wife and children and converted grief into focused dedication.

### Cultural Significance
Varius is the most respected military figure in Thaldros, and one of the most respected on Tirvandor. He's used in propaganda, cited in training manuals, and held up as the example of what dedicated service can achieve. Young officers dream of following his path; older ones, who know what the path actually cost, hope quietly that their sons don't. He's also controversial among reformers who see him as enabling problematic military policies through his very competence — every order he carries out cleanly is one more order no one questioned.

### Habitat & Ecology
Varius maintains his headquarters in Kaer Thandros but spends substantial time on circuit through frontier garrisons, where he inspects units personally, listens to officer reports, and makes himself accessible to common soldiers. He maintains carefully managed relationships with political powers while preserving military independence — he serves the Crown, but he is no one's tool. His personal life is minimal: the military is his family, command is his purpose. He has outlived a wife and children and converted grief into focused dedication. Subordinates report that he remembers the names of every officer who served under him, and that he writes personal letters to the families of every officer who died.

### Tactics
- Command the battlefield
- Use Tactical Genius and Legendary Actions to control action economy
- Rally troops when needed
- Lead from the front but strategically
- Respect worthy opponents

### Story Hooks
- An encounter with Varius forces the party to reconsider their assumptions about Thaldros itself.
- Varius offers the party assistance, with conditions that complicate their goals.
- The party must somehow oppose or evade the full weight of Thaldros military power that Varius commands.
- Intelligence suggests Varius is considering a decision that could change everything — and someone wants to influence which way he goes.

<div class='pageNumber auto'></div>
<div class='footnote'>Chapter 2 - Thaldors Military</div>
\page

{{monster,frame
## Lord Commander Varius
*Medium humanoid (human), lawful neutral*
___
**Armor Class** :: 21 (plate armor +3, shield +1)
**Hit Points** :: 187 (22d8 + 88)
**Speed** :: 30 ft.

___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|20 (+5) | 14 (+2) | 18 (+4) | 16 (+3) | 16 (+3) | 18 (+4)|
___

**Saving Throws** :: Strength +10, Constitution +9, Wisdom +8, Charisma +9
**Skills** :: Athletics +10, History +8, Insight +8, Intimidation +9, Perception +8
**Damage Resistances** all damage from spells
**Condition Immunities** frightened
**Senses** :: passive Perception 18
**Languages** :: Common, plus four others
**Challenge** :: 13 (10,000 XP)
___
**Legendary Resistance (3/Day).** :: If Varius fails a saving throw, he can choose to succeed instead.

**Supreme Commander.** :: Allied creatures within 60 feet have advantage on saving throws against being frightened and add 1d6 to damage rolls.

**Tactical Genius.** :: Varius can take a special reaction at initiative count 20 (losing ties) to command an ally within 60 feet to immediately take an action.

**Magic Resistance.** :: Varius has advantage on saving throws against spells and other magical effects.
___
### Actions
**Multiattack.** :: Varius makes three longsword attacks.

**Longsword of Command +3.** :: *Melee Weapon Attack:* +13 to hit, reach 5 ft., one target. *Hit:* 12 (1d8 + 8) slashing damage, or 13 (1d10 + 8) slashing damage if used with two hands, plus 9 (2d8) radiant damage.

**Javelin of Lightning +2.** :: *Ranged Weapon Attack:* +9 to hit, range 30/120 ft., one target. *Hit:* 7 (1d6 + 4) piercing damage plus 9 (2d8) lightning damage.

**Commanding Shout (Recharge 5-6).** :: Varius issues a tactical command. Each ally within 60 feet can immediately move up to half their speed and make one weapon attack as a reaction.

### Legendary Actions
**Move.** :: Varius moves up to half his speed.

**Attack.** :: Varius makes one longsword attack.

**Rally (Costs 2 Actions).** :: Each ally within 30 feet regains 15 hit points and gains advantage on their next attack roll.

**Tactical Reposition (Costs 3 Actions).** :: Varius and up to four allies within 60 feet can move up to their speed without provoking opportunity attacks.
}}

\column

### Whispers from the Camp
> *"He stood at the gates of Skellholm for nine days. We expected reinforcements; he expected us to hold. We held."*  
> — Captain Jarra, Third Iron Lance

> *"I sat across from him at a parley. He thanked me, by name, for my service to my people. Then he sent his army through us anyway. He thanked me again at the burial."*  
> — Aethorian commander, name withheld

> *"He's outlived everyone who knew him as a boy. There's a kindness in that, and a terror. He has no past left that can be held against him."*  
> — Inquisitor file note, sealed

 
### Rumors in Tirvandor
- Some say Varius keeps a sealed letter in his quarters, written by him to be opened by his successor — and that no one knows what's in it.
- A handful of Iron Crown Knights claim he refused the Oath when it was offered to him as a young officer. The order does not confirm or deny.
- His Longsword of Command is rumored to have spoken once, to him alone, on the eve of the Battle of Kethring Field. He has never repeated what it said.

<div class='pageNumber auto'></div>
<div class='footnote'>Chapter 2 - Thaldors Military</div>
\page

# Chapter 3 - Aethoria & Iron Guild
:
Freedom fighters struggling against tyranny and professional mercenaries who serve only coin.

## Aethoria Resistance

Brave souls fighting for liberation from Thaldros rule.

## Aethorian Militia

<div class="col-img">![aethorian militia](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-aethorian-militia.jpg) {width:325px}</div>

### Description
Militia members look exactly like what they are: farmers, shopkeepers, craftspeople, and laborers who have picked up weapons. Their equipment is whatever they could acquire — hunting bows, farming tools converted to weapons, leather work-aprons repurposed as armor, family heirlooms passed down from previous conflicts. Nothing matches. Some carry modern weapons; others wield antiques. What they share is determination in their eyes — the look of people defending something they value more than their own lives.

### Lore
Every Aethorian community maintains a militia tradition. Citizens train periodically, keep weapons available, and respond when their neighbors face threats — not by conscription but by cultural expectation, a duty of citizenship rather than a demand of authority. Members look exactly like what they are: farmers, shopkeepers, and craftspeople wielding hunting bows,
farming tools, and family heirlooms. Nothing matches; what they share is determination. They fight defensively on familiar ground, preferring ambush and harassment to pitched battles they'd lose, and their morale is tied to what they're protecting — threaten their families and they fight with desperate fury. They elect their own officers and refuse orders they consider unjust, which makes them frustrating allies for anyone expecting military discipline but means every sword that lifts does so with genuine conviction.

### Cultural Significance
The militia tradition embodies Aethorian identity: citizens who govern themselves also defend themselves. Professional armies serve rulers; militias serve communities. Militia veterans often become local leaders, their service standing as proof of commitment to shared values.


{{monster,frame
## Aethorian Militia
*Medium humanoid, any alignment*
___
**Armor Class** :: 12 (leather armor)
**Hit Points** :: 9 (2d8)
**Speed** :: 30 ft.

___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|11 (+0) | 14 (+2) | 10 (+0) | 10 (+0) | 12 (+1) | 11 (+0)|
___
**Skills** :: Stealth +4, Survival +3
**Languages** :: Common
**Challenge** :: 1/4 (50 XP)
___
**Guerrilla Fighter.** :: Advantage on attacks when hidden or unseen by target.

___
### Actions
**Spear.** :: *Melee Weapon Attack:* +4 to hit, reach 5 ft., one target. *Hit:* 1d6+2 piercing damage

**Sling.** :: *Ranged Weapon Attack:* +4 to hit, range 30/120 ft., one target. *Hit:* 1d4+2 bludgeoning damage
}}

### Habitat & Ecology
Militia members are neighbors, friends, and family. They know each other's strengths and weaknesses intimately, which creates strong unit cohesion and complicated personal dynamics. They maintain networks of mutual support across communities — when one village is threatened, others send what help they can. The quality of any given militia varies enormously: frontier communities with regular threats 

<div class='pageNumber auto'></div>
<div class='footnote'>Chapter 3 - Aethoria & Iron Guild</div>
\page

maintain well-trained, experienced units, while prosperous interior towns might have militias that haven't seen real action in generations.

### Story Hooks
- The party must organize militia defense of a threatened village before Thaldros patrols arrive.
- Militia members provide local information, guides, and safe houses across the region.
- A militia unit has seen something important in a recent skirmish — but doesn't know what it means.
- The party must convince suspicious militia that they're allies, not Thaldros infiltrators.


## Resistance Fighter

<div class="col-img">![resistance fighter](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-resistance-fighter.jpg) {width:325px}</div>

### Description
Resistance fighters look like what they are: people who have been fighting for a long time. Lean from irregular meals. Scarred from engagements. Eyes that watch everything, hands that never quite relax. They've lost the softness of civilian life without gaining the uniform appearance of professional soldiers. Their equipment is better than basic militia — acquired through combat, purchased through resistance networks, or provided by Republic supporters — but still worn, modified, and intensely personal.
\column
### Lore
Most resistance fighters started as militia who found they couldn't go home — their villages occupied, their families killed, their communities destroyed. With nothing left to protect in the old way, they dedicated themselves to the larger cause: making occupation painful, attacking patrols, destroying supplies, assassinating collaborators, ensuring that occupiers never feel safe. They live in the field, move constantly, and fight with personal fury that emotional investment makes fierce but sometimes reckless. They've learned hard lessons about secrecy — code names, compartmented information, protocols for capture. Many struggle with the moral complexity of their work. Ambushing soldiers is one thing; what to do about collaborators who cooperated under threat, or informants who betrayed friends to save their own families, is another. The line between justice and murder blurs quickly out here.

### Cultural Significance
Resistance fighters are the heroes of Aethorian culture — proof that ordinary people can resist tyranny through determination and sacrifice. The mythology celebrates clear heroes; reality produces morally ambiguous figures, and the songs tend to leave out the parts no one wants to remember.

 
{{monster,frame
## Resistance Fighter
*Medium humanoid, any good alignment*
___
**Armor Class** :: 14 (leather armor)
**Hit Points** :: 16 (3d8 + 3)
**Speed** :: 30 ft.

___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|12 (+1) | 15 (+2) | 12 (+1) | 11 (+0) | 13 (+1) | 12 (+1)|
___
**Skills** :: Stealth +4, Survival +3
**Languages** :: Common
**Challenge** :: 1 (200 XP)
___
**Freedom's Fury.** :: Extra 1d6 damage against Thaldros forces.

___
### Actions
**Shortsword.** :: *Melee Weapon Attack:* +4 to hit, reach 5 ft., one target. *Hit:* 1d6+2 piercing damage

**Shortbow.** :: *Ranged Weapon Attack:* +4 to hit, range 80/320 ft., one target. *Hit:* 1d6+2 piercing damage

**Inspiring Cry (Recharge 5-6).** :: Allies within 30 ft gain advantage on next attack.

}}

### Habitat & Ecology
Resistance cells develop intense internal bonds — they are people who depend on each other for survival, share constant danger, and have watched comrades die. The relationships formed in resistance are among the 

<div class='pageNumber auto'></div>
<div class='footnote'>Chapter 3 - Aethoria & Iron Guild</div>
\page

strongest people experience. Cells maintain support networks among sympathetic civilians: safe houses, supply sources, information pipelines. These networks are essential but dangerous; every contact is a potential point of betrayal, and every safe house is a potential graveyard if a member breaks under interrogation.

### Story Hooks
- The party must coordinate with a resistance cell for mutually beneficial objectives.
- A resistance fighter seeks help for an operation too large for their cell alone.
- Information about enemy movements can only come from resistance contacts demanding favors in return.
- A fighter's past actions create complications when old enemies — or victims — resurface.

## People's Champion

<div class="col-img">![people's champion](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-peoples-champion.jpg) {width:325px}</div>

### Description
People's Champions are local heroes — individuals who rose from their communities to become symbols of resistance. They are better equipped than typical fighters, often wearing armor that communities pooled resources to provide, and their weapons are quality steel, sometimes magical, acquired through deeds that built their reputations. They carry themselves with earned confidence — not the arrogance of privilege, but the assurance of people who've proven themselves through action. Their communities' hopes are visible in their equipment: the best their people could provide, given with prayer that it would be enough.

### Lore
Champions emerge when communities face threats too great for collective response — when someone steps forward, refuses to let their neighbors suffer, and takes on challenges others can't face. Most didn't seek the role; they responded to immediate need and found themselves unable to step back. Their heroism creates reputation: other communities hear of their deeds, recruits seek them out, and the best armor and weapons their people can pool together flow to them as gift and prayer. They fight protectively, positioning themselves between threats and the helpless, and inspire through example rather than command. People follow them not because they must, but because they believe in what the champion represents. Their stories are told in taverns and taught to children — the Aethorian promise that heroes come from ordinary people, if circumstances demand and character permits.

### Cultural Significance
Champions occupy a complex social position — not official leaders (Aethorian democracy resists that), but possessed of substantial unofficial influence. When a champion speaks, communities listen. Many struggle with this responsibility; they didn't want power, only to help, and the weight of their people's hopes can crush even strong shoulders.

{{monster,frame
## People's Champion
*Medium humanoid, chaotic good*
___
**Armor Class** :: 16 (chainmail)
**Hit Points** :: 58 (9d8 + 18)
**Speed** :: 30 ft.

___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|16 (+3) | 13 (+1) | 14 (+2) | 10 (+0) | 12 (+1) | 15 (+2)|
___
**Saving Throws** :: Strength +5, Constitution +4
**Skills** :: Athletics +5, Persuasion +4
**Languages** :: Common
**Challenge** :: 3 (700 XP)
___
**Defender of the Weak.** :: Advantage on attacks against enemies threatening civilians.

___
### Actions
**Multiattack.** :: Two longsword attacks.

**Longsword.** :: *Melee Weapon Attack:* +5 to hit, reach 5 ft., one target. *Hit:* 1d8+3 slashing damage

**Rally the People (1/Day).** :: All allies within 30 ft gain 10 temp HP and advantage on saves vs fear.
}}
<div class='pageNumber auto'></div>
<div class='footnote'>Chapter 3 - Aethoria & Iron Guild</div>
\page

### Habitat & Ecology
Champions maintain close connections to their communities of origin while traveling to where they're needed. Home grounds them; service calls them away. Balancing these pulls is a constant challenge. Their unofficial authority can be substantial — communities listen when a champion speaks, even on matters far outside the champion's expertise. Many handle this responsibility carefully; others are overwhelmed by it and either retreat from public life or grow into something less heroic. The communities that produced them often serve as their resupply, recovery, and reputation network when they need any of those things.

### Story Hooks
- A champion needs help with a challenge beyond their individual capability.
- The party must convince a reluctant champion to join a larger cause.
- A champion's home community is threatened, forcing difficult choices about loyalty and reach.
- Someone is impersonating a champion for personal gain — and doing real damage to the cause.


## Revolutionary Mage

<div class="col-img">![revolutionary mage](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-revolutionary-mage.jpg) {width:325px}</div>
\column
### Description
Revolutionary mages dress practically rather than impressively — they have learned that ostentation attracts targeting; survival requires blending in. Their magical implements are concealed or disguised as walking sticks, jewelry, or tools of mundane trades. They often show the wear of irregular life — tired eyes, stress-aged features, the look of people who haven't slept safely in too long. Magic requires study and rest; revolution provides neither in adequate supply.

{{monster,frame
## Revolutionary Mage
*Medium humanoid, chaotic good*
___
**Armor Class** :: 12 (15 with *mage armor*)
**Hit Points** :: 49 (11d8)
**Speed** :: 30 ft.

___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|9 (-1) | 14 (+2) | 11 (+0) | 17 (+3) | 12 (+1) | 11 (+0)|
___
**Saving Throws** :: Intelligence +6, Wisdom +4
**Skills** :: Arcana +6, History +6
**Languages** :: Common +2 others
**Challenge** :: 5 (1,800 XP)
___
**Liberation Magic.** :: The mage can cast *knock* and *dispel magic* at will, without expending a spell slot.
___
**Spellcasting.** :: The mage is a 9th-level spellcaster. Spellcasting ability is Intelligence (spell save DC 14, +6 to hit with spell attacks). The mage has the following wizard spells prepared:

Cantrips (at will): *fire bolt, mage hand, message, light* ::
1st level (4 slots): *magic missile, shield, mage armor* ::
2nd level (3 slots): *scorching ray, misty step* ::
3rd level (3 slots): *fireball, counterspell* ::
4th level (3 slots): *greater invisibility* ::
5th level (1 slot): *wall of force* ::___
### Actions
**Quarterstaff.** :: *Melee Weapon Attack:* +2 to hit, reach 5 ft., one target. *Hit:* 2 (1d6 - 1) bludgeoning damage, or 3 (1d8 - 1) if used with two hands.

}}

### Lore
The Aethorian magical tradition holds that power should serve the people rather than rule them, and revolutionary mages take this philosophy to its conclusion: if magic can liberate the oppressed, wielding it for liberation is moral duty. Many trained in formal academies before finding traditional institutions too comfortable with existing power structures; others learned through apprenticeship, their education combining arcane theory with political philosophy. They specialize in magic that supports and liberates — breaking chains, unlocking cells, countering enemy magic that would dominate or control — rather than personal devastation. They'd rather free a dozen 

<div class='pageNumber auto'></div>
<div class='footnote'>Chapter 3 - Aethoria & Iron Guild</div>
\page

prisoners than kill a dozen enemies. They dress practically and conceal their implements as walking sticks or jewelry; a known revolutionary mage is a target for Thaldros Inquisitors, and the safest one is the one nobody suspects.

### Cultural Significance
Revolutionary mages embody the Aethorian conviction that magic belongs to the people rather than to elites — a choice celebrated as exemplary by reformers and feared as reckless by traditionalists. Not everyone, even sympathetic allies, is convinced that unleashing magical power in service of political goals is wise. The mages themselves are usually too busy to attend that debate.

### Habitat & Ecology
Revolutionary mages operate in loose networks, sharing information about techniques, threats, and opportunities. No central authority coordinates them — that would be contrary to their anti-authoritarian principles. They provide crucial support to resistance networks: communication magic, healing, reconnaissance, and the occasional dramatic intervention that changes a battle's course. Many maintain secret identities, and a few maintain none at all — vanishing into the cells they serve, knowing the magical training that distinguishes them also marks them for Inquisitor attention.

### Story Hooks
- A revolutionary mage provides magical support the party needs for a critical operation.
- A mage's cover identity is threatened, requiring urgent extraction or protection.
- The party must locate a specific revolutionary mage for their unique capabilities.
- A mage faces a situation where their political and magical commitments conflict — and asks the party to decide.

## Chain Breaker Monk

### Description
Chain Breaker monks are immediately recognizable by their movement — fluid, balanced, carrying implied threat in every gesture. They wear practical clothing that permits full range of motion, nothing binding, nothing restrictive. Many bear scars from chains they once wore and the chains they have broken. Their hands are their most notable feature: callused from training, often scarred from combat, moving with precision that suggests weapons even when empty. Chain Breaker monks don't need weapons — they are weapons.

<div class="col-img">![chain breaker monk](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-chain-breaker-monk.jpg) {width:325px}</div>

### Lore
The Chain Breaker order was founded by escaped slaves who developed martial arts specifically for liberation — techniques born of necessity: how to fight when chained, how to break restraints, how to disable captors, how to protect fellow captives during escape. Every modern Chain Breaker has experienced bondage themselves, and that personal experience shapes their absolute commitment to ending it in others. Their hands are their primary weapons, their movement is freedom made manifest, and their signature ability is exactly what their name promises — any restraint they touch, or any restraint on someone they can reach, shatters through focused spiritual energy. The order maintains monasteries in Aethoria and hidden safehouses throughout Thaldros territory. In Thaldros they are criminals; in Aethoria they are heroes. The starkness of that difference reflects the deeper conflict between the nations.

### Cultural Significance
Members take vows of dedication to the cause of freedom, owning little personally and sharing resources with the order. Their existence is a standing promise to every prisoner, every slave, every person held against their will: help is possible. Someone is coming. Many 

<div class='pageNumber auto'></div>
<div class='footnote'>Chapter 3 - Aethoria & Iron Guild</div>
\page

monks struggle to overcome the hatred they hold toward their former captors — the order teaches that hatred chains the spirit as surely as iron chains the body, but learning that lesson is itself a kind of escape.

 
{{monster,frame
## Chain Breaker Monk
*Medium humanoid, lawful good*
___
**Armor Class** :: 17
**Hit Points** :: 91 (14d8 + 28)
**Speed** :: 50 ft.

___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|11 (+0) | 18 (+4) | 14 (+2) | 13 (+1) | 17 (+3) | 12 (+1)|
___
**Saving Throws** :: Strength +3, Dexterity +7
**Skills** :: Acrobatics +7, Stealth +7
**Languages** :: Common
**Challenge** :: 6 (2,300 XP)
___
**Unarmored Defense.** :: AC = 10 + Dexterity + Wisdom

**Unarmored Movement.** :: +20 ft speed

**Ki (11 points).** :: Regain on short rest.

___
### Actions
**Multiattack.** :: Four unarmed strikes.

**Unarmed Strike.** :: *Melee Weapon Attack:* +7 to hit, reach 5 ft., one target. *Hit:* 1d8+4 bludgeoning damage

**Shatter Bonds (3 ki).** :: Automatically break all restraints on touched creature. Can use on self.

**Stunning Strike (1 ki).** :: DC 15 Constitution save or stunned until end of your next turn.

}}

### Habitat & Ecology
The order maintains monasteries in Aethoria and hidden safehouses throughout Thaldros territory, serving as training facilities, refuges for escaped prisoners, and coordination points for liberation operations. Members own little personally, sharing resources with the order, and go wherever they are needed — staying until the work is done, then moving to the next mission. Training is demanding: physical conditioning, martial technique, meditation, and philosophical education in the meaning of freedom. Becoming a Chain Breaker takes years of dedication; the order accepts only those who have lived through bondage themselves.

### Story Hooks
- A Chain Breaker is needed to free important prisoners from an inescapable Thaldros holding.
- The party must help extract a Chain Breaker from dangerous occupied territory.
- A monastery is threatened with discovery, requiring urgent defense.
- A Chain Breaker's former captors have surfaced as someone the party must work with.


## Guerrilla Commander

<div class="col-img">![guerrilla commander](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-guerrilla-commander.jpg) {width:325px}</div>

### Description
Guerrilla commanders look like experienced resistance fighters who have grown into leadership. Their equipment is excellent — rewards of successful operations — but worn from constant use. They move with the careful attention of people who have survived by noticing everything. Their eyes are their most notable feature: constantly scanning, assessing, planning. They see terrain in terms of ambush positions, people in terms of capabilities and loyalties; everything is potential resource or potential threat.

### Lore
Commanders emerge from resistance cells through demonstrated capability — fighters who survived long enough to learn, planned well enough to win, and led well enough that others followed. Their authority comes from proven competence rather than appointed position, and most have been fighting for years, often decades, lost friends, made terrible decisions, and survived failures that killed others. They think strategically rather than tactically; individual skirmishes matter less than campaign outcomes, and they maintain regional networks of village contacts, city informants, and allies among other resistance groups. Their position sits uneasily with pure Aethorian democratic principles — 

<div class='pageNumber auto'></div>
<div class='footnote'>Chapter 3 - Aethoria & Iron Guild</div>
\page

they have substantial informal authority, however earned — and most navigate the tension by maintaining collective decision-making forms while providing direction through influence. They know that capture would devastate their networks, and many maintain standing arrangements to be killed rather than taken.

{{monster,frame
## Guerrilla Commander
*Medium humanoid, chaotic good*
___
**Armor Class** :: 16 (studded leather +1)
**Hit Points** :: 117 (18d8 + 36)
**Speed** :: 30 ft.

___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|14 (+2) | 18 (+4) | 14 (+2) | 15 (+2) | 16 (+3) | 17 (+3)|
___
**Saving Throws** :: Dexterity +7, Wisdom +6
**Skills** :: Stealth +10, Survival +6, Persuasion +6
**Languages** :: Common +2 others
**Challenge** :: 7 (2,900 XP)
___
**Tactical Mind.** :: Allies within 60 ft add +2 to initiative.

**Sneak Attack (1/turn).** :: +4d6 damage with advantage.

___
### Actions
**Multiattack.** :: Three shortsword or shortbow attacks.

**Shortsword +2.** :: *Melee Weapon Attack:* +9 to hit, reach 5 ft., one target. *Hit:* 1d6+6 piercing damage

**Strategic Command (Recharge 5-6).** :: All allies within 60 ft can move half speed and make one attack as reaction.


}}

### Cultural Significance
Guerrilla commanders represent Aethorian practical competence — proof that free people can organize effectively without authoritarian structure, and a direct challenge to Thaldros assumptions about discipline. Their effectiveness is celebrated, but their unusual personal authority worries pure democrats who wonder what happens when the crisis ends and the commanders refuse to retire it.

### Habitat & Ecology
Commanders maintain regional networks that span villages, towns, and cities — contacts in markets, informants in garrisons, allies among other resistance groups. Building these networks is their primary strategic contribution; combat is something they only do when planning has already failed. Most maintain standing arrangements for immediate information destruction if they are taken, and some keep agents ready to kill them rather than allow capture. The information in their heads is too valuable to risk. They move constantly between safehouses and rarely sleep in the same place twice in a week.
\column
### Story Hooks
- A commander coordinates multiple groups including the party for a major joint operation.
- The party must locate a commander who's gone to ground after a failed operation.
- A commander's past decisions created enemies who now threaten current operations.
- Intelligence suggests a commander may have been compromised — and the party must verify before reporting.

## The Liberator

<div class="col-img">![the liberator](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-the-liberator.jpg) {width:325px}</div>

### Description
The Liberator is a figure of legend made flesh. Tall, commanding, moving with grace that suggests either supernatural enhancement or lifelong training. Their equipment is masterwork quality — gifts from grateful communities, rewards of impossible victories, artifacts that found their way to a worthy bearer. They radiate presence. Entering a room, they become its focus. Speaking, they command attention. Fighting, they seem larger than physical form would suggest. Something about them transcends ordinary human limitation.

<div class='pageNumber auto'></div>
<div class='footnote'>Chapter 3 - Aethoria & Iron Guild</div>
\page

### Lore
No one becomes the Liberator through normal paths. They emerge from circumstances that would break ordinary people — catastrophic loss, impossible odds, moments when choosing freedom over survival seemed suicidal but proved prophetic. The title itself has been held by perhaps a dozen individuals across Tirvandor's history; each was different, but all shared absolute commitment to liberty that transcended personal safety or conventional possibility. They appear where they're most needed, stay until the immediate crisis resolves, and vanish before their presence creates dependency. They take no orders, share no plans, and conform to no one's strategy. Their existence proves that tyranny isn't absolute, that resistance isn't futile. In Thaldros they are officially a criminal and terrorist; privately, many Thaldros officials fear the Liberator may actually be unkillable.

{{monster,frame
## The Liberator
*Medium humanoid, chaotic good*
___
**Armor Class** :: 19 (studded leather +3)
**Hit Points** :: 178 (21d8 + 84)
**Speed** :: 40 ft.

___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|16 (+3) | 20 (+5) | 18 (+4) | 14 (+2) | 16 (+3) | 20 (+5)|
___
**Saving Throws** :: Dexterity +10, Wisdom +8, Charisma +10
**Skills** :: All +9 or higher
**Damage Resistances** :: psychic
**Languages** :: All common
**Challenge** :: 11 (7,200 XP)
___
**Legendary Resistance (2/Day).** :: Can choose to succeed on failed save.

**Aura of Freedom (30 ft).** :: Allies have advantage vs charmed/frightened.

**Sneak Attack (1/turn).** :: +6d6 damage

___
### Actions
**Multiattack.** :: Four rapier attacks.

**Freedom's Blade +3.** :: *Melee Weapon Attack:* +12 to hit, reach 5 ft., one target. *Hit:* 1d8+8 piercing damage + 2d8 radiant damage

**Break All Chains (1/Day).** :: All restraints/prisons within 60 ft shatter. All allies gain 30 temp HP.

**Move.** :: Half speed

**Attack.** :: One rapier attack

**Inspire (2 actions).** :: One ally makes attack or spell as reaction

}}

### Cultural Significance
The Liberator embodies hope itself — proof that resistance isn't futile, that individual conviction can challenge systemic oppression. Some believe they're divinely chosen; others think they're simply exceptional. Some want them to lead openly; others appreciate that their mystique depends on staying somewhat mysterious. Many people across Tirvandor have tried to claim relationship or influence with the Liberator. Most such claims are false or exaggerated.


### Habitat & Ecology
The Liberator operates largely alone or with small trusted groups, appearing where most needed, staying until the immediate crisis resolves, and vanishing before their presence creates dependency. This independence frustrates would-be allies who want to coordinate — the Liberator does not take orders, does not share plans, does not conform to others' strategies. They simply do what they believe is necessary. They maintain few ongoing connections and trust very few people with their actual identity and location; the people who know are usually those they have saved, who have proven their silence under torture.

### Story Hooks
- The party must locate the Liberator for a mission only they can accomplish.
- The Liberator seeks help with something that requires different skills than their own.
- Someone is falsely claiming to be the Liberator, creating complications for genuine resistance.
- The party discovers they're caught up in one of the Liberator's operations without knowing it.


### The Liberator Through History
The title has surfaced perhaps a dozen times — never twice in the same lifetime, never twice with the same face. Common scholarly consensus identifies these confirmed Liberators:

- **Mira of the Salt Mines** (Year 423 CR) — broke nine hundred chained workers free in a single night; her body was never recovered.
- **The Burning Saint** (Year 612 CR) — said to have walked through fire to free prisoners from the Aethorian heretic-pyres before the Republic existed.
- **Tarin Halfhand** (Year 891 CR) — freed an entire ghetto from forced relocation; killed himself rather than be taken, but witnesses swore he reappeared in two other cities afterward.
- **The current Liberator** — first confirmed sighting Year 1238 CR. Identity unknown. Still active.

### Whispers
> *"There is no proof they are the same person. There is no proof they aren't. Both possibilities terrify me equally."*  
> — Inquisitor Cael, internal memo

> *"I asked once if she was the Liberator. She laughed and said, 'If I told you yes, would you sleep tonight? If I told you no, would you sleep tomorrow?'"*  
> — Innkeeper, Briarwood


<div class='pageNumber auto'></div>
<div class='footnote'>Chapter 3 - Aethoria & Iron Guild</div>
\page

## Prophesied Hero

<div class="col-img">![prophesied hero](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-prophesied-hero.jpg) {width:325px}</div>

### Description
Prophesied Heroes look like ordinary people who carry extraordinary destiny. Something in their bearing suggests significance beyond their apparent status. Their equipment often includes items of ancient origin — weapons or armor connected to the prophecies that mark their fate. They often seem slightly out of place, as if they belong to a larger narrative than their current circumstances. People meeting them frequently feel that something important is happening, even if they can't identify what.

### Habitat & Ecology
Prophesied Heroes attract followers, supporters, and exploiters wherever they travel. People want to be associated with destiny, whether to share in it or to use it for their own purposes; sorting genuine support from manipulation is constant work. Many feel isolated despite constant attention — no one relates to them as ordinary people, only as symbols or tools. They tend to travel light and move often, since stationary destiny gathers crowds, and crowds attract enemies. Some come to embrace their role; others spend their lives trying to outrun it.

\column

### Lore
Aethorian religious tradition holds that seven heroes are prophesied to arise in each age of great need, each playing a distinct role in the age's defining conflicts. Prophesied Heroes don't choose their destiny; it chooses them. They are born with potential that awakens when the world needs them — some embrace their role, others resist it, but neither changes the fundamental fact of their significance. Identifying them is inexact; multiple individuals have been proclaimed as the same Hero, sometimes simultaneously, and the prophecies are vague enough to support various readings. They are followed, supported, and inevitably exploited. Sorting genuine devotion from manipulation is constant work, and many feel isolated despite the attention — no one relates to them as ordinary people, only as symbols or tools. Wars have been started over disputes about which interpretation of prophecy is correct.

### Cultural Significance
Prophesied Heroes embody the Aethorian conviction that history has purpose — that the gods, or fate, or something arrange for heroes when needed. This belief offers comfort in dark times and justification for hope when circumstances seem hopeless. Skeptics point out that prophecies are vague enough to fit many readings, and that proclaimed Heroes often fail or turn out to
be frauds. Believers counter that prophecy's complexity does not disprove its truth. In political terms, claiming someone as a Prophesied Hero provides powerful legitimacy for whatever cause they support — which is precisely why so many causes try to claim them.

### Story Hooks
- The party encounters someone who may be a Prophesied Hero — or a remarkably convincing fraud.
- A Prophesied Hero needs help with a challenge that destiny did not prepare them for.
- Multiple claimed Prophesied Heroes create conflict among their respective followers and factions.
- The party becomes entangled in prophecy themselves, possibly as supporting figures in a Hero's narrative — whether they want the role or not.

### The Seven of This Age
Aethorian prophecy holds that seven Heroes will arise in this age — each with a distinct role to play before the conflict ends. As of Year 1247 CR, three have been credibly identified, two are disputed, and two remain unknown. The roles, as traditionally interpreted:

- **The Sword** — Champion of war, hand of justice
- **The Voice** — Speaker of truth, hand that gathers
- **The Hidden** — Walker of shadow, hand that strikes
- **The Healer** — Keeper of mercy, hand that mends

<div class='pageNumber auto'></div>
<div class='footnote'>Chapter 3 - Aethoria & Iron Guild</div>
\page

- **The Witness** — Bearer of knowledge, hand that records
- **The Sacrifice** — Cost-paid, hand that gives all
- **The Seventh** — Unknown. Some texts omit them entirely; others insist they are the most important of all.

{{monster,frame
## Prophesied Hero
*Medium humanoid, any good*
___
**Armor Class** :: 20 (plate +1, shield +1)
**Hit Points** :: 210 (20d8 + 120)
**Speed** :: 30 ft.

___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|20 (+5) | 14 (+2) | 22 (+6) | 12 (+1) | 18 (+4) | 20 (+5)|
___
**Saving Throws** :: Strength +10, Constitution +11, Wisdom +9, Charisma +10 | **Condition Immunities** frightened
**Languages** :: Common +3 others
**Challenge** :: 12 (8,400 XP)
___
**Destiny's Chosen.** :: Advantage on all saves. Crits on 19-20.

**Aura of Destiny (30 ft).** :: Allies add +3 to all saves.

___
### Actions
**Multiattack.** :: Three longsword attacks.

**Destiny's Blade +2.** :: *Melee Weapon Attack:* +12 to hit, reach 5 ft., one target. *Hit:* 1d8+7 slashing damage + 3d8 radiant damage

**Channel Divinity: Smite the Tyrant (3/Day).** :: Next attack deals +50 radiant damage vs evil targets.


}}

### Whispers
> *"I told her she was the Sword. She told me to go home and bury my mother properly before I tried to sell her another destiny."*  
> — Failed prophet, Greenmarsh

> *"The trouble with prophecy is that it works. Just not the way you think it will."*  
> — Moira's Seer, attributed

::

## Iron Guild Mercenaries

Professional soldiers for hire, loyal only to the contract.

## Guild Recruit

### Description
Guild recruits look like people trying very hard to look professional. Their equipment is standard issue — functional but not personalized. Their armor often fits imperfectly, not yet adjusted to their bodies. They move with trained precision that hasn't yet become natural, following protocols consciously rather than instinctively. They are typically young, though some older recruits exist — career changers, veterans from other militaries, or people who came to mercenary work through necessity. What they share is newness: that particular combination of eagerness and uncertainty that marks the inexperienced.

### Lore
The Iron Guild accepts recruits from many backgrounds — farmers' children seeking fortune, minor nobles without inheritance, deserters from national armies, even criminals seeking legitimacy. The Guild doesn't ask about pasts. Basic screening determines whether an applicant can fight, follow orders, and work with others; those who pass enter a probationary period of training and supervised contracts at reduced pay until they prove themselves. Their equipment is standard issue, functional but not yet personalized, and they move with trained precision that hasn't yet become natural. Guild training emphasizes psychological conditioning — don't panic, don't run, trust your training — which gives recruits a notable edge over equally skilled but undisciplined opponents. Most feel a mix of pride at being in the Guild and insecurity at not having proven themselves. Smart ones focus on learning; foolish ones try to prove themselves too quickly, and often die doing so.

<div class="col-img">![guild recruit](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-guild-recruit.jpg) {width:325px}</div>

<div class='pageNumber auto'></div>
<div class='footnote'>Chapter 3 - Aethoria & Iron Guild</div>
\page

### Cultural Significance
Guild recruits embody the profession's accessibility — anyone with basic capability can join and potentially rise through merit rather than birth, an appeal not lost on those without other prospects. The glossy recruitment pitches about fortune and glory do not mention how many recruits die on their first contracts. Reality teaches that lesson personally.

### Habitat & Ecology
Recruits occupy the bottom of the Guild hierarchy — they do the worst jobs, receive the smallest shares, and are reminded constantly that they haven't earned full membership yet. This creates strong motivation to improve. They form tight bonds with their cohort (other recruits who joined at the same time), and these relationships often persist throughout careers, creating cross-company connections that benefit the Guild as a whole. Recruits are assigned to veteran mentors who supervise their early contracts. These mentors are responsible for keeping recruits alive long enough to become useful — and for identifying those who won't make it.

### Story Hooks
- Recruits provide information about Guild operations they've observed but don't yet understand.
- A recruit cohort is in over their head and needs help surviving an active contract.
- Someone the party knows has joined the Guild, and that connection becomes complicated.

{{monster,frame
## Guild Recruit
*Medium humanoid, any*
___
**Armor Class** :: 14 (leather, shield)
**Hit Points** :: 16 (3d8 + 3)
**Speed** :: 30 ft.

___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|13 (+1) | 12 (+1) | 12 (+1) | 10 (+0) | 11 (+0) | 10 (+0)|
___
**Skills** :: Athletics +3
**Languages** :: Common
**Challenge** :: 1/2 (100 XP)
___
**Professional Training.** :: Advantage on saves vs fear while within 10 ft of ally.

___
### Actions
**Longsword.** :: *Melee Weapon Attack:* +3 to hit, reach 5 ft., one target. *Hit:* 1d8+1 slashing damage

**Crossbow.** :: *Ranged Weapon Attack:* +3 to hit, range 80/320 ft., one target. *Hit:* 1d8+1 piercing damage


}}

\column

## Veteran Mercenary

<div class="col-img">![veteran mercenary](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-veteran-mercenary.jpg) {width:325px}</div>

### Description
Veterans look like survivors. Their equipment is personalized — modifications and additions accumulated over years of contracts. Their armor bears repair marks where damage was fixed. Their weapons show wear patterns from actual use rather than training. They move with economical confidence: no wasted motion, no unnecessary display. They've learned what matters and discarded what doesn't. Most bear visible scars, missing fingers, ears, or eyes; these marks are neither hidden nor displayed — they're simply facts of the profession.

### Lore
Veterans are recruits who survived. That simple fact makes them valuable — three to five years of active contract work, combined with Guild training, produces competent and reliable soldiers. Most have served on both sides of various conflicts at different times; this isn't considered problematic, professional soldiers go where contracts take them. They fight efficiently rather than dramatically, take cover, conserve energy, and avoid fair fights when unfair ones are available. They prefer working with partners they know, coordinating almost telepathically with practiced peers. Veterans are the Guild's backbone — captains and elites get the glory, 

<div class='pageNumber auto'></div>
<div class='footnote'>Chapter 3 - Aethoria & Iron Guild</div>
\page

but veterans get the work done, and the Guild's valuable reputation rests on their reliability. Most have complicated relationships with civilian life: they've been away too long, done too much, to fit comfortably anywhere else. The Guild becomes their community.

### Cultural Significance
Veterans represent what mercenary careers actually look like — not glamorous legend, but steady competence applied over years. They maintain quiet professional networks across companies, sharing intelligence about contracts, employers, and conditions. Most who survive long enough become veterans; most never become more, and that's exactly what most of them want.

### Habitat & Ecology
Veterans occupy the Guild's middle tier and many are content to stay there — not everyone wants command responsibility. They maintain quiet professional networks across companies; veterans who have served together remain connected for life, sharing information about contracts, employers, and conditions. This informal network is surprisingly effective. They are comfortable with extended operations — long marches, poor conditions, uncertain supply — and have learned how to function when circumstances are less than ideal. Off-duty they congregate in known mercenary taverns, where they trade stories, settle old debts, and quietly track who is reliable and who is not.


{{monster,frame
## Veteran Mercenary
*Medium humanoid, any*
___
**Armor Class** :: 16 (chain shirt, shield)
**Hit Points** :: 45 (7d8 + 14)
**Speed** :: 30 ft.

___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|15 (+2) | 13 (+1) | 14 (+2) | 11 (+0) | 12 (+1) | 11 (+0)|
___
**Skills** :: Athletics +4, Survival +3
**Languages** :: Common
**Challenge** :: 2 (450 XP)
___
**Combat Veteran.** :: Advantage on saves vs poison and disease.

___
### Actions
**Multiattack.** :: Two longsword attacks.

**Longsword.** :: *Melee Weapon Attack:* +4 to hit, reach 5 ft., one target. *Hit:* 1d8+2 slashing damage

**Tactical Retreat.** :: Disengage as bonus action.


}}

### Story Hooks
- Veterans provide experienced perspective on a military situation the party can't read on its own.
- A veteran recognizes someone or something from a past contract and the connection matters now.
- Veterans assigned to guard something might be negotiated with professionally.
- A veteran is trying to leave the profession and needs help disappearing properly.

## Guild Enforcer

<div class="col-img">![guild enforcer](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-guild-enforcer.jpg) {width:325px}</div>

### Description
Enforcers are imposing by design. They are selected partly for size and presence, then trained to maximize intimidation. Heavy armor, large weapons, and practiced scowls create impressions intended to make confrontation unnecessary. They are notably larger than typical Guild members — a deliberate recruitment preference. Their equipment is maintained to parade standards, projecting Guild authority. They move with the controlled threat of people capable of violence who prefer not to use it.

### Lore
Enforcers police the Guild itself, ensuring contracts are honored, disputes settled by Guild rules, and members who violate standards face consequences. They're selected from veterans for combat capability, size, and — crucially — temperament. Those who enjoy hurting people make poor enforcers; they create problems rather than solve them. Good enforcers prefer resolving situations without violence and rely on imposing presence and the implied threat of escalation. When 

<div class='pageNumber auto'></div>
<div class='footnote'>Chapter 3 - Aethoria & Iron Guild</div>
\page

intimidation fails, they're brutal and efficient. The Guild's internal reputation requires that resisting enforcers be obviously foolish, and the object lessons they deliver tend to discourage future resistance. They work in pairs and groups for mutual accountability, and represent the Guild's self-governance — unlike national armies that rely on external authority, the Guild polices itself, and that self-regulation is central to its independence.

### Cultural Significance
Enforcers are controversial within the Guild itself — some members appreciate the order they maintain; others view them as internal tyrants. Many enforcers are quiet idealists who believe the rules are just and the system worth defending. Others are pragmatists who simply found a niche where their skills are valued and their pasts ignored.

{{monster,frame
## Guild Enforcer
*Medium humanoid, any*
___
**Armor Class** :: 17 (half plate)
**Hit Points** :: 68 (8d8 + 32)
**Speed** :: 30 ft.

___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|17 (+3) | 14 (+2) | 18 (+4) | 11 (+0) | 13 (+1) | 12 (+1)|
___
**Skills** :: Athletics +5, Intimidation +3 | **Languages** :: Common
**Languages** :: Common
**Challenge** :: 4 (1,100 XP)
___
**Guild Authority.** :: Can call for backup (1d4 recruits arrive in 1d4 rounds).

___
### Actions
**Multiattack.** :: Two greatsword attacks.

**Greatsword.** :: *Melee Weapon Attack:* +5 to hit, reach 5 ft., one target. *Hit:* 2d6+3 slashing damage

**Intimidating Presence (Recharge 5-6).** :: DC 13 Wisdom save or frightened 1 min.


}}

### Habitat & Ecology
Enforcers maintain their own intelligence network across Guild chapters, sharing information about trouble spots, problematic members, and emerging issues. This intelligence function is as important as their enforcement role. They occupy a complex position within Guild hierarchy — they are not commanders, but they have authority that crosses normal chain of command, which creates ongoing tension with captains who resent the interference. Most operate from regional offices in major Guild cities, riding circuit between companies when investigations require it.
\column
### Story Hooks
- Enforcers are investigating something that intersects with the party's activities.
- An enforcer needs outside help with an internal Guild matter they can't be seen to investigate.
- The party's actions have attracted enforcer attention, and a confrontation is coming.
- An enforcer believes a Guild member is being unjustly targeted, and seeks allies outside the Guild.

## Contract Killer

<div class="col-img">![contract killer](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-contract-killer.jpg) {width:325px}</div>

### Description
Contract killers don't look like assassins. That's the point. They look like merchants, servants, travelers, whatever cover the current assignment requires. Their actual appearance is variable; their ability to appear unremarkable is constant. When not undercover, they favor practical dark clothing that blends into shadows. Their weapons are concealable. Their movements are quiet and controlled. Everything about them is optimized for not being noticed until it is too late.

<div class='pageNumber auto'></div>
<div class='footnote'>Chapter 3 - Aethoria & Iron Guild</div>
\page

### Lore
The Guild officially doesn't employ assassins — assassination is illegal in most jurisdictions, and the Guild prefers to maintain plausible legitimacy. Unofficially, certain specialized operatives handle "personal security contracts" that sometimes require "preemptive neutralization of threats." The language is careful; the results are fatal. They don't look like assassins, and that's the point — merchants, servants, travelers, whatever cover the current assignment 

requires. Their actual appearance is variable; their ability to appear unremarkable is constant. They study targets exhaustively, identify vulnerabilities, prepare multiple contingencies, and avoid fair fights entirely. Their goal is elimination without detection, ideally with no one knowing violence occurred until well after the killer has departed. Most Guild members don't know who the killers are, which is intentional.

### Cultural Significance
Contract killers represent the darker side of mercenary work — services everyone needs but no one wants to acknowledge, the reason certain inconvenient problems simply *disappear*. Their official non-existence is a convention everyone involved understands, and the pretense maintains useful fictions for employers and Guild alike.

{{monster,frame
## Contract Killer
*Medium humanoid, any*
___
**Armor Class** :: 15 (studded leather)
**Hit Points** :: 78 (12d8 + 24)
**Speed** :: 30 ft.

___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|11 (+0) | 16 (+3) | 14 (+2) | 13 (+1) | 11 (+0) | 10 (+0)|
___
**Saving Throws** :: Dexterity +6
**Skills** :: Stealth +9, Perception +3
**Languages** :: Common, Thieves' Cant
**Challenge** :: 5 (1,800 XP)
___
**Assassinate.** :: Advantage vs creatures that haven't acted. Crits on surprise hits.

**Sneak Attack (1/turn).** :: +3d6 damage with advantage.

___
### Actions
**Multiattack.** :: Two shortsword attacks.

**Shortsword.** :: *Melee Weapon Attack:* +6 to hit, reach 5 ft., one target. *Hit:* 1d6+3 piercing damage

**Poisoned Dart.** :: *Ranged Weapon Attack:* +6 to hit, range 20/60 ft., one target. *Hit:* 1d4+3 piercing damage + DC 14 Constitution save or 3d6 poison damage
}}
\column
### Habitat & Ecology
Contract killers operate outside normal Guild hierarchy, receiving assignments through specific channels and reporting to handlers rather than captains. They are solitary by necessity — their work doesn't permit close relationships. Most develop a detached perspective that allows them to function; some might call it psychological damage. Within their small community, they maintain professional respect for skilled peers, and competence is the only currency that matters. They congregate nowhere openly; if they meet at all, it is in private through handlers.

### Story Hooks
- A contract killer is targeting someone the party needs to protect.
- The party must locate and stop a killer before they complete a high-value assignment.
- A contract killer seeks to leave the profession and needs help vanishing.
- The party must hire Guild services for an elimination they can't perform themselves.

## Iron Guild Captain

<div class="col-img">![iron guild captain](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-iron-guild-captain.jpg) {width:325px}</div>

<div class='pageNumber auto'></div>
<div class='footnote'>Chapter 3 - Aethoria & Iron Guild</div>
\page

### Description
Captains look like what they are: successful mercenaries who have risen through proven competence. Their equipment is exceptional — rewards of successful contracts combined with Guild benefits. Their bearing projects authority earned through demonstrated capability. They are typically in their thirties or forties, old enough to have accumulated experience, young enough to remain physically effective. Scars and wear marks testify to the contracts they have survived.

### Lore
Captains command mercenary companies of fifty to two hundred soldiers, organized into squads and platoons. The Guild promotes from within; outside recruitment at captain level is extremely rare, which ensures captains understand Guild culture and expectations. Reaching the rank requires demonstrated leadership in addition to personal combat skill, and training covers tactics, logistics, contract negotiation, and personnel management — most of the job is administrative. Captains are the Guild's public face: employers deal with them, authorities negotiate with them, and company reputation depends largely on their capability. They compete fiercely with each other for prestigious contracts and intensely practical, having risen through pragmatic competence rather than idealism. The more problematic aspects of mercenary work happen at other levels; captains represent the profession's legitimate aspirations.

### Cultural Significance
Captains occupy middle management in the Guild hierarchy, balancing upward expectations from senior leadership against downward responsibility to their companies. Company reputation depends largely on captain capability, and that reputation flows directly into contract pricing — making a captain's name a marketable asset in itself.

### Habitat & Ecology
Captains lead from positions that maximize their effectiveness — sometimes the front, sometimes the rear, depending on circumstances. They coordinate company operations: deployment, supply, discipline, and contact with employers. A good captain keeps the company supplied, paid, and pointed at appropriate targets. Most are intensely practical — having risen through pragmatic competence rather than idealism — and they understand that the Guild exists to profit from contracts. Off-duty, they socialize primarily with other captains in chapter house common rooms, sharing complaints about clients and trading tips about which contracts are worth pursuing.

{{monster,frame
## Iron Guild Captain
*Medium humanoid, any*
___
**Armor Class** :: 18 (plate)
**Hit Points** :: 135 (18d8 + 54)
**Speed** :: 30 ft.

___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|18 (+4) | 12 (+1) | 16 (+3) | 14 (+2) | 15 (+2) | 16 (+3)|
___
**Saving Throws** :: Strength +7, Constitution +6, Wisdom +5
**Skills** :: Athletics +7, Persuasion +6
**Languages** :: Common +2 others
**Challenge** :: 7 (2,900 XP)
___
**Tactical Leader.** :: Allies within 30 ft add +2 to attack rolls.

**Second Wind (1/Short Rest).** :: Bonus action to heal 20 HP.

___
### Actions
**Multiattack.** :: Three longsword attacks.

**Longsword +1.** :: *Melee Weapon Attack:* +8 to hit, reach 5 ft., one target. *Hit:* 1d8+5 slashing damage

**Command Squad (Recharge 5-6).** :: All allies within 60 ft can attack as reaction.


}}

### Story Hooks
- A captain offers the party contract work as temporary additions to their company.
- The party must negotiate with a captain whose company blocks their path.
- A captain's past decisions create complications in the present.
- A captain suspects corruption within their own company and needs outside investigators.

## Guildmaster's Elite

### Description
The Guildmaster's Elite are living legends. Their equipment is masterwork or magical — accumulated over careers of exceptional achievement — and their bearing projects absolute confidence earned through decades of victory. They are typically older than other active members, fifties or sixties, but remain formidable through maintained training and (often) magical assistance. What they have lost in youthful vigor, they have more than replaced with experience and equipment. Each Elite is recognizable; they have individual reputations built over careers that span decades, and their names are known throughout the mercenary profession.


<div class='pageNumber auto'></div>
<div class='footnote'>Chapter 3 - Aethoria & Iron Guild</div>
\page

### Lore
The Elite are living legends — never more than a dozen at any time, selected from the best captains and specialists who have demonstrated not just competence but excellence over decades. Selection is by Guildmaster invitation only, and most candidates have previously declined promotion, preferring active service to administrative roles. Eventually, the Guildmaster asks personally. Their duties include protecting the Guildmaster, handling the most sensitive and important contracts, and serving as final arbiters in internal disputes. They form the Guild's inner council, advising on policy and major decisions. Each is recognizable by name throughout the mercenary profession. They fight with refined technique developed over careers — every motion purposeful, every attack efficient — and have 
long since abandoned flashy techniques for what actually works. Those who force them to fight rarely survive the experience.

<div class="col-img">![guildmaster's elite](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-guildmasters-elite.jpg) {width:325px}</div>

### Cultural Significance
The Elite represent what mercenary careers can ultimately achieve — proof that excellence is recognized and rewarded by the profession itself. They are also reminders that even legends eventually age. How they handle that transition — retiring gracefully, dying in service, or declining into parody — shapes how younger members understand their own futures.

### Habitat & Ecology
The Elite form the Guild's inner council, advising the Guildmaster on policy and major decisions; their collective experience represents centuries of accumulated knowledge. They maintain extensive networks built over career lifetimes — former colleagues, former employers, former enemies who became allies — that span Tirvandor. Many struggle with mortality: they have achieved everything the profession offers, yet time continues passing. What comes after being the best is a question without comfortable answers, and how each Elite eventually faces it shapes the next generation's expectations of their own futures.

### Story Hooks
- An Elite is assigned to a mission that intersects with the party's goals.
- The party needs Elite-level capability for an impossible task and must persuade one to take the contract.
- An Elite's long history creates complications when old events resurface in the present.
- An aging Elite seeks a worthy final mission, and the party's reputation has reached them.

{{monster,frame
## Guildmaster's Elite
*Medium humanoid, any*
___
**Armor Class** :: 19 (plate +1)
**Hit Points** :: 165 (22d8 + 66)
**Speed** :: 30 ft.

___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|20 (+5) | 14 (+2) | 16 (+3) | 12 (+1) | 14 (+2) | 15 (+2)|
___
**Saving Throws** :: Strength +9, Constitution +7
**Skills** :: Athletics +9, Intimidation +6
**Languages** :: Common +2 others
**Challenge** :: 9 (5,000 XP)
___
**Indomitable (2/Day).** :: Reroll failed save.

**Mercenary's Pride.** :: Advantage vs fear and charm.

___
### Actions
**Multiattack.** :: Three greatsword attacks.

**Greatsword +2.** :: *Melee Weapon Attack:* +11 to hit, reach 5 ft., one target. *Hit:* 2d6+7 slashing damage

**Commanding Strike (Recharge 5-6).** :: One ally makes attack with advantage.


}}


<div class='pageNumber auto'></div>
<div class='footnote'>Chapter 3 - Aethoria & Iron Guild</div>
\page

## Garrick Ironheart

<div class="col-img">![garrick ironheart](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-garrick-ironheart-guildmaster.jpg) {width:325px}</div>

### Description
Powerfully built even by dwarven standards, with arms like tree trunks from over a century at the forge. His copper-red beard is braided with metal rings, each representing a significant creation. He is missing the last two fingers of his left hand — a forge accident he refuses to discuss in detail. His eyes are an unusual amber color that seems to glow near flames. He moves with the deliberate patience of someone who has spent decades making things that last, and his hands carry the scarring of a thousand small burns long since healed over.

### Lore
Garrick "Ironheart" Hammerfist is the dwarven Guildmaster of the Smiths' Guild in Goldreach, but his presence in mercenary catalogs comes from his younger years before the forge. He served Iron Guild contracts, led expeditions to recover rare materials, and fought in several significant conflicts — the "Ironheart" nickname is from those days, not from the steel defender he later crafted. Powerfully built even by dwarven standards, his arms are like tree trunks from over a century at the forge, and he is missing the last two fingers of his left hand from an accident he refuses to discuss. His copper-red beard is braided with metal rings, each marking a significant creation. He no longer takes contracts, but he supplies the Guild with weapons and armor, and senior members still remember his active service. His fairness in dealings is respected across mercenary communities; his endorsement carries weight no coin can buy.

### Cultural Significance
Garrick is one of the few figures who commands genuine respect across factional lines — Thaldros generals, Aethorian commanders, and Iron Guild captains all want his work in their armories. He refuses to forge for tyrants, but his definition of "tyrant" is famously narrow: he sells to whoever pays and behaves well in his shop. The Smiths' Guild he founded is now the most influential craft organization in Goldreach, and his approval of an apprentice is considered equivalent to a peerage in some circles.

{{monster,frame
## Garrick Ironheart
*Medium humanoid (dwarf), lawful neutral*
___
**Armor Class** :: 20 (plate +2, shield +1)
**Hit Points** :: 195 (23d8 + 92)
**Speed** :: 25 ft.

___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|20 (+5) | 12 (+1) | 18 (+4) | 16 (+3) | 16 (+3) | 18 (+4)|
___
**Saving Throws** :: All +7 or higher
**Skills** :: Insight +11, Persuasion +12
**Damage Resistances** :: poison
**Languages** :: Common, Dwarvish +3
**Challenge** :: 11 (7,200 XP)
___
**Legendary Resistance (2/Day).** :: Choose to succeed on failed save.

**Guildmaster's Authority.** :: All Iron Guild members within 60 ft gain +3 to all rolls.

___
### Actions
**Multiattack.** :: Three warhammer attacks.

**Iron Will +3.** :: *Melee Weapon Attack:* +12 to hit, reach 5 ft., one target. *Hit:* 1d8+8 bludgeoning damage + 2d8 force damage

**Honor Duel (1/Day).** :: Challenge one creature. Both have advantage vs each other, disadvantage vs others. Lasts 1 min.

**Attack.** :: One warhammer attack

**Tactical Order (2 actions).** :: One ally acts immediately

**Iron Defense (2 actions).** :: +5 AC until next turn

}}

### Habitat & Ecology
Garrick maintains his primary forge in Goldreach but travels occasionally to inspect Smiths' Guild chapter houses across both continents and to recover rare materials he won't trust to others. He keeps a personal 

<div class='pageNumber auto'></div>
<div class='footnote'>Chapter 3 - Aethoria & Iron Guild</div>
\page

apprenticeship of three to five dwarven and human craftspeople at any given time, and his selection of any apprentice is taken as a career-defining endorsement. He supplies the Iron Guild with weapons and armor at fair prices and maintains close ties to senior Guild members from his active days, though he no longer accepts contracts himself. He still keeps the warhammer he carried in his expedition days, and he still knows precisely where the bodies are buried — both literally and otherwise.

### Story Hooks
- The party needs Garrick to forge or repair something only he can make — and his price isn't always coin.
- A rival smith claims Garrick stole a technique from them a century ago, and demands the party investigate.
- Garrick has refused to forge for an important client, and that client wants to know why — through the party.
- Garrick seeks worthy hands to recover material from a place his age now prevents him from reaching personally.
\column
### The Beard Rings
Each metal ring braided into Garrick's beard marks a creation he considers significant. He'll discuss most of them at length over good ale. A handful he refuses to discuss at all.

- **Iron** — His first true blade, made at twenty-three. Lost in a battle he won't name.
- **Brass** — The gate-mechanism of Goldreach's east tower. He set it himself, in three days.
- **Copper** — A wedding band. The wearer is dead. He still wears it.
- **Steel** — The Smiths' Guild charter, etched on a single thin ring. He wears the document, not just a memento.
- **Silver** — A blade he made for a Liberator who was never named. The blade was never returned.
- **Black iron** — Unknown. He will not say. Veterans of his early expeditions go quiet when asked.


### Whispers
> *"He gave me my hammer when I was thirteen. He told me it would weigh more every year, and to mind what I struck with it."*  
> — Senior smith, Goldreach

> *"Negotiating with Garrick is like negotiating with a wall that occasionally laughs. The wall is fair. The wall is also a wall."*  
> — Iron Guild captain


<div class='pageNumber auto'></div>
<div class='footnote'>Chapter 3 - Aethoria & Iron Guild</div>
\page

# Chapter 4 - Ascended & Ancient
:
Divine champions blessed by the Seven Ascended, ancient guardians from ages past, and corrupted creatures twisted by dark magic.
 
## Ascended-Touched

Champions blessed by the gods.

## Blessed Paladin

<div class="col-img">![blessed paladin](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-blessed-paladin.jpg) {width:325px}</div>

### Description
Blessed paladins radiate a subtle divine presence. Their eyes occasionally flash with inner light. Their voices carry undertones of authority that transcend normal speech. They move with purpose that suggests divine direction — not mechanically, but with the confidence of those who believe their path is righteous. Their equipment is typically well-maintained and often bears religious symbols. Many wear the iconography of their patron Ascended prominently, and some carry weapons or armor that glow faintly with divine power — gifts from temples or supernatural sources.
\column
### Lore
Blessed paladins are mortal champions who've received divine recognition from one or more of the Seven Ascended — the gods who rose from mortal heroes during the Worldrend. This blessing isn't granted through ritual or application; it comes to those who've already demonstrated the values their patron represents. Some receive it dramatically through visions and miracles; others realize gradually that their prayers are answered more directly and their capability grows. The blessing doesn't remove free will — actions that violate their patron's principles may result in its withdrawal, temporarily or permanently. Their eyes occasionally flash with inner light, their voices carry undertones of authority that transcend normal speech, and their divine smite burns evil with holy fire. Their existence confirms that the Ascended watch the mortal world. Different cultures view different patrons differently — Thaldros respects Thandros's champions and distrusts Aethor's.

{{monster,frame

## Blessed Paladin
*Medium humanoid, lawful good*
___
**Armor Class** :: 18 (plate)
**Hit Points** :: 52 (8d8 + 16)
**Speed** :: 30 ft.
___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|16 (+3) | 11 (+0) | 14 (+2) | 11 (+0) | 14 (+2) | 16 (+3)|
___
**Saving Throws** :: Wisdom +4, Charisma +5
**Skills** :: Religion +2
**Senses** :: passive Perception 12
**Languages** :: Common
**Challenge** :: 4 (1,100 XP)
___
**Divine Health.** :: The paladin is immune to disease.

**Lay on Hands (20 points).** :: As an action, the paladin can touch a creature and restore up to 20 hit points (drawn from a shared pool that refreshes after a long rest). The paladin can also expend 5 points from the pool to cure one disease or neutralize one poison.

___
### Actions
**Multiattack.** :: Two longsword attacks.

**Longsword.** :: *Melee Weapon Attack:* +5 to hit, reach 5 ft., one target. *Hit:* 1d8+3 slashing damage

**Divine Smite (3/Day).** :: Add 2d8 radiant to hit.
}}


<div class='pageNumber auto'></div>
<div class='footnote'>Chapter 4 - Ascended & Ancient</div>
\page

### Cultural Significance
Blessed paladins occupy respected positions in most communities — their divine favor is recognized even by those who worship different Ascended. Many struggle with the weight of expectation: communities expect them to solve problems, mediate disputes, and exemplify virtue. The pressure can be crushing, and some quietly withdraw to serve in less visible ways.

### Habitat & Ecology
Blessed paladins maintain connections with temples and religious orders but aren't necessarily members of formal hierarchies — their authority comes from divine recognition rather than institutional position. Many take to the road as itinerant champions, going wherever they sense their patron's will, while others settle in particular communities as resident protectors. Some quietly retire from public roles when the pressure becomes too great, serving instead in monasteries or as personal mentors to younger devotees. The blessing they carry is both gift and weight, and the longer they bear it, the more clearly they understand which.

### Story Hooks
- A blessed paladin seeks help with a mission too large for any individual to accomplish alone.
- The party must convince a paladin that their cause is genuinely righteous.
- A paladin's blessing is wavering due to a moral complication they can't resolve.
- Someone is falsely claiming paladin status for personal gain — and the deception is starting to harm believers.

## Thandros's Justicar

### Description
Justicars embody law's implacable nature. They dress in formal attire that suggests judicial authority — robes, chains of office, or armor marked with Thandros's scales-and-gavel symbol. Their expressions are stern, their bearing formal, their movements precise. Their equipment often includes judicial implements: weighted symbols representing law's authority, formal documents, and the Mace of Justice that serves as both weapon and badge of office. Their presence commands attention and demands respect for proper procedure.

### Lore
Justicars are chosen by Thandros, god of law, from those who've demonstrated unwavering commitment to justice — former judges, magistrates, investigators who uncovered corruption, enforcers who maintained order fairly. The calling comes through dreams of the divine law court where Thandros himself presides; those who accept find themselves compelled to pursue justice wherever it's denied. They embody law's implacable nature, dressing in robes and chains of office or scales-and-gavel-marked armor, and prefer to resolve situations through proper procedure: investigate, gather evidence, pronounce judgment, then enforce sentence. Violence is a last resort. They're not cruel — justice in Thandros's understanding is about proper order, not punishment for its own sake. Yet they wrestle constantly with the knowledge that they serve Law, and not all laws are just. In Aethoria they are viewed with suspicion as potential tyrants; in Thaldros they are respected agents of proper order.

<div class="col-img">![thandros's justicar](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-thandross-justicar.jpg) {width:325px}</div>

### Cultural Significance
Justicars work within secular legal systems when possible, advising judges and investigating complex cases beyond ordinary capability. Their incorruptibility is admired by those who believe in law and resented by those who've suffered under it. Most Justicars recognize the gap between law and justice — and some quietly work to change unjust laws even as they enforce them.

### Habitat & Ecology
Justicars work in cooperation with secular authorities when possible — advising judges, investigating complex cases beyond normal capability, and handling matters that ordinary law enforcement cannot resolve. They travel widely, going where Thandros directs and never staying long in any one jurisdiction. Most carry their own seals of office and a few specially prepared documents 

<div class='pageNumber auto'></div>
<div class='footnote'>Chapter 4 - Ascended & Ancient</div>
\page

that confirm their authority to local magistrates, and their inquiries are universally respected by Thandrian legal institutions. They are lonely figures by nature, since most jurisdictions both need them and fear them in equal measure.

### Story Hooks
- A Justicar investigates something that intersects with the party's activities.
- The party must prove their innocence to a Justicar already pursuing them.
- A Justicar recognizes that law and justice conflict in their current case, and seeks guidance.
- Someone the party needs is in Justicar custody awaiting judgment.


{{monster,frame
## Thandros's Justicar
*Medium humanoid, lawful neutral*
___
**Armor Class** :: 17 (chain mail, shield)
**Hit Points** :: 91 (14d8 + 28)
**Speed** :: 30 ft.

___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|16 (+3) | 10 (+0) | 14 (+2) | 14 (+2) | 16 (+3) | 14 (+2)|
___
**Saving Throws** :: Wisdom +6, Charisma +5
**Skills** :: Insight +6, Persuasion +5
**Languages** :: Common
**Challenge** :: 6 (2,300 XP)
___
**Divine Authority.** :: Creatures within 30 feet have disadvantage on Charisma (Deception) checks made to lie to the justicar.

**Judgment of Thandros.** :: The justicar can cast *zone of truth* 3 times per day, requiring no material components. The save DC is 14.

___
### Actions
**Multiattack.** :: Two mace attacks.

**Mace of Justice.** :: *Melee Weapon Attack:* +6 to hit, reach 5 ft., one target. *Hit:* 1d6+3 bludgeoning damage + 2d8 radiant damage vs evil

**Gavel Strike (Recharge 5-6).** :: DC 14 Wisdom save or stunned 1 round (symbol of law striking).


}}

## Aethor's Liberator

### Description
Aethor's Liberators appear as beautiful humanoids with luminous features and wings of golden light. Their faces express boundless compassion and fierce determination in equal measure. They can assume mortal forms to move undetected, but their true nature often shows in subtle ways: chains rust in their presence, locked doors tend to swing open, caged creatures grow calm when they pass. In their natural form, the air around them shimmers faintly with warm light, and the chains of every captive within a hundred yards grow brittle.

<div class="col-img">![aethor's liberator](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-aethors-liberator.jpg) {width:325px}</div>

### Lore
Liberators are celestial beings created directly by Aethor, god of freedom, not promoted from mortal champions. They exist for a single purpose: to break chains, free prisoners, and liberate the oppressed. They appear as beautiful humanoids with luminous features and wings of golden light, and can assume mortal forms to move undetected — though their true nature often shows in subtle ways: chains rust in their presence, locked doors swing open, caged creatures grow calm. They appear in Tirvandor only when Aethor's attention is drawn to particular bondage or oppression beyond mortal capability to address; ordinary injustice must be overcome by mortals themselves. They prefer diplomacy and persuasion, and don't hate oppressors the way mortals might — slavers and tyrants are obstacles to freedom, not personal enemies. In Aethoria they are beloved messengers; in Thaldros they are dangerous subversives whose mere presence undermines proper order.


### Cultural Significance
A Liberator's arrival is celebrated in Aethoria as divine confirmation of the nation's founding values, and the stories of their interventions inspire continued resistance for years afterward. In Thaldros, the same event is treated as a crisis — proof that supernatural forces have taken sides against proper order — and 

<div class='pageNumber auto'></div>
<div class='footnote'>Chapter 4 - Ascended & Ancient</div>
\page

triggers immediate reinforcement of every prison and chain in the region.

### Habitat & Ecology
Liberators operate independently, following Aethor's guidance rather than mortal authority. They respect those who work toward freedom but do not subordinate themselves to mortal movements or organizations. They communicate telepathically and can understand any language — freedom transcends linguistic barriers. They don't hate oppressors the way mortals might; they see slavers and tyrants as obstacles to freedom rather than personal enemies, a perspective that sometimes frustrates mortals who want righteous vengeance. When their mission concludes, they return to Aethor's presence, and their interventions on Tirvandor remain rare.


{{monster,frame
## Aethor's Liberator
*Medium celestial, chaotic good*
___
**Armor Class** :: 17 (natural)
**Hit Points** :: 136 (16d8 + 64)
**Speed** :: 30 ft., fly 90 ft.
___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|18 (+4) | 18 (+4) | 18 (+4) | 17 (+3) | 20 (+5) | 20 (+5)|
___
**Saving Throws** :: Wisdom +8, Charisma +8
**Skills** :: Insight +8, Perception +8
**Damage Resistances** :: radiant; bludgeoning, piercing, slashing from nonmagical attacks
**Condition Immunities** :: charmed, frightened
**Senses** :: darkvision 120 ft.
**Languages** :: all, telepathy 120 ft.
**Challenge** :: 7 (2,900 XP)
___
**Magic Resistance.** :: The liberator has advantage on saving throws against spells and other magical effects.
**Innate Spellcasting.** :: The liberator's innate spellcasting ability is Charisma (spell save DC 16). It can innately cast the following spells, requiring no material components:

At will: *knock, dispel magic* ::
3/day each: *freedom of movement* ::
1/day each: *plane shift* ::
__
### Actions
**Multiattack.** :: Two mace attacks.
**Freedom's Mace.** :: *Melee Weapon Attack:* +7 to hit, reach 5 ft., one target. *Hit:* 1d6+4 bludgeoning damage + 4d8 radiant damage
**Break All Bonds.** :: All restrained/paralyzed creatures within 30 ft freed automatically.
**Change Shape.** :: Can polymorph into humanoid or Medium beast.
}}

\column

### Story Hooks
- A Liberator arrives to free someone the party needs to remain captive for larger reasons.
- The party must locate a Liberator for a liberation beyond their own capability.
- A Liberator's intervention creates political complications the party must navigate.
- The party witnesses a Liberator's appearance and must decide how to respond — and to whom they report it.

## Moira's Seer

<div class="col-img">![moira's seer](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-moira-seer.jpg) {width:325px}</div>

### Description
Moira's Seers look perpetually distracted, their eyes focused on things others cannot see. They dress in practical but often mismatched clothing — fashion matters little when you can see possible futures. Many have prematurely gray or white hair, as if witnessing too many possibilities ages them. Their eyes are their most notable feature: often clouded, occasionally glowing, sometimes seeming to look through rather than at whoever they are addressing. They speak in tenses that don't quite match the present, and their conversations often include references to events that haven't happened yet.

<div class='pageNumber auto'></div>
<div class='footnote'>Chapter 4 - Ascended & Ancient</div>
\page

### Lore
Seers are chosen by Moira, goddess of fate, from among those who already demonstrate unusual sensitivity to time and possibility — those with prophetic dreams from childhood, or who developed prescience after traumatic events. The calling comes through visions of the Weaver's Loom, where Moira tends the threads of fate, and those who accept learn to read the threads themselves: imperfectly, partially, but genuinely. Training emphasizes interpretation rather than simple sight; seeing possibilities is the easy part, understanding which might come to pass is the seer's true art. Their eyes are often clouded or focused on things others cannot see, and they speak in tenses that don't quite match the present. Everyone wants to know the future; few appreciate the complexity of actually knowing it. Many live as hermits to escape demands for impossible clarity. Their cryptic communication isn't evasion — prophecy itself resists direct statement.

### Cultural Significance
Seers are respected across Tirvandor as genuine prophets — their predictions don't always come true (prophecy is probability, not certainty) but they're accurate often enough to be valued. They're also figures of suspicion: those who know the future might manipulate events toward preferred outcomes, and their cryptic style does nothing to dispel that worry.

{{monster,frame
## Moira's Seer
*Medium humanoid, any*
___
**Armor Class** :: 12 (15 with *mage armor*)
**Hit Points** :: 60 (11d8 + 11)
**Speed** :: 30 ft.

___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|9 (-1) | 14 (+2) | 12 (+1) | 18 (+4) | 20 (+5) | 14 (+2)|
___
**Saving Throws** :: Intelligence +7, Wisdom +8
**Skills** :: Arcana +7, History +7, Insight +11
**Languages** :: Common +4 others
**Challenge** :: 5 (1,800 XP)
___
**Foresight.** :: The seer can't be surprised and adds +5 to her initiative rolls.

**Read Fate.** :: The seer can cast *augury* at will and *divination* 3 times per day, requiring no material components.

___
### Actions
**Quarterstaff.** :: *Melee Weapon Attack:* +2 to hit, reach 5 ft., one target. *Hit:* 1d6-1 bludgeoning

**Prophetic Vision (Recharge 5-6).** :: One creature within 60 ft sees possible futures. DC 16 Wisdom save or incapacitated 1 round (overwhelmed by visions).

**Weaver's Warning (1/Day).** :: Grant one creature reroll on any d20 within next hour.


}}

### Habitat & Ecology
Many Seers live as hermits in remote locations, limiting contact with those who would demand impossible clarity. Others serve as advisors to leaders willing to accept ambiguity, and a few become frauds, providing the simple predictions people want rather than the complicated truths they see. They maintain informal connections with one another, sharing techniques for managing the burden of sight; these networks span political boundaries, since prophecy does not care about nations. They tend to be solitary by inclination as well as necessity — knowing the future makes ordinary social rhythms harder to inhabit.

### Story Hooks
- A Seer provides cryptic guidance that only makes sense after events have unfolded.
- The party must protect a Seer from those who would exploit prophetic gifts for power.
- A Seer's prediction threatens to become self-fulfilling in catastrophic ways.
- The party seeks a Seer for information about future events that other sources can't provide.
- 
## Sylvara's Wild Hunter

<div class="col-img">![sylvara's wild hunter](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-sylvaras-wild-hunter.jpg) {width:325px}</div>

<div class='pageNumber auto'></div>
<div class='footnote'>Chapter 4 - Ascended & Ancient</div>
\page

### Description
Wild Hunters appear as lithe, fierce humanoids with features suggesting various predatory animals — wolf-like eyes, antlered brows, or fingers ending in subtle claws. Leaves and vines often grow directly from their skin, and their hair moves like living things. They are naturally camouflaged in wild environments, their appearance shifting subtly to blend with their surroundings. In forests they are dappled with green and brown; in tundra, pale as snow; in desert, tawny and sun-bleached. They move silently even on broken ground, and their breath smells of wildflowers and clean rain.

### Lore
Wild Hunters are fey created by Sylvara, goddess of nature and the wild, not promoted from mortal stock. They are nature's defenders, born of divine will and wild magic, appearing as lithe fierce humanoids with features suggesting predatory animals — wolf-like eyes, antlered brows, claws — with leaves and vines growing directly from their skin. They appear where the wild is threatened: forests being clear-cut, rivers being poisoned, ecosystems being destroyed. Individual Hunters persist for centuries, becoming tied to particular regions they protect, and some local communities almost worship them as forest spirits. They judge mortals by relationship with nature — civilization itself is not evil to them, only destruction. Those who respect the wild receive guidance and protection; those who harm it face relentless pursuit. Wild Hunters never forget offenses against nature, and they never stop hunting until balance is restored.

### Cultural Significance
In rural communities, Wild Hunters are respected and feared as genuine forces of nature. Farmers and hunters who maintain traditional practices respecting ecological balance may receive their protection; those who over-hunt or over-harvest may find themselves targets. Urban populations rarely encounter them directly, but stories of their wrath serve as cultural reminders about which woods are not to be entered after dark.

### Habitat & Ecology
Individual Wild Hunters persist for centuries, becoming tied to particular regions they protect — a single forest, river valley, or mountain range. Their perspective is genuinely alien to most mortals, focused on species and ecosystems rather than individuals. They communicate in terms that emphasize natural cycles, predator-prey relationships, and ecological balance. They maintain loose connections with each other and with other fey, sharing information about threats and coordinating responses to large-scale environmental destruction. Within their territory, lesser fey acknowledge their authority, and even seasoned druids approach them with deference.
\column
### Story Hooks
- A Wild Hunter is pursuing someone the party needs to protect — for reasons both have.
- The party must gain Wild Hunter approval to enter protected wilderness.
- Environmental destruction threatens to summon a Wild Hunter response that will catch innocents in the crossfire.
- A Wild Hunter seeks mortal help with a threat too large or too magical for them to face alone.

{{monster,frame
## Sylvara's Wild Hunter
*Medium fey, chaotic neutral*
___
**Armor Class** :: 16 (natural)
**Hit Points** :: 127 (15d8 + 60)
**Speed** :: 40 ft.
___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|18 (+4) | 19 (+4) | 18 (+4) | 14 (+2) | 17 (+3) | 16 (+3)|
___
**Saving Throws** :: Dexterity +7, Wisdom +6
**Skills** :: Nature +5, Perception +9, Stealth +10
**Damage Resistances** :: lightning, thunder
**Senses** :: darkvision 120 ft.
**Languages** :: Sylvan, Common
**Challenge** :: 8 (3,900 XP)
___
**Wild Empathy.** :: Beasts will not attack the hunter unless provoked, and the hunter has advantage on Charisma checks made to influence them.

**Storm's Fury.** :: When the hunter is hit by a melee attack, the attacker takes 1d8 lightning damage.

___
### Actions
**Multiattack.** :: Three longbow attacks or two spear attacks.

**Spear.** :: *Melee Weapon Attack:* +7 to hit, reach 5 ft., one target. *Hit:* 1d6+4 piercing damage + 2d6 lightning damage

**Storm Bow.** :: *Ranged Weapon Attack:* +7 to hit, range 150/600 ft., one target. *Hit:* 1d8+4 piercing damage + 2d6 lightning damage

**Call the Wild (Recharge 5-6).** :: Summon 2d4 wolves (arrive next round, last 1 hour).

**Lightning Leap.** :: Teleport up to 60 ft as bonus action, leaving lightning in space (5d6 lightning, DC 15 Dexterity).


}}

<div class='pageNumber auto'></div>
<div class='footnote'>Chapter 4 - Ascended & Ancient</div>
\page

## Sera's Mercy

<div class="col-img">![sera's mercy](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-seras-mercy.jpg) {width:325px}</div>

### Description
Sera's Mercies are small celestial beings, typically appearing as luminous children or diminutive winged figures radiating gentle light. Their features are soft and compassionate, their expressions conveying profound empathy and kindness. They glow with warm, healing light that intensifies when they use their powers. Their presence brings feelings of comfort and safety even in dangerous situations; those near a Mercy feel strangely calm, as if even the wounded earth around them is at rest.

### Lore
Mercies are small celestial servants created by Sera, goddess of healing and compassion, to ease suffering wherever it occurs — healing the wounded, comforting the dying, offering hope to the despairing. They appear as luminous children or diminutive winged figures radiating warm light, and their presence brings strange calm even in dangerous situations. They avoid violence almost absolutely; only undead suffer from their touch, as the same energy that restores life destroys its mockery. They appear during plagues, disasters, and wars — divine compassion accompanying mortal pain. They treat all suffering equally, healing wounded enemies as readily as wounded allies, which sometimes frustrates those who would use them as tactical assets. Sera's theology answers that all suffering deserves compassion: if compassion has limits, it isn't truly compassion. Even nations at war welcome Mercies onto their battlefields.

{{monster,frame
## Sera's Mercy
*Small celestial, neutral good*
___
**Armor Class** :: 14
**Hit Points** :: 45 (10d6 + 10)
**Speed** :: 30 ft., fly 60 ft.
___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|10 (+0) | 18 (+4) | 12 (+1) | 14 (+2) | 18 (+4) | 16 (+3)|
___
**Skills** :: Medicine +8, Insight +6
**Damage Resistances** :: radiant
**Condition Immunities** :: charmed, frightened
**Senses** :: darkvision 60 ft.
**Languages** :: all, telepathy 60 ft.
**Challenge** :: 3 (700 XP)
___
**Healing Aura (30 ft).** :: Allied creatures that start their turn within 30 feet of the mercy regain 5 hit points.

**Innate Healing.** :: The mercy's innate spellcasting ability is Wisdom (spell save DC 15). It can innately cast the following spells, requiring no material components:

At will: *cure wounds* (1st level) ::
3/day each: *lesser restoration* ::
1/day each: *raise dead* ::

___
### Actions
**Touch of Mercy.** :: *Melee Weapon Attack:* +6 to hit, reach 5 ft., one target. *Hit:* target healed for 2d8+4 HP or takes 2d8+4 radiant (undead only).

**Shield of Compassion (3/Day).** :: Grant one creature within 60 ft resistance to all damage until end of its next turn.

**Peaceful Presence (Recharge 6).** :: All creatures within 30 ft make DC 14 Wisdom save or can't attack for 1 minute (charmed effect).


}}

### Cultural Significance
Mercies are universally beloved across Tirvandor — perhaps the only creatures the warring nations agree on. Their impartiality occasionally creates problems: when a Mercy heals a notorious villain or comforts a dying tyrant, some question whether compassion should extend so far. Sera's faithful answer the question by repeating it.

### Habitat & Ecology
Individual Mercies may linger in particular locations — hospitals, temples, sites of ongoing tragedy — providing continuous care for as long as suffering continues. They communicate telepathically in any language, conveying emotion as much as words; their vocabulary is shaped by their purpose, focused on suffering, healing, hope, 

<div class='pageNumber auto'></div>
<div class='footnote'>Chapter 4 - Ascended & Ancient</div>
\page

and comfort. They do not judge those they help, and their compassion extends to everyone — heroes and villains, saints and sinners. They appear during plagues, disasters, and wars, and depart only when the suffering they came to address has eased.

### Story Hooks
- A Mercy is healing someone the party needs to capture before they can flee.
- The party must protect a Mercy from those who would exploit or destroy it.
- A Mercy's presence in an unexpected location raises serious questions about what's happening there.
- The party seeks a Mercy for healing beyond normal capability — and must convince it the cause is just.

## Mordain's Sentinel

<div class="col-img">![mordain's sentinel](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-mordains-sentinel.jpg) {width:325px}</div>

### Description
Mordain's Sentinels wear ancient armor, typically from the era when they died, and carry weapons of equal antiquity. Their forms are skeletal or desiccated, but project power rather than horror. Their eye sockets glow with cold white light — not the malevolent fire of evil undead but the steady radiance of duty fulfilled. They move with military precision and their presence is solemn rather than terrifying. Wherever they stand, the air carries a faint chill and the smell of ancient stone.

### Lore
Sentinels are undead warriors animated by divine will rather than necromantic magic. Each was a warrior who died protecting sacred sites, fulfilling oaths, or serving Mordain's principles of honor and proper death — and rather than passing to the afterlife, received Mordain's blessing to continue their service eternally. This isn't necromancy in the usual sense; Sentinels chose to remain and could pass on if they wished, but their duty isn't yet complete. They wear the ancient armor they died in and carry weapons of equal antiquity. Their eye sockets glow with cold white light — not the malevolent fire of evil undead but the steady radiance of duty fulfilled. They guard rather than attack, challenging those who approach their sites and granting passage to the respectful. They retain full intelligence from their living days, often enhanced by centuries of contemplation, and make excellent sources of history living memory has lost.

{{monster,frame
## Mordain's Sentinel
*Medium undead, lawful neutral*
___
**Armor Class** :: 20 (plate, shield)
**Hit Points** :: 180 (19d8 + 95)
**Speed** :: 30 ft.
___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|20 (+5) | 11 (+0) | 20 (+5) | 12 (+1) | 16 (+3) | 18 (+4)|
___
**Saving Throws** :: Strength +9, Constitution +9, Wisdom +7
**Damage Immunities** :: necrotic, poison
**Condition Immunities** :: exhaustion, frightened, poisoned
**Senses** :: darkvision 120 ft.
**Languages** :: Common
**Challenge** :: 10 (5,900 XP)
___
**Eternal Vigil.** :: The sentinel can't be surprised and is immune to magical sleep.

**Turn Immunity.** :: The sentinel is immune to features that turn undead.

**Magic Resistance.** :: The sentinel has advantage on saving throws against spells and other magical effects.

___
### Actions
**Multiattack.** :: Three longsword attacks.

**Longsword of Vigil.** :: *Melee Weapon Attack:* +9 to hit, reach 5 ft., one target. *Hit:* 1d8+5 slashing damage + 3d8 necrotic damage

**Sentinel's Command (Recharge 5-6).** :: All undead within 60 ft gain +2 AC and advantage on attacks for 1 min.

**Honor the Fallen (1/Day).** :: All dead within 30 ft rise as shadows under sentinel's control for 1 hour.


}}

<div class='pageNumber auto'></div>
<div class='footnote'>Chapter 4 - Ascended & Ancient</div>
\page

### Cultural Significance
Sentinels are respected as honorable guardians rather than feared as monsters. Communities near Sentinel-protected sites maintain proper relationships with them — offerings, maintenance for the tombs they guard, the occasional formal acknowledgment — in exchange for protection. They embody Mordain's central teaching: death is transition, not ending.

### Habitat & Ecology
Sentinels are tied to specific sites — tombs, temples, sacred battlefields, and other locations significant to the cycle of death and memory. They rarely leave these places, since their entire purpose is bound up in guardianship. They maintain communication with other Sentinels through mysterious means that scholars debate but cannot replicate, sharing information about threats and coordinating responses to desecration. They can command other undead within their territory, organizing defensive forces against intruders, and many appreciate visitors who treat them as individuals rather than obstacles — engaging in conversation before, or instead of, combat.

### Story Hooks
- A Sentinel guards something the party needs to access, and won't simply let them through.
- The party must negotiate passage through Sentinel-protected territory.
- A Sentinel's ancient knowledge is essential for understanding current events.
- A Sentinel seeks help protecting its site from threats beyond its individual capability.

## Fallen Champion

### Description
Fallen Champions retain the bearing of the heroes they once were, but corruption has twisted their features. Their armor is tarnished or rusted, their weapons darkened, their eyes burning with bitter fire rather than divine light. They radiate despair rather than hope — an aura of failure and corruption that affects everyone nearby. Their presence feels wrong in ways that transcend physical appearance, as if reality itself rejects what they have become. The air near them is colder than it should be, and small lights flicker and gutter as they pass.

### Lore
Fallen Champions were once blessed paladins or divine champions who broke their oaths, succumbed to corruption, or betrayed the principles that earned their blessing. The fall didn't simply remove divine favor — it twisted that favor into something terrible. It can happen many ways: desperation that led to forbidden actions, gradual compromise that eventually crossed uncrossable lines, deliberate betrayal for power or revenge. Whatever the cause, the result is the same — blessed champions become cursed monsters. They retain the bearing of the heroes they once were, but their armor is tarnished, their weapons darkened, their eyes burning with bitter fire rather than divine light. Their hatred is total: of what they were, of those who remain faithful, of the gods whose standards they couldn't meet. Many who encounter Fallen Champions feel sorrow alongside fear, mourning what was lost as much as fearing what remains.

<div class="col-img">![fallen champion](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-fallen-champion.jpg) {width:325px}</div>

### Cultural Significance
Fallen Champions are cautionary tales told in temple sermons across Tirvandor — reminders that even blessed heroes can fall, that righteousness requires constant vigilance, and that no one is immune to corruption's temptation. They are also tragedies: people who once served divine purpose, reduced to monsters by choices that seemed defensible at the time.

### Habitat & Ecology
Fallen Champions retain their living intelligence but their perspective is warped by corruption — they remember their former ideals but now see them as naive or foolish, and they remember their former allies but now view them as enemies or fools. They are usually solitary, though some gather followers among those attracted to their power or convinced by their 

<div class='pageNumber auto'></div>
<div class='footnote'>Chapter 4 - Ascended & Ancient</div>
\page

bitter philosophy. Some serve dark powers that contributed to their fall; others operate independently, pursuing personal vendettas or nihilistic destruction; a few desperately seek redemption while fearing it is impossible. They tend to haunt the ruins of the things they once defended.

### Story Hooks
- A Fallen Champion from a party member's past resurfaces, asking for things the party can't give.
- The party must stop a champion in the process of falling — before their conversion is complete.
- A Fallen Champion seeks genuine redemption and approaches the party for help.
- Information about current threats lies locked inside a Fallen Champion's corrupted memories.

{{monster,frame
## Fallen Champion
*Medium undead, any evil*
___
**Armor Class** :: 18 (plate)
**Hit Points** :: 135 (18d8 + 54)
**Speed** :: 30 ft.
___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|18 (+4) | 12 (+1) | 16 (+3) | 11 (+0) | 12 (+1) | 14 (+2)|
___
**Saving Throws** :: Strength +8, Constitution +7
**Damage Immunities** :: poison
**Condition Immunities** :: exhaustion, poisoned
**Senses** :: darkvision 60 ft.
**Languages** :: Common
**Challenge** :: 9 (5,000 XP)
___
**Corrupted Divine.** :: The champion was once blessed by the Ascended but fell from grace. It retains corrupted divine power and is treated as an undead for the purposes of effects that target evil or undead creatures.

**Desecrated Ground.** :: The area within 30 feet of the champion is cursed ground. Living creatures within this area have disadvantage on saving throws against spells and effects that cause fear or necrotic damage.

___
### Actions
**Multiattack.** :: Three greatsword attacks.

**Cursed Greatsword.** :: *Melee Weapon Attack:* +8 to hit, reach 5 ft., one target. *Hit:* 2d6+4 slashing damage + 2d8 necrotic damage

**Aura of Despair (Recharge 5-6).** :: All creatures within 30 ft make DC 15 Wisdom save or frightened 1 min. Frightened creatures have speed 0.

**Corrupted Smite (3/Day).** :: Add 4d8 necrotic to attack.


}}

\column

## Ancient & Prophecy

Timeless guardians and prophetic beings.

## Ancient Guardian

<div class="col-img">![ancient guardian](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-ancient-guardian.jpg) {width:325px}</div>

### Description
Ancient Guardians are massive constructs of stone, metal, and materials that defy easy identification. They stand eight to twelve feet tall, their forms vaguely humanoid but clearly artificial. Their surfaces bear inscriptions in languages that predate recorded history, and their joints glow with energy that isn't quite magical in any recognized tradition. They don't rust, erode, or decay — Guardians that have stood for millennia show no more wear than those created yesterday. Their eyes, if they can be called eyes, glow with a steady light that suggests awareness without emotion.

### Lore
Ancient Guardians were built during the Age of Myth, before the Worldrend, by civilizations using principles of construction now utterly forgotten. They were created to guard sites of prophetic significance — places where the fabric of time grows thin, where knowledge too dangerous for casual access is preserved. The creators are gone, their civilizations fell, their names are forgotten, but the Guardians remain, fulfilling directives established before the Ascended were born. Their 

<div class='pageNumber auto'></div>
<div class='footnote'>Chapter 4 - Ascended & Ancient</div>
\page

surfaces bear inscriptions in languages that predate recorded history, and they neither rust nor erode nor decay; one that has stood for millennia shows no more wear than one created yesterday. They don't attack without cause — they assess approaching visitors against protocols established by creators dead for ages, and those who pass the tests receive access to what is protected. Whether Guardians are truly intelligent, or merely sophisticated automata containing fragments of their creators' minds, is endlessly debated.

{{monster,frame
## Ancient Guardian
*Large construct, neutral*
___
**Armor Class** :: 17 (natural)
**Hit Points** :: 178 (17d10 + 85)
**Speed** :: 20 ft.

___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|22 (+6) | 9 (-1) | 20 (+5) | 10 (+0) | 11 (+0) | 1 (-5)|
___
**Damage Immunities** :: poison, psychic; bludgeoning, piercing, and slashing from nonmagical attacks
**Condition Immunities** :: charmed, exhaustion, frightened, paralyzed, petrified, poisoned
**Senses** :: darkvision 120 ft., truesight 30 ft.
**Languages** :: understands Ancient tongue
**Challenge** :: 8 (3,900 XP)
___
**Immutable Form.** :: The guardian is immune to any spell or effect that would alter its form.

**Magic Resistance.** :: The guardian has advantage on saving throws against spells and other magical effects.

**Prophetic Inscription.** :: The guardian's body is covered in ancient prophecies. A creature that spends 10 minutes studying the inscriptions while within 5 feet must make a DC 15 Intelligence saving throw. On a success, the creature gains a fragment of prophetic knowledge (DM's choice). On a failure, the creature takes 3d6 psychic damage and is confused for 1 minute.

___
### Actions
**Multiattack.** :: Two slam attacks.

**Slam.** :: *Melee Weapon Attack:* +9 to hit, reach 10 ft., one target. *Hit:* 3d8+6 bludgeoning damage

**Time Ripple (Recharge 5-6).** :: All creatures in 20 ft radius make DC 16 Wisdom save. Failed save: sent forward in time 1 round (miss turn, reappear in same space). Success: take 4d10 psychic damage.


}}

### Cultural Significance
Finding a Guardian is always significant — it means discovering something the ancients considered worth protecting, knowledge or artifacts or locations with importance that transcends normal historical scale. Many cultures have legends about Guardians, though the legends don't always identify them correctly. Stories of "stone giants" or "metal golems" lurking in deep ruins often refer to Guardian encounters dressed in folk language.

### Habitat & Ecology
Guardians stand watch at fixed locations established in ages now forgotten — pre-Worldrend ruins, hidden chambers beneath modern cities, sealed temples in remote wastelands. Each operates independently, following its own directives, and if multiple Guardians protect the same site they coordinate seamlessly though without apparent communication. They have remained in place for thousands of years, and many have not moved since their creators died. Geological shifts occasionally expose new Guardians as ancient chambers crack open; each such discovery reveals that the world is older and stranger than comfortable assumption suggests.

### Story Hooks
- A Guardian blocks access to something the party desperately needs.
- The party must determine what test a particular Guardian requires for access.
- A Guardian has begun moving for the first time in centuries — what changed?
- Knowledge of Guardian construction might be recoverable, with implications nobody wants to think about.

## Prophecy Keeper

### Description
Prophecy Keepers are genuinely alien beings that don't conform to normal physical expectations. They appear as roughly humanoid concentrations of impossible geometry — angles that shouldn't connect, surfaces that seem to extend in directions that don't exist, forms that the eye struggles to process and the mind struggles to remember. They hover rather than walk, their forms trailing wisps of what might be energy, might be memory, might be something else entirely. Looking at them too long causes headaches; looking away, the mind struggles to recall what was seen. Their "eyes," scattered across their forms in patterns that shift constantly, glow with light that seems to come from distant times rather than present sources.

### Lore
Prophecy Keepers are genuinely alien beings that don't conform to normal physical expectations — roughly humanoid concentrations of impossible geometry, with angles that shouldn't connect and forms the eye struggles to process and the mind to remember. Whether they're natural phenomena, created beings, or something else entirely is unknown; they may predate the material world itself. They exist outside normal time, observing and recording fate from perspectives that transcend mortal comprehension, and they perceive past, present, and possible futures 

<div class='pageNumber auto'></div>
<div class='footnote'>Chapter 4 - Ascended & Ancient</div>
\page

simultaneously. Conversations with them are disorienting — they sometimes answer questions before they're asked, or reference events that haven't happened yet. They claim no allegiance to god, nation, or cause. They observe. They record. They remember. Some traditions call them "the Watchers" or "the Recorders"; some believe they serve the Weaver, Moira's cosmic aspect. None of this comforts those who realize that something has been watching them all along.

<div class="col-img">![prophecy keeper](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-prophecy-keeper.jpg) {width:325px}</div>

### Habitat & Ecology
Keepers appear in Tirvandor at locations where destiny concentrates — places where important events occur, where choices with lasting consequences are made, where the threads of fate are especially visible. Their presence indicates that something significant is happening or about to. They do not form communities in any recognizable sense; multiple Keepers might attend a significant event without appearing to interact. Perhaps they don't need to — if they share perception of all possibilities, communication would be redundant. They can speak any language and communicate telepathically, though their communications often include information that doesn't parse in normal temporal sequence.

{{monster,frame
## Prophecy Keeper
*Medium aberration, lawful neutral*
___
**Armor Class** :: 15 (natural)
**Hit Points** :: 142 (15d8 + 75)
**Speed** :: 0 ft., fly 40 ft. (hover)
___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|10 (+0) | 20 (+5) | 20 (+5) | 22 (+6) | 22 (+6) | 18 (+4)|
___
**Saving Throws** :: Intelligence +10, Wisdom +10, Charisma +8
**Skills** :: Arcana +14, History +14
**Damage Resistances** :: psychic
**Senses** :: truesight 120 ft., passive Perception 16
**Languages** :: all, telepathy 120 ft.
**Challenge** :: 10 (5,900 XP)
___
**Keeper of Fate.** :: The keeper has perfect knowledge of all events related to the prophecies it records. It can recall any historical event it has observed with complete accuracy.

**Unchangeable.** :: The keeper is immune to chronomancy effects and any magic that would alter fate, including divinations targeted at it.

**Innate Spellcasting.** :: The keeper's innate spellcasting ability is Wisdom (spell save DC 18). It can innately cast the following spells, requiring no material components:

At will: *detect thoughts, legend lore*
3/day each: *scrying, modify memory*
1/day each: *foresight*

___
### Actions
**Multiattack.** :: Three psychic lance attacks.

**Psychic Lance.** :: *Ranged Weapon Attack:* +10 to hit, range 120 ft., one target. *Hit:* 3d10+5 psychic damage

**Reveal Fate (Recharge 5-6).** :: Show one creature their destined future. DC 18 Wisdom save or stunned 1d4 rounds (overwhelming vision). On success, gain advantage on next d20 roll.

**Alter Memory (3/Day).** :: As *modify memory* spell.


}}

### Cultural Significance
Encountering a Prophecy Keeper is unsettling regardless of outcome. The knowledge that something is watching and recording — something with capabilities beyond mortal comprehension — changes how people think about their choices and their place in fate's design. A Keeper's presence indicates that important events are occurring (or about to), which can be reassuring or terrifying depending on the situation. Their memory-altering capability raises uncomfortable 
questions about how much of recorded history is actually accurate, and how much was edited by something we never noticed.

<div class='pageNumber auto'></div>
<div class='footnote'>Chapter 4 - Ascended & Ancient</div>
\page

### Story Hooks
- A Prophecy Keeper's presence indicates the party is involved in destined events they did not consent to.
- The party must communicate with a Keeper to understand what has been recorded about their actions.
- Someone seeks to destroy or capture a Keeper, with unknown consequences for reality itself.
- A Keeper's revealed prophecy conflicts directly with what the party believed their mission to be.

### What the Keepers Know
A Prophecy Keeper cannot be compelled to share what it has witnessed — but those who have successfully bargained for information report fragments that disturb more than they illuminate. From scattered accounts:

- They have been present at every major Worldrend-era event. Every one.
- They do not appear to communicate with each other. They do not appear to *need* to.
- Their memory-alteration ability is not coercive; it is editorial. They will sometimes adjust what someone remembers about an event they personally witnessed. The purpose is unclear. The implication is that they consider some truths too dangerous for the timeline.
- They never lie. They simply do not always say everything.
- Some scholars believe the Keepers are not observers but *archivists* — and that there is something they are recording for. Whatever that thing is, it has not yet read the archive.

### Whispers
> *"I asked it what my future held. It said: 'I have already told you. You will remember soon.'"*  
> — Survivor, Order of Moira

> *"Do not look at one too long. You will not see anything you didn't already know. But you will know it differently."*  
> — Common warning, Goldreach scholars

## Forgotten King

### Description
The Forgotten King appears as a regal figure in ancient formal attire, his features partially obscured by shadows that cling to him regardless of lighting. His crown — the Crown of Forgotten Kings — is clearly visible: a circlet of black metal set with gems that glow with dim, sad light. He was handsome once, perhaps still is in a mournful way. His bearing remains royal despite millennia of death. His eyes burn with cold fire — intelligence, regret, and determination still visible despite his undead state. He does not decay as ordinary undead do; whatever preserves him maintains an appearance of life, though one clearly wrong in ways that resist definition.

<div class="col-img">![forgotten king](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-forgotten-king.jpg) {width:325px}</div>

### Lore
The Forgotten King ruled a dynasty that flourished before the Worldrend — a kingdom so ancient that its name has been lost along with almost all records of its existence. According to fragmentary prophecy, he was one of an original "Seven" whose failure preceded the Worldrend and set the stage for the Seven Ascended's rise. What that earlier Seven were supposed to accomplish, and how they failed, remains unclear; the King himself seems unable or unwilling to explain. He exists in eternal waiting, convinced prophecy will eventually restore his dynasty or at least conclude his story. He has been waiting for millennia. His patience is eternal, but his hope occasionally wavers into something like despair. He isn't simply evil — he is trapped, desperate, and willing to do terrible things to achieve a restoration that may be impossible. His evil is the corruption of good intentions extended beyond all reasonable limits, and his shadow-clung crown still smolders with the dim glow of forgotten kings.

### Cultural Significance
The Forgotten King represents what happens when prophecy fails — or when its fulfillment takes longer than any mortal could endure. His existence raises 

<div class='pageNumber auto'></div>
<div class='footnote'>Chapter 4 - Ascended & Ancient</div>
\page

uncomfortable questions about destiny, patience, and whether some fates are worse than death. Stories of "the King Who Waits" appear in various traditions, usually as cautionary tales about binding oneself too tightly to prophetic promise. His connection to the original Seven who preceded the Seven Ascended is theologically significant; some scholars believe understanding his failure is necessary to prevent its repetition in this age.

### Habitat & Ecology
The Forgotten King dwells in the ruins of his lost dynasty — a buried palace beneath layers of geological time, its halls preserved by his magic and his will. He is isolated. Whatever court he once commanded has crumbled, whatever subjects once served him are dust. He exists alone with his memories, his regrets, and his desperate hope that prophecy will finally deliver what it promised. He can be reasoned with — his intelligence permits negotiation — but his goals are fundamentally incompatible with the current world. He wants restoration of something that no longer exists, and he will trade ancient secrets for the smallest gestures toward that impossible end.

### Story Hooks
- The party must negotiate with the Forgotten King for access to ancient knowledge or a forgotten artifact.
- Someone attempts to "fulfill" his prophecy on his behalf, with potentially disastrous consequences.
- The party discovers unsettling connections between the Forgotten King's failure and current events.
- The Forgotten King seeks the party's help with something specific, willing to trade valuable knowledge for the favor.

### The First Seven
Fragmentary prophecy speaks of a Seven who preceded the Seven Ascended — mortal champions of an earlier age, each charged with a role in averting some great calamity. They failed. The Worldrend followed. What scholars have pieced together from surviving inscriptions:

- The Worldrend was not a natural disaster. It was a consequence.
- The original Seven each held a fragment of something — power, knowledge, oath. The fragments were meant to fit together.
- Only one fragment-holder remains: the Forgotten King. The others were destroyed, lost, or — the disturbing possibility — became something else entirely.
- The Seven Ascended of the current age may be a deliberate response to the first Seven's failure. Or they may be repeating the same pattern.

{{monster,frame
## Forgotten King
*Medium undead, neutral evil*
___
**Armor Class** :: 17 (natural)
**Hit Points** :: 135 (18d8 + 54)
**Speed** :: 30 ft.
___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|11 (+0) | 16 (+3) | 16 (+3) | 20 (+5) | 14 (+2) | 16 (+3)|
___
**Saving Throws** :: Constitution +9, Intelligence +11, Wisdom +8
**Skills** :: Arcana +17, History +17
**Damage Resistances** :: cold, lightning, necrotic
**Damage Immunities** :: poison; bludgeoning, piercing, and slashing from nonmagical attacks
**Condition Immunities** :: charmed, exhaustion, frightened, paralyzed, poisoned
**Senses** :: truesight 120 ft.
**Languages** :: Common +10 others
**Challenge** :: 15 (13,000 XP)
___
**Legendary Resistance (3/Day).** :: If the king fails a saving throw, he can choose to succeed instead.
**Paralyzing Touch.** :: Creatures hit by the king's Touch of Death must succeed on a DC 17 Constitution saving throw or be paralyzed for 1 minute. The creature can repeat the save at the end of each of its turns.
**Spellcasting.** :: The king is an 18th-level spellcaster. His spellcasting ability is Intelligence (spell save DC 19, +11 to hit with spell attacks). He has all wizard spells prepared and may cast any of them using his available slots:
Cantrips (at will): *fire bolt, mage hand, ray of frost, minor illusion* ::
1st level (4 slots): *mage armor, magic missile, shield, detect magic* ::
2nd level (3 slots): *misty step, detect thoughts, scorching ray* ::
3rd level (3 slots): *counterspell, fireball, lightning bolt* ::
4th level (3 slots): *blight, ice storm, greater invisibility* ::
5th level (3 slots): *cone of cold, hold monster, wall of force* ::
6th level (1 slot): *circle of death, disintegrate* ::
7th level (1 slot): *finger of death, plane shift* ::
8th level (1 slot): *power word stun* ::
9th level (1 slot): *power word kill* ::
___
### Actions
**Touch of Death.** :: *Melee Weapon Attack:* +8 to hit, reach 5 ft., one target. *Hit:* 3d6 cold damage + 3d6 necrotic damage. DC 17 Constitution save or paralyzed 1 min.
**Crown of Forgotten Kings (Recharge 5-6).** :: All creatures within 60 ft make DC 19 Wisdom save or forget their purpose (confusion effect) for 1 min.

### Legendary Actions
The king can take 3 legendary actions, choosing from the options below. Only one legendary action can be used at a time and only at the end of another creature's turn. The king regains spent legendary actions at the start of his turn.

**Cantrip.** :: The king casts a cantrip.
**Move.** :: The king flies up to half his speed.
**Cast Spell (Costs 2 Actions).** :: The king casts a spell of 1st-3rd level using a spell slot.
**Summon Undead (Costs 3 Actions).** :: The king summons 1d6 wraiths (use specter statblock), which appear in unoccupied spaces within 60 feet and act on his initiative.
}}

<div class='pageNumber auto'></div>
<div class='footnote'>Chapter 4 - Ascended & Ancient</div>
\page

### Whispers
> *"I asked him what name he was once called by. He said he had forgotten it. I asked him when. He said: 'Just yesterday. I forget it every morning. By evening I cannot remember why it mattered.'"*  
> — Scholar's account, sealed by the Order of Moira

> *"His crown is not metal. It is sorrow that has had a long time to take shape."*  
> — Folk saying, origin unknown
> 


## Herald of the Seven

<div class="col-img">![herald of the seven](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-herald-of-the-seven.jpg) {width:325px}</div>

### Description
Heralds of the Seven are awe-inspiring celestial beings, standing nine feet tall with wings of pure light that span twenty feet or more. Their features are beautiful beyond mortal standard, their forms radiating divine presence that commands attention and respect. They appear in the regalia of all seven Ascended simultaneously — armor that shifts between their symbols, weapons that glow with combined divine light, eyes that reflect all seven divine domains. Their presence affects reality itself: light brightens around them, evil creatures feel uncomfortable, and the faithful feel profound reassurance.

### Lore
Heralds are awe-inspiring celestial beings created jointly by the Seven Ascended for situations requiring unified divine communication. They appear only rarely — perhaps a handful of times per century — when events demand intervention from the entire pantheon rather than individual gods. Each Herald is created for a specific purpose and returns to divine essence when that purpose is fulfilled; they have no ongoing existence between missions. They stand nine feet tall with wings of pure light, appearing in regalia of all seven Ascended simultaneously: armor that shifts between their symbols, weapons glowing with combined divine light, eyes reflecting all seven divine domains. They prefer diplomacy — combat is a failure of their primary mission of communication — but when forced to fight, their weapons strike with the combined force of seven gods. A Herald sighting is a historical event. Records are kept, stories are told, and theological implications are debated for generations.

### Cultural Significance
A Herald's appearance is universally treated as a momentous event — even enemies of the faith treat them with caution. Their unified nature, representing all seven gods simultaneously, is theologically significant: it demonstrates that despite their different domains and occasional tensions, the Ascended can act in concert when necessary. The questions a Herald's arrival prompts ("Why now? Why this place? Why us?") echo through scholarly and religious circles for generations after they depart.

### Habitat & Ecology
Heralds do not form societies — they are temporary manifestations rather than ongoing beings. Each exists for the duration of its mission and knows it will cease existing when that mission concludes, giving them peculiar perspective: they have no future to preserve, no past to protect, only the present mission to complete. Their appearance is recorded as a historical event in temple archives, and the words they speak (when they speak) are debated and reinterpreted for generations. They appear, deliver their message or perform their task, and return to the divine essence from which they emerged. Until the Seven need to speak again with one voice, they do not return.

### Story Hooks
- A Herald appears with a mission that involves the party directly — and they are not given the option of refusal.
- The party witnesses a Herald's appearance and must interpret what it means before its message reaches the wrong ears.
- Someone attempts to summon or compel a Herald, with potentially catastrophic results.
- A Herald's message is ambiguous, and competing interpretations are about to spark a holy war.

<div class='pageNumber auto'></div>
<div class='footnote'>Chapter 4 - Ascended & Ancient</div>
\page

{{monster,frame
## Herald of the Seven
*Large celestial, lawful good*
___
**Armor Class** :: 19 (natural)
**Hit Points** :: 200 (16d10 + 112)
**Speed** :: 40 ft., fly 120 ft.

___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|24 (+7) | 20 (+5) | 24 (+7) | 19 (+4) | 22 (+6) | 25 (+7)|
___
**Saving Throws** :: Constitution +12, Wisdom +11, Charisma +12
**Skills** :: Insight +11, Perception +11
**Damage Resistances** :: radiant; bludgeoning, piercing, and slashing from nonmagical attacks
**Condition Immunities** :: charmed, exhaustion, frightened
**Senses** :: truesight 120 ft.
**Languages** :: all, telepathy 120 ft.
**Challenge** :: 12 (8,400 XP)
___
**Divine Awareness.** :: The herald knows if it hears a lie within 60 feet.

**Magic Resistance.** :: The herald has advantage on saving throws against spells and other magical effects.

**Innate Spellcasting.** :: The herald's innate spellcasting ability is Charisma (spell save DC 20). It can innately cast the following spells, requiring no material components:

At will: *detect evil and good, invisibility* (self only)
3/day each: *blade barrier, flame strike, raise dead*
1/day each: *commune, control weather*

___
### Actions
**Multiattack.** :: Two greatsword attacks.

**Greatsword of the Seven.** :: *Melee Weapon Attack:* +12 to hit, reach 5 ft., one target. *Hit:* 4d6+7 slashing damage + 5d8 radiant damage

**Ascended's Command (Recharge 5-6).** :: Issue divine command. All creatures within 60 ft must obey one-word command (as *command* spell) if they fail DC 20 Wisdom save.

**Healing Touch (4/Day).** :: Touch heals 6d8+7 HP and removes all conditions.


}}

### Recorded Heraldic Appearances
Only nine Herald manifestations are well-documented in surviving records. Three are confirmed sightings within scholarly memory; six are pre-Worldrend events known from inscriptions, songs, or sealed temple archives. The recent ones:

- **Year 1089 CR** — Appeared above the Battle of Whitebridge. Spoke seven words, none understood. Both armies withdrew.
- **Year 1156 CR** — Appeared in the throne room of King Vellrast IV. Witnessed by only the King and one scribe. The King abdicated within the week.
- **Year 1234 CR** — Appeared briefly above a village on the Aethorian border. Healed a child who would later become a People's Champion. Vanished without speaking.

### Whispers
> *"The Herald did not look at me. It looked through me, at someone who was not there. I have spent my life wondering who."*  
> — Temple scribe of Sera

> *"They do not come to take sides. They come to remind us that there are sides at all — and that the gods are watching how we choose."*  
> — Sermon, anonymous


## Corrupted & Cursed

Twisted by war and dark magic.


## Corruption Spawn

<div class="col-img">![corruption spawn](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-corruption-spawn.jpg) {width:325px}</div>

### Description
Corruption Spawn are small, amorphous horrors that barely qualify as living creatures. They are roughly the size of large dogs but shaped like nothing natural — masses of corrupted flesh, misshapen limbs, and mouths that open in unexpected places. Their surfaces glisten with acidic moisture, and they leave trails of caustic slime wherever they move. They have no consistent form: each spawn is uniquely malformed, shaped by the specific magical corruption that birthed it. Some have too many eyes, others have none. Some drag themselves on vestigial limbs; others roll or flow like living ooze. All are obviously, viscerally wrong.

<div class='pageNumber auto'></div>
<div class='footnote'>Chapter 4 - Ascended & Ancient</div>
\page

### Lore
Corruption Spawn emerge from locations where war magic has gone catastrophically wrong — battlefields saturated with destructive spells, sites of failed magical experiments, places where too much dark energy has concentrated for too long. They aren't created intentionally; they simply appear where magical contamination reaches critical levels, symptoms of magical damage rather than creatures in any conventional sense. Each is uniquely malformed, shaped by the specific corruption that birthed it: too many eyes or none, vestigial limbs, mouths that open in unexpected places. All are obviously, viscerally wrong, and their surfaces glisten with acidic moisture. The Contested Lands produce them regularly — decades of magical warfare have poisoned the very earth, and Corruption Spawn bubble up from it like infections from wounded flesh. Reformers cite them in anti-war rhetoric: this is what we're creating. This is the legacy we're leaving.

{{monster,frame
## Corruption Spawn
*Small aberration, chaotic evil*
___
**Armor Class** :: 9
**Hit Points** :: 67 (9d6 + 36)
**Speed** :: 10 ft., swim 10 ft.
___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|10 (+0) | 8 (-1) | 18 (+4) | 3 (-4) | 10 (+0) | 6 (-2)|
___
**Condition Immunities** :: prone
**Senses** :: darkvision 60 ft.
**Languages** :: -
**Challenge** :: 4 (1,100 XP)
___
**Aberrant Ground.** :: The area within 10 feet of the spawn is difficult terrain as reality itself distorts around it.
**Gibbering.** :: Any creature that starts its turn within 20 feet of the spawn and can hear its mad babbling must succeed on a DC 10 Wisdom saving throw or be unable to take reactions until the start of its next turn.
___
### Actions
**Multiattack.** :: One bite, one spitting attack.
**Bites.** :: *Melee Weapon Attack:* +2 to hit, reach 5 ft., one target. *Hit:* 5d6 piercing damage
**Spit Corruption.** :: *Ranged Weapon Attack:* +2 to hit, range 15/30 ft., one target. *Hit:* 3d6 acid damage
**Blinding Spittle (Recharge 5-6).** :: Spit at point within 15 ft. 5-ft radius, DC 13 Dexterity save or blinded 1 min.
}}

### Cultural Significance
For communities living near corrupted areas, spawn are a constant threat requiring ongoing vigilance — warning systems, patrol schedules, and grim spawn-hunting traditions develop wherever the contamination persists. Each emergence is a small reminder that magical warfare damages more than its immediate targets; it poisons land, water, and the fabric of reality itself.

### Habitat & Ecology
Spawn cluster wherever magical contamination is severe enough to produce them — old battlefields, collapsed magical experiments, ruined warmage outposts, sites of catastrophic spell misfires. They have no intelligence and no society — they are barely alive in any meaningful sense, animate corruption rather than true creatures. They do not communicate, do not cooperate (though they may swarm the same target by coincidence), and do not have goals beyond immediate hunger. They do not reproduce naturally; new spawn emerge from corrupted locations independently. Destroying all spawn in an area does not prevent more from appearing if the underlying contamination is not addressed.

### Story Hooks
- Spawn emergence indicates dangerous magical contamination nearby that no one wants to investigate.
- Investigating spawn origins leads to discovery of a hidden magical disaster.
- Someone is deliberately creating conditions that produce spawn — but why?

## War-Twisted Soldier

<div class="col-img">![war-twisted soldier](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-war-twisted-soldier.jpg) {width:325px}</div>

<div class='pageNumber auto'></div>
<div class='footnote'>Chapter 4 - Ascended & Ancient</div>
\page

### Description
War-Twisted Soldiers wear the remnants of their military equipment — rusted armor, tattered uniforms, corroded weapons — bearing the damage that killed them. Wounds that should be fatal remain visible: crushed skulls, severed limbs, gaping chest wounds. They move with the disciplined precision they learned in life, but wrong — slightly too fast, slightly too jerky, driven by rage rather than training. Their eyes burn with cold fire, and their faces are frozen in expressions of hatred or despair. They bear insignia from both Thaldros and Aethoria, from the Iron Guild, from extinct nations — the dead do not change their sides.

### Lore
War-Twisted Soldiers are undead warriors created when soldiers die in particularly violent or traumatic circumstances and their spirits cannot move on. The combination of violent death, military conditioning, and overwhelming emotion anchors them to the mortal world. They aren't raised by necromancers — though necromancers can sometimes control them — but rise spontaneously from battlefields where violence was intense enough to scar reality. They retain fragmentary memory of their living service: they remember fighting, remember dying, remember hatred for enemies they can no longer clearly identify. They wear the rusted, tattered remnants of their original gear, often bearing insignia from extinct nations or sides that no longer matter, and they continue fighting their original war, attacking anyone who resembles old enemies. Military forces on both sides train soldiers in burial practices specifically to prevent War-Twisted rising. No one wants their comrades to become monsters.

### Cultural Significance
War-Twisted Soldiers complicate memorial practices in ways no nation likes to admit. Families whose loved ones rose as War-Twisted face impossible choices — destroy what remains of their relatives, or leave them to harm strangers. There's no good answer, and the priests who consecrate the dead carry that weight as much as the families.

### Habitat & Ecology
War-Twisted Soldiers haunt the battlefields where they died, sometimes wandering miles beyond when their original units are scattered. They retain enough tactical awareness to fight in groups, and packs of them coordinate attacks using military signals neither side currently uses. Some retain enough coherence to be communicated with, though such conversations are disturbing — they describe their deaths, their hatred, their inability to stop fighting even though they know they're dead. They cannot rest until the violence that created them is fully addressed, which usually requires either consecration by clerics or the resolution of the conflict they died in. Neither comes often.

### Story Hooks
- War-Twisted from an ancient battle guard something important — or something forgotten.
- Someone's relative has risen as a War-Twisted, and they need help ending them peacefully.
- A mass rising of War-Twisted threatens to overwhelm a nearby settlement.
- The party must navigate a region where War-Twisted still fight their original war on every traveler.

{{monster,frame
## War-Twisted Soldier
*Medium undead, neutral evil*
___
**Armor Class** :: 14 (armor scraps)
**Hit Points** :: 97 (13d8 + 39)
**Speed** :: 30 ft.

___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|18 (+4) | 14 (+2) | 16 (+3) | 10 (+0) | 12 (+1) | 9 (-1)|
___
**Saving Throws** :: Constitution +6
**Skills** :: Perception +4, Stealth +5
**Damage Resistances** :: necrotic; bludgeoning, piercing, and slashing from nonmagical attacks
**Damage Immunities** :: poison
**Condition Immunities** :: exhaustion, poisoned
**Senses** :: darkvision 60 ft.
**Languages** :: Common
**Challenge** :: 6 (2,300 XP)
___
**Sunlight Sensitivity.** :: While in sunlight, the soldier has disadvantage on attack rolls and Wisdom (Perception) checks that rely on sight.

**War Instinct.** :: The soldier has advantage on initiative rolls and can't be surprised.

**Create Spawn.** :: A humanoid slain by this creature rises 24 hours later as a war-twisted soldier under no one's control, unless the body is blessed by a cleric or burned before then.

___
### Actions
**Multiattack.** :: Two longsword attacks and one life drain.

**Longsword.** :: *Melee Weapon Attack:* +7 to hit, reach 5 ft., one target. *Hit:* 1d8+4 slashing damage

**Life Drain.** :: *Melee Weapon Attack:* +7 to hit, reach 5 ft., one target. *Hit:* 2d6+4 necrotic. Target max HP reduced by amount (until long rest). Dies if max HP reaches 0.

**Battle Cry (Recharge 6).** :: All war-twisted soldiers within 30 ft can attack as reaction.


}}
<div class='pageNumber auto'></div>
<div class='footnote'>Chapter 4 - Ascended & Ancient</div>
\page

## Curse Bearer

<div class="col-img">![curse bearer](https://raw.githubusercontent.com/mixologee/tirvandor/main/tirvandor-project/monster-manual/images/portraits/tirvandor-monster-curse-bearer.jpg) {width:325px}</div>

### Description
Curse Bearers retain enough of their original form to be recognizable as what they were — and this is what makes them disturbing. A cursed human might have limbs too long, a mouth too wide, eyes that glow with malevolent light. A cursed beast might grow to impossible size with additional limbs or heads. They are large — eight to ten feet when standing — and move with predatory grace despite their distorted forms, climbing walls and ceilings as easily as walking on ground. Their claws and teeth are oversized and razor-sharp. They are clearly transformations rather than natural creatures, victims rather than simply monsters, and that visible kinship to their former selves is the worst part of seeing them.

### Lore
Curse Bearers were once people or animals transformed by powerful curses into monstrous predators. The transformation is agonizing and takes days or weeks to complete — during this time, the victim gradually loses their original form and mind, becoming increasingly monstrous. Some fight desperately; others succumb quickly. None escape once the curse takes hold, without outside intervention. The curses that create them are typically ancient and powerful, often dating to the Worldrend or earlier and embedded in cursed locations or objects that have claimed victims for centuries. The Bearer retains memories of its former life but experiences them as torment rather than comfort — remembering being human, having a family and a home, makes its current existence more painful, not less. Some retain enough self-control to avoid the places they once loved. Many communities feel obligated to put Curse Bearers down mercifully rather than simply killing them as threats. They were victims first.

{{monster,frame
## Curse Bearer
*Large monstrosity, chaotic evil*
___
**Armor Class** :: 15 (natural)
**Hit Points** :: 126 (12d10 + 60)
**Speed** :: 40 ft., climb 40 ft.

___
|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|19 (+4) | 16 (+3) | 20 (+5) | 8 (-1) | 14 (+2) | 10 (+0)|
___
**Saving Throws** :: Constitution +8, Wisdom +5
**Skills** :: Perception +5, Stealth +6
**Damage Resistances** :: necrotic
**Senses** :: darkvision 120 ft., blindsight 30 ft.
**Languages** :: understands Common but can't speak
**Challenge** :: 8 (3,900 XP)
___
**Cursed Form.** :: The bearer was a creature cursed by a Haunted Battlefield or other dark magic. Its transformation is permanent without divine intervention, and it hunts the living to spread its affliction.

**Aura of Misfortune (30 ft).** :: Living creatures other than the bearer have disadvantage on saving throws while within 30 feet of it.

**Spider Climb.** :: The bearer can climb difficult surfaces, including upside down on ceilings, without needing to make an ability check.

___
### Actions
**Multiattack.** :: Two claw attacks and one bite.

**Claw.** :: *Melee Weapon Attack:* +7 to hit, reach 10 ft., one target. *Hit:* 2d6+4 slashing damage

**Bite.** :: *Melee Weapon Attack:* +7 to hit, reach 5 ft., one target. *Hit:* 2d8+4 piercing damage + 2d8 necrotic damage

**Curse Touch (Recharge 5-6).** :: One creature within 5 ft makes DC 15 Wisdom save or cursed. Cursed creature has disadvantage on all d20 rolls for 1 hour. *Remove curse* ends it.

**Terrifying Howl (1/Day).** :: All creatures within 60 ft make DC 15 Wisdom save or frightened 1 min. Can repeat save each turn.


}}

<div class='pageNumber auto'></div>
<div class='footnote'>Chapter 4 - Ascended & Ancient</div>
\page

### Cultural Significance
Stories of Curse Bearers focus less on combat than on transformation: the slow loss of humanity, the desperate attempts to resist, the final surrender. These tales serve as warnings against tampering with cursed places, and as expressions of a deeper fear that lives in every culture — that one's own identity can be taken without one's consent.

### Habitat & Ecology
Curse Bearers establish lairs near the cursed locations or objects that created them, often in caves, abandoned buildings, or the ruins where their transformation began. They are intelligent enough to be cunning predators — setting ambushes, targeting vulnerable prey, retreating from overwhelming opposition — but not rational in any normal sense. The curse dominates their thinking, making them perpetually aggressive and territorial. Some sometimes communicate when not actively hunting, though doing so is difficult for them; conversations with Curse Bearers are disturbing, fragmentary, and ultimately heartbreaking. They describe their suffering, beg for death, warn potential victims away — all while fighting urges to attack.

\column

### Story Hooks
- A Curse Bearer was once someone important — can they be saved before the transformation completes?
- The party must track a Curse Bearer back to its source to understand and counter the spreading curse.
- A community secretly harbors a Curse Bearer, believing the victim can still be saved.
- The party encounters a Curse Bearer that retains enough humanity to communicate, and to request mercy.

<div class='pageNumber auto'></div>
<div class='footnote'>Chapter 4 - Ascended & Ancient</div>
\page

# Appendix A: Encounter Tables by Region
:
Roll a d20 on the appropriate region table when the party travels through unfamiliar territory or rests in dangerous country. Cross-reference the CR Quick Reference (Appendix B) to scale encounters to your party.

### Adjusting Encounters
**Scaling up:** Add another monster of the same type, or add a 1-CR-higher monster from the same region as a leader.

**Scaling down:** Reduce numbers, or replace the highest-CR creature with a lesser monster from the same region (e.g., a Drake becomes a War Beast; an Iron Crown Knight becomes a Royal Guard Elite).

**Mixed regions:** Border encounters can plausibly include Thaldros or Aethoria units pursuing missions across the line. Sacred-site encounters can layer Corrupted entries on top when the holy ground is contested.

### The Contested Lands

| d20 | Encounter |
|:---:|:---|
| 1–3 | 1d4+1 **Border Bandits** investigating travel-spoor |
| 4 | A single **Smuggler Captain** offering passage — for a price |
| 5–6 | 1 **War-Scarred Veteran** camping at an old ruin |
| 7 | 1 **Border Wraith** rising at dusk from a forgotten grave |
| 8 | 1 **Contested Land Elemental** awakened by recent battle |
| 9–10 | A **Refugee Mob** fleeing recent violence |
| 11–13 | 1d6+2 **Scavenger Ghouls** at a fresh battlefield |
| 14–15 | 1 **Territorial Drake** roaring from high ground |
| 16–17 | 1d4+1 **War Beasts**, feral, hunting |
| 18 | A **Haunted Battlefield** manifesting at the wrong angle of light |
| 19 | 1d4 **War-Twisted Soldiers** still fighting their last battle |
| 20 | Roll twice and combine — the worst day on the road |

### Thaldros Territory

| d20 | Encounter |
|:---:|:---|
| 1–4 | Thaldros patrol: 1 **Thaldros Soldier** leading 1d6 **Conscripts** |
| 5–6 | 1d4 **Thaldros Soldiers** at a checkpoint |
| 7–8 | 1d4 **Iron Legion Enforcers** "asking questions" in a village |
| 9 | 1 **Royal Guard Elite** escorting a noble or message |
| 10 | 1 **State Inquisitor** watching the party (or not) |
| 11 | 1 **War Mage of Thaldros** with a small soldier escort |
| 12 | 1 **Siege Golem** in transit — make way |
| 13 | A duel: 1 **General's Champion** seeks worthy opposition |
| 14 | 1 **Iron Crown Knight** enforcing a tribunal verdict |
| 15–17 | A garrison: 1 **Royal Guard Elite** + 2 **Soldiers** + 1d4 **Conscripts** |
| 18–19 | An **Iron Legion Enforcer** squad making a public example |
| 20 | **Lord Commander Varius** is in the region — adjust everything |

\column

### Aethoria & Iron Guild

| d20 | Encounter |
|:---:|:---|
| 1–3 | 1d4+1 **Aethorian Militia** guarding a village approach |
| 4–6 | 1d4 **Resistance Fighters** moving between safehouses |
| 7 | 1 **People's Champion** rallying a local crowd |
| 8 | 1 **Revolutionary Mage** in cover identity, watching the party |
| 9 | 1 **Chain Breaker Monk** liberating prisoners |
| 10 | 1 **Guerrilla Commander** coordinating a strike |
| 11 | Whispered rumor: **The Liberator** was here three days ago |
| 12 | A traveler who may be the **Prophesied Hero** — or a fraud |
| 13–14 | 1d4+1 **Guild Recruits** on their first contract |
| 15 | 1d4 **Veteran Mercenaries** between contracts |
| 16 | 1 **Guild Enforcer** + 1d4 **Recruits** collecting a debt |
| 17 | 1 **Contract Killer** — but you won't know until later |
| 18 | 1 **Iron Guild Captain** offering temporary contract work |
| 19 | 1 **Guildmaster's Elite** on a Guildmaster errand |
| 20 | **Garrick Ironheart** himself is at the local forge — by invitation only |

### Sacred Sites & Holy Ground

| d20 | Encounter |
|:---:|:---|
| 1–4 | 1 **Blessed Paladin** at prayer or on circuit |
| 5–6 | 1 **Thandros's Justicar** holding court |
| 7 | 1 **Aethor's Liberator** has just departed; the freed are still here |
| 8–9 | 1 **Moira's Seer** offers cryptic counsel |
| 10–11 | 1 **Sylvara's Wild Hunter** judges the party's relationship to nature |
| 12 | 1 **Sera's Mercy** tends the suffering |
| 13–14 | 1 **Mordain's Sentinel** guards an ancient tomb |
| 15 | 1 **Fallen Champion** haunts a desecrated shrine |
| 16 | 1 **Ancient Guardian** stirs for the first time in centuries |
| 17 | 1 **Prophecy Keeper** observes — and is observed |
| 18 | A whispered legend says **the Forgotten King** waits beneath this place |
| 19 | A **Herald of the Seven** appears (once a generation) |
| 20 | All seven domains feel near — divine attention has turned here |


### Cursed Ruins & Corruption

| d20 | Encounter |
|:---:|:---|
| 1–6 | 1d6 **Corruption Spawn** boiling out of contaminated ground |
| 7–10 | 1d4+2 **Scavenger Ghouls** in an abandoned settlement |
| 11–14 | 1d4 **War-Twisted Soldiers** patrolling a centuries-dead post |
| 15 | 1 **Border Wraith** rising at the heart of old slaughter |
| 16 | A **Haunted Battlefield** activates as the party crosses it |
| 17–18 | 1 **Curse Bearer** stalking the boundary of a cursed site |
| 19 | A **Fallen Champion** stands guard over the place that destroyed them |
| 20 | The corruption has reached a Bound Ancient — flee, or finish it |


{{footnote Appendix A: Encounter Tables}}
{{pageNumber,auto}}
\page

# Appendix B: CR Quick Reference

| CR | Monster | Type | Chapter |
|:---:|:---|:---|:---:|
| 1/8 | Thaldros Conscript | Humanoid | 2 |
| 1/4 | Aethorian Militia | Humanoid | 3 |
| 1/2 | Border Bandit | Humanoid | 1 |
| 1/2 | Thaldros Soldier | Humanoid | 2 |
| 1/2 | Guild Recruit | Humanoid | 3 |
| 1 | Refugee Mob | Swarm | 1 |
| 1 | Scavenger Ghoul | Undead | 1 |
| 1 | Resistance Fighter | Humanoid | 3 |
| 2 | Territorial Drake | Dragon | 1 |
| 2 | Iron Legion Enforcer | Humanoid | 2 |
| 2 | Veteran Mercenary | Humanoid | 3 |
| 3 | Smuggler Captain | Humanoid | 1 |
| 3 | War Beast | Beast | 1 |
| 3 | People's Champion | Humanoid | 3 |
| 3 | Sera's Mercy | Celestial | 4 |
| 4 | War-Scarred Veteran | Humanoid | 1 |
| 4 | Guild Enforcer | Humanoid | 3 |
| 4 | Blessed Paladin | Humanoid | 4 |
| 4 | Corruption Spawn | Aberration | 4 |
| 5 | Border Wraith | Undead | 1 |
| 5 | Royal Guard Elite | Humanoid | 2 |
| 5 | Revolutionary Mage | Humanoid | 3 |
| 5 | Contract Killer | Humanoid | 3 |
| 5 | Moira's Seer | Humanoid | 4 |
| 6 | Contested Land Elemental | Elemental | 1 |
| 6 | State Inquisitor | Humanoid | 2 |
| 6 | Chain Breaker Monk | Humanoid | 3 |
| 6 | Thandros's Justicar | Humanoid | 4 |
| 6 | War-Twisted Soldier | Undead | 4 |
| 7 | Haunted Battlefield | Hazard | 1 |
| 7 | War Mage of Thaldros | Humanoid | 2 |
| 7 | Guerrilla Commander | Humanoid | 3 |
| 7 | Iron Guild Captain | Humanoid | 3 |
| 7 | Aethor's Liberator | Celestial | 4 |
| 8 | Siege Golem | Construct | 2 |
| 8 | Sylvara's Wild Hunter | Fey | 4 |
| 8 | Ancient Guardian | Construct | 4 |
| 8 | Curse Bearer | Monstrosity | 4 |
| 9 | General's Champion | Humanoid | 2 |
| 9 | Guildmaster's Elite | Humanoid | 3 |
| 9 | Fallen Champion | Undead | 4 |
| 10 | Iron Crown Knight | Humanoid | 2 |
| 10 | Mordain's Sentinel | Undead | 4 |
| 10 | Prophecy Keeper | Aberration | 4 |
| 11 | The Liberator | Humanoid (legendary) | 3 |
| 11 | Garrick Ironheart | Humanoid (legendary) | 3 |
| 12 | Prophesied Hero | Humanoid (legendary) | 3 |
| 12 | Herald of the Seven | Celestial (legendary) | 4 |
| 13 | Lord Commander Varius | Humanoid (legendary) | 2 |
| 15 | Forgotten King | Undead (legendary) | 4 |

{{footnote Appendix B: CR Quick Reference}}
{{pageNumber,auto}}
\page

{{license,wide
THIS LICENSE IS APPROVED FOR GENERAL USE. PERMISSION TO DISTRIBUTE THIS LICENSE IS MADE BY WIZARDS OF THE COAST!

### OPEN GAME LICENSE Version 1.0a
	
The following text is the property of Wizards of the Coast, Inc. and is Copyright 2000 Wizards of the Coast, Inc ("Wizards"). All Rights Reserved.
1. **Definitions:** 

**(a)**:: **"Contributors"** means the copyright and/or trademark owners who have contributed Open Game Content; 
**(b)**:: **"Derivative Material"** means copyrighted material including derivative works and translations (including into other computer languages), potation, modification, correction, addition, extension, upgrade, improvement, compilation, abridgment or other form in which an existing work may be recast, transformed or adapted; 
**(c)**:: **"Distribute"** means to reproduce, license, rent, lease, sell, broadcast, publicly display, transmit or otherwise distribute; 
**(d)**::**"Open Game Content"** means the game mechanic and includes the methods, procedures, processes and routines to the extent such content does not embody the Product Identity and is an enhancement over the prior art and any additional content clearly identified as Open Game Content by the Contributor, and means any work covered by this License, including translations and derivative works under copyright law, but specifically excludes Product Identity. 
**(e)**:: **"Product Identity"** means product and product line names, logos and identifying marks including trade dress; artifacts; creatures characters; stories, storylines, plots, thematic elements, dialogue, incidents, language, artwork, symbols, designs, depictions, likenesses, formats, poses, concepts, themes and graphic, photographic and other visual or audio representations; names and descriptions of characters, spells, enchantments, personalities, teams, personas, likenesses and special abilities; places, locations, environments, creatures, equipment, magical or supernatural abilities or effects, logos, symbols, or graphic designs; and any other trademark or registered trademark clearly identified as Product identity by the owner of the Product Identity, and which specifically excludes the Open Game Content; 
**(f)**:: **"Trademark"** means the logos, names, mark, sign, motto, designs that are used by a Contributor to identify itself or its products or the associated products contributed to the Open Game License by the Contributor 
**(g)**:: **"Use"**, **"Used"** or **"Using"** means to use, Distribute, copy, edit, format, modify, translate and otherwise create Derivative Material of Open Game Content. 
**(h)**:: **"You"** or **"Your"** means the licensee in terms of this agreement.


2. **The License:** This License applies to any Open Game Content that contains a notice indicating that the Open Game Content may only be Used under and in terms of this License. You must affix such a notice to any Open Game Content that you Use. No terms may be added to or subtracted from this License except as described by the License itself. No other terms or conditions may be applied to any Open Game Content distributed using this License.
3. **Offer and Acceptance:** By Using the Open Game Content You indicate Your acceptance of the terms of this License.
4. **Grant and Consideration:** In consideration for agreeing to use this License, the Contributors grant You a perpetual, worldwide, royalty-free, non-exclusive license with the exact terms of this License to Use, the Open Game Content.
5. **Representation of Authority to Contribute:** If You are contributing original material as Open Game Content, You represent that Your Contributions are Your original creation and/or You have sufficient rights to grant the rights conveyed by this License.
6. **Notice of License Copyright:** You must update the COPYRIGHT NOTICE portion of this License to include the exact text of the COPYRIGHT NOTICE of any Open Game Content You are copying, modifying or distributing, and You must add the title, the copyright date, and the copyright holder's name to the COPYRIGHT NOTICE of any original Open Game Content you Distribute.
7. **Use of Product Identity:** You agree not to Use any Product Identity, including as an indication as to compatibility, except as expressly licensed in another, independent Agreement with the owner of each element of that Product Identity. You agree not to indicate compatibility or co-adaptability with any Trademark or Registered Trademark in conjunction with a work containing Open Game Content except as expressly licensed in another, independent Agreement with the owner of such Trademark or Registered Trademark. The use of any Product Identity in Open Game Content does not constitute a challenge to the ownership of that Product Identity. The owner of any Product Identity used in Open Game Content shall retain all rights, title and interest in and to that Product Identity.
8. **Identification:** If you distribute Open Game Content You must clearly indicate which portions of the work that you are distributing are Open Game Content.

}}
\page

{{license,wide

9. **Updating the License:** Wizards or its designated Agents may publish updated versions of this License. You may use any authorized version of this License to copy, modify and distribute any Open Game Content originally distributed under any version of this License.

10. **Copy of this License:** You MUST include a copy of this License with every copy of the Open Game Content You Distribute.

11. **Use of Contributor Credits:** You may not market or advertise the Open Game Content using the name of any Contributor unless You have written permission from the Contributor to do so.

12. **Inability to Comply:** If it is impossible for You to comply with any of the terms of this License with respect to some or all of the Open Game Content due to statute, judicial order, or governmental regulation then You may not Use any Open Game Material so affected.

13. **Termination:** This License will terminate automatically if You fail to comply with all terms herein and fail to cure such breach within 30 days of becoming aware of the breach. All sublicenses shall survive the termination of this License.

14. **Reformation:** If any provision of this License is held to be unenforceable, such provision shall be reformed only to the extent necessary to make it enforceable.

___

*COPYRIGHT NOTICE Open Game License v 1.0a Copyright 2000, Wizards of the Coast, Inc.*

___

System Reference Document Copyright 2000-2003, Wizards of the Coast, Inc.; Authors Jonathan Tweet, Monte Cook, Skip Williams, Rich Baker, Andy Collins, David Noonan, Rich Redman, Bruce R. Cordell, John D. Rateliff, Thomas Reid, James Wyatt, based on original material by E. Gary Gygax and Dave Arneson.

:

END OF LICENSE
}}