#### drawText() [3/3]


 void Graphics::drawText ( const String & text, 
 
 Rectangle< float > area, 
 Justification justificationType, 
 bool useEllipsesIfTooBig = true ) const 

Draws a line of text within a specified rectangle.The text will be positioned within the rectangle based on the justification flags passedin. If the string is too long to fit inside the rectangle, it will either be truncated or will have ellipsis added to its end (if the useEllipsesIfTooBig flag is true).See alsodrawSingleLineText, drawFittedText, drawMultiLineText, GlyphArrangement::addJustifiedText