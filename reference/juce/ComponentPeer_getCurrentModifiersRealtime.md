#### getCurrentModifiersRealtime()


 static ModifierKeys ComponentPeer::getCurrentModifiersRealtime ( ) staticnoexcept 
 

On desktop platforms this method will check all the mouse and key states and return a ModifierKeys object representing them.This isn't recommended and is only needed in special circumstances for uptodate modifier information at times when the app's event loop isn't running normally.Another reason to avoid this method is that it's not stateless and calling it may update the ModifierKeys::currentModifiers object, which could cause subtle changes in the behaviour of some components.