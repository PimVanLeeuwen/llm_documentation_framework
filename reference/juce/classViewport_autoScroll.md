#### autoScroll()


 bool Viewport::autoScroll ( int mouseX, 
 
 int mouseY, 
 int distanceFromEdge, 
 int maximumSpeed ) 

If the specified position is at the edges of the viewport, this method scrolls the viewport to bring that position nearer to the centre.Call this if you're dragging an object inside a viewport and want to make it scroll when the user approaches an edge. You might also find Component::beginDragAutoRepeat() useful when autoscrolling.Parameters

 mouseX the x position, relative to the Viewport's topleft 
 
 mouseY the y position, relative to the Viewport's topleft 
 distanceFromEdge specifies how close to an edge the position needs to be before the viewport should scroll in that direction 
 maximumSpeed the maximum number of pixels that the viewport is allowed to scroll by. 



Returnstrue if the viewport was scrolled