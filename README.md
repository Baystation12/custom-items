###How to add a custom item

1. Add a config entry to custom_items.txt. Example:

  ````
  {
  ckey: zuhayr
  character_name: Jane Doe
  item_path: /obj/item/toy/plushie
  item_name: ugly plush toy
  item_icon: flagmask
  item_desc: It's truly hideous.
  req_titles: Assistant, Security Officer
  req_access: 1
  }
  ````

  - ckey should be your key with no spaces, all in lowercase. 
  - character_name is the exact name you will use for the character the item belongs to.
  - item_name is the object name that will be used when spawned.
  - item_path is the object type the item is based on.
  - item_icon is the icon state the item will use. More details on this below.
  - item_desc is the description the item will use.
  - req_titles is a list of exact titles and alt titles that this item will spawn for. Separate them with a comma and a space (, ) or they will break.
  - req_access is a numerical value corresponding to the various station access constants. I don't recommend using this.

2. Add an icon to represent the item when held in the hand to icons/obj/custom_items.dmi (or whatever your codebase defines as CUSTOM_ITEM_OBJ). The icon state should be the same as the value set for item_icon in the config.

3. Add icons to icons/mob/custom_items.dmi (or, again, whatever your codebase defines as CUSTOM_ITEM_MOB) for inhands. You need a left and right icon. The icon state should be the item_icon followed by _l for left and _r for right.

4. If the item is wearable, add an icon to icons/mob/custom_items.dmi for the on-mob icon.

5. If the item isn't a kit, you're done. Have fun. Kits have several extra variables and icons.

  ````
  {
  ckey: zuhayr
  character_name: Jane Doe
  item_path: /obj/item/device/kit/paint
  item_name: APLU customisation kit
  item_desc: A customisation kit with all the parts needed to turn an APLU into a "Titan's Fist" model.
  kit_name: APLU "Titan's Fist"
  kit_desc: Looks like an overworked, under-maintained Ripley with some horrific damage.
  kit_icon: titan
  additional_data: ripley, firefighter
  }
  ````

  - kit_name is the name that will be used for the items the kit is used on.
  - kit_desc is the description that will be applied to items the kit is used on.
  - kit_icon is the icon_state that the kit will use.
  - additional_data has two roles. For voidsuit kits, it's the type of helmet light overlay to use. For mechs, it's a list of the mech types the kit can be used on (separated by ', ' like titles).

6. For mechs, add three icons to icons/obj/custom_items.dmi - kit_icon, kit_icon-open and kit_icon-broken. These are the mech icon, the icon when stationary and without a pilot, and the wreckage icon respectively. You're done now, good work.

7. For suits, add two icons to icons/obj/custom_items.dmi - kit_icon_suit and kit_icon_helmet. These icons represent the suit parts when in inventory.

8. Add four icons to icons/mob/custom_items.dmi. You need to add in-hand icons (see 3) for both kit_icon_suit and kit_icon_helmet.

9. Add a final two icons to icons/mob/custom_items.dmi under kit_icon_suit and kit_icon_helmet for the on-mob icons.

10. You're done. Compile, test, and discover you misspelled a state, etc.
