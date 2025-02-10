#### getGlyphPositions()


 void Typeface::getGlyphPositions ( TypefaceMetricsKind , 
 
 const String & text, 
 Array< int > & glyphs, 
 Array< float > & xOffsets, 
 float normalisedHeight = 1.0f, 
 float horizontalScale = 1.0f ) 

DeprecatedThis function has several shortcomings:The height parameter is specified in JUCE units rather than in points.Ligatures are deliberately ignored, which will lead to ugly results if the positions are used to paint text using latin scripts, and potentially illegible results for other scripts. There's also no way of specifying a language used for the string, which may affect the rendering of CJK text.If the typeface doesn't contain suitable glyphs for all characters in the string, missing characters will be substituted with the notdef/tofu glyph instead of attempting to use a different font that contains suitable glyphs.Converts a line of text into its glyph numbers and their positions. You should never need to call this!