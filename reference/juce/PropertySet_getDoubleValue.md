#### getDoubleValue()


 double PropertySet::getDoubleValue ( StringRef keyName, double defaultReturnValue = 0.0 ) const noexcept 
 

Returns one of the properties as an double.If the value isn't found in this set, then this will look for it in a fallback property set (if you've specified one with the setFallbackPropertySet() method), and if it can't find one there, it'll return the default value passedin.Parameters

 keyName the name of the property to retrieve 
 
 defaultReturnValue a value to return if the named property doesn't actually exist