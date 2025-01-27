#### setBounds()


 virtual void ComponentPeer::setBounds ( const Rectangle< int > & newBounds, bool isNowFullScreen ) pure virtual 
 

Moves and resizes the window.If the native window is contained in another window, then the coordinates are relative to the parent window's origin, not the screen origin.This should result in a callback to handleMovedOrResized().