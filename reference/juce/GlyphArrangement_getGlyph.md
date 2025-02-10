#### getGlyph()


 PositionedGlyph & GlyphArrangement::getGlyph ( int index ) noexcept 
 

Returns one of the glyphs from the arrangement.Parameters

 index the glyph's index, from 0 to (getNumGlyphs() 1). Be careful not to pass an outofrange index here, as it doesn't do any boundschecking.