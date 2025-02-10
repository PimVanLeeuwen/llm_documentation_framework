#### mouseMove()


 void ResizableBorderComponent::mouseMove ( const MouseEvent & event ) overrideprotectedvirtual 
 

Called when the mouse moves inside a component.If the mouse button isn't pressed and the mouse moves over a component, this will be called to let the component react to this.A component will always get a mouseEnter callback before a mouseMove.Parameters

 event details about the position and status of the mouse event, including the source component in which it occurred 
 



See alsomouseEnter, mouseExit, mouseDrag, contains Reimplemented from Component.