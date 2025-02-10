#### getComponentAt() [3/3]


 Component \* Component::getComponentAt ( Point< float > position ) 
 

Returns the component at a certain point within this one.Parameters

 position the coordinate to test, relative to this component's topleft. 
 



Returnsthe component that is at this position which may be 0, this component, or one of its children. Note that overlapping siblings that might actually be in the way are not taken into account by this method to account for these, instead call getComponentAt on the toplevel parent of this component. 
See alsohitTest, contains, reallyContains