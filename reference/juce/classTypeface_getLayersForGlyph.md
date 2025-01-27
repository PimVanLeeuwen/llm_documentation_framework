#### getLayersForGlyph()


 std::vector< GlyphLayer > Typeface::getLayersForGlyph ( TypefaceMetricsKind , 
 
 int glyphNumber, 
 const AffineTransform & , 
 float normalisedHeight ) const 

Returns the layers that should be painted in order to display this glyph.Layers should be painted in the same order as they are returned, i.e. layer[0], layer[1] etc.This should generally be preferred to getEdgeTableForGlyph, as it is more flexible. Currently, this only supports COLRv0 and bitmap fonts (no SVG or COLRv1). Support for SVG and COLRv1 may be added in the future, depending on demand. However, this would require significant additions to JUCE's rendering code, so it has been omitted for now.The height is specified in JUCE fontheight units.