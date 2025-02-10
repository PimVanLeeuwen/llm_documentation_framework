#### justifyGlyphs()


 void GlyphArrangement::justifyGlyphs ( int startIndex, 
 
 int numGlyphs, 
 float x, 
 float y, 
 float width, 
 float height, 
 Justification justification ) 

Justifies a set of glyphs within a given space.This moves the glyphs as a block so that the whole thing is located within the given rectangle with the specified layout.If the Justification::horizontallyJustified flag is specified, each line will be stretched out to fill the specified width.