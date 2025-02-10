#### setTypefaceName()


 void Font::setTypefaceName ( const String & faceName ) 
 

Changes the font family of the typeface.e.g. "Arial", "Courier", etc.This may also be set to Font::getDefaultSansSerifFontName(), Font::getDefaultSerifFontName(), or Font::getDefaultMonospacedFontName(), which are not actual platformspecific font family names, but are generic font family names that are used to represent the various default fonts. If you need to know the exact typeface font family being used, you can call Font::getTypefacePtr()>getName(), which will give you the platformspecific font family.If a suitable font isn't found on the machine, it'll just use a default instead.