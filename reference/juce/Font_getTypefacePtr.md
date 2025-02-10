#### getTypefacePtr()


 Typeface::Ptr Font::getTypefacePtr ( ) const 
 

Returns the main typeface used by this font.Note: This will only ever return the typeface for the "main" family. Before attempting to render glyphs from this typeface, it's a good idea to check that those glyphs are present in the typeface, and to select a different face if necessary.