#### getNativeHandle()


 virtual void \* ComponentPeer::getNativeHandle ( ) const pure virtual 
 

Returns the raw handle to whatever kind of window is being used.On windows, this is probably a HWND, on the mac, it's likely to be a WindowRef, but remember there's no guarantees what you'll get back.