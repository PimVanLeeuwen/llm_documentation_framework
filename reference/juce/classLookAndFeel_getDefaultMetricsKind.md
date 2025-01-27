#### getDefaultMetricsKind()


 virtual TypefaceMetricsKind LookAndFeel::getDefaultMetricsKind ( ) const virtual 
 

Widgets can call this to find out the kind of metrics they should use when creating their own fonts.The default implementation returns the portable metrics kind, but you can override this if you want to use the legacy metrics kind instead, to avoid rendering changes in existing projects. Switching between metrics kinds may cause text to render at a different size, so you should check that text in your app still renders at an appropriate size, and potentially adjust font sizes where necessary after overriding this function.References portable.