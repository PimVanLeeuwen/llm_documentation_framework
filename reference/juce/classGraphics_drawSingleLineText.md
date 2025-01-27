#### drawSingleLineText()


 void Graphics::drawSingleLineText ( const String & text, 
 
 int startX, 
 int baselineY, 
 Justification justification = Justification::left ) const 

Draws a oneline text string.This will use the current colour (or brush) to fill the text. The font is the last one specified by setFont().Parameters

 text the string to draw 
 
 startX the position to draw the lefthand edge of the text 
 baselineY the position of the text's baseline 
 justification the horizontal flags indicate which end of the text string is anchored at the specified point. 



See alsodrawMultiLineText, drawText, drawFittedText, GlyphArrangement::addLineOfText