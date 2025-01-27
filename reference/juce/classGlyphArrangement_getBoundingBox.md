#### getBoundingBox()


 Rectangle< float > GlyphArrangement::getBoundingBox ( int startIndex, 
 
 int numGlyphs, 
 bool includeWhitespace ) const 

Finds the smallest rectangle that will enclose a subset of the glyphs.Parameters

 startIndex the first glyph to test 
 
 numGlyphs the number of glyphs to include; if this is < 0, all glyphs after startIndex will be included 
 includeWhitespace if true, the extent of any whitespace characters will also be taken into account 


Referenced by getStringBounds().