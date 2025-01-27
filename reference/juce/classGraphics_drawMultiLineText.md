#### drawMultiLineText()


 void Graphics::drawMultiLineText ( const String & text, 
 
 int startX, 
 int baselineY, 
 int maximumLineWidth, 
 Justification justification = Justification::left, 
 float leading = 0.0f ) const 

Draws text across multiple lines.This will break the text onto a new line where there's a newline or carriagereturn character, or at a wordboundary when the text becomes wider than the size specified by the maximumLineWidth parameter. Newlines will be vertically separated by the specified leading.See alsosetFont, drawSingleLineText, drawFittedText, GlyphArrangement::addJustifiedText