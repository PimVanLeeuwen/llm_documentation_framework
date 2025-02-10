#### mouseDoubleClick()


 void Component::mouseDoubleClick ( const MouseEvent & event ) overridevirtual 
 

Called when a mouse button has been doubleclicked on a component.The MouseEvent object passed in contains lots of methods for finding out which button was pressed, as well as which modifier keys (e.g. shift, ctrl) were held down at the time.Parameters

 event details about the position and status of the mouse event, including the source component in which it occurred 
 



See alsomouseDown, mouseUp Reimplemented from MouseListener.Reimplemented in Label, Slider, and TextEditor.