#### getAllToolbarItemIds()


 virtual void ToolbarItemFactory::getAllToolbarItemIds ( Array< int > & ids ) pure virtual 
 

Must return a list of the IDs for all the item types that this factory can create.The ids should be added to the array that is passedin.An item ID can be any integer you choose, except for 0, which is considered a null ID, and the predefined IDs in the SpecialItemIds enum.You should also add the builtin types (separatorBarId, spacerId and flexibleSpacerId) to this list if you want your toolbar to be able to contain those items.The list returned here is used by the ToolbarItemPalette class to obtain its list of available items, and their order on the palette will reflect the order in which they appear on this list.See alsoToolbarItemPalette