#### mouseEnter()


 void MidiKeyboardComponent::mouseEnter ( const MouseEvent & event ) overridevirtual 
 

Called when the mouse first enters a component.If the mouse button isn't pressed and the mouse moves into a component, this will be called to let the component react to this.When the mouse button is pressed and held down while being moved in or out of a component, no mouseEnter or mouseExit callbacks are made only mouseDrag messages are sent to the component that the mouse was originally clicked on, until the button is released.Parameters

 event details about the position and status of the mouse event, including the source component in which it occurred 
 



See alsomouseExit, mouseDrag, mouseMove, contains Reimplemented from Component.