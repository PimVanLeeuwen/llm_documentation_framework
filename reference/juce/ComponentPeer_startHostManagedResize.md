#### startHostManagedResize()


 virtual void ComponentPeer::startHostManagedResize ( Point< int > mouseDownPosition, ResizableBorderComponent::Zone zone ) virtual 
 

Asks the windowmanager to begin resizing this window, on platforms where this is useful (currently just Linux/X11).Parameters

 mouseDownPosition The position of the mouse event that started the resize in unscaled peer coordinates 
 
 zone The edges of the window that may be moved during the resize