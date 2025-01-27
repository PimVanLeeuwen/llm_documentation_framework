#### getStringBounds() [2/2]


 static Rectangle< float > TextLayout::getStringBounds ( const Font & font, StringRef text ) static 
 

This convenience function adds text to a TextLayout using the specified font and returns the bounding box of the text after shaping.The returned bounding box is positioned with its origin at the left end of the text's baseline.References AttributedString::append().