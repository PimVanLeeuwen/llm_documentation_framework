#### paintOpenCloseButton()


 virtual void TreeViewItem::paintOpenCloseButton ( Graphics & , const Rectangle< float > & area, Colour backgroundColour, bool isMouseOver ) virtual 
 

Draws the item's open/close button.If you don't implement this method, the default behaviour is to call LookAndFeel::drawTreeviewPlusMinusBox(), but you can override it for custom effects. You may want to override it and call the baseclass implementation with a different backgroundColour parameter, if your implementation has a background colour other than the default (white).