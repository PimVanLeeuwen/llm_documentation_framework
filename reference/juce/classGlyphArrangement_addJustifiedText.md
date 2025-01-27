#### addJustifiedText()


 void GlyphArrangement::addJustifiedText ( const Font & font, 
 
 const String & text, 
 float x, 
 float y, 
 float maxLineWidth, 
 Justification horizontalLayout, 
 float leading = 0.0f ) 

Adds some multiline text, breaking lines at wordboundaries if they are too wide.This will add text to the arrangement, breaking it into new lines either where there is a newline or carriagereturn character in the text, or where a line's width exceeds the value set in maxLineWidth.Each line that is added will be laid out using the flags set in horizontalLayout, so the lines can be left or rightjustified, or centred horizontally in the space between x and (x + maxLineWidth).The y coordinate is the position of the baseline of the first line of text subsequent lines will be placed below it, separated by a distance of font.getHeight() + leading.