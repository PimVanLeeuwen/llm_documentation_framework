#### reallyContains() [2/2]


 bool Component::reallyContains ( Point< float > localPoint, 
 
 bool returnTrueIfWithinAChild ) 

Returns true if a given point lies in this component, taking any overlapping siblings into account.Parameters

 localPoint the coordinate to test, relative to this component's topleft. 
 
 returnTrueIfWithinAChild if the point actually lies within a child of this component, this determines whether that is counted as a hit. 



See alsocontains, getComponentAt