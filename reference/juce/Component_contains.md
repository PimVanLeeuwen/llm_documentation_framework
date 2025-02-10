#### contains() [2/2]


 bool Component::contains ( Point< float > localPoint ) 
 

Returns true if a given point lies within this component or one of its children.Never override this method! Use hitTest to create custom hit regions.Parameters

 localPoint the coordinate to test, relative to this component's topleft. 
 



Returnstrue if the point is within the component's hittest area, but only if that part of the component isn't clipped by its parent component. Note that this won't take into account any overlapping sibling components which might be in the way for that, see reallyContains() 
See alsohitTest, reallyContains, getComponentAt