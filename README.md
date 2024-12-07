# Anno 2205 New Frontiers
**Für die deutsche Version des readmes, bitte [hier](https://taludas.github.io/#/de/Anno2205/Anno2205NewFrontiers) klicken.**

![Anno 2205 New Frontiers Cover](https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/aa973742-5af0-4828-9df4-bfe5cd46d078)

The Year is 2205.

You have created one of the most successful corporations ever. Your cities are continuing to grow rapidly and so do their resource and space requirements.

With the completion of the Lunar Licensing Program, your Moon Colonies are now filled to the brim.
After nine years of living in these circumstances, Mankind is longing for another giant leap towards interorbital colonisation: The Red Planet.

Hire the greatest scientists of all time to take on the challenge of traveling to Mars. Research advanced rocket technologies and prepare yourself for the second mission to Mars.

Explore the Red Planet, establish an autonomous AI Mars colony and begin to exploit its rare resources. With the help of AI and the special Martian environment, your scientist will be able to innovate even more powerful technologies than ever before, ensuring a life of plenty on Earth for centuries to come.

# Table of Content

- [Features](#features)
- [Installation Instructions](#installation-instructions)
- [FAQ](#faq)
- [Known Issues](#known-issues)
- [Detailed Changelog from Vanilla](#detailed-changelog-from-vanilla)
  - [Additions to the game](#additions-to-the-game)
  - [Quality of Life improvements](#quality-of-life-improvements)
  - [Changes to the base game including Tundra and Frontiers DLC](#changes-to-the-base-game-including-tundra-and-frontiers-dlc)
  - [Overhauled Population Needs](#overhauled-population-needs)
  - [Overhauled and New Production Chains](#overhauled-and-new-production-chains)
  - [Overhauled Public Buildings](#overhauled-public-buildings)
  - [Other Overhauled Buildings](#other-overhauled-buildings-from-vanilla-game)
  - [Changes to Orbit DLC](#changes-to-orbit-dlc)
  - [Overhauled Sector Traits](#overhauled-sector-traits)
- [Credits](#credits)

# Features

- Complete overhaul of all production chains, adding 9 new goods to the game and reworking several existing ones, enhancing game depth, complexity, and region interaction
- New Arctic Tier 3 population
- New Mars Sector featuring four seasons, separate Synth population, new questline and new Science system
- Rework of the Public Building Concept
- Intense Rework of the Orbital Station and Technology Nexus
- For more details, read [here](#detailed-changelog-from-vanilla)

# Installation Instructions

> [!CAUTION]
> **You need to start a new savegame in order to enjoy this mod's content!**
>
> **You need to own all three official DLCs to play this mod!**
>
> **If you want to experience the full effect of Mars' four seasons, it is required that you start your savegame with edited difficulty settings upon game creation: `Calamities=[Seldom, Regular or Frequent]` and `Assignment Time=[Long, Medium or Short]`. The later option influences the length of the Mars Seasons.**

  1. Download the latest release from [here](https://github.com/Taludas/Anno2205-NewFrontiers/releases/latest/download/Anno2205_NewFrontiers.zip).
  2. Open your Anno 2205 installation directory.

> [!TIP]
> Easiest way is through the game launcher of your choice. For Ubisoft Connect follow this path: Library -> Anno 2205 -> Manage (top right corner with the gear icon) -> Properties -> Installation -> Open folder

  3. Make sure you have no other mods installed for the game. If you are not sure, use the "verify files" option of your game launcher.

  4. Copy the "data" folder from the downloaded zip-file to the Anno 2205 installation directory. Overwrite existing files, if prompted to do so.

  5. Now open the Windows "Documents" folder (Standard path is: C:\Users\YOUR_NAME\Documents). Go into the "Anno 2205" folder that is inside of it. If there is none, make sure you have started the game at least once after installation.

  6. Inside the "Anno 2205" folder, follow the path "Anno 2205\config\engine.ini". Open the engine.ini file with an editor program. Editor, Notepad++ or VSCode are good programs to do this.

  7. Search for the `"PreferLocalFiles"` entry. Change the value behind it from `"false"` to `"true"`. If it has been changed already, you don't need to do it. Make sure to save the edited .ini file on exit.

  8. Read the [FAQ](#faq) and the [Known Issues List](#known-issues)

  9. You are good to go!

> [!TIP]
> You will notice if the installation has been successful when the usual epilepsy warning has been changed to a custom text. Enjoy the mod!

# FAQ
1. **When do I unlock the Mars?**

    The new storyline to reach the Mars is unlocked after you have completed the Main Story of 2205. The Quest will then ask you to finish the Sector Quest for the "Greentide Archipelago" to unlock Synthetics. Afterwards, the Second Mars Mission begins which will eventually take you to the Red Planet.

2. **What is the difference between "Services" and "Urbanisation"? How do I fulfill these needs?**

    Services are a newly introduced product that can only be produced by Public Buildings. I created them to overhaul and diversify the 2205 Public Building game mechanic. While the first community centers on Earth and in the Arctic operate without input goods to start with, you will need to supply your higher level Public Buildings with certain goods in order to produce services. The more sophisticated the inputs, the more services the building will produce.

    While it's theoretically possible to supply an Investor City with Community Centers alone, you'd need so many of them that there wouldn't be much room left for houses. Also, this is where Urbanisation comes into play. Urbanisation is basically the "old" way, Public Buildings worked in 2205. The concept is the same as in Logistics. Your houses must be built close to Urban Centers (i.e. Public Buildings) in order to meet their Urbanisation needs. Factories also provide a certain amount of Urbanisation, so - if you like it - you have an incentive to build them into your cities as well. However, most of the Urbanisation is generated by Public Buildings, and the higher the level, the more you get. I kept this mechanic in place to prevent players from following the hypothesis of piling up a lot of Public Buildings at one end of the map and building the city at the other.

3. **Why are some of my buildings locked without unlock condition shown?**

    You have discovered one of the new mechanics I introduced in the Orbit DLC, where certain buildings are locked behind research in the Technology Nexus. As Anno cannot adequately display the unlocking requirements of a building if the unlocking condition is anything other than "have x amount of population level y", I have created five additional quests to guide you on your way to unlocking these buildings. You can find them on the left-hand side, just below the main quest tracker, as soon as they are relevant to your progress.

    All five buildings will simplify the production process and logistics costs of certain goods. For example: The AI Assembly Hall, which produces Cybersynth Circuits, is initially locked on the Moon, even though you need it to produce BioEnhancers for your Executives. For now, you will have to rely on the more expensive AI Assembly Hall in the Tundra Region and ship them to the Moon for processing. However, by researching the level 3 tech of the linking tree between the standard Biotech and Electronics techs, you can unlock this building on the Moon, greatly simplifying the production chain. If you also research Aeroponic Farming on the Moon, you can produce all the inputs for the Cybersynth circuits on the Moon, drastically reducing the logistical costs involved in producing BioEnhancers.

4. **Why are additional secondary modules like the drone hive modules THAT expensive?**

    I have decided to reintroduce the rare materials as well as additional - more specific - building materials into the secondary module costs. A major gameplay loop in 2205 is the constant balancing of workforce, energy and credits. I feel that this change to the building costs, by restricting access to the maintenance reduction modules to the mid to late game, improves this gameplay loop beyond that of the original game.

    Example: In the late Operator - early Executive stage, you will most likely struggle to keep up with the increased labour costs of maintaining your production facilities. To overcome this obstacle, you cannot just spam the five reduction modules on the cheap. You need to build a proper Smart Drones production chain in the Tundra first and ship them to the other sectors before you can take advantage of these modules. Of course, you could just build more houses, but that would also require additional work...

    **TL:DR** The material costs have been increased to make the game more complex. Finding ways to reduce the cost of maintaining your factories has become more important than in the base game.
    By the way, have you noticed that the useless logistics module has been replaced with the actually relevant finance calculator to reduce the maintenance costs of non-energy buildings?

# Known Issues

**Base game:**
- The four new products (Organic Food, Fine Food, Sustenance Packs and Thermal Shells) cannot be traded with the world market.
- There are five quests to guide you to do specific research to unlock certain buildings as the "Unlock Condition" tooltip only works with population milestones. Unfortunately those quests will be visible in all sessions, not only in those the buildings are located in.
- Certain Secondary Module tooltips will not show the correct tooltip description (i.e. Energy module on Energy Production buildings giving +15% output, or Mars Research Lab modules)
- The population overview filter in the strategic view does not work properly with the new Arctic Tier 3. It does not show the correct portrait next to the number. Same goes for the Martian Synthetics.
- Services are a new "product". The balance can not be shown in the "usual" balance menu, otherwise they would be tradeable via trade route. Instead you can find them in the building material bar at the top or click on any Public Building and hover over the "Globe" icon to see the current sector balance.
- Company Headquarter infotip in the bottom of the screen seems to be hardcoded and displays tier 2, 3 and 4 public needs although those have been removed from the game.
- Factories that produce Urbanisation as a site-product cannot be paused anymore.
- Selecting a mining site on the Moon will only show 5 possible entries in the UI. As there are now 6 mines in total, the Regolith Gatherer can only be build via buildmenu.
- Increased storage for Rare Resource Generators only comes into effect after collecting the resources once. Therefore always wait until the first unit has been generated and collect it immediately after building to set the storage amount to the modded one.
- The UI of the Astronaut Training Camps have been changed to that of a standard factory to support the display of extra goods generated by activating the tier 5 Heavy Industry tech "Orbital Warehouses". Unfortunately this leads to an issue, where the output of the Astronauts is shown with "0 per minute". This is only a visual issue. The Camp still trains 25 Astronauts per full 10 minute cycle on 100% productivity. You can view the cumulated numbers per session in the Orbital Station tooltip shown on the left site of your money once you have build one Training Camp. Same goes for the time till the next supply flight to the Station. This is now exclusive to the aforementioned UI.

**Mars Sector:** Due to the way, Mars Sector is coded to be part of the Moon region, some issues arise from this specifically:
- Mars sector takes longer than other sectors to load.
- The unlock notification for new buildings on the Moon has been changed, so that all newly unlocked Moon buildings will show up as "New Moon Buildings" in the notification.
- To manage the build menu and to restrict Mars buildings to the Mars sector, I had to use a workaround by locking the Moon buildings when entering the Mars session. When you leave the Mars session (for example to adjust trade routes), you will get a notification, that again "New Moon Buildings" have been unlocked. I already shortened the notification by using the "New Moon Buildings" pool, but if I disable them completely, you will get no notification on first unlock.
- After entering the Mars sector and open the build menu, you regularly need to select "Martian Synthetics" tab again to see the available buildings.
- Pressing the Hotkey for "Build Street" on the Mars will result in the Moon Tracks instead of the expected Mars Tracks. Pipette it or use the build menu entry to lay down Mars Tracks instead.
- Using the buildings filter tab next to the minimap (the population button) in the Mars Session will lead to a game freeze, only resolvable by killing the task.
- The Mars sector has some unique sector traits available. Notice, that on entering the sector, the welcome UI shows a random Moon trait instead of the Martian one. That one will only be given to the sector on first enter. You can reroll the sector trait by completing a special quest. This involves delivering certain products to your space port. Notice that the usual way of rerolling sector traits will result in a random trait from the Moon!
- Mars Meteors use Moon ground textures.
- While loading the Mars Sector icon will change to a white rectangle. After clicking for loading, click anywhere on the strategic view again to get the icon back.
- Whenever Mars season changes and you are in another sector, the time of day will change to that one used by the Martian season effect on its own accord. You can adjust the time via the camera menu next to the minimap.
- Whenever Mars season changes and you are in another sector, the time of day will change to that one used by the Martian season effect on its own accord. You can adjust the time via the camera menu next to the minimap.
- If you use the Geo-Engineering quest on Mars, the script may randomly choose to apply the same trait that is already active. This will cause the sector to lose its trait altogether. In that case, you can use the console to reapply the effect. The GUIDs can be found [here](/en/Anno2205/SectorTraits.md). First, enter the Mars session. Now press Shift+F1 to open the console and type `debug.toggleSectorEffect(GUID)` using the corresponding number of the wanted trait. Press enter and close the console with Shift+F1 again.
- Sometimes, Martian Season effects can randomly start on the Moon/Earth. This is a problem, as they last for a very long time and cannot be resolved with a quest. Again, you need to use the console to get rid of them, if it happens to you: First, enter the session in question. Now press Shift+F1 to open the console and type `debug.toggleSectorEffect(GUID)`. Proceed to replace the "GUID" placeholder with the corresponding GUID from the currently active season effect (see below). Press enter and close the console with Shift+F1 again. The effect should be gone.
- Sometimes, Martian Season effects can end up mismatched with the current season quest. If you currently suffer from mismatched season effect to the shown season quest in the quest tracker on the left side of the screen, you have to use the console to fix this:
> 1. Press Shift+F1 to open the console.
> 2. Enter (without any typing errors, pay attention to upper and lower case!), replace "CurrentSeasonGUID" with the correct number from the table below:
`debug.startSectorEffect(CurrentSeasonGUID,19990093)`
> 3. Press Enter
> 4. Enter (without any typing errors, pay attention to upper and lower case!), , replace "CorrectSeasonGUID" with the correct number from the table below:
`debug.startSectorEffect(CorrectSeasonGUID,19990093)`
> 5. Press Shift+F1 to close the console.
> 6. The sector effect should now match the current season quest.

  |Season|Summer|Autumn|Winter|Spring|
  |---|---|---|---|---|
  |GUID|19990307|19990378|19990370|19990374|

- Sometimes Drake's invasions bug out after unlocking Mars. Apparently he tries to invade there(?) (which is not possible because there is no sea there obviously to put his ships upon). The quest description doesn't contain the usual sector name, and the quest log shows the requirement to destroy -1/1 ships and no invasion force is in any sector to clear them out. However, sometimes the quest resolves automatically if you enter "the correct" sector (which is not visible/logically deducible). If this happens to you it is best practice to end this invasion quest via the console to prevent possible damage:
> 1. Select the quest in the outliner (active quest, showing all details).
> 2. Press Shift+F1 to open the console.
> 3. Type `quests.reachSelectedQuest()` and press enter.
> 4. The quest should resolve. Close the console with Shift+F1 again.

# Detailed Changelog from Vanilla

1. ## Additions to the game

    - **9 New Products**

     |**Product**|**Nutrient Powder**|**Organic Food**|**Fine Food**|**Hyaluronic Acid**|**Sustenance Packs**|**Thermal Shells**|**Superconductors**|**Neural Interfaces**|**Services**|
     |---|---|---|---|---|---|---|---|---|---|
     |**Icon**|<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/1fb79866-40e8-4949-b665-d2f28b14229b" height="32" />|<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/78d4d69c-5a49-4ea9-9643-50b754666d88" height="32" />|<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/8a1c6487-e183-40da-8f6a-d1a13b518057" height="32" />|<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/e5c5c32b-5074-4a77-b6c4-e99d96267594" height="32" />|<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/64bd8fdd-2675-4102-9e3e-d779847b2cbe" height="32" />|<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/068e0a5d-e3ae-427c-8ef0-14d52038827c" height="32" />|<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/83ccc971-925b-424e-9d56-9e3227dba755" height="32" />|<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/a43f53f1-2240-4cdd-9021-1f56ec3bb856" height="32" />|<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/886d132c-3945-47c7-ad3e-736aaa04b42f" height="32" />|

    - **Additional Mars Session**
       - It can be found in the upper right corner of the strategic view. It is accessible after completing a new questline available once you have completed the Lunar Licensing Program and the Greentide Archipelago's sector story questline surrounding the Synths.
       - Add 10 New Mars Sector Traits for the new sector. One trait is distributed to it randomly on first entry. With a special geo-engineering quest you can reroll the sector trait as well (Warning: normal rerolling results in Moon Traits!) For details see: [here](#overhauled-sector-traits)
       - Add 4 seasons to the Mars session, which cycle in regular intervals. Each season has its own unique calamity effect that the player will have to deal with. To compensate for the increased difficulty, each season also has a bonus for certain buildings:
     
        |**Season**|**Length**|**Effect**|
        |---|---|---|
        |<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/7c3c9922-f84d-4936-95b5-29e92e9de7fc" height="32" /> Summer|`Assignment Time = Long` = 60 min <br> `Assignment Time = Medium` = 30 min <br> `Assignment Time = Short` = 15 min|**Solar Flares** <br> Energy Transfer Routes ineffective <br> Solar Panels have higher productivity|
        |<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/888b2a4d-6b11-4f6e-b0c0-8b84dec39c06" height="32" /> Autumn|`Assignment Time = Long` = 30 min <br> `Assignment Time = Medium` = 15 min <br> `Assignment Time = Short` = 7:30 min|**Vulcanic Activity** <br> Mining sites closed <br> Energy Research Lab has higher productivity|
        |<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/3573264d-da6e-4c8d-966f-2a4ced1304d4" height="32" /> Winter|`Assignment Time = Long` = 60 min <br> `Assignment Time = Medium` = 30 min <br> `Assignment Time = Short` = 15 min|**Dry Ice Rain** <br> Martian Synths need more Services <br> Methane Ice Extractors have higher productivity|
        |<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/6d8593ec-c137-4f49-a5d5-cdec1d9727db" height="32" /> Spring|`Assignment Time = Long` = 30 min <br> `Assignment Time = Medium` = 15 min <br> `Assignment Time = Short` = 7:30 min|**Dust Storms** <br> Traderoutes shout down <br> Windpark, KREEP Gatherer and Diamond Extractor have higher output|

        ![marssectorunlocked](https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/063416d6-31df-4bc3-bf0b-f3fe975ac43b)
        ![mars1](https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/40869164-e788-4347-8d78-49ea4be93214)

    - **New Main Quests**
      - *"30. The AI Revolution": Settle 50000 Synthetics*

        As humanity craves for even more galactic expansion after your successful Moon colonization, the daunting challenge to conduct a second mission to Mars and of sustaining life in the harsh Martian environment presents itself once again. As there is no chance that humans can survive this journey with current technology, the Global Union presents you with the task to develop an advanced artificial intelligence that is capable to overcome the formidable obstacles of interplanetary travel and colonization.

      - *"31. The Second Mars Mission": Settle 10000 Geniuses and upgrade your Transmission Spaceport in one of your Moon sectors with a Mars Launcher.*

        After more than one hundred years, you are chosen to ready humanity for its second expedition to the Red Planet. Extensive research conducted by your foremost aerospace engineers is imperative for the development of a robust rocket system capable of enduring the arduous journey to Mars.

      - *"32.  The First Martian AI Colony": Settle 1000 Martian Synths.*

        Congratulations! Once more, you've surpassed expectations with excellence in executing the second mission to mars. Your inaugural Synthetics have successfully treaded upon the surface of the Red Planet. Ensure an ample provision of goods and resources to maintain your androids amidst the dusty Martian environment. Continue in expanding your first colony to allow exploiting the ample resources of this unknown ground and build up a strong additional Expertise gain to support your Orbital Station.

      - *"33. Maintaining the Colony": Build a Martian Research Cluster and generate your first Expertise on Mars*

        Now that you've built up a decent workforce, let's start producing some things locally to ensure your Androids can survive in the harsh Martian climate. Our ultimate goal is to be self-sufficient in the production of services. This is a multi-step process that will also familiarise you with the functions of the Martian Research Laboratories. Our first step is the construction of a small research hub.

      - *"33.1 Maintaining the Colony": Build an Energy Research Laboratory and produce Natural Gas on Mars*

        We can support the production of Expertise by building additional Research Labs on Mars. Each specialisation has it's own input goods and produces a specific output product in addition to the usual Expertise. The loop to produce Services starts with the Energy Lab, that produces Gas from the locally mined Methane Ice.

      - *"33.2 Maintaining the Colony": Build an Agricultural Research Laboratory and produce Nutrient Powder on Mars*

        The next step is agricultural research, which is necessary to support the most basic forms of life on Mars: Corals and Moss. Start by filtering some of the Methane Ice for some residual Water, which you can then use to grow the very first plants on Mars - the foundation for human life on Mars!

      - *"33.3 Maintaining the Colony": Build a Heavy Industry Research Laboratory and produce Multispec Prisms on Mars*

        With one of the ingredients for Cybersynth Circuits out of the way, let's start digging up some Martian dust to scour for the rare resources that are hidden beneath its rusty crust. We need these to manufacture high quality lenses for further mineral processing.

      - *"33.4 Maintaining the Colony": Build an Electronics Research Laboratory and produce Silicon on Mars*

        Equipped with the appropriate lenses, you will be able to start analysing and separating all of the rare resources of the Red Planet for further use in the production of Cybersynth Circuits.

      - *"33.5 Maintaining the Colony": Build a Biotech Research Laboratory and produce Cybersynth Circuits on Mars*

        You have done it! The final preparations are complete and the first locally produced Cybersynth Circuits are rolling out of your Biotech Lab! This is the crucial step towards basic self-sustaining Android life on Mars - your machines will be able to analyse, repair and improve themselves without you having to intervene. With your Martian colony now fully equipped with research labs of all kinds, it is highly recommended that you strengthen your Martian population and continue on this path to total knowledge!

      - *"The Martian AI Research Program - Steps 1 to 15": Settle 75000 Martian Synths in total.*

        By increasing your population of Synths on the Mars you can now unlock more Workshop- and Module-Permits to expand the capabilities of your Orbital Station even further: Per 5000 Martian Synths you unlock 1 extra workshop permit for your Orbital Station along with some more modules and connectors. A total of 14 additional permits can be gained, so that you can now fully exploit the Nexus' research capabilities by building 5 workshops of each specialisation. Upon reaching the maximum required population you unlock the technology to geo-engineer the Mars' sector trait to a random new one.

    - **New Mars Buildings**
        - Mars Tracks
        - Martian Transportation Center
        - Martian Windpark (mine slot)
        ![mars3](https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/7471bbbc-6bc1-4d5d-843f-69c1444ca213)

        - Martian Solar Panel
        - Small and Large Shield Generator
        - Martian Dwellings
        - Martian AI Maintenance Station
        ![mars2](https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/cc5babae-a757-494e-8a1e-af4f17d30b11)

        - Martian Gas Drilling Rig
        ![mars4](https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/22d8253d-2aa4-461b-b3dd-5ac90c367a14)

        - Martian Cobalt Open Pit Mine
        - Martian Titanium Open Pit Mine
        - Martian Tungsten Open Pit Mine
        ![mars5](https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/c6857641-fe4e-4507-ae96-a9124106bbe2)

        - Martian Rare Earth Extractor
        - Martian Feldspar Quarry
        - Martian Diamond Extractor
        ![mars7](https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/bf245c4b-474f-4cc4-99cf-9c92ca4708a7)

        - Martian Ion Welder
        - Martian Robot Assembly Hall
        - Martian Methane Ice Filter
        - Martian Coral Breeder
        - Martian Moss Breeder

        - **Research Cluster:** Generates Expertise and Energy without input goods, but uses a larger radius instead (overlaps with Martian Solar Panel)
        - **Martian Agriculture Research Lab:** Generates Expertise and Nutrient Powder from Deep Water Corals and Moss, uses a smaller radius (overlaps with other Research Labs)
        - **Martian Biotech Research Lab:** Generates Expertise and Cybersynth Circuits from Silicon and Nutrient Powder, uses a smaller radius (overlaps with other Research Labs)
        - **Martian Electronics Research Lab:** Generates Expertise and Silicon from Rare Earth Elements and MultiSpec Prisms, uses a smaller radius (overlaps with other Research Labs)
        - **Martian Energy Research Lab:** Generates Expertise and Natural Gas from Methane Ice and Tungsten, uses a smaller radius (overlaps with other Research Labs)
        - **Martian Heavy Industry Research Lab:** Generates Expertise and MultiSpec Prisms from Diamonds and Rare Earth Elements, uses a smaller radius (overlaps with other Research Labs)
        - and corresponding primary and secondary **Modules** to those Labs: Greenhouse, Artificial G-Lab, Storage Platform, Solar Panel, Radiator, Recycling Station. There are also connectors available if you like them.
          - <details>
              <summary> Expand to find out more about the module's properties</summary>

              | **Module**|<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/27870b77-a9b9-4ab6-9823-8d7cfb7bd772" height="16" /> Greenhouse|<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/10196c8c-b66e-4eeb-9c02-b4d74adbccea" height="16" /> Artificial-G Lab|<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/8b208cd5-69a2-4c62-89ca-6556ac2b1c2f" height="16" /> Recycling Module|<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/ae819604-dc32-4c62-aeb0-7c84ff46a9ee" height="16" /> Solar Cells|<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/03f8ae22-f305-48e8-bcbc-932cf44e0202" height="16" /> Storage Platform|<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/38a08c94-f9fe-4607-9ca6-1734403df0fd" height="16" /> Cooling Module |
              |---|---|---|---|---|---|---|
              |***Output***|+15%|+15%|+15%|+10%|+10%|-|
              |***Input***|+10%|+10%|-10%|-|-|-5%|
              |***Maintenance***|+25%|+25%|+100%|-15%|-15%|-15%|
              |***Workforce***|+25%|+25%|+100%|+15%|-15%|+15%|
              |***Energy***|+25%|+25%|+100%|-15%|+15%|+15%|
            </details>

        ![mars6](https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/4e96e802-576e-489f-a192-71cd4d127f2d)

    - **New Tier 3 Arctic Population: Geniuses**
        - Portrait

        ![icon_portrait_resident_arctic_03](https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/1c6d784b-d733-4470-a5f4-4d3ee1a32d07)

        - Housing
        ![arctictier3_2](https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/fd046a50-87ae-4be1-b361-59c282cf882f)

        - For needs, see table [here](#overhauled-population-needs).

    - <details>
        <summary>

        **Expand to see pictures of the added new Production Buildings for the overhauled Production Chains and the new Public Buildings**

        </summary>

        - Community Center Earth
        ![communitycenter](https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/630780dc-4d7c-4c69-8e00-c237cb0d5483)

        - Nutrient Processing Laboratory Earth/Tundra/Arctic
        ![arcticnutrientpowder](https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/c886bf31-e2d8-48de-8936-9d1ab82a8377)

        - Vegetable Farm Earth
        - Organic Food Factory Earth
        - Fine Food Kitchen Earth
        ![sushiroller](https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/3e4640cd-ff7e-4b1b-b306-71f556401b60)

        - Solar Park Earth/Tundra/Arctic
        ![solarpark](https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/011ca551-c291-4824-b7b3-4a61458280ff)

        - Sustenance Packs Factory Earth
        ![sustenancepacksearth](https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/28bb8768-d4b0-4654-af8b-cf6e3e34a1bd)

        - AI Maintenance Station Earth
        - Water Pump Tundra
        ![tundra_waterpump](https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/213bb2eb-2ef5-43d5-a225-2019252bb40e)


        - Hyaluron Concentrator Tundra
        ![hyaluronicacid](https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/1158176d-31e6-4dec-b7a7-d6a7e56f2f63)

        - Off-shore Drilling Rig Tundra
        ![tundra_trilltower](https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/5c0ba807-ebfe-4eaa-8d41-170ba91f4da8)


        - Tundra Healthcenter
        - Boreal Tailor Tundra
        ![tundraborealtailor](https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/536a2198-f623-492a-b8b5-bf3389621c4e)

        - Tundra Infodrome
        - Arctic Health Center
        - Arctic Tailor
        ![arctictailor](https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/8e93ddf8-4ef2-4885-8fa1-1a2eb843ba82)

        - Methane Gas Refinery
        ![arcticgasrefinery](https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/341582b3-75f0-4ac0-9ad7-8327a7d5c8c8)

        - Arctic Infodrome
        - Superconductor Fabrication Hall
        - Neural Interfaces Factory
        ![arctic neuralinterfaces](https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/736007bb-4306-475a-a5ea-1894d55252f2)

        - Moon Ice Melter
        ![icemelter](https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/24aded0a-3f5f-472d-9897-7287cf959f96)

        - Aluminum Mine
        ![aluminiumminemoon](https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/b2f57e16-db53-4d39-a721-d7900e385887)

        - Sustenance Pack Factory
        - Organic Food Factory
        - Luxury Food Manufactory
        ![foodmoon](https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/660c1d8d-762a-4073-a27c-2e4603f604f1)

        - Synthcell Incubator Moon
        ![moon_synthcellincubator](https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/ca3ea9b8-5210-4fe3-9786-fd46e4f81c5f)

        - AI Composition Plant Moon
        ![bioenhancer1](https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/3b813f86-aaf5-4c29-b285-7c96ea044e61)
      </details>

    - **Moon Aeroponic Farms and Food Production**

        One of the new features on the Moon is the possibility to produce any farming product through Aeroponic Farms. Those need to be unlocked first in the Nexus (Agriculture-Biotech tier 3). The Aeroponic Farm requires Water and Oxygen to operate. With this mod there is the option to produce Water on Moon from Moonice and Nano-Ceramics. Aeroponic Farms can produce a multiple of their counterparts on the earth.
        Another option with this mod is to produce part of your Food needs on the Moon as well. Sustenance Packs and Luxury Food are available. For the first one and Oxygen, I have introduced a new Aluminum Mine to the Moon. Luxury Food production chain on the Moon needs Organic Food and Wine. Organic Food can be produced here as well, from Rice and Vegetables using the Aeroponic Farming System.

        - Aeroponic Farms Moon (one for each crop type)
        ![newfarmsmoon](https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/41c95ec1-2dc2-4eba-a441-b9988d702a62)

3. ## Quality of Life Improvements
   - You can now open the ingame console by pressing Left Shift + F1. Some commands can be found [here](https://www.nexusmods.com/anno2205/mods/1?tab=description). While having basic autocomplete, notice that the console is not tolerant to spelling errors or incorrectly formatted arguments. The game will freeze in those cases.
   - All cutscene videos can be skipped by pressing escape. Same goes for Ubisoft logo and intro movie. Fade out duration has been shortened.
   - <details>
      <summary>Removed annoying NPC reminder messages</summary>

      Several NPC reminder messages have been removed, since they are quite intrusive and come in to short intervals for my liking:
      - Docks Reminder: John Rafferty does not remind you to upgrade your ships anymore.
      - Arctic Custodians: Hovard Young will not remind you that "This building plot is at your disposal" every time you build a mine or a coastal building in the Arctic.
      - Event Sectors: removed starting/reminder messages from the Mysterious Lady, trader Jorgensen, John Rafferty, Hovard Young
      - Voting: removed start/reminder messages from the Mysterious Lady (voting is broken anyways...)
      - Orbital Station: removed the annoying notifications every time the space shuttle launches with a new batch of Astronauts (why in the first place would you need to know this?!) as well as the regular message if you float Expertise.
      - Tundra: removed "welcome back" message from Esther Nylund every time you enter the sector after initial unlock.
      - Share Market: removed most basic AI starting and winning notifications.
     </details>
   - Changed World Market Route Durations from 2 hours to 12 hours (world market price adjustments are broken anyways...), reminder notification for route expiration shortened to 5 minutes before ending, expiration offer timer is unchanged at 2 minutes before expiration.
   - Increase the storage capacity (999) and production rate (1/min) of all rare resource generators (Sector Quest rewards)

4. ## Changes to the base game including Tundra and Frontiers DLC
   - Exchanged Drink and Food need position in the UI for Worker tier to match the new setup for Operators.
   - Changed Construction costs and build time for all Monumental Bridges:

    |Bridge No.|Build Time|Build Cost|Finalization Cost|
    |---|---|---|---|
    |<div align=center>1</div>|10 minutes|25t/min Superalloys <br> 750 workforce|150000 credits <br> 100 Graphene|
    |<div align=center>2</div>|20 minutes|50t/min Superalloys <br> 1500 workforce|300000 credits <br> 125 Graphene|
   
   - Lowered the required balance for the very last quest of the sector project in Walbruck Basin from +50k to +25k as the original one was quite hard to achieve in higher difficulty runs before having >150k Investors.
   - <details>
     <summary>Overhauled effects and build costs of Secondary Modules.</summary>

      - removed the logistics module as it is quite useless.
      - added the Finance Calculator known from energy buildings to all productions, reducing credit maintenance.
      - replaced the logistics module of energy buildings with a new Accumulator Unit, increasing the productivity by 15% each.
      - adjusted build costs: every module now uses the region's rare resource (energy module uses Iridium). Workforce modules now cost SmartDrones, Energy modules cost Fusion Power Cells and Credit modules cost Quantum Computers.
      - adjusted effect strength: normal versions now reduce maintenance by -10%. Special once from voting or the dominance mode -15%.
     </details>
   - VR Generators and SuperCoolants have been moved from being a Biotech product to Electronics.
   - Changed balancing of credit maintenance and income across the three difficulty settings to reflect the immensely higher maintenance costs of new products and production chains:
     <details>
      <summary>Revenue multiplier</summary>

      - Plenty: 1.5 (unchanged)
      - Medium: 1.375 (was 1.25)
      - Sparse: 1.25 (was 1.00)
     </details>
     <details>
      <summary>Tax generation of each population level</summary>

      - Workers: 64 (unchanged)
      - Operators: 220 (was 192)
      - Executives: 1680 (was 896)
      - Investors: 5640 (was 3760)
      - Protectors: 48 (unchanged)
      - Scientists: 317 (was 276)
      - Geniuses: 2024 (new)
      - Miners: 64 (was 36)
      - Officers: 317 (was 164)
      - Tundra Ecologists: 48 (unchanged)
      - Tundra Field Researchers: 317 (was 276)
     </details>

   - Changed balancing of workforce generation to reflect the higher maintenance costs of new and overhauled factories:
     <details>
      <summary>Workforce generation of each population level (Plenty/Medium/Sparse)</summary>

      - Workers: 20/20/16 (unchanged)
      - Operators: 60/50/40 (was 70/40/32)
      - Executives: 145/135/125 (was 175/80/64)
      - Investors: 305/265/225 (was 438/160/128)
      - Synthetics: 576/480/384 (was 384/320/256)
      - Protectors: 20/20/16 (was 15/20/16)
      - Scientists: 50/40/35 (was 50/40/32)
      - Geniuses: 250/200/150 (new)
      - Miners: 20/20/16 (unchanged)
      - Officers: 50/40/32 (unchanged)
      - Tundra Ecologists: 28/26/24 (was 20/20/16)
      - Tundra Field Researchers: 56/52/48 (was 50/40/32)
     </details>

   - Changed balancing for product consumption by residents to better take into account the more complex production chains and modified outputs of certain factories:
     <details>
      <summary>Consumption multiplier</summary>

      - Sparse: 1.00 (unchanged)
      - Medium: 1.25 (was 1.50)
      - Plenty: 1.5 (was 2.00)
     </details>

   - Changed consumption values of many needs for all population levels (haven't fully figured out how the actual consumption is calculated from the values in population_balancing.xml, use the ingame statistics menu)
   - Removed "Trade Route Administration Cost" (in vanilla each trade route costs additional money, it was increased by 250 per route, cap was 10k with 4 free routes to start with)
   - Adjusted several unlock triggers to fit with the new progression of the Main Quest, new buildings and Arctic Tier 3 population:
     <details>
      <summary>Changes:</summary>

      - Vegetable Farm, Organic Food Factory, Fine Food Manufactory are unlocked with 1000 Operators
      - Sustenance Packs Factory Earth unlocks with 5000 Executives
      - Energy Transmitter Spaceport Earth/Moon needs at least 1 Genius
      - Energy Transmitter Spaceport Arctic needs at least 5000 Geniuses
      - Switched unlock conditions for Desalination Plant and Rice Farm
      - New Triggers to unlock the five special production buildings via Research in the Technology Nexus: Aeroponic Farms and Water Filter Moon; AI Assembly Hall Moon; Fusion Reactor; Gas Rig Tundra, Gas Refinery Arctic, Gas Power Plants in Arctic and Tundra; Water Pump Tundra
      - changed unlock condition of Rejuvenator Chain to 1750 Operators
      - changed the unlock condition of the Transmission Spaceport on Moon to 5000 Officers and 2500 Geniuses
      - changed unlock condition of the Diamond Mine to 20000 Executives in order to make supply of Quantum Computers possible at this stage
      - changed unlock conditions for Stadium to 99999 Investors
      - moved Quantum Computers to be unlocked with 1 Genius
      - moved Secrecy Lab to be unlocked with 5000 Geniuses
      - moved BioEnhancer production chain to be unlocked with 150 Officers
      - moved Fusion Power Cells production chain to be unlocked with 1000 Officers
      - Tundra region unlock has been moved to 1750 Operators to fit the new progress
      - Public Building 2 in Tundra (new Infodrome) has been changed to unlock at 5000 Field Researchers
      - Space Station unlock has been moved to after Spaceport Upgrade II (Moon unlock) to fit story
      - Ornaments from Frontiers DLC and FCP02 are unlocked with 1 Worker.
     </details>

   - Changed first steps of the Questline in Tundra Region to reflect changes in population needs and Technology Nexus. Added 10 Petrochemicals as a reward for settling the first Ecologists in Tundra to make upgrading the spaceport there possible without extra work.

   - Construction costs and time have been changed for all Tundra Pumps. They now require Aluminium, Superalloys, Titanium or Titanium Plating in addition to Construct-o-Bots. Times have been shortened to 3 Minutes each, but input requirements increased. Finalization costs have been altered to include Graphene, Petrochemicals or Magnetite for the first step. Maintenance costs for the second stage have been increased and include workforce now. Time has been shortened to 6 minutes. Finalization costs for the second stage have been changed to include credits and reduce demand on Petrochemicals.

   - Changed trade route vehicles in the Tundra to "normal" cargo ships from Temperate sectors. This reduces costs for trade route maintenance especially in the early game.

   - Overhauled the Main Questline of the game to reflect all changes and additions:
     <details>
     <summary>Changed Main Quests:</summary>

      - *"1. Work in Progress"*:
        - Exchanged goal to build a Rice Farm with goal to build a Desalinization Plant
      - *"2. Smooth Operation:"*
        - Exchanged goal to build a Desalinization Plant with goal to build a Rice Farm
        - Change goal to build an Infodrome to build a Community Center
      -  *"4. The Trade Blockade"*:
         - Added the option to skip the military quest like it is done in later quests by advancing one company level
         - Added 10 Graphene as a reward to complete the Space Port extension in case of pacifist route
      - *"8. A Place to Warm Up"*:
        - Exhanged the goal to supply Canned Food with the goal to supply Sustenance Packs
      - *"12. It's Rocket Science"*:
        - Add subgoal to establish a trade route for Nanoceramics to Arctic
      - *"14. Shared Responsibility"*:
        - Add subgoal to establish a trade route for Fish to Temperate
        - Add subgoal to produce Fine Food in Temperate
        - Add subgoal to enter Tundra region
        - Add subgoal to produce Hyaluronic Acid
        - Add subgoal to establish a trade route for Smart Drones to Temperate
      - *"23. Self Supporter"*:
        - Add subgoal to establish a trade route for Sustenance Packs to Moon
        - Add subgoal to upgrade Spaceport in Arctic to Orbital Spaceport
        - Add subgoal to establish a trade route for Rare Earth Elements to Arctic
        - Add subgoal to establish a trade route for VitaPills to Moon
        - Add subgoal to build a Maintenance Station on Moon
      - *"24. The Fusion Reactor"*:
        - Add subgoal to hire 3000 Officers on Moon
        - Add subgoal to hire 2500 Geniuses in Arctic
        - Add subgoal to research the required Technology "Fusion Reaction" in the Nexus
        - Remove the subgoal to upgrade Spaceport in Arctic to Orbital Spaceport
      - *"25. Starting Transmission"*:
        - Add subgoal to hire 5000 Moon Officers to unlock the Transmission Spaceport on Moon
        - Add subgoal to hire 25000 Investors on Earth
        - Add subgoal to establish a trade route for Flax Fibres from Tundra
        - Add subgoal to produce IntelliWear
        - Add subgoal to establish a trade route for BioEnhancers from Moon
        - Add subgoal to establish a trade route for Quantum Computers from Arctic
      - *"28. The Sixth Among Five"*:
        - Change subgoal to produce Quantum Computers with the goal to produce Neural Interfaces
     </details>

6. ## Overhauled Population Needs:
   Each Population tier requires the needs of its predecessor in addition to its own. Synthetics do not follow this logic however.

    | **Tier**|**Needs**||**Tier**|**Needs** |
    |---|---|---|---|---|
    |<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/ea56ef9a-c935-4fa9-9d8c-27391854b5a6" />|<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/4ccc4fd5-9f7b-45f8-bf36-2e0198fc67ea" height="32" /> **Water** <br> <img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/e259cd6e-9936-46d6-b2ee-0bccdd643c41" height="32" /> **Rice** <br> <img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/45358436-1dc8-4d88-8598-8f9e98fb4f3b" height="32" /> **Urbanisation** <br> <img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/886d132c-3945-47c7-ad3e-736aaa04b42f" height="32" /> **Services** <br> <img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/b9a4979e-bddd-452d-8003-00c15ecdb64b" height="32" /> **Energy**||<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/78ce0432-bc08-42cb-bd7d-5dd1f3ac03e1" />|<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/64bd8fdd-2675-4102-9e3e-d779847b2cbe" height="32" /> **Sustenance Packs** <br> <img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/dd943f29-8958-465f-9964-4318d0063f80" height="32" /> **Vitamin Drinks** <br> <img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/0a0a7bb2-e61f-4d70-b316-ce0d4dd4f624" height="32" /> **Neuro Implants** <br> <img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/45358436-1dc8-4d88-8598-8f9e98fb4f3b" height="32" /> **Urbanisation** <br> <img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/886d132c-3945-47c7-ad3e-736aaa04b42f" height="32" /> **Services**|
    |<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/428f93ee-53ba-47a3-86d1-14f8f9f632c7" />|<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/dd943f29-8958-465f-9964-4318d0063f80" height="32" /> **Vitamin Drinks** <br> <img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/8a1c6487-e183-40da-8f6a-d1a13b518057" height="32" /> **Fine Food** <br> <img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/0a0a7bb2-e61f-4d70-b316-ce0d4dd4f624" height="32" /> **Neuro Implants** <br> <img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/1f489b9e-96bf-4f65-bb5b-e38529c83a0b" height="32" /> **Rejuvenators** <br> <img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/886d132c-3945-47c7-ad3e-736aaa04b42f" height="32" /> **Services**||<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/4260cb9b-aed8-479d-8ad6-c00b90c73e4d" />|<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/2893cfae-de51-424d-87f4-4e4074efdc32" height="32" /> **VitaPills** <br> <img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/8a1c6487-e183-40da-8f6a-d1a13b518057" height="32" /> **Fine Food** <br> <img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/4825a138-9b5f-4dc4-a89f-e29166649cd7" height="32" /> **Smart Drones** <br> <img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/068e0a5d-e3ae-427c-8ef0-14d52038827c" height="32" /> **Thermal Shells** <br> <img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/886d132c-3945-47c7-ad3e-736aaa04b42f" height="32" /> **Services**|
    |<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/567eb810-4819-4553-afa5-0d1b3ab0d2b6" />|<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/dc92a25b-b9d5-43d5-a44a-83554d40e366" height="32" /> **Luxury Food** <br> <img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/a6c67014-c180-4172-99ba-2e7317e1775a" height="32" /> **IntelliWear** <br> <img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/c7c55f86-a704-46ab-a6b5-e4188662884c" height="32" /> **BioEnhancers** <br> <img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/b8836de1-eef8-43b8-aa78-c3611526b54c" height="32" /> **Quantum Computers** <br> <img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/886d132c-3945-47c7-ad3e-736aaa04b42f" height="32" /> **Services**||<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/1c6d784b-d733-4470-a5f4-4d3ee1a32d07" />|<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/b8836de1-eef8-43b8-aa78-c3611526b54c" height="32" /> **Quantum Computers** <br> <img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/4bc05992-1860-4668-ae47-bcb544c68390" height="32" /> **MediBots** <br> <img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/79cc638a-5721-442d-b185-018dfa367d0a" height="32" /> **Androids** <br> <img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/a43f53f1-2240-4cdd-9021-1f56ec3bb856" height="32" /> **Neural Interfaces** <br> <img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/886d132c-3945-47c7-ad3e-736aaa04b42f" height="32" /> **Services**|
    |<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/1d74990c-f33f-47b7-895f-39f20d717047" />|<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/233a4ffc-a7d8-40dd-b0de-c68065025e19" height="32" /> **Replicators** <br> <img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/79cc638a-5721-442d-b185-018dfa367d0a" height="32" /> **Androids** <br> <img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/c5cf1c0e-83fa-43dc-8ec2-d3536fe6c77e" height="32" /> **Anti-Grav Compensators** <br> <img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/a43f53f1-2240-4cdd-9021-1f56ec3bb856" height="32" /> **Neural Interfaces** <br> <img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/886d132c-3945-47c7-ad3e-736aaa04b42f" height="32" /> **Services**||
    |<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/e91aaec8-5d06-4df1-bc61-5fa63a6237a8" />|<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/a6c67014-c180-4172-99ba-2e7317e1775a" height="32" /> **IntelliWear** <br> <img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/c7c55f86-a704-46ab-a6b5-e4188662884c" height="32" /> **BioEnhancers** <br> <img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/a43f53f1-2240-4cdd-9021-1f56ec3bb856" height="32" /> **Neural Interfaces** <br> <img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/7ffb8c0b-692b-40e0-8104-e639f3a4678e" height="32" /> **Maintenance** <br> <img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/b9a4979e-bddd-452d-8003-00c15ecdb64b" height="32" /> **Energy**|
    |||||
    |<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/67d7e936-69a5-4212-b726-d0846763a8fd" />|<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/28251618-1c80-4f4f-b59e-03694aa07388" height="32" /> **Oxygen** <br> <img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/64bd8fdd-2675-4102-9e3e-d779847b2cbe" height="32" /> **Sustenance Packs** <br> <img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/1f489b9e-96bf-4f65-bb5b-e38529c83a0b" height="32" /> **Rejuvenators** <br> <img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/2893cfae-de51-424d-87f4-4e4074efdc32" height="32" /> **VitaPills** <br> <img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/45358436-1dc8-4d88-8598-8f9e98fb4f3b" height="32" /> **Urbanisation** <br> <img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/886d132c-3945-47c7-ad3e-736aaa04b42f" height="32" /> **Services**||<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/8a14a7ed-eaae-4cf7-bf8f-72cb993a76da" />|<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/dd943f29-8958-465f-9964-4318d0063f80" height="32" /> **Vitamin Drinks** <br> <img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/8a1c6487-e183-40da-8f6a-d1a13b518057" height="32" /> **Fine Food** <br> <img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/4825a138-9b5f-4dc4-a89f-e29166649cd7" height="32" /> **Smart Drones** <br> <img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/45358436-1dc8-4d88-8598-8f9e98fb4f3b" height="32" /> **Urbanisation** <br> <img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/886d132c-3945-47c7-ad3e-736aaa04b42f" height="32" /> **Services**|
    |<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/386fccc2-cd15-45d2-a300-6721e7dea0ea" />|<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/dc92a25b-b9d5-43d5-a44a-83554d40e366" height="32" /> **Luxury Food** <br> <img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/c7c55f86-a704-46ab-a6b5-e4188662884c" height="32" /> **BioEnhancers** <br> <img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/a6c67014-c180-4172-99ba-2e7317e1775a" height="32" /> **IntelliWear** <br> <img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/c5cf1c0e-83fa-43dc-8ec2-d3536fe6c77e" height="32" /> **Anti-Grav Compensator** <br> <img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/886d132c-3945-47c7-ad3e-736aaa04b42f" height="32" /> **Services**||<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/ff88c227-c1c0-4eba-a07d-03f5cf54b878" />|<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/dc92a25b-b9d5-43d5-a44a-83554d40e366" height="32" /> **Luxury Food** <br> <img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/068e0a5d-e3ae-427c-8ef0-14d52038827c" height="32" /> **Thermal Shells** <br> <img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/4bc05992-1860-4668-ae47-bcb544c68390" height="32" /> **MediBots** <br> <img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/233a4ffc-a7d8-40dd-b0de-c68065025e19" height="32" /> **Replicators** <br> <img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/886d132c-3945-47c7-ad3e-736aaa04b42f" height="32" /> **Services**|

7. ## Overhauled and New Production Chains:
    - <details>
        <summary>Vitamin Drinks:</summary>

        ![productionchain_vitamindrinks](https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/effd5e0f-40ce-4b22-8a0e-1c3ddb6be543)

        Vitamin Drinks now require Algae, that is first processed into Nutrient Powder. It is a multi-region good, as all regions apart from the moon have an option to produce it from a different input:
          - Temperate: Algae
          - Arctic: Deep Water Corals
          - Tundra: Moss

        For the Vitamin Drinks Production, extra coastal slots are needed in the beginning, until we can branch off into the other regions.

        Here is an overview of this chain's modified buildings:
        ![vitamindrinks](https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/3fc43d9b-4b27-4404-9ff8-1db6d2498002)
      </details>

    - <details>
        <summary>Fine Food:</summary>

        ![productionchain_sushi](https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/6be5f9c8-6b49-4fce-a41c-5856dfed5a60)

        For this Chain, two completely new products are added for the mod: Fine Food aka Sushi and Organic Food, an intermediate product in its production chain. "Original" Organic Food was renamed to Rice and is the basic Food for Workers.

        The chain starts off very basic with Water, which is needed for the Greenhouse to grow Vegetables. Vegetables and Rice are now combined in a Rice Cooker into the first of the four unused products: Organic Food. Organic Food is now combined with Fish brought in flash frozen from your first Arctic sector into Sushi inside a Sushi Rolling Factory.

        Here is an overview of this chain's modified buildings:
        ![sushiroller](https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/6d7d949c-64f2-4b29-b5e7-421a9060dbe3)
      </details>

    - <details>
        <summary>Rejuvenators:</summary>

        ![productionchain_rejuvenators](https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/77b8ac87-034a-4c63-87db-15f6e9a8951d)

        This production chain requires opening up the Tundra region to get access to one of the input products. Synth Cells are unchanged. The new input for the Biomedical Laboratory is Hyaluronic Acid which can only be produced in the Tundra region from Moss.

        Here is an overview of this chain's modified buildings:
        ![rejuvenators4](https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/1929071c-5aac-4c00-a18c-ad3b85dc1823)
      </details>

    - <details>
        <summary>Neuro Implants:</summary>

        ![productionchain_neuroimplants](https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/8de1a98f-d98d-4028-a612-d7c989af258b)

        Molybdenum is unchanged. Nano-Ceramics have been introduced as a second input.
      </details>

    - <details>
        <summary>Luxury Food:</summary>

        ![productionchain_luxuryfood](https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/0b29151a-0717-47fc-ab8f-0c556cf6b072)

        Water was introduced as a second input for the Cattle Farm. Rest is unchanged.
      </details>

    - <details>
        <summary>IntelliWear:</summary>

        ![productionchain_intelliwear](https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/048b617d-821f-4c7d-bc6b-7d39360f5d8c)

        Bioresin is a new input product for Microchips. Alternatively Microchips can be produced from Tungsten in the Tundra. Flax has been moved to be produced exclusively in the Tundra region as well.

        Here is an overview of this chain's modified buildings:
        ![intelliwearedited](https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/95367c88-c949-4f29-a12a-c1ad2603ced8)
      </details>

    - <details>
        <summary>BioEnhancers:</summary>

        ![productionchain_bioenhancers](https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/45902d12-3c7a-43ea-b3f9-b48338c28a42)

        BioEnhancers have been changed to be way more complex than in the original game. Cybersynth Circuits are now required as well as Titanium instead of Rare Earth Elements. Until you research the technology to produce the Cybersynth Circuits on the Moon, you will need to import them from the Tundra. The AI Assembly Hall on the Moon uses Rare Earth Elements instead of Microchips to produce Cybersynth Circuits.

        Here is an overview of this chain's modified buildings:
        ![bioenhancer1](https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/18bcb264-0fc8-4ee9-ad7d-db947782c999)
      </details>

    - <details>
        <summary>Quantum Computers:</summary>

        ![productionchain_quantumpcs](https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/8ee1ca75-a7b5-4d56-a8e6-672a0e39ef49)

        Quantum Computers now require production of Superconductors. Those can be produced only in the Arctic and require SuperCoolants and Nano-Ceramics as an input. As Quantum Computers are now required at Executive tier, the Diamond Mine is unlocked earlier than before. To produce Quantum Computers you need at least 1 Genius in the Arctic.

        Here is an overview of this chain's modified buildings:
        ![quantumcomputers1](https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/82477e8d-c6b9-40f4-a9cf-df1251160490)
      </details>

    - <details>
        <summary>Anti-Grav Compensators:</summary>

        ![productionchain_gravitationcompensators](https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/c74148f1-bcf7-4fca-a881-1fbd4d4ffa30)

        Anti-Grav Compensators now require the input of Superconductors as well, which need to be imported from the Arctic to produce them.
      </details>

    - <details>
        <summary>Replicators:</summary>

        ![productionchain_replicators](https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/2509698f-bfad-4075-b2db-c6c303e83ab0)

        Replicators are pretty standard, only change is the requirement for Bioresin for Microchip production.
      </details>

    - <details>
        <summary>Androids:</summary>

        ![productionchain_androids](https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/bbbd4688-ea06-481f-bc14-74972d104243)

        Androids now require the changed Cybersynth Circuits as well. The other input used to be Synth Cells. But as those are already part of the Cybersynth Circuit chain, they are dropped in favour of Biopolymers.
      </details>

    - <details>
        <summary>Neural Interfaces:</summary>

        ![productionchain_neuralinterfaces](https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/baccd1e5-b30f-4e0a-ab76-557a4b23fd19)

        Neural Interfaces is a completely new product introduced with the mod. It is produced exclusively in the Arctic region and requires input of MultiSpec-Prisms and Superconductors. The chain is unlocked with Geniuses. It's production building is one of the most expensive in terms of credit-, workforce- and energy maintenance in the entire game. Neural Interfaces are also required by Geniuses and Synthetics.

        Here is an overview of this chain's modified buildings:
        ![arctic neuralinterfaces](https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/7f53c96e-3137-46cb-bf3d-237e5630eb96)
      </details>

    - <details>
        <summary>Sustenance Packs:</summary>

        ![productionchain_sustenancepacksarctic](https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/b1dfcfc7-278f-45e8-b253-ad3f35433760)

        Sustenance Packs essentially is the reworked Canned Food product from Arctic. Aluminum was added as an additional input. Sustenance Packs can also be produced on Earth from Manager Tier onwarfs to supply your first Moon Colony more easily. Here the chain uses Organic Food and Aluminum:

        ![productionchain_sustenancepacksearth](https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/4ee18294-21dd-4803-b336-f0227ade0174)

        The same is true for the Moon version of this chain. With Officers and the Aeroponic Farming tech from the Nexus you get the opportunity to prodce them on the Moon as well.
      </details>

    - <details>
        <summary>VitaPills:</summary>

        ![productionchain_vitapills](https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/6dcdb1ed-cffa-42cd-914c-fa6cc5eaaa0e)

        Renamed Stimulants with a new icon. Instead of only using Corals, those need to be processed into Nutrient Powder first. As a second input Rare Earth Elements are necessary. Those need to be shipped from the Moon.

        Here is an overview of this chain's modified buildings:
        ![vitapills1](https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/08bf19de-b36a-4344-abdf-71c4df62a647)
      </details>

    - <details>
        <summary>Smart Drones:</summary>

        ![productionchain_laboratoryequipment](https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/4f9b691f-7dcd-45e8-a5d7-de4a3f5abb76)

        Smart Drones are a new need of the Scientists in the Arctic. They can only be produced in the Tundra. As I recycled the Nanometre Processors into another good, they now require Microchips instead. Those can be produced from Tungsten in the Tundra just like the Nanometre Processors used to be.

        Here is an overview of this chain's modified buildings:
        ![tundramicrochips](https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/76c7d4d4-a1ec-4f3a-9ed3-c54473f0dcac)
      </details>

    - <details>
        <summary>Thermal Shells:</summary>

        ![productionchain_thermalshells](https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/4ac2521c-8b15-47b2-9a4f-65ea97faea70)

        Thermal Shells are a new clothing need for Scientists, Geniuses and Field Researchers. They are similar to IntelliWear, but require Fusion Power Cells from the Moon instead of Microchips. The new product can be produced in Arctic (requiring importing flax as well) and in Tundra regions.

        Here is an overview of this chain's modified buildings:
        ![tundraborealtailor](https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/0c2f0126-22f1-4fe9-b158-da6bbc181362)
        ![arctictailor](https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/0cf916b7-f8d0-45c4-8bfe-91586a35227f)
      </details>

    - <details>
        <summary>Oxygen:</summary>

        ![productionchain_oxygen](https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/5dfcd2f0-92dd-4f16-a143-573c129b386a)

        Oxygen production now requires Aluminum from the new Moon Aluminum Mine as well.
      </details>

8.  ## Overhauled Public Buildings
    - Services are a newly introduced product that can only be produced by Public Buildings. I created them to overhaul and diversify the 2205 Public Building game mechanic.
    - Public buildings now take 4t/min of varying input goods to produce Services. In addition, Urbanisiation is provided passively. This product uses the "regular" 2205 Public Building mechanic.
    - The Cooporation HQ is now limited to one per sector
      - <details>
        <summary> Expand to find out more about the changed public buildings:</summary>

        | **Name**|**Region**|**Input**|**Output Services**|**Output Urbanisation** |
        |---|---|---|---|---|
        |<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/2cd3b2b4-20c3-4468-b951-17811b407df2" height="16" /> Community Center|Earth|nothing|10|10|
        |<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/5bbbfd4e-15da-4d6f-9c92-c1bd2fec1e70" height="16" /> Police Station|Earth| <img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/4825a138-9b5f-4dc4-a89f-e29166649cd7" height="16" /> Smart Drones|25|20|
        |<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/621f6067-7f8d-4f09-bd2c-18987f86ec73" height="16" /> Metro Station|Earth|<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/83ccc971-925b-424e-9d56-9e3227dba755" height="16" /> Superconductors|30|75|
        |<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/626c9fa6-2c6d-41c2-85c9-793bc98d16c4" height="16" /> Infodrome|Earth|<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/b8836de1-eef8-43b8-aa78-c3611526b54c" height="16" /> Quantum Computers|75|30|
        |<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/04de96b3-3677-46c7-9649-e707972ba55b" height="16" /> Stadium|Earth|<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/79cc638a-5721-442d-b185-018dfa367d0a" height="16" /> Androids & <img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/3600b9f4-ba69-4125-8fcc-9e06e4fe4ef4" height="16" /> Fusion Power Cells|150|50|
        |<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/07890501-e687-46c5-99aa-e2080fd7bc82" height="16" /> Maintenance Station|Earth|<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/6686c3cb-dc53-46e4-95be-e31ee5c4048f" height="16" /> Construct-o-Bots & <img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/61b96781-c813-4462-a023-39c9383107ff" height="16" /> Cybersynth Circuits|80|20 Maintenance (Synths)|
        |<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/bd21fce4-060a-4366-8ed8-cf10b74ceaf1" height="16" /> Corporation Headquarter|Earth|nothing|250|100|
        ||||||
        |<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/2cd3b2b4-20c3-4468-b951-17811b407df2" height="16" /> Community Center|Arctic|nothing|2,5|5|
        |<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/7907ee71-4c39-403e-b9f2-71166fb4cf7d" height="16" /> Health Center|Arctic|<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/1f489b9e-96bf-4f65-bb5b-e38529c83a0b" height="16" /> Rejuvenators|10|10|
        |<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/626c9fa6-2c6d-41c2-85c9-793bc98d16c4" height="16" /> Infodrome|Arctic|<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/d5855466-6bbe-41dd-a678-73f7e4bbfeb7" height="16" /> Microchips|20|20|
        |<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/e13612c8-9552-4346-8771-17528ff25f09" height="16" /> Secrecy Lab|Arctic|<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/4825a138-9b5f-4dc4-a89f-e29166649cd7" height="16" /> SmartDrones & <img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/c5cf1c0e-83fa-43dc-8ec2-d3536fe6c77e" height="16" /> Anti-Gravity Compensators|40|40|
        ||||||
        |<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/07890501-e687-46c5-99aa-e2080fd7bc82" height="16" /> Maintenance Station|Moon|<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/6686c3cb-dc53-46e4-95be-e31ee5c4048f" height="16" /> Construct-o-Bots|10|10|
        |<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/7907ee71-4c39-403e-b9f2-71166fb4cf7d" height="16" /> Health Center|Moon|<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/4bc05992-1860-4668-ae47-bcb544c68390" height="16" /> MediBots|20|15|
        ||||||
        |<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/7907ee71-4c39-403e-b9f2-71166fb4cf7d" height="16" /> Health Center|Tundra|<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/1f489b9e-96bf-4f65-bb5b-e38529c83a0b" height="16" /> Rejuvenators|10|5|
        |<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/626c9fa6-2c6d-41c2-85c9-793bc98d16c4" height="16" /> Infodrome|Tundra|<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/b8836de1-eef8-43b8-aa78-c3611526b54c" height="16" /> Quantum Computers|20|10|
        ||||||
        |<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/07890501-e687-46c5-99aa-e2080fd7bc82" height="16" /> Maintenance Station|Mars|<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/6686c3cb-dc53-46e4-95be-e31ee5c4048f" height="16" /> Construct-o-Bots & <img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/61b96781-c813-4462-a023-39c9383107ff" height="16" /> Cybersynth Circuits|40|20 Maintenance (Synths)|
        </details>

9.  ## Other Overhauled Buildings from Vanilla Game:
    - Residences on Earth now cost credits to upgrade (normal/complex): upgrade to Operator 5/10, upgrade to Executive 25/100, upgrade to Investor 250/1000, upgrade to Synth 10000 (building material cost changed to 10 Biopolymers, 6 Construct-o-Bots, 10 Superalloys, 8 Fusion Power Cells, 8 Androids, 10 Iridium, 5 of each rare resource)
    - Residences in the Arctic now cost credits to upgrade: upgrade to Scientist 250, upgrade to Genius 1000
    - Windparks produce base 125 Energy (was 50), making them more competitive in later stages of the game
    - Desalination Plant: Changed Output from 5t/min to 8t/min
    - Output of Feldspar and Cobalt Mines changed to 10 t/min (was 5 t/min)
    - Corporation headquarter can now support 50 modules (was 30)
    - Corporation headquarter modules changed Maintenance modifier to +10% (was +5%). Output modifier is now +5% for Services and +10 Urbanisation
    - Added Superalloy build material costs to all buildings in the Arctic from Scientists onwards
    - Output of Aluminum Mine changed to 10 t/min (was 6 t/min)
    - Subzero Cleanroom: Changed Module boost from +100% to +150%
    - Added Construct-o-Bot build material costs to all buildings on the Moon from unlocking the interorbital spaceport
    - Adjusted build material and credits costs for many Moon buildings
    - Farms will no longer require Biocatalyst for their Tundra Module but Rare Earth Elements
    - Tundra modules now cost 10 rare resources
    - Residences in the Tundra now cost credits to upgrade: upgrade to Field Researcher 250
    - Added Construct-o-Bots to more of the Tundra buildings
    - Output of the Moss Plantation changed to 6 t/min (was 4 t/min)
    - Added Tundra modules to Advanced Bioreactor (requires Rare Earth Elements) and Ionization Chamber (requires Oxygen)
    - Changed Desalination Plant in Tundra from coastal building to land based Water Pump (Research required to unlock)
    - Changed Gas Drilling Rig from land based building to coastal (Research required to unlock)
    - Output of Vitamin Extractor in Tundra changed to 16 t/min (was 12 t/min), input for Water changed to 8 t/min (was 1t/min)

10. ## Changes to Orbit DLC
   - Changed starting permit count for Orbital Station to 1 workshop, 4 modules and 8 connectors (was 2/8/16) for changes in Techtree and Mars additions.
   - Add Urbanisation to all Astronaut Training Centers
   - Changed required population of Arctic Astronaut trainings camp for 100% productivity from 500 to 2500
   - Changed required population of Moon and Tundra Astronaut trainings camp for 100% productivity from 500 to 1000
   - Unlocked a second unused graphic variant for the Radiator module
   - Changed base workshop Expertise production to 20 (was 10)
   - Changed modifiers for additional Expertise gain from modules and input goods for workshops (total increase 900% up to 200 Expertise). Re-weighted the distribution of modifiers from 3,5:1 modules:goods to 2:1 modules:goods.
   - Changed necessary amount of modules for all workshop
   - Changed Standard Temperature and Optimal Temperature for some workshops
     - <details>
        <summary> Expand to find out more about the new values:</summary>

        |**Icon**| **Module**|**Modifier**||**Icon**|**Good**|**t/min**|**Modifier** |
        |---|---|---|---|---|---|---|---|
        |||||||||
        |<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/ef758bd7-0dd2-47eb-9512-ae684943a0d0" height="32" />|***Agriculture***||||||||
        |<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/10196c8c-b66e-4eeb-9c02-b4d74adbccea" height="32" />| Artificial-G Lab|125%||<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/64bd8fdd-2675-4102-9e3e-d779847b2cbe" height="32" />|Sustenance Packs|5|60%|
        |<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/ae819604-dc32-4c62-aeb0-7c84ff46a9ee" height="32" />| Solar Cells|75%||<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/26031e29-c019-4d4f-90f8-ee6d1f2b6417" height="32" />|Corals|5|120%|
        |<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/27870b77-a9b9-4ab6-9823-8d7cfb7bd772" height="32" />| Greenhouse|400%||<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/78d4d69c-5a49-4ea9-9643-50b754666d88" height="32" />|Nutrient Powder|10|120%|
        |||||||||
        |<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/f8ce0f80-f79d-42e6-b0bc-cb9cbe92c52c" height="32" />|***Biotech***|||||||
        |<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/10196c8c-b66e-4eeb-9c02-b4d74adbccea" height="32" />| Artificial-G Lab|375%||<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/64bd8fdd-2675-4102-9e3e-d779847b2cbe" height="32" />|Sustenance Packs|5|60%|
        |<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/ae819604-dc32-4c62-aeb0-7c84ff46a9ee" height="32" />| Solar Cells|150%||<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/df42a000-25c3-49e7-9471-fac0dc32325b" height="32" />|Cybersynth Circuits|5|120%|
        |<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/27870b77-a9b9-4ab6-9823-8d7cfb7bd772" height="32" />| Greenhouse|75%||<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/e5c5c32b-5074-4a77-b6c4-e99d96267594" height="32" />|Hyaluronic Acid|10|120%|
        |||||||||
        |<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/910c9145-a06d-43b5-bf0a-59e3f7991af0" height="32" />|***Electronics***||||||
        |<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/ae819604-dc32-4c62-aeb0-7c84ff46a9ee" height="32" />| Solar Cells|250%||<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/64bd8fdd-2675-4102-9e3e-d779847b2cbe" height="32" />|Sustenance Packs|5|60%|
        |<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/03f8ae22-f305-48e8-bcbc-932cf44e0202" height="32" />| Storage Platform|100%||<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/d5855466-6bbe-41dd-a678-73f7e4bbfeb7" height="32" />|Microchips|10|120%|
        |<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/8b208cd5-69a2-4c62-89ca-6556ac2b1c2f" height="32" />| Recycling Module|250%||<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/70f52ce3-b540-44e1-bc59-3b08996afb27" height="32" />|Qubit Processors|5|120%|
        |||||||||
        |<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/4146020f-57de-453d-ad3f-629cd62f9614" height="32" />|***Energy***|||||||
        |<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/10196c8c-b66e-4eeb-9c02-b4d74adbccea" height="32" />| Artificial-G Lab|75%||<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/64bd8fdd-2675-4102-9e3e-d779847b2cbe" height="32" />|Sustenance Packs|5|60%|
        |<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/ae819604-dc32-4c62-aeb0-7c84ff46a9ee" height="32" />| Solar Cells|450%||<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/f21dab2e-11b6-430f-9922-5d48b74f94b6" height="32" />|Fusion Power Cells|5|120%|
        |<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/03f8ae22-f305-48e8-bcbc-932cf44e0202" height="32" />| Storage Platform|75%||<img src="!https://github.com/Taludas/Anno2205-NewFrontiers/assets/64583643/2add03e8-036e-4d71-b5cb-0550602485b3" height="32" />|Aerogel|5|120%|
        |||||||||
        |<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/a3462631-7d4f-4022-97b6-1f84dae024ee" height="32" />|***Heavy Industries***|||||||
        |<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/ae819604-dc32-4c62-aeb0-7c84ff46a9ee" height="32" />| Solar Cells|75%||<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/64bd8fdd-2675-4102-9e3e-d779847b2cbe" height="32" />|Sustenance Packs|5|60%|
        |<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/03f8ae22-f305-48e8-bcbc-932cf44e0202" height="32" />| Storage Platform|300%||<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/b37f1cd1-a1cb-41d6-b066-ae134cba906a" height="32" />|Natural Gas|10|120%|
        |<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/8b208cd5-69a2-4c62-89ca-6556ac2b1c2f" height="32" />| Recycling Module|225%||<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/96ca1b11-0910-4d9c-b175-dc521afec1ad" height="32" />|Rare Earth Elements|10|120%|
        </details>

   - Orbit modules now produce additional Expertise in exchange for various input goods. They require 2 additional Astronauts to operate. The Buff towards the main workshop is not dependent on the supply of the module with the requested product. The heat value of the modules do not affect their Expertise production.
      |**Icon**|**Module**|**Icon**|**Input**|**t/min**|**Expertise Output**|
      |---|---|---|---|---|---|
      |<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/10196c8c-b66e-4eeb-9c02-b4d74adbccea" height="32" />|Artificial-G Lab|<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/c5cf1c0e-83fa-43dc-8ec2-d3536fe6c77e" height="32" />|Anti-G-Compensator|<div align=center>1<div>|<div align=center>10<div>|
      |<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/ae819604-dc32-4c62-aeb0-7c84ff46a9ee" height="32" />|Solar Cells|<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/83ccc971-925b-424e-9d56-9e3227dba755" height="32" />|Superconductors|<div align=center>1<div>|<div align=center>5<div>|
      |<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/27870b77-a9b9-4ab6-9823-8d7cfb7bd772" height="32" />|Greenhouse|<img src="https://github.com/Taludas/Anno2205-NewFrontiers/assets/64583643/6157b6bc-1717-442d-ae06-b18458d7c601" height="32" />|Biocatalyst|<div align=center>1<div>|<div align=center>10<div>|
      |<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/03f8ae22-f305-48e8-bcbc-932cf44e0202" height="32" />|Storage Platform|<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/4825a138-9b5f-4dc4-a89f-e29166649cd7" height="32" />|Smart Drones|<div align=center>1<div>|<div align=center>5<div>|
      |<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/8b208cd5-69a2-4c62-89ca-6556ac2b1c2f" height="32" />|Recycling Module|<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/233a4ffc-a7d8-40dd-b0de-c68065025e19" height="32" />|Replicators|<div align=center>1<div>|<div align=center>10<div>|
      |<img src="https://github.com/Taludas/Anno2205-NewFrontiers/assets/64583643/9c071e80-b44e-47e8-b8f1-960b1055cdd6" height="32" />|Radiator|<img src="https://github.com/Taludas/Anno2205-NewFrontiers/assets/64583643/2cba5191-3434-41b7-8744-0b026f793929" height="32" />|Supercoolants|<div align=center>1<div>|<div align=center>5<div>|
   - Total possible workshop count is now 25 after completing all 14 quests for the Martian Research Program
   - Expertise Cost for all Techs have been increased. See the table below for details:

        | ***Tech Tier***|1|2|3|4|5|
        |---|---|---|---|---|---|
        |***Cost***|100|150|200|250|500|

   - Total cost for activating all 55 Techs is 12000 Expertise
   - Total possible Expertise gain is now 6250 from workshops plus the amount you generate on Mars (only limited by building space and goods input)
   - All Technologies have been reworked:
        ![orbital_new_nexus](https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/f458afdc-c8de-4a05-aa5a-711a9fb5c932)

        - <details>
          <summary> Expand for detailed changes about Orbit Technologies:</summary>

          - Special buildings are now locked behind research of Tier 3 technologies in the interconnecting tree of each branch.

          - Example: The AI Assembly Hall, which produces Cybersynth Circuits, is initially locked on the Moon, even though you need it to produce BioEnhancers for your Executives. For now, you will have to rely on the more expensive AI Assembly Hall in the Tundra Region and ship them to the Moon for processing. However, by researching the level 3 tech of the linking tree between the standard Biotech and Electronics techs, you can unlock this building on the Moon, greatly simplifying the production chain. If you also research Aeroponic Farming on the Moon, you can produce all the inputs for the Cybersynth circuits on the Moon, drastically reducing the logistical costs involved in producing BioEnhancers.
          - All permanent research technologies from the interconnecting trees:

          ||**Agriculture-Biotech**|**Biotech-Electronics**|**Electronics-Energy**|**Energy-Heavy Industry**|**Heavy Industry-Agriculture** |
          |---|---|---|---|---|---|
          |1|**Workshop Expansion** <br> +2 workshops <br> +8 modules <br> +16 connectors|**Shield Reinforcement** <br> +1 shield radius|**Workshop Expansion** <br> +2 workshops <br> +8 modules <br> +16 connectors|**Shield Reinforcement** <br> +1 shield radius|**Workshop Expansion** <br> +2 workshops <br> +8 modules <br> +16 connectors|
          |2|**Shield Reinforcement** <br> +1 shield radius|**Workshop Expansion** <br> +2 workshops <br> +8 modules <br> +16 connectors|**Shield Reinforcement** <br> +1 shield radius|**Workshop Expansion** <br> +2 workshops <br> +8 modules <br> +16 connectors|**Shield Reinforcement** <br> +1 shield radius|
          |3|**Aeroponic Farming** <br> Unlocks Aeroponic Farms on the Moon|**Advanced AI Computing** <br> Unlocks AI Assembly Hall on Moon|**Fusion Energy** <br> Unlocks Fusion Reactor|**Gas Cracking** <br> Unlocks Gas Power Plants in Arctic and Tundra|**Well Drilling** <br> Unlocks Water Pump in Tundra
          |4|**Mars Mission Preparation** <br> +1 rocket engine for Mars Mission|**Workshop Expansion** <br> +4 modules <br> +8 connectors|**Mars Mission Preparation** <br> +1 rocket engine for Mars Mission|**Workshop Expansion** <br> +4 modules <br> +8 connectors|**Mars Mission Preparation** <br> +1 rocket engine for Mars Mission|
          |5|**Workshop Expansion** <br> +4 modules <br> +8 connectors|**Mars Mission Preparation** <br> +1 rocket engine for Mars Mission|**Workshop Expansion** <br> +4 modules <br> +8 connectors|**Mars Mission Preparation** <br> +1 rocket engine for Mars Mission|**Workshop Expansion** <br> +4 modules <br> +8 connectors|

          - All research technologies from the normal trees:

          ||<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/ef758bd7-0dd2-47eb-9512-ae684943a0d0" height="32" /> **Agriculture**|<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/f8ce0f80-f79d-42e6-b0bc-cb9cbe92c52c" height="32" /> **Biotech**|<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/910c9145-a06d-43b5-bf0a-59e3f7991af0" height="32" /> **Electronics**|<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/4146020f-57de-453d-ad3f-629cd62f9614" height="32" /> **Energy**|<img src="https://github.com/Taludas/Anno-2205-New-Frontiers-Mod/assets/64583643/a3462631-7d4f-4022-97b6-1f84dae024ee" height="32" /> **Heavy Industry** |
          |---|---|---|---|---|---|
          |1|***Mutation Optimizer*** <br> +10% increased productivity in agricultural facilities|***Personalized Medicine*** <br> +10% increase productivity in biotech facilities|**Self-Testing Hardware** <br> +10% increased productivity of electronic facilities|***Accumulator Overload*** <br> +10% increase productivity in energy facilities|***Mineral Cultivation*** <br> +10% increase productivity in heavy industry facilities|
          |||||||
          |2|***Parfums de terroir*** <br> Fruit Plantations also produce Wine|***Artificial Tissue Cultivation*** <br> Synth Cell Incubators also produce Meat|***Drone Reprogramming*** <br> Drone Hives also produce Construct-o-Bots|***Hypercharged Superconductors*** <br> Superconductor Fabrication Hall also produce Fusion Power Cells|***Phyllosilicates*** <br> Silicon Mines also produce Nano Ceramics|
          |2|***Dual Filtration Process*** <br> Desalination Plants also produce Algae. Water Pumps also produce Moss.|***Spare Parts Doctrine*** <br> Neuro-Module Factory also produce Cybersynth Circuits|***Anti-G Accessory*** <br> Anti-G Workshops additionally produce IntelliWear|***Liquid Extraction*** <br> Methane Extractors also produce Deuterium|***Aluminum Separation*** <br> Molybdenum Mines also produce Aluminum|
          |2|***Rescue System*** <br> Support Fleet now calls John Rafferty for help instead|***Meteor-grade Shields*** <br> Radius of the Kinetic Shield increases by +100% and fuel costs are reduced by 2|***Damage Detection*** <br> Radius of Repair Drone increases by +100% and fuel cost are reduced by 2|***Orbital Laser*** <br> Missile Barrages fires from Satellite Artillery instead|***Staggered Detonation Pattern*** <br> Damage and repulsion of Wave Mines increases by +100% and fuel costs are reduced by 1|
          |||||||
          |3|***Shrinkflation*** <br> Food Processors require -20% input goods|***Autocatalysis*** <br> +25% Increased productivity in Advanced Bioreactors|***Rapid Digitalisation*** <br> +10% Increased Need for Quantum Computers and Neural Interfaces across all pops. +5% Energy Maintenance in all Facilities. -20% Workforce Maintenance in all Facilities|***Efficient Transformers*** <br> -15% Energy Maintenance in all Facilities|***Construction Sector Subsidisation*** <br> +25% Productivity in all building material industries|
          |3|***Individual Crop Tracking*** <br> Farms can support +2 main modules|***DNA Recombineering*** <br> -20% Input Goods needed in all biotech facilities|***Rapid Prototyping*** <br> -20% Input Goods needed in all electronics facilities|***Turbine Optimisation*** <br> -20% Input Goods needed in all energy facilities|***Semi-autonomous Machinery*** <br> -15% Workforce Maintenance in heavy industry facilities|
          |3|***Sensor Overclocking*** <br> +100% increased resource salvaging in Crisis Sectors|***Petrochemicals Reprocessing*** <br> Obtain 10 Petrochemicals per minute|***Graphene Reprocessing*** <br> Obtain 11 Graphene units per minute|***Iridium Reprocessing*** <br> Obtain 15 Iridium units per minute|***Magnetite Reprocessing*** <br> Obtain 6 Magnetite units per minute|
          |||||||
          |4|***Sustainable Packaging*** <br> Sustenance Pack Producers use Biopolymers instead of Aluminum|***Rejuvenation Program*** <br> Ionization Chambers use Hyaluronic Acid instead of Cobalt <br> +25% Productivity <br> -10% Workforce Maintenance |***Slow Methane Fermentation*** <br> Boreal and Arctic Tailors use Natural Gas instead of Fusion Power Cells|***Biogas*** <br> Gas Power Plants use Soy Beans instead of Natural Gas and Fossil-fuel Power Plants use Moss instead of Natural Gas|***Semiconductor Doping*** <br> Microfabrication Halls use Rare Earth Elements instead of Bioresins <br> +25% Productivity in Microfabrication Halls|
          |4|***Fishing Quotas*** <br>Fine Food Kitchens use Soy Beans instead of Fish.|***Phytopharmacy*** <br> Biomedical Laboratories use Fruits instead of Synthcells|***Hardware Optimization*** <br> Hardware Fabrication Plants use Fusion Power Cells instead of Superconductors|***Liquid Extraction*** <br> Fusion Preparation Plants use Moon Ice instead of Deuterium|***Cobalt Alloys*** <br> Nano-Cutting Units use Cobalt instead of Rare Earth Elements|
          |4|***Rewards Program*** <br> +15% Workforce increase <br> +5% Goods consumption in Arctic, Tundra and Lunar Regions|***Consumption Damper*** <br> -15% Decrease in Revenue <br> -5% Goods consumption <br> In Arctic, Tundra and Lunar Regions|***Consumer Electronics*** <br> +5% Increase in Revenue <br> -15% Workforce generation <br> In the Temperate Region <br> +25% Productivity in Consumer Electronic Facilities|***Daylight Saving Time*** <br> -25% Energy Maintenance in residences <br> -5% Workforce generation <br> In the Temperate Region|***Austerity Policy*** <br> -10% Goods consumption <br> -10% Workforce generation <br> In the Temperate Region|
          |||||||
          |5|***Dietary Supplement*** <br> -20% Reduced consumption of food goods in all populations <br> +5% Consumption of Vitamin Drinks and VitaPills|***Robotic Workforce*** <br> Androids in storage provide Workforce <br> -20% Reduced consumption of services in all populations <br> +5% Consumption of Androids and Medibots |***Control System Overclocking*** <br> +25% Increased productivity in all HighTech facilities <br> +50% Energy Maintenance in all HighTech facilities|***Kinetic Micro-Generator*** <br> All residents produce energy <br> -5% Decrease in Revenue|***Orbital Warehouses*** <br> A new, global storage for all construction materials is opened <br> All Astronaut Camps produce extra goods (Earth: Androids, Arctic/Tundra: Neural Interfaces, Moon: Bioenhancers)<br> +3 Logistic Maintenance for all production facilities|
        </details>

11. ## Overhauled Sector Traits
    - <details>
        <summary> Overhauled effects of most available Sector Traits. Also included some new ones and some of the ones Annothek created for his mod. Details as well as weight chance can be found in the table below.</summary>

        | ***Temperate Region*** |  |  |  |
        |---|---|---|---|
        | **Trait** | **Description** | **Effects** | **Weight** |
        | Cultivated Minerals | Mines provide a higher output in this sector. | All Mining Facilities Production Rate +10% | 15 |
        | Ocean Nourishment | Coastal Facilities provide a higher output in this sector. | All Coastal Facilities Production Rate +10% | 15 |
        | Terra Preta | Farms provide a higher output in this sector. | All Farms Production Rate +10% | 15 |
        | Trade Winds | Windparks are more effective in this sector. | Windpark Production Rate +20% | 10 |
        | Strong Currents | Tidal Power Stations are more effective in this sector. | Tidal Power Station Production Rate +20% | 10 |
        | Low Salinity | Desalinization Plants provide a higher output in this sector. | Desalinization Plant Production Rate +20% | 10 |
        | Deep Cobalt Deposits | Certain Mines provide a higher output in this sector. | Cobalt Mine Production Rate +20% | 5 |
        | Deep Feldspar Deposits | Certain Mines provide a higher output in this sector. | Feldspar Quarry Production Rate +20% | 5 |
        | Deep Silicium Deposits | Certain Mines provide a higher output in this sector. | Silicium Mine Production Rate +20% | 5 |
        | Deep Diamond Deposits | Certain Mines provide a higher output in this sector. | Diamond Mine Production Rate +20% | 5 |
        | Sun Exposure | Due to the high solar light efficiency, the yield of sunflower farms and solar panels in this sector is increased. | Sunflower Farm Production Rate +20% <br> Solar Panels Production Rate +20% | 10 |
        | Magma Chamber | Construct-o-Bot production is cheaper in this sector. | Robot Assembly Hall Input Amount -20% | 10 |
        | King Tides | Tidal Power Stations are more effective, but production in all other coastal facilities is impaired. | Tidal Power Station: Production Rate +30% <br> Desalinization Plant, Algae Farm: Production Rate -15% | 20 |
        | Compacted Soil | Production facilities need less logistics, but production in farms is impaired. | All Production Facilities: Logistic Maintenance -1 <br> All Farms: Production Rate -15% | 20 |
        | High Humidity | Farms yield higher gains, but energy usage for all electronics facilities increase. | All Farms: Energy Maintenance -30% <br> Electronics Buildings: Credit Maintenance +15% | 20 |
        | Flood Plain | Rice Farms employ the natural flooding, but Fruit Plantations suffer from it. | Rice Farm: Production Rate +30% <br> Fruit Plantation: Production Rate -15% | 20 |
        | Slate Terroir | Wine yields are increased, but mining facilities use more refinement steps. | Vineyard: Production Rate: +30% <br> All Mining Facilities: Energy Maintenance +15% | 20 |
        | Recreational Area | Public buildings can provide more services, but the output of heavy industry production facilities is legally restricted. | All Public Buildings: Production Rate +30% <br> All Heavy Industry Production Facilities: Production Rate -10% | 20 |
        | High Starch Rice Varieties | Health food production requires less input, but rice farms need more workforce. | Sushi Manufactory: -30% Input <br> Rice Farm: +50% workforce requirement | 20 |
        | High Protein Meat | Meat production is increased, but food design requires more energy to cut it down. | Cattle Farm: Production +30% <br> Food Design Workshop: Energy Maintenance +15% | 20 |
        | Climate Change | Farms provide a higher output in this sector, but because of regulations production in Heavy Industry facilities is impaired. | All Agricultural Buildings: Production Rate +30% <br> All Heavy Industries: Production Rate -15% | 20 |
        | Optimised Circuits | Energy facilities provide limited output, but Electronics facilities require less energy. | All Electronic Facilities: Energy Maintenance -30% <br> All Energy Facilities: -15% Output | 20 |
        | Cheap Wages | Cheap wages reduce the maintenance costs of all factories, but production is reduced in turn. | All Factories: Credit Maintenance -30% <br> All Factories: Production Rate -15% | 20 |
        | Fine Living | Employees need less Services, Urbanisation and Energy, but their productivity suffers from it. | All Residents: Need for Services, Urbanisation and Energy -30% <br> All Factories: Production Rate -15% | 20 |
        |||||
        | ***Tundra Region*** |  |  |  |
        | **Trait** | **Description** | **Effects** | **Weight** |
        | Cultivated Minerals | Mines provide a higher output in this sector. | All Mining Facilities Production Rate +10% | 15 |
        | Terra Preta | Farms provide a higher output in this sector. | All Farms Production Rate +10% | 15 |
        | Trade Winds | Windparks are more effective in this sector. | Windpark Production Rate +20% | 10 |
        | Sun Exposure | Due to the high solar light efficiency, the yield of sunflower farms and solar panels in this sector is increased. | Sunflower Farm Production Rate +20% <br> Solar Panels Production Rate +20% | 10 |
        | Deep Cobalt Deposits | Certain Mines provide a higher output in this sector. | Cobalt Mine Production Rate +20% | 5 |
        | Deep Feldspar Deposits | Certain Mines provide a higher output in this sector. | Feldspar Quarry Production Rate +20% | 5 |
        | Marsh Soil | Moss Farms provide a higher output, but all production facilities need more logistics. | Moss Plantation: Production Rate +30% <br> All Production Facilities: Logistic Maintenance +1 | 20 |
        | Unclean Waters | Due to the polluted input goods, the vitamin extractors require more water, but the algae farm can achieve a higher yield. | Algae Farm: Produktion Rate +30% <br> Vitamin Extractor: Input Goods +15% | 20 |
        | Föhn | Warm winds mean Thermal Shells need less lining, but Natural Gas containers hold less because of gas expansion. | Boreal Tailor: Input Demand -50% <br> Fossil-fuel Power Plant: Production Rate -15% | 20 |
        | Volatile Gas Pockets | Natural Gas resources are vast, but additional security measures slow down production in some facilities. | Drilling Rig: Production Rate +30% <br> All Mining Facilities: Production Rate -15% | 20 |
        | Gas-powered Vans | Gas yields are increased at the cost of greater logistics demand. | Drilling Rig: Production Rate +30% <br> All Production Facilities: Logistic Maintenance +1 | 20 |
        | Climate Change | Farms provide a higher output in this sector, but because of regulations production in Heavy Industry facilities is impaired. | All Agricultural Buildings: Production Rate +30% <br> All Heavy Industries: Production Rate -15% | 20 |
        | Optimised Circuits | Energy facilities provide limited output, but Electronics facilities require less energy. | All Electronic Facilities: Energy Maintenance -30% <br> All Energy Facilities: -15% Output | 20 |
        | Cheap Wages | Cheap wages reduce the maintenance costs of all factories, but production is reduced in turn. | All Factories: Credit Maintenance -30% <br> All Factories: Production Rate -15% | 20 |
        | Pristine Lands | Due to higher ground water levels, Water Pumps have higher yields, but all production facilities require more energy to keep their building's foundation dry. | Water Pumps: Production Rate +30% <br> All Factories: Energy Maintenance +15% | 20 |
        |||||
        | ***Arctic Region*** |  |  |  |
        | **Trait** | **Description** | **Effects** | **Weight** |
        | Cultivated Minerals | Mines provide a higher output in this sector. | All Mining Facilities Production Rate +10% | 15 |
        | Ocean Nourishment | Coastal Facilities provide a higher output in this sector. | All Coastal Facilities Production Rate +10% | 15 |
        | Deep Aluminum Deposits | Certain Mines provide a higher output in this sector. | Aluminum Mine Production Rate +20% | 5 |
        | Deep Molybdenum Deposits | Certain Mines provide a higher output in this sector. | Molybdenum Mine Production Rate +20% | 5 |
        | Hot Spot | Geothermal Turbines are more effective in this sector. | Geothermal Turbines Production Rate +20% | 10 |
        | Restored Reefs | Coral Farms provide a higher output in this sector. | Coral Farm Production Rate +20% | 10 |
        | Borate Minerals | Pharma Labs benefit from borate-containing minerals in the processed corals, but due to the borate impurities, Molybdenum Mines have reduced output. | Pharma Lab: Production Rate +30% <br> Molybdenum Mine Production Rate -15% | 20 |
        | Heavy Water | Deuterium Strainers have increased yields, but Fishing Harbors generate less output. | Deuterium Strainer: Production Rate +30% <br> Fishing Harbor: Production Rate -15% | 20 |
        | Tectonic Activity | Coral Farms and Fishing Harbors provide a higher output, but production in Aluminum and Molybdenum Mines is impaired. | Coral Farm, Fishing Harbor: Production Rate +30% <br> Aluminum Mine, Molybdenum Mine: Production Rate -15% | 20 |
        | Nature Reserve | Subzero Cleanrooms provide a higher output, but production in Methane Extractors is impaired. | Subzero Cleanroom: Production Rate +30% <br> Methane Extractor: Production Rate -15% | 20 |
        | Katabatic Winds | Energy facilities save on cooling, but logistics suffer from snow-covered roads. | All Electronic Facilities: Energy Maintenance -30% <br> All Production Facilities: Logistic Maintenance +2 | 20 |
        | Stratospheric Warming | The melting snow makes roads are easier to travel, but Neuro Implants experience a higher failure rate. | All Production Facilities: Logisitic Maintenance -3 <br> All Electronic Facilities: Production Rate -15% | 20 |
        | Deep Waters | Deuterium and methane yields are increased, but coral and fishing production is impaired. | Deuterium Strainer and Methane Extractor: Production Rate +30% <br> Coral and Fish Farm: Production Rate -15% | 20 |
        | Specialised Employees | Biotech facilities production is increased, but all facilities have higher maintenance. | All Biotech Productions: Production rate +30% <br> All Productions: Maintenance Cost +50% | 20 |
        | Optimised Circuits | Energy facilities provide limited output, but Electronics facilities require less energy. | All Electronic Facilities: Energy Maintenance -30% <br> All Energy Facilities: -15% Output | 20 |
        | Cheap Wages | Cheap wages reduce the maintenance costs of all factories, but production is reduced in turn. | All Factories: Credit Maintenance -30% <br> All Factories: Production Rate -15% | 20 |
        | Overclocker | Electronics production is inreased, but all production facilities require more manpower. | All Electronic Productions: Production Rate +30% <br> All Factories: Workforce Maintenance +15% | 20 |
        | Heavy Snowfall | Heavy snowfall limits logistics networks, and therfore reduces local production. | All Factories: Logistic Maintenance +3 <br> All Factories: Production Rate -15% | 20 |
        |||||
        | ***Lunar Region*** |  |  |  |
        | **Trait** | **Description** | **Effects** | **Weight** |
        | Sheltering Crater | Shield Genrerators require less energy in the sector. | Small and Large Shield Generator Energy Maintenance -30% | 10 |
        | Rich Nutrients | The Moon Ice used for watering your Aeroponic Farms is high in micro-nutrients, so that their output is increased. | All Aeroponic Farms: Production Rate +20% | 10 |
        | Cultivated Minerals | Mines provide a higher output in this sector. | All Mining Facilities Production Rate +10% | 15 |
        | Abundant Kreep Deposits | Certain Mines provide a higher output in this sector. | KREEP Gatherer Production Rate +20% | 5 |
        | Deep Moon Ice Deposits | Certain Mines provide a higher output in this sector. | Core Ice Driller Production Rate +20% | 5 |
        | Abundant Helium-3 Depsoits | Certain mines provide a higher output in this sector. | Regolith Collector: Production Rate +20% | 5 |
        | Deep Titanium Depsoits | Certain mines provide a higher output in this sector. | Titanium Mine: Production Rate +20% | 5 |
        | High Insolation | Solar Arrays are more effective in this sector, but all production facilities need more workforce. | Solar Array: Production Rate +30% <br> All Production Facilities: Workforce Maintenance +15% | 20 |
        | Mineral Ice | Aeroponic Farms need less input, but Oxygen Separators generate less output. | Aeroponic Farm: Input Demand -30% <br> Oxygen Separator: Production Rate -15% | 20 |
        | Exposed Crater | Regolith Collectors provide a higher output, but Shield Generators require more energy. | Regolith Collector: Production Rate +30% <br> Small and Large Shield Generator: Energy Maintenance +15% | 20 |
        | Magnetized Grounds | Fusion Reactors use the stronger local magnetic field, but instruments in Cybernetics Factories are disturbed by it. | Fusion Reactor: Production Rate +30% <br> Cybernetics Factory: Energy Maintenance +50% | 20 |
        | Peak Libration | Reduced gravitational pull benefits Anti-G Workshops, but hinders regular work on all Factories. | Anti-G Workshop: Production Rate +30% <br> All Production Facilities: Workforce Maintenance +15% | 20 |
        | Pyrite Veins | Pyrite replaces other impurities and is easy to extract for Titanium Mines, but not for Core Ice Drillers. | Titanium Mine: Production Rate +30% <br> Core Ice Driller: Production Rate -15% | 20 |
        | Moonquake Territory | The shaking ground benefits KREEP Gatherers, but requires more work of Maintenance Stations. | KREEP Gatherer: Production Rate +30% <br> Maintenance Station: Input Amount +100% | 20 |
        | Artificial Intelligence | Cybernetic factories have increased output, but all production facilities require more logistics. | Cybernetic Factories: Production Rate +30% <br> All production facilities: Logistic Maintenance +1 | 20 |
        | High Voltage | Fusion power cell production is increased, but Energy facilities have higher maintenance. | Fusion Preparation Plant: Production Rate +30% <br> Energy facilities: Credit Maintenance +15% | 20 |
        | Optimised Circuits | Energy facilities provide limited output, but Electronics facilities require less energy. | All Electronic Facilities: Energy Maintenance -30% <br> All Energy Facilities: -15% Output | 20 |
        | Cheap Wages | Cheap wages reduce the maintenance costs of all factories, but production is reduced in turn. | All Factories: Credit Maintenance -30% <br> All Factories: Production Rate -15% | 20 |
        | Concentrated Gravitational Environment | Gravity compensator production is increased, but all production facilities require more manpower. | Gravity Compensator Fabrication Hall: Production Rate +30% <br> All Factories: Workforce Maintenance +15% | 20 |
        |||||
        | ***Mars*** |  |  |  |
        | **Trait** | **Description** | **Effects** | **GUID** |
        | Foreign Contact | Contact to foreign species increases research output of all Martian Laboratories, but your Androids need more Communication Devices to keep contact. | All Martian Research Laboratorys Production Rate +15% <br> Input Demand for Neural Interfaces for martian Synths +30% | 19990315 |
        | Dust Storms | Windparks are more effictive during the storms in this sector, but productivity of KREEP Gatheres and Diamond Extractors is impaired. | Windpark Production Rate +30% <br> KREEP Gatherer and Diamond Extractor Production Rate -15% | 19990319 |
        | Old Mars Rovers | Exploring the wrackages of left behind Mars Reovers of the First Mission reduces your Androids need for Services, but due to the long journeys, all buildings need more logistics. | Martian Synthetics Services Need -30% <br> All production buildings: Logistics Maintenance +2 | 19990322 |
        | Meteor Showers | Open Pit Mines provide from a higher output from minable meteors in this sector, but shield generators require more energy to operate. | All Open Pit Mining Facilities Production Rate +30% <br> Shield Generators Energy Maintenance +15% | 19990325 |
        | Marsquake Territory | The shaking ground benefits Gas Drilling Rigs, but requires more work of Maintenance Stations. | Gas Drilling Rig: Production Rate +30% <br> Maintenance Station: Input Amount +100% | 19990328 |
        | Martian Terraforming | Through increased research efforts in your Martian Agricultural Laboratories, Greenhouses can now produce part of the required research goods self-sustaining. | Martian Agricultural Laboratory Production Rate +15% <br> Martian Agricultural Laboratory Input Requirements -30% <br> All other Martian Research Laboratories: Production Rate -15% | 19990331 |
        | Martian Bio-Engineering | Through increased research efforts in your Martian Biotech Laboratories, your Androids need less spare parts to function properly. | Martian Biotech Laboratory Production Rate +15% <br> Martian Synthetics BioEnhancer Need -30% <br> All other Martian Research Laboratories: Production Rate -15% | 19990334 |
        | Martian Nano-Processing | Through increased research efforts in your Martian Electronics Laboratories, processing information through Neural Interfaces becomes easier for your Androids. | Martian Electronics Laboratory Production Rate +30% <br> Martian Synthetics Neural Interfaces Need -30% <br> All other Martian Research Laboratories: Production Rate -15% | 19990337 |
        | Martian Atmospheric Charging | Through increased research efforts in your Martian Energy Laboratories, all Martian Buildings can save energy while operating. | Martian Energy Laboratory Production Rate +15% <br> All Martian Buildings: Energy Maintenance -30% <br> All other Martian Research Laboratories: Production Rate -15% | 19990340 |
        | Martian Core Drilling | Through increased research efforts in your Martian Heavy Industry Laboratories, Open Pit Mines can now support more primary modules. | Martian Heavy Industry Laboratory Production Rate +15% <br> All Martian Open Pit Mines +4 Primary Modules <br> All other Martian Research Laboratories: Production Rate -15% | 19990343 |
        </details>

# Credits
- The Anno 2205 team at Ubisoft Mainz for creating a fantastic modding base!
- Annothek (Author of the Anno 2205 Revolutions Mod): With his permission this mod uses some of his Ornamental/Military Buildings, his small Public Buildings and some ideas for new Sector Traits for the Temperate Region
- Active Playtesters:
  - AnnoEffect
  - 8wayz
  - DuxVitae
  - Ionovia
  - Kurila
  - Taubenangriff
  - The-Rebuilder
  - Wiesl
- Monthly Ko-Fi supporters:
  - The-Rebuilder
  - Nayumi
