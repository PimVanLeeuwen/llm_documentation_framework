#### stretchRangeOfGlyphs()


 void GlyphArrangement::stretchRangeOfGlyphs ( int startIndex, 
 
 int numGlyphs, 
 float horizontalScaleFactor ) 

Expands or compresses a set of glyphs horizontally.Parameters

 startIndex the first glyph to transform 
 
 numGlyphs the number of glyphs to stretch; if this is < 0, all glyphs after startIndex will be used 
 horizontalScaleFactor how much to scale their horizontal width by