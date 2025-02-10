#### addKeyListener()


 void Component::addKeyListener ( KeyListener \* newListener ) 
 

Adds a listener that wants to hear about keypresses that this component receives.The listeners that are registered with a component are called by its keyPressed() or keyStateChanged() methods (assuming these haven't been overridden to do something else).If you add an object as a key listener, be careful to remove it when the object is deleted, or the component will be left with a dangling pointer.See alsokeyPressed, keyStateChanged, removeKeyListener