#### removeFromDesktop()


 void Component::removeFromDesktop ( ) 
 

If the component is currently showing on the desktop, this will hide it.You can also use setVisible() to hide a desktop window temporarily, but removeFromDesktop() will free any system resources that are being used up.See alsoaddToDesktop, isOnDesktop