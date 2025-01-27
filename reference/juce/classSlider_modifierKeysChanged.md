#### modifierKeysChanged()


 void Slider::modifierKeysChanged ( const ModifierKeys & modifiers ) overridevirtual 
 

Called when a modifier key is pressed or released.Whenever the shift, control, alt or command keys are pressed or released, this method will be called.The component that is currently under the main mouse pointer will be tried first and, if there is no component currently under the pointer, the component that currently has the keyboard focus will have this method called. Remember that a component will only be given the focus if its setWantsKeyboardFocus() method has been used to enable this.The default implementation of this method actually calls its parent's modifierKeysChanged method, so that focused components which aren't interested in this will give their parents a chance to act on the event instead.See alsokeyStateChanged, ModifierKeys Reimplemented from Component.