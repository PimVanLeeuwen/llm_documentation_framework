#### addLineOfText()


 void GlyphArrangement::addLineOfText ( const Font & font, 
 
 const String & text, 
 float x, 
 float y ) 

Appends a line of text to the arrangement.This will add the text as a single line, where x is the lefthand edge of the first character, and y is the position for the text's baseline.If the text contains newlines or carriagereturns, this will ignore them use addJustifiedText() to add multiline arrangements.Referenced by getStringBounds().