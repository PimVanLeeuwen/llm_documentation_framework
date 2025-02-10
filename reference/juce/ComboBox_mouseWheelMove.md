#### mouseWheelMove()


 void ComboBox::mouseWheelMove ( const MouseEvent & event, const MouseWheelDetails & wheel ) overridevirtual 
 

Called when the mousewheel is moved.This callback is sent to the component that the mouse is over when the wheel is moved.If not overridden, a component will forward this message to its parent, so that parent components can collect mousewheel messages that happen to child components which aren't interested in them.Parameters

 event details about the mouse event 
 
 wheel details about the wheel movement 


Reimplemented from MouseListener.