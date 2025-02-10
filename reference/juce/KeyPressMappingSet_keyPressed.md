#### keyPressed()


 bool KeyPressMappingSet::keyPressed ( const KeyPress & key, Component \* originatingComponent ) overridevirtual 
 

Called to indicate that a key has been pressed.If your implementation returns true, then the key event is considered to have been consumed, and will not be passed on to any other components. If it returns false, then the key will be passed to other components that might want to use it.Parameters

 key the keystroke, including modifier keys 
 
 originatingComponent the component that received the key event 



See alsokeyStateChanged, Component::keyPressed Implements KeyListener.