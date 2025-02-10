#### addColouredItem() [2/2]


 void PopupMenu::addColouredItem ( int itemResultID, 
 
 String itemText, 
 Colour itemTextColour, 
 bool isEnabled, 
 bool isTicked, 
 std::unique\_ptr< Drawable > iconToUse ) 

Appends a text item with a special colour.This is the same as addItem(), but specifies a colour to use for the text, which will override the default colours that are used by the current lookandfeel. See addItem() for a description of the parameters.