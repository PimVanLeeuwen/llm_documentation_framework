#### keyPressed()


 bool AlertWindow::keyPressed ( const KeyPress & key ) overrideprotectedvirtual 
 

Called when a key is pressed.When a key is pressed, the component that has the keyboard focus will have this method called. Remember that a component will only be given the focus if its setWantsKeyboardFocus() method has been used to enable this.If your implementation returns true, the event will be consumed and not passed on to any other listeners. If it returns false, the key will be passed to any KeyListeners that have been registered with this component. As soon as one of these returns true, the process will stop, but if they all return false, the event will be passed upwards to this component's parent, and so on.The default implementation of this method does nothing and returns false.See alsokeyStateChanged, getCurrentlyFocusedComponent, addKeyListener Reimplemented from Component.