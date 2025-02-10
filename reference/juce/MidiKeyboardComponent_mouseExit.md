#### mouseExit()


 void MidiKeyboardComponent::mouseExit ( const MouseEvent & event ) overridevirtual 
 

Called when the mouse moves out of a component.This will be called when the mouse moves off the edge of this component.If the mouse button was pressed, and it was then dragged off the edge of the component and released, then this callback will happen when the button is released, after the mouseUp callback.Parameters

 event details about the position and status of the mouse event, including the source component in which it occurred 
 



See alsomouseEnter, mouseDrag, mouseMove, contains Reimplemented from Component.