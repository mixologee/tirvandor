# The Homebrewery *V3*
Welcome traveler from an antique land. Please sit and tell us of what you have seen. The unheard of monsters, who slither and bite. Tell us of the wondrous items and and artifacts you have found, their mysteries yet to be unlocked. Of the vexing vocations and surprising skills you have seen.

### Homebrew D&D made easy
The Homebrewery makes the creation and sharing of authentic looking Fifth-Edition homebrews easy. It uses [Markdown](https://help.github.com/articles/markdown-basics/) with a little CSS magic to make your brews come to life.

**Try it!** Simply edit the text on the left and watch it *update live* on the right. Note that not every button is visible on this demo page. Click New {{fas,fa-plus-square}} in the navbar above to start brewing with all the features!

### Editing and Sharing
When you create a new homebrew document ("brew"), your document will be given a *edit link* and a *share link*.

The *edit link* is where you write your brew. If you edit a brew while logged in, you are added as one of the brew's authors, and no one else can edit that brew until you add them as a new author via the {{fa,fa-info-circle}} **Properties** tab. Brews without any author can still be edited by anyone with the *edit link*, so be careful about who you share it with if you prefer to work without an account.

Anyone with the *share url* will be able to access a read-only version of your homebrew.

{{note
##### PDF Creation
PDF Printing works best in Google Chrome. If you are having quality/consistency issues, try using Chrome to print instead.

After clicking the "Print" item in the navbar a new page will open and a print dialog will pop-up.
* Set the **Destination** to "Save as PDF"
* Set **Paper Size** to "Letter"
* If you are printing on A4 paper, make sure to have the **PRINT → {{far,fa-file}} A4 Pagesize** snippet in your brew
* In **Options** make sure "Background Images" is selected.
* Hit print and enjoy! You're done!

If you want to save ink or have a monochrome printer, add the **PRINT → {{fas,fa-tint}} Ink Friendly** snippet to your brew!
}}

![homebrew mug](https://i.imgur.com/hMna6G0.png) {position:absolute,bottom:20px,left:130px,width:220px}

{{artist,bottom:160px,left:100px
##### Homebrew Mug
[naturalcrit](https://homebrew.naturalcrit.com)
}}

{{pageNumber 1}}
{{footnote PART 1 | FANCINESS}}

\column

## V3 vs Legacy
The Homebrewery has two renderers: Legacy and V3. The V3 renderer is recommended for all users because it is more powerful, more customizable, and continues to receive new feature updates while Legacy does not. However Legacy mode will remain available for older brews and veteran users.
	
At any time, any individual brew can be changed to your renderer of choice via the {{fa,fa-info-circle}} **Properties** tab on your brew. However, converting between Legacy and V3 may require heavily tweaking the document; while both renderers can use raw HTML, V3 prefers a streamlined curly bracket syntax that avoids the complex HTML structures required by Legacy.


Scroll down to the next page for a brief summary of the changes and features available in V3!
#### New Things All The Time!
Check out the latest updates in the full changelog [here](/changelog).

### Helping out
Like this tool? Head over to our [Patreon](https://www.patreon.com/Naturalcrit) to help us keep the servers running.


This tool will **always** be free, never have ads, and we will never offer any "premium" features or whatever.

### Bugs, Issues, Suggestions?
- Check the [Frequently Asked Questions](/faq) page first for quick answers.
- Get help or the right look for your brew by posting on [r/Homebrewery](https://www.reddit.com/r/homebrewery/submit?selftext=true&title=%5BIssue%5D%20Describe%20Your%20Issue%20Here) or joining the [Discord Of Many Things](https://discord.gg/by3deKx).
- Report technical issues or provide feedback on the [GitHub Repo](https://github.com/naturalcrit/homebrewery/).

### Legal Junk
The Homebrewery is licensed using the [MIT License](https://github.com/naturalcrit/homebrewery/blob/master/license). Which means you are free to use The Homebrewery codebase any way that you want, except for claiming that you made it yourself.

If you wish to sell or in some way gain profit for what's created on this site, it's your responsibility to ensure you have the proper licenses/rights for any images or resources used.
#### Crediting Us
If you'd like to credit us in your brew, we'd be flattered! Just reference that you made it with The Homebrewery.

### More Homebrew Resources
[![Discord](/assets/discordOfManyThings.svg){width:50px,float:right,padding-left:10px}](https://discord.gg/by3deKx)

If you are looking for more 5e Homebrew resources check out [r/UnearthedArcana](https://www.reddit.com/r/UnearthedArcana/) and their list of useful resources [here](https://www.reddit.com/r/UnearthedArcana/wiki/resources). The [Discord Of Many Things](https://discord.gg/by3deKx) is another great resource to connect with fellow homebrewers for help and feedback.


{{position:absolute;top:20px;right:20px;width:auto
[![Discord](/assets/discord.png){height:30px}](https://discord.gg/by3deKx)
[![Github](/assets/github.png){height:30px}](https://github.com/naturalcrit/homebrewery)
[![Patreon](/assets/patreon.png){height:30px}](https://patreon.com/NaturalCrit)
[![Reddit](/assets/reddit.png){height:30px}](https://www.reddit.com/r/homebrewery/)
}}

\page

## Markdown+
The Homebrewery aims to make homebrewing as simple as possible, providing a live editor with Markdown syntax that is more human-readable and faster to write with than raw HTML.

From version 3.0.0, with a goal of adding maximum flexibility without users resorting to complex HTML to accomplish simple tasks, Homebrewery provides an extended verision of Markdown with additional syntax.

### Curly Brackets
Standard Markdown lacks several equivalences to HTML. Hence, we have introduced `{{ }}` as a replacement for `<span></span>` and `<div></div>` for a cleaner custom formatting. Inline spans and block elements can be created and given ID's and Classes, as well as CSS properties, each of which are comma separated with no spaces. Use double quotes if a value requires spaces. Spans and Blocks start the same:

#### Span
My favorite author is {{pen,#author,color:orange,font-family:"trebuchet ms" Brandon Sanderson}}.  The orange text has a class of `pen`, an id of `author`, is colored orange, and given a new font. The first space outside of quotes marks the beginning of the content.


#### Block
{{purple,#book,text-align:center,background:#aa88aa55
My favorite book is Wheel of Time. This block has a class of `purple`, an id of `book`, and centered text with a colored background. The opening and closing brackets are on lines separate from the block contents.
}}

#### Injection
For any element not inside a span or block, you can *inject* attributes using the same syntax but with single brackets in a single line immediately after the element.

Inline elements like *italics* {color:#D35400} or images require the injection on the same line.

Block elements like headers require the injection to start on the line immediately following.

##### A Purple Header
{color:purple,text-align:center}

\* *this does not currently work for tables yet*

### Vertical Spacing
A blank line can be achieved with a run of one or more `:` alone on a line. More `:`'s will create more space.

::


Much nicer than `<br><br><br><br><br>`

### Definition Lists
**Example** :: V3 uses HTML *definition lists* to create "lists" with hanging indents.



### Column Breaks
Column and page breaks with `\column` and `\page`.

\column
### Tables
Tables now allow column & row spanning between cells. This is included in some updated snippets, but a simplified example is given below.

A cell can be spanned across columns by grouping multiple pipe `|` characters at the end of a cell.

Row spanning is achieved by adding a `^` at the end of a cell just before the `|`.  

These can be combined to span a cell across both columns and rows. Cells must have the same colspan if they are to be rowspan'd.

##### Example
| Head A | Spanned Header ||
| Head B | Head C | Head D |
|:-------|:------:|:------:|
| 1A     |    1B  |    1C  |
| 2A    ^|    2B  |    2C  |
| 3A    ^|    3B       3C ||
| 4A     |    4B       4C^||
| 5A    ^|    5B  |    5C  |
| 6A     |    6B ^|    6C  |

## Images
Images must be hosted online somewhere, like [Imgur](https://www.imgur.com). You use the address to that image to reference it in your brew\*.

Using *Curly Injection* you can assign an id, classes, or inline CSS properties to the Markdown image syntax.

![alt-text](https://s-media-cache-ak0.pinimg.com/736x/4a/81/79/4a8179462cfdf39054a418efd4cb743e.jpg) {width:100px,border:"2px solid",border-radius:10px}

\* *When using Imgur-hosted images, use the "direct link", which can be found when you click into your image in the Imgur interface.*

## Snippets
Homebrewery comes with a series of *code snippets* found at the top of the editor pane that make it easy to create brews as quickly as possible.  Just set your cursor where you want the code to appear in the editor pane, choose a snippet, and make the adjustments you need.

## Style Editor Panel
{{fa,fa-paint-brush}} Usually overlooked or unused by some users, the **Style Editor** tab is located on the right side of the Snippet bar. This editor accepts CSS for styling without requiring `<style>` tags-- anything that would have gone inside style tags before can now be placed here, and snippets that insert CSS styles are now located on that tab.

{{pageNumber 2}}
{{footnote PART 2 | BORING STUFF}}
\page
![cat warrior](https://s-media-cache-ak0.pinimg.com/736x/4a/81/79/4a8179462cfdf39054a418efd4cb743e.jpg) {width:325px,mix-blend-mode:multiply}
![homebrewery_mug](http://i.imgur.com/hMna6G0.png) {width:280px,margin-right:-3cm,wrapLeft}
![homebrewery_mug](http://i.imgur.com/hMna6G0.png) {width:280px,margin-left:-3cm,wrapRight}
![homebrew mug](http://i.imgur.com/hMna6G0.png) {position:absolute,top:50px,right:30px,width:280px}
{{watercolor1,top:20px,left:30px,width:300px,background-color:#BBAD82,opacity:80%}}


\page

Table Examples::

##### Character Advancement
| Experience Points | Level | Proficiency Bonus |
|:------------------|:-----:|:-----------------:|
| 0                 | 1     | +2                |
| 300               | 2     | +2                |
| 900               | 3     | +2                |
| 2,700             | 4     | +2                |
| 6,500             | 5     | +3                |
| 14,000            | 6     | +3                |



{{wide
##### Weapons
| Name                    | Cost  | Damage          | Weight  | Properties |
|:------------------------|:-----:|:----------------|--------:|:-----------|
| *Simple Melee Weapons*  |       |                 |         |            |
| &emsp; Club             | 1 sp  | 1d4 bludgeoning | 2 lb.   | Light      |
| &emsp; Dagger           | 2 gp  | 1d4 piercing    | 1 lb.   | Finesse    |
| &emsp; Spear            | 1 gp  | 1d6 piercing    | 3 lb.   | Thrown     |
| *Simple Ranged Weapons* |       |                 |         |            |
| &emsp; Dart             | 5 cp  | 1d4 piercig     | 1/4 lb. | Finesse    |
| &emsp; Shortbow         | 25 gp | 1d6 piercing    | 2 lb.   | Ammunition |
| &emsp; Sling            | 1 sp  | 1d4 bludgeoning | &mdash; | Ammunition |
}}


##### Typical Difficulty Classes
{{column-count:2
| Task Difficulty | DC |
|:----------------|:--:|
| Very easy       | 5  |
| Easy            | 10 |
| Medium          | 15 |

| Task Difficulty   | DC |
|:------------------|:--:|
| Hard              | 20 |
| Very hard         | 25 |
| Nearly impossible | 30 |
}}


{{classTable,frame,decoration
##### The Concierge
| Level | Proficiency Bonus | Features | Gunpowder Torturer    |
|:-----:|:-----------------:|:---------|:---------------------:|
|  1st  |  +2  | Exo Interfacer        |          2            |
|  2nd  |  +2  | Spiritual Illusionism |          2            |
|  3rd  |  +2  | Biochemical Sorcery   |          3            |
|  4th  |  +2  | Police Necromancer    |          3            |
|  5th  |  +3  | Genetic Banishing     |          3            |
|  6th  |  +3  | Sixgun Poisoner       |          4            |
|  7th  |  +3  | Genetic Banishing     |          4            |
|  8th  |  +3  | Spell Analyst         |          4            |
|  9th  |  +4  | Nuclear Biochemistry  |          4            |
| 10th  |  +4  | Hermetic Geography    |          4            |
| 11th  |  +4  | Pharmaceutical Outlaw |          4            |
| 12th  |  +4  | Phased Linguist       |          5            |
| 13th  |  +5  | Consecrated Augury    |          5            |
| 14th  |  +5  | Spell Analyst         |          5            |
| 15th  |  +5  | Civil Divination      |          5            |
| 16th  |  +5  | Phased Linguist       |          5            |
| 17th  |  +6  | Torque Interfacer     |          6            |
| 18th  |  +6  | Sixgun Poisoner       |          6            |
| 19th  |  +6  | Spiritual Illusionism |          6            |
| 20th  |  +6  | Nuclear Biochemistry  |      unlimited        |
}}
\column
{{classTable,frame,decoration
##### Manicurist Spellcasting
| Level | Cantrips | Spells |--- Spells Slots per Spell Level ---||||
|      ^| Known   ^| Known ^|   1st   |   2nd   |   3rd   |   4th   |
|:-----:|:--------:|:------:|:-------:|:-------:|:-------:|:-------:|
|  3rd  |    2     |   3    |    2    |    —    |    —    |    —    |
|  4th  |    2     |   4    |    3    |    —    |    —    |    —    |
|  5th  |    2     |   4    |    3    |    —    |    —    |    —    |
|  6th  |    2     |   4    |    3    |    —    |    —    |    —    |
|  7th  |    2     |   5    |    4    |    2    |    —    |    —    |
|  8th  |    2     |   6    |    4    |    2    |    —    |    —    |
|  9th  |    2     |   6    |    4    |    2    |    —    |    —    |
| 10th  |    3     |   7    |    4    |    3    |    —    |    —    |
| 11th  |    3     |   8    |    4    |    3    |    —    |    —    |
| 12th  |    3     |   8    |    4    |    3    |    —    |    —    |
| 13th  |    3     |   9    |    4    |    3    |    2    |    —    |
| 14th  |    3     |   10   |    4    |    3    |    2    |    —    |
| 15th  |    3     |   10   |    4    |    3    |    2    |    —    |
| 16th  |    3     |   11   |    4    |    3    |    3    |    —    |
| 17th  |    3     |   11   |    4    |    3    |    3    |    —    |
| 18th  |    3     |   11   |    4    |    3    |    3    |    —    |
| 19th  |    3     |   12   |    4    |    3    |    3    |    1    |
| 20th  |    3     |   13   |    4    |    3    |    3    |    1    |
}}

\page

{{classTable,frame,decoration,wide
##### The Manicurist
| Level | Proficiency | Features     | Cantrips | --- Spell Slots Per Spell Level ---|||||||||
|      ^| Bonus      ^|             ^| Known   ^|1st |2nd |3rd |4th |5th |6th |7th |8th |9th |
|:-----:|:-----------:|:-------------|:--------:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|  1st  | +2 | Gunslinger Corruptor  |    2     | 2  | —  | —  | —  | —  | —  | —  | —  | —  |
|  2nd  | +2 | Phased Linguist       |    2     | 3  | —  | —  | —  | —  | —  | —  | —  | —  |
|  3rd  | +2 | Mathematical Pharmacy |    2     | 4  | 2  | —  | —  | —  | —  | —  | —  | —  |
|  4th  | +2 | Plasma Gunslinger     |    3     | 4  | 3  | —  | —  | —  | —  | —  | —  | —  |
|  5th  | +3 | Police Necromancer    |    3     | 4  | 3  | 2  | —  | —  | —  | —  | —  | —  |
|  6th  | +3 | Immunological Cultist |    3     | 4  | 3  | 3  | —  | —  | —  | —  | —  | —  |
|  7th  | +3 | Divinatory Mineralogy |    3     | 4  | 3  | 3  | 1  | —  | —  | —  | —  | —  |
|  8th  | +3 | Exo Interfacer        |    3     | 4  | 3  | 3  | 2  | —  | —  | —  | —  | —  |
|  9th  | +4 | Genetic Banishing     |    3     | 4  | 3  | 3  | 2  | 1  | —  | —  | —  | —  |
| 10th  | +4 | Gunpowder Torturer    |    3     | 4  | 3  | 3  | 2  | 1  | —  | —  | —  | —  |
| 11th  | +4 | Spiritual Illusionism |    4     | 4  | 3  | 3  | 2  | 1  | 1  | —  | —  | —  |
| 12th  | +4 | Immunological Cultist |    4     | 4  | 3  | 3  | 2  | 1  | 1  | —  | —  | —  |
| 13th  | +5 | Immunological Cultist |    4     | 4  | 3  | 3  | 2  | 1  | 1  | 1  | —  | —  |
| 14th  | +5 | Seismological Alchemy |    4     | 4  | 3  | 3  | 2  | 1  | 1  | 1  | —  | —  |
| 15th  | +5 | Immunological Cultist |    4     | 4  | 3  | 3  | 2  | 1  | 1  | 1  | 1  | —  |
| 16th  | +5 | Seismological Alchemy |    4     | 4  | 3  | 3  | 2  | 1  | 1  | 1  | 1  | —  |
| 17th  | +6 | Consecrated Augury    |    4     | 4  | 3  | 3  | 2  | 1  | 1  | 1  | 1  | 1  |
| 18th  | +6 | Seismological Alchemy |    4     | 4  | 3  | 3  | 3  | 1  | 1  | 1  | 1  | 1  |
| 19th  | +6 | Consecrated Augury    |    4     | 4  | 3  | 3  | 3  | 2  | 2  | 1  | 1  | 1  |
| 20th  | +6 | Consecrated Augury    |    4     | 4  | 3  | 3  | 3  | 2  | 2  | 2  | 1  | 1  |
}}

{{classTable,frame,decoration,wide
##### The Weirkeeper
| Level | Proficiency | Features     | Spells |--- Spell Slots Per Spell Level ---|||||
|      ^| Bonus      ^|             ^| Known ^|  1st  |  2nd  |  3rd  |  4th  |  5th  |
|:-----:|:-----------:|:-------------|:------:|:-----:|:-----:|:-----:|:-----:|:-----:|
|  1st  | +2 | Gunpowder Torturer    |   —    |   —   |   —   |   —   |   —   |   —   |
|  2nd  | +2 | Civil Divination      |   2    |   2   |   —   |   —   |   —   |   —   |
|  3rd  | +2 | Malefic Chemist       |   3    |   3   |   —   |   —   |   —   |   —   |
|  4th  | +2 | Orbital Gravedigger   |   3    |   3   |   —   |   —   |   —   |   —   |
|  5th  | +3 | Pharmaceutical Outlaw |   4    |   4   |   2   |   —   |   —   |   —   |
|  6th  | +3 | Phased Linguist       |   4    |   4   |   2   |   —   |   —   |   —   |
|  7th  | +3 | Civil Divination      |   5    |   4   |   3   |   —   |   —   |   —   |
|  8th  | +3 | Pharmaceutical Outlaw |   5    |   4   |   3   |   —   |   —   |   —   |
|  9th  | +4 | Immunological Cultist |   6    |   4   |   3   |   2   |   —   |   —   |
| 10th  | +4 | Plasma Gunslinger     |   6    |   4   |   3   |   2   |   —   |   —   |
| 11th  | +4 | Phased Linguist       |   7    |   4   |   3   |   3   |   —   |   —   |
| 12th  | +4 | Statistical Occultism |   7    |   4   |   3   |   3   |   —   |   —   |
| 13th  | +5 | Torque Interfacer     |   8    |   4   |   3   |   3   |   1   |   —   |
| 14th  | +5 | Biochemical Sorcery   |   8    |   4   |   3   |   3   |   1   |   —   |
| 15th  | +5 | Nuclear Biochemistry  |   9    |   4   |   3   |   3   |   2   |   —   |
| 16th  | +5 | Astrological Botany   |   9    |   4   |   3   |   3   |   2   |   —   |
| 17th  | +6 | Malefic Chemist       |   10   |   4   |   3   |   3   |   3   |   1   |
| 18th  | +6 | Torque Interfacer     |   10   |   4   |   3   |   3   |   3   |   1   |
| 19th  | +6 | Mathematical Pharmacy |   11   |   4   |   3   |   3   |   3   |   2   |
| 20th  | +6 | Mathematical Pharmacy |   11   |   4   |   3   |   3   |   3   |   2   |
}}

\page

Font Style Options ::
new line is a double :

{{font-family:OpenSans Dummy Text}}::
{{font-family:CodeBold Dummy Text}}::
{{font-family:CodeLight Dummy Text}}::
{{font-family:ScalySansRemake Dummy Text}}::
{{font-family:BookInsanityRemake Dummy Text}}::
{{font-family:MrEavesRemake Dummy Text}}::
{{font-family:Pagella Dummy Text}}::
{{font-family:SolberaImitationRemake Dummy Text}}::
{{font-family:ScalySansSmallCapsRemake Dummy Text}}::
{{font-family:WalterTurncoat Dummy Text}}::
{{font-family:Lato Dummy Text}}::
{{font-family:Courier Dummy Text}}::
{{font-family:NodestoCapsCondensed Dummy Text}}::
{{font-family:Overpass Dummy Text}}::
{{font-family:Davek Dummy Text}}::
{{font-family:Iokharic Dummy Text}}::
{{font-family:Rellanic Dummy Text}}::
{{font-family:"Times New Roman" Dummy Text}}::

\page
#### Overwhelming Enchantment of the Chocolate Fairy
*3rd-level divination*

**Casting Time:** :: 1 action
**Range:**        :: 30 feet
**Components:**   :: M (discarded gum wrapper, a small doll)
**Duration:**     :: 1 hour

A flame, equivalent in brightness to a torch, springs from an object that you touch. 
The effect look like a regular flame, but it creates no heat and doesn't use oxygen. 
A *continual flame* can be covered or hidden but not smothered or quenched.

:::::::::::::::::::

{{spellList,wide
##### Cantrips (0 Level) 
- Erruption of Immaturity
- Protection from Mucus Giant
- Spiritual Invocation of the Costumers
- Call Fangirl
- Magical Enchantment of Arrogance
- Tinsel Blast
- Hellish Cage of Mucus 

##### 1st Level 
- Create Nervousness
- Astral Rite of Acne
- Mystic Spell of the Poser
- Alchemical Evocation of the Goths
- Occult Globe of Salad Dressing 

##### 2nd Level 
- Necromantic Armor of Salad Dressing
- Ball of Annoyance
- Extra-Planar Spell of Irritation
- Mystic Spell of the Poser 

##### 3rd Level 
- Heal Bad Hygene
- Steak Sauce Ray
- Alchemical Evocation of the Goths
- Spiritual Invocation of the Costumers 

##### 4th Level 
- Tinsel Blast
- Steak Sauce Ray
- Astonishing Chant of Chocolate
- Astral Rite of Acne
- Control Noodles Elemental
- Luminous Erruption of Tea
- Protection from Mucus Giant
- Mystic Spell of the Poser
- Create Acne 

##### 5th Level 
- Flaming Disc of Inconvenience
- Sorcerous Dandruff Globe
- Cursed Ramen Erruption
- Ball of Annoyance
- Occult Transfiguration of Foot Fetish
- Luminous Erruption of Tea
- Create Acne
- Divine Spell of Crossdressing 

##### 6th Level 
- Ball of Annoyance
- Overwhelming Enchantment of the Chocolate Fairy
- Protection from Mucus Giant
- Astonishing Chant of Chocolate
- Ultimate Rite of the Confetti Angel 

##### 7th Level 
- Spiritual Invocation of the Costumers
- Necromantic Armor of Salad Dressing
- Dominate Ramen Giant
- Occult Transfiguration of Foot Fetish
- Ultimate Ritual of Mouthwash
- Tinsel Blast
- Overwhelming Enchantment of the Chocolate Fairy 

##### 8th Level 
- Call Fangirl
- Cursed Ramen Erruption
- Heavenly Transfiguration of the Cream Devil
- Erruption of Immaturity
- Sorcerous Dandruff Globe
- Steak Sauce Ray
- Control Noodles Elemental 

##### 9th Level 
- Tinsel Blast
- Dark Chant of the Dentists
- Astounding Pasta Puddle
- Astonishing Chant of Chocolate
- Steak Sauce Ray 

}}

\page
## Class Features

As a manicurist, you gain the following class features

#### Hit Points
**Hit Dice:**                    :: 1d4 per manicurist level
**Hit Points at 1st Level:**     :: 4 + your Constitution modifier
**Hit Points at Higher Levels:** :: 1d4 (or 3) + your Constitution modifier per manicurist level after 1st

#### Proficiencies
**Armor:**   :: Heavy armor, Shields, Light armor
**Weapons:** :: Squeegee, Martial weapons
**Tools:**   :: None

**Saving Throws:** :: Charisma, Constitution
**Skills:**        :: Choose two from Investigation, Sleight of Hand, History, Perception, Animal Handling

#### Spellcasting Ability
{{text-align:center
**Spell save DC**:: = 10 + your proficiency bonus + your Charisma modifier

**Spell attack modifier**:: = your proficiency bonus + your Charisma modifier
}}

#### Equipment
You start with the following equipment, in addition to the equipment granted by your background:
- (*a*) a martial weapon and a shield or (*b*) two martial weapons
- (*a*) five javelins or (*b*) any simple melee weapon
- 10 lint fluffs

::::

{{quote
The thief crept through the shadows, his eyes scanning the room for any sign of danger. He knew that one false move could mean the difference between success and failure, and he was determined to come out on top.

{{attribution Theron Shadowbane, *Darkness Rising*}}
}}

::::
{{note
##### Time to Drop Knowledge
Use notes to point out some interesting information.

**Tables and lists** both work within a note.
}}

::::
{{descriptive
##### Time to Drop Knowledge
Use descriptive boxes to highlight text that should be read aloud.

**Tables and lists** both work within a descriptive box.
}}

::::
#### Paper Armor of Folding
*Weapon, Common (requires attunement)*
:
This knob is pretty nice. When attached to a door, it allows a user to
open that door with the strength of the nearest animal. For example, if
there is a cow nearby, the user will have the "strength of a cow" while
opening this door.

\page


\column

\page
{{pageNumber 1}}
{{pageNumber,auto}}
{{pageNumber $[HB_pageNumber]}}
{{skipCounting}}
{{resetCounting}}

{{footnote The Homebrewery V3}}

{{footnote Class Features}}

{{footnote Tables}}

{{footnote Paper Armor of Folding}}

{{footnote Typical Difficulty Classes}}

{{footnote PART 1 | SECTION NAME}}

::::
 {{width:100px}} 

{{wide
Everything in here will be extra wide. Tables, text, everything!
Beware though, CSS columns can behave a bit weird sometimes. You may
have to manually place column breaks with `\column` to make the
surrounding text flow with this wide block the way you want.
}}

<!-- This is a comment that will not be rendered into your brew. Hotkey (Ctrl/Cmd + /). -->
