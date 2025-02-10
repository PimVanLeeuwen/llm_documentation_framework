#### getStringWidth()


 int Font::getStringWidth ( const String & text ) const 
 

Returns the total width of a string as it would be drawn using this font.For a more accurate floatingpoint result, use getStringWidthFloat().This function does not take font fallback into account. If this font doesn't include glyphs to represent all characters in the string, then the width will be computed as though those characters were replaced with the "glyph not
found" character.If you are trying to find the amount of space required to display a given string, you'll get more accurate results by actually measuring the results of whichever text layout engine (e.g. GlyphArrangement, TextLayout) you'll use when displaying the string.See alsoTextLayout::getStringWidth(), GlyphArrangement::getStringWidthInt()