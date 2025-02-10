#### getPeer()


 ComponentPeer \* Component::getPeer ( ) const 
 

Returns the heavyweight window that contains this component.If this component is itself on the desktop, this will return the window object that it is using. Otherwise, it will return the window of its toplevel parent component.This may return nullptr if there isn't a desktop component.See alsoaddToDesktop, isOnDesktop