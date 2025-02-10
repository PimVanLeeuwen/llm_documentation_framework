#### getDefaultTypefaceForFont()


 static Typeface::Ptr Font::getDefaultTypefaceForFont ( const Font & font ) static 
 

Returns the default system typeface for the given font.Note: This will only ever return the typeface for the font's "main" family. Before attempting to render glyphs from this typeface, it's a good idea to check that those glyphs are present in the typeface, and to select a different face if necessary.