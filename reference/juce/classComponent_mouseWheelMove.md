#### mouseWheelMove()


 void Component::mouseWheelMove ( const MouseEvent & event, const MouseWheelDetails & wheel ) overridevirtual 
 

Called when the mousewheel is moved.This callback is sent to the component that the mouse is over when the wheel is moved.If not overridden, a component will forward this message to its parent, so that parent components can collect mousewheel messages that happen to child components which aren't interested in them. (Bear in mind that if you attach a component as a mouselistener to other components, then those wheel moves will also end up calling this method and being passed up to the parents, which may not be what you intended to happen).Parameters

 event details about the mouse event 
 
 wheel details about the mouse wheel movement 


Reimplemented from MouseListener.Reimplemented in KeyboardComponentBase, ListBox, ScrollBar, Slider, TextEditor, and Viewport.