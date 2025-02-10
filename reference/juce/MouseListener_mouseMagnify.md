#### mouseMagnify()


 virtual void MouseListener::mouseMagnify ( const MouseEvent & event, float scaleFactor ) virtual 
 

Called when a pinchtozoom mousegesture is used.If not overridden, a component will forward this message to its parent, so that parent components can collect gesture messages that are unused by child components.Parameters

 event details about the mouse event 
 
 scaleFactor a multiplier to indicate by how much the size of the target should be changed. A value of 1.0 would indicate no change, values greater than 1.0 mean it should be enlarged. 


Reimplemented in Component.