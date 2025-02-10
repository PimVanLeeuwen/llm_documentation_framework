#### getFrameSizeIfPresent()


 virtual OptionalBorderSize ComponentPeer::getFrameSizeIfPresent ( ) const pure virtual 
 

Returns the size of the window frame that's around this window.Depending on the platform the border size may be invalid for a short transient after creating a new window. Hence the returned value must be checked using operator bool() and the contained value can be accessed using operator\*() only if it is present.Whether or not the window has a normal window frame depends on the flags that were set when the window was created by Component::addToDesktop()