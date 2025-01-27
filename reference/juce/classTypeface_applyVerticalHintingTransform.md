#### applyVerticalHintingTransform()


 void Typeface::applyVerticalHintingTransform ( float fontHeight, 
 
 Path & path ) 

Makes an attempt at performing a good overall distortion that will scale a font of the given size to align vertically with the pixel grid.The path should be an unscaled (i.e. normalised to height of 1.0) path for a glyph.