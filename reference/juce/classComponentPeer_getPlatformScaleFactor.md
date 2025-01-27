#### getPlatformScaleFactor()


 virtual double ComponentPeer::getPlatformScaleFactor ( ) const virtualnoexcept 
 

On Windows and Linux this will return the OS scaling factor currently being applied to the native window.This is used to convert between physical and logical pixels at the OS API level and you shouldn't need to use it in your own code unless you are dealing directly with the native window.