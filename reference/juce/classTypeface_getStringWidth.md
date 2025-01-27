#### getStringWidth()


 float Typeface::getStringWidth ( TypefaceMetricsKind , 
 
 const String & text, 
 float normalisedHeight = 1.0f, 
 float horizontalScale = 1.0f ) 

DeprecatedThis function has several shortcomings:The height parameter is specified in JUCE units rather than in points.The result is computed assuming that ligatures and other font features will not be used when rendering the string. There's also no way of specifying a language used for the string, which may affect the widths of CJK text.If the typeface doesn't contain suitable glyphs for all characters in the string, missing characters will be substituted with the notdef/tofu glyph instead of attempting to use a different font that contains suitable glyphs.Measures the width of a line of text. You should never need to call this!