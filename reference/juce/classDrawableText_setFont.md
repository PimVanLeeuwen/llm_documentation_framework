#### setFont()


 void DrawableText::setFont ( const Font & newFont, 
 
 bool applySizeAndScale ) 

Sets the font to use.Note that the font height and horizontal scale are set using setFontHeight() and setFontHorizontalScale(). If applySizeAndScale is true, then these height and scale values will be changed to match the dimensions of the font supplied; if it is false, then the new font object's height and scale are ignored.