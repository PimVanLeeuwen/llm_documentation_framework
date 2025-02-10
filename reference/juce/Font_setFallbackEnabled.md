#### setFallbackEnabled()


 void Font::setFallbackEnabled ( bool enabled ) 
 

When drawing text using this Font, specifies whether glyphs that are missing in the main typeface should be replaced with glyphs from other fonts.To find missing glyphs, the typefaces for the preferred fallback families will be checked in order, followed by the system fallback fonts. The system fallback font is likely to be different on each platform.Fallback is enabled by default.