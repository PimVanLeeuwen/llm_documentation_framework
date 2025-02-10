#### updatePosition()


 void CallOutBox::updatePosition ( const Rectangle< int > & newAreaToPointTo, 
 
 const Rectangle< int > & newAreaToFitIn ) 

Updates the position and size of the box.You shouldn't normally need to call this, unless you need more precise control over the layout.Parameters

 newAreaToPointTo the rectangle to make the box's arrow point to 
 
 newAreaToFitIn the area within which the box's position should be constrained