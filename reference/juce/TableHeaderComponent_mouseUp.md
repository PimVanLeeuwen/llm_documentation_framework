#### mouseUp()


 void TableHeaderComponent::mouseUp ( const MouseEvent & event ) overridevirtual 
 

Called when a mouse button is released.A mouseUp callback is sent to the component in which a button was pressed even if the mouse is actually over a different component when the button is released.The MouseEvent object passed in contains lots of methods for finding out which buttons were down just before they were released.Parameters

 event details about the position and status of the mouse event, including the source component in which it occurred 
 



See alsomouseDown, mouseDrag, mouseDoubleClick, contains Reimplemented from Component.