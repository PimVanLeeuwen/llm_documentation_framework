#### setPosition() [3/3]


 void BubbleComponent::setPosition ( Rectangle< int > rectangleToPointTo, 
 
 int distanceFromTarget = 15, 
 int arrowLength = 10 ) 

Moves and resizes the bubble to point at a given rectangle.This will resize the bubble to fit its content, then find a position for it so that it's next to, but doesn't overlap the given rectangle. The rectangle's coordinates are relative to either the bubble component's parent component if it has one, or they are screen coordinates if not.It'll put itself either above, below, or to the side of the component depending on where there's the most space, honouring any restrictions that were set with setAllowedPlacement().distanceFromTarget is the amount of space to leave between the bubble and the target rectangle, and arrowLength is the length of the arrow that it will draw.