#### getEdgeTableForGlyph()


 EdgeTable \* Typeface::getEdgeTableForGlyph ( TypefaceMetricsKind , 
 
 int glyphNumber, 
 const AffineTransform & transform, 
 float normalisedHeight ) 

DeprecatedReturns a new EdgeTable that contains the path for the given glyph, with the specified transform applied.This is only capable of returning monochromatic glyphs. In fonts that contain multiple glyph styles with fallbacks (COLRv1, COLRv0, monochromatic), this will always return the monochromatic variant.The height is specified in JUCE fontheight units.getLayersForGlyph() has better support for multilayer and bitmap glyphs, so it should be preferred in new code.