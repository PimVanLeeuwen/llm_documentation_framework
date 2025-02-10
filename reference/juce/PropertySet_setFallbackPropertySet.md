#### setFallbackPropertySet()


 void PropertySet::setFallbackPropertySet ( PropertySet \* fallbackProperties ) noexcept 
 

Sets up a second PopertySet that will be used to look up any values that aren't set in this one.If you set this up to be a pointer to a second property set, then whenever one of the getValue() methods fails to find an entry in this set, it will look up that value in the fallback set, and if it finds it, it will return that.Make sure that you don't delete the fallback set while it's still being used by another set! To remove the fallback set, just call this method with a null pointer.See alsogetFallbackPropertySet