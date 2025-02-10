#### getColourGlyphFormats()


 int Typeface::getColourGlyphFormats ( ) const 
 

Returns an int with bits set indicating the format of colour glyphs contained in the typeface.If the typeface has no colour glyphs, no bits will be set. Otherwise, one or more bits will be set depending on the format of the colour glyph information. You can use a bitwiseand operation with the members of the ColourGlyphFormat enum to determine whether a particular format is supported.const auto isMonochrome = typeface>getColourGlyphFormats() == 0;
const auto isSvg = (typeface>getColourGlyphFormats() & Typeface::colourGlyphFormatSvg) != 0;
const auto isSimpleColour = (typeface>getColourGlyphFormats() & (Typeface::colourGlyphFormatBitmap Typeface::colourGlyphFormatCOLRv0)) != 0;
Typeface::colourGlyphFormatSvg@ colourGlyphFormatSvgThe typeface includes glyphs represented as SVGs.Definition juce\_Typeface.h:278
Typeface::colourGlyphFormatBitmap@ colourGlyphFormatBitmapThe typeface includes glyphs represented as bitmaps (normally PNGs)Definition juce\_Typeface.h:277
Typeface::colourGlyphFormatCOLRv0@ colourGlyphFormatCOLRv0The typeface uses the COLRv0 format, with support for flat colours.Definition juce\_Typeface.h:279