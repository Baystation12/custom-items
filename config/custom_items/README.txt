This is a brief overview of the custom item format. Examples can be found in `config/custom_items/examples/` (open them with any text editor).

**HOW TO ADD A CUSTOM ITEM:**
- Pick the most relevant directory for your item, and examine the template.
- Create one JSON file per custom item.
- Name your file YourByondKey-itemtype.json (e.g. babydoll-necklace.json)
- The file must be valid JSON.
- The file must adhere to the values below.
- If you do not need/care about a value, do not include it in the JSON.

**EXPLANATION OF VALUES:**
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
