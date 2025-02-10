#### keyStateChanged()


 virtual bool KeyListener::keyStateChanged ( bool isKeyDown, Component \* originatingComponent ) virtual 
 

Called when any key is pressed or released.When this is called, classes that might be interested in the state of one or more keys can use KeyPress::isKeyCurrentlyDown() to check whether their key has changed.If your implementation returns true, then the key event is considered to have been consumed, and will not be passed on to any other components. If it returns false, then the key will be passed to other components that might want to use it.Parameters

 originatingComponent the component that received the key event 
 
 isKeyDown true if a key is being pressed, false if one is being released 



See alsoKeyPress, Component::keyStateChanged Reimplemented in KeyPressMappingSet.