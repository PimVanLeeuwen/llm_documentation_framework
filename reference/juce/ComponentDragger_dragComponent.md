#### dragComponent()


 void ComponentDragger::dragComponent ( Component \* componentToDrag, 
 
 const MouseEvent & e, 
 ComponentBoundsConstrainer \* constrainer ) 

Call this from your mouseDrag() callback to move the component.This will move the component, using the given constrainer object to check the new position.Parameters

 componentToDrag the component that you want to drag 
 
 e the current mousedrag event 
 constrainer an optional constrainer object that should be used to apply limits to the component's position. Pass null if you don't want to constrain the movement. 



See alsostartDraggingComponent