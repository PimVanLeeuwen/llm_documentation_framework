#### addCurtailedLineOfText()


 void GlyphArrangement::addCurtailedLineOfText ( const Font & font, 
 
 const String & text, 
 float x, 
 float y, 
 float maxWidthPixels, 
 bool useEllipsis ) 

Adds a line of text, truncating it if it's wider than a specified size.This is the same as addLineOfText(), but if the line's width exceeds the value specified in maxWidthPixels, it will be truncated using either ellipsis (i.e. dots: "..."), if useEllipsis is true, or if this is false, it will just drop any subsequent characters.