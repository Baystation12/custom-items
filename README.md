## How to add a custom item
1. Pick the most relevant directory for your item, and examine the template inside.

2. Create a .json file in the directory with the following naming scheme: ckey-itemtype.json (e.g. babydoll-necklace.json)

3. Fill out the provided template in the directory of your choice. See chart below for an explanation of the values.

| Key             | Expected Value   | Function                                                                                                         |
|-----------------|------------------|------------------------------------------------------------------------------------------------------------------|
| ckey            | string           | Your ckey. This is not quite the same as your BYOND key, ask an admin or check the BYOND docs if you are unsure. |
| character_name  | string           | The name of the character the item should spawn with.                                                            |
| item_name       | string           | The name of your custom item ingame. For kits, the name of the kit product.                                      |
| item_desc       | string           | The description of your custom item ingame. For kits, the descriptor for the kit product.                        |
| item_icon_state | string           | The icon state for your custom item. For kits, the icon state of the kit product.                                |
| item_path       | string           | A fully specified BYOND object path (ie. /obj/item/foo/bar).                                                     |
| inherit_inhands | true/false       | Whether or not it should override the inhands of the base item.                                                  |
| req_access      | array of strings | Access strings required for the character to have this item on spawn.                                            |
| req_titles      | array of strings | Titles and alt titles that are allowed to spawn with this item.                                                  |
| additional_data | array of values  | An associative list of other values. Currently used fields: "light_overlay".                                     |

**Note** - All icons should be added to the **END** of the relevant file. This helps organisation.

4. Add an icon to represent the item when held in the hand to icons/obj/custom_items.dmi (or whatever your codebase defines as CUSTOM_ITEM_OBJ). The icon state should be the same as the value set for item_icon in the config.

5. Add icons to icons/mob/custom_items.dmi (or, again, whatever your codebase defines as CUSTOM_ITEM_MOB) for inhands. You need a left and right icon. The icon state should be the item_icon followed by _l for left and _r for right.

6. If the item is wearable, add an icon to icons/mob/custom_items.dmi for the on-mob icon.

7. For mechs, add three icons to icons/obj/custom_items.dmi - kit_icon, kit_icon-open and kit_icon-broken. These are the mech icon, the icon when stationary and without a pilot, and the wreckage icon respectively. You're done now, good work.

8. For suits, add two icons to icons/obj/custom_items.dmi - kit_icon_suit and kit_icon_helmet. These icons represent the suit parts when in inventory.

9. Add four icons to icons/mob/custom_items.dmi. You need to add in-hand icons (see 3) for both kit_icon_suit and kit_icon_helmet.

10. Add a final two icons to icons/mob/custom_items.dmi under kit_icon_suit and kit_icon_helmet for the on-mob icons.

11. You're done. Compile, test, and discover you misspelled a state, etc.

## How to add a custom robot icon sheet
1. Add a config entry to custom_sprites.txt:
```
ckey-robotname
```

1. Create icon and eye states for each of the following modules: Standard, Engineering, Construction, Janitor, Surgeon, Crisis, Miner, Security, Service, Clerical, Research
1. Create maintenance panel states for: opened, cell removed, and wires cut.
1. Name your main states in the following format: `yourckey-ModuleName`
1. Name your eyes states in the following format: `eyes-yourckey-ModuleName`
1. The open panel should be named yourkey-openpanel +c; the panel with no cell should be named `yourckey-openpanel-c`; the wire panel should be named `yourckey-openpanel +w`

## How to add a custom AI display
1. Add a config entry to custom_sprites.txt. Either:
  ````
  ckey:ai_name
  ````
  or
  ````
  ckey:ai_name:icon_state
  ````

  - ckey should be your key with no spaces or underscores, all in lowercase. 
  - ai_name is the exact name you will use for the AI the display belongs to.
  - icon_state is the name of your AI icon states without the "-ai" or "-ai-crashed" suffixes. Defaults to the ckey value if unset.
  
  Multiple entries per player is possible, as long as the icon_state value is set and unique, i.e.:
  ````
  ckey:ai_name:custom_icon_1
  ckey:ai_name:custom_icon_2
  ````

2. Add the first or both of the following icon states to icons/custom_synthetic.dmi named {icon_state}-ai and {icon_state}-ai-crash (the ai-crash icon state is optional), replacing {icon_state} with the icon_state value you've selected.
  ````
  ckey_example:ExampleAIName
  ````
  With the example above the resulting icon state names would be "ckey_example-ai" (required) and "ckey_example-ai-crash" (optional).
  
  ````
  ckey_example:ExampleAIName:example_icon_state
  ````
  With the example above the resulting icon state names would be "example_icon_state-ai" (required) and "example_icon_state-ai-crash" (optional).

## How to locally test a custom item

1. Create a .json file as directed above, and place it in the `config/custom_items` directory of your local copy of your main repository (eg. Baystation12)
3. Change ckey in the definition to YOUR CKEY. Change name to a character name you will be using for testing, or just use their name.
4. Add the relevant icons to the relevant files in your main repo folder.
5. Compile and run the game. Ready up, taking note of any job or access restrictions, and start the round. If you did it all correctly, you will have spawned the custom item. If not, it should hopefully give you an error message that can point you in the right direction. 
6. Once you're done testing, make sure you revert any changes made in your main repo folder. Do not push custom items related things to the main repo!
