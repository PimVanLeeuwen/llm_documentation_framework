#### closeInputMethodContext()


 virtual void ComponentPeer::closeInputMethodContext ( ) virtual 
 

If there's a currently active inputmethod context i.e.characters are being composed using multiple keystrokes this should commit the current state of the context to the text and clear the context. This should not hide the virtual keyboard.