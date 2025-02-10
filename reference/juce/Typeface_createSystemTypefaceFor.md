#### createSystemTypefaceFor() [3/3]


 static Ptr Typeface::createSystemTypefaceFor ( Span< const std::byte > ) static 
 

Attempts to create a font from some raw font file data (e.g.a TTF or OTF file image). The system will take its own internal copy of the data.The typeface will remain registered with the system for as long as there is at least one owner of the returned Ptr. This allows typefaces registered with createSystemTypefaceFor to be created using just a typeface family name, e.g. in font fallback lists.