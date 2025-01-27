#### checkBounds()


 void BorderedComponentBoundsConstrainer::checkBounds ( Rectangle< int > & bounds, const Rectangle< int > & previousBounds, const Rectangle< int > & limits, bool isStretchingTop, bool isStretchingLeft, bool isStretchingBottom, bool isStretchingRight ) overridevirtual 
 

This callback changes the given coordinates to impose whatever the current constraints are set to be.Parameters

 bounds the target position that should be examined and adjusted 
 
 previousBounds the component's current size 
 limits the region in which the component can be positioned 
 isStretchingTop whether the top edge of the component is being resized 
 isStretchingLeft whether the left edge of the component is being resized 
 isStretchingBottom whether the bottom edge of the component is being resized 
 isStretchingRight whether the right edge of the component is being resized 


Reimplemented from ComponentBoundsConstrainer.