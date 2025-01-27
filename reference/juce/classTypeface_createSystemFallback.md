#### createSystemFallback()


 virtual Typeface::Ptr Typeface::createSystemFallback ( const String & text, const String & language ) const pure virtual 
 

Attempts to locate a font with a similar style that is capable of displaying the requested string.This uses system facilities, so will produce different results depending on the operating system and installed fonts. If it's important that your app uses the same fonts on all platforms, then you probably shouldn't use the results of this function.Note that this accepts a string instead of a single codepoint because the OS may take combining marks and variation selectors into account when selecting an appropriate font. As an example, many fonts include a 'text'/'outline' version of the smiley face emoji. macOS may return Helvetica if the smiley emoji codepoint is passed on its own, but will return the emoji font if the emoji codepoint is followed by the variationselector16 codepoint.To specify your own fallback fonts:ensure your preferred fonts provide coverage of all languages/scripts/codepoints that you may need to displaybundle the fonts in your product, e.g. as binary data and register them when your product startsuse Font::setPreferredFallbackFamilies() to specify that the bundled fonts should be used before requesting a fallback font from the systemParameters

 text the returned font will normally be capable of displaying the majority of codepoints in this string 
 
 language BCP 47 language code of the text that includes this codepoint 



Returnsnullptr if no fallback could be created