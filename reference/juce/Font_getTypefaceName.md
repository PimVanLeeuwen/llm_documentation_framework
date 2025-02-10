#### getTypefaceName()


 String Font::getTypefaceName ( ) const noexcept 
 

Returns the font family of the typeface that this font uses.e.g. "Arial", "Courier", etc.This may also be set to Font::getDefaultSansSerifFontName(), Font::getDefaultSerifFontName(), or Font::getDefaultMonospacedFontName(), which are not actual platformspecific font family names, but are generic font family names that are used to represent the various default fonts.If you need to know the exact typeface font family being used, you can call Font::getTypefacePtr()>getName(), which will give you the platformspecific font family.