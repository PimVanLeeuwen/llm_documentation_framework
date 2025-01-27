#### getStringBounds()


 static Rectangle< float > GlyphArrangement::getStringBounds ( const Font & font, StringRef text ) static 
 

This convenience function adds text to a GlyphArrangement using the specified font and returns the bounding box of the text after shaping.The returned bounding box is positioned with its origin at the left end of the text's baseline.References addLineOfText(), getBoundingBox(), and getNumGlyphs().