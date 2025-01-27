#### addToDesktop() [2/2]


 void TopLevelWindow::addToDesktop ( int windowStyleFlags, void \* nativeWindowToAttachTo = nullptr ) overridevirtual 
 

Makes this component appear as a window on the desktop.Note that before calling this, you should make sure that the component's opacity is set correctly using setOpaque(). If the component is nonopaque, the windowing system will try to create a special transparent window for it, which will generally take a lot more CPU to operate (and might not even be possible on some platforms).If the component is inside a parent component at the time this method is called, it will first be removed from that parent. Likewise if a component is on the desktop and is subsequently added to another component, it'll be removed from the desktop.Parameters

 windowStyleFlags a combination of the flags specified in the ComponentPeer::StyleFlags enum, which define the window's characteristics. 
 
 nativeWindowToAttachTo this allows an OS object to be passedin as the window in which the juce component should place itself. On Windows, this would be a HWND, a HIViewRef on the Mac. Not necessarily supported on all platforms, and best left as 0 unless you know what you're doing. 



See alsoremoveFromDesktop, isOnDesktop, userTriedToCloseWindow, getPeer, ComponentPeer::setMinimised, ComponentPeer::StyleFlags, ComponentPeer::getStyleFlags, ComponentPeer::setFullScreen Reimplemented from Component.