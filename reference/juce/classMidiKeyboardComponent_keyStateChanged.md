#### keyStateChanged()


 bool MidiKeyboardComponent::keyStateChanged ( bool isKeyDown ) overridevirtual 
 

Called when a key is pressed or released.Whenever a key on the keyboard is pressed or released (including modifier keys like shift and ctrl), this method will be called on the component that currently has the keyboard focus. Remember that a component will only be given the focus if its setWantsKeyboardFocus() method has been used to enable this.If your implementation returns true, the event will be consumed and not passed on to any other listeners. If it returns false, then any KeyListeners that have been registered with this component will have their keyStateChanged methods called. As soon as one of these returns true, the process will stop, but if they all return false, the event will be passed upwards to this component's parent, and so on.The default implementation of this method does nothing and returns false.To find out which keys are up or down at any time, see the KeyPress::isKeyCurrentlyDown() method.Parameters

 isKeyDown true if a key has been pressed; false if it has been released 
 



See alsokeyPressed, KeyPress, getCurrentlyFocusedComponent, addKeyListener Reimplemented from Component.