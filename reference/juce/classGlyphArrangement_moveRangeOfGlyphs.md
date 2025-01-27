#### moveRangeOfGlyphs()


 void GlyphArrangement::moveRangeOfGlyphs ( int startIndex, 
 
 int numGlyphs, 
 float deltaX, 
 float deltaY ) 

Shifts a set of glyphs by a given amount.Parameters

 startIndex the first glyph to transform 
 
 numGlyphs the number of glyphs to move; if this is < 0, all glyphs after startIndex will be used 
 deltaX the amount to add to their xpositions 
 deltaY the amount to add to their ypositions