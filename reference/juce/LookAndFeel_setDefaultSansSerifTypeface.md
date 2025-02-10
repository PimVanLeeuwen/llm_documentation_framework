#### setDefaultSansSerifTypeface()


 void LookAndFeel::setDefaultSansSerifTypeface ( Typeface::Ptr newDefaultTypeface ) 
 

Allows you to supply a default typeface that will be returned as the default sansserif font.Instead of a typeface object, you can specify a typeface by name using the setDefaultSansSerifTypefaceName() method.You can perform more complex typeface substitutions by overloading getTypefaceForFont() but this lets you easily set a global typeface.