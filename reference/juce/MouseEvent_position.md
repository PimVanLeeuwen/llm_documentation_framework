#### position


 const Point<float> MouseEvent::position 
 

The position of the mouse when the event occurred.This value is relative to the topleft of the component to which the event applies (as indicated by the MouseEvent::eventComponent field).This is a more accurate floatingpoint version of the position returned by getPosition() and the integer x and y member variables.