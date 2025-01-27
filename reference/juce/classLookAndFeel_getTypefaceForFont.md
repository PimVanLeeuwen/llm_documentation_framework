#### getTypefaceForFont()


 virtual Typeface::Ptr LookAndFeel::getTypefaceForFont ( const Font & ) virtual 
 

Returns the typeface that should be used for a given font.The default implementation just does what you'd expect it to, but you can override this if you want to intercept fonts and use your own custom typeface object.See alsosetDefaultTypeface