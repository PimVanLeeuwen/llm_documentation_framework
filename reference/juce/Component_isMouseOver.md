#### isMouseOver()


 bool Component::isMouseOver ( bool includeChildren = false ) const 
 

Returns true if the mouse is currently over this component.If the mouse isn't over the component, this will return false, even if the mouse is currently being dragged so you can use this in your mouseDrag method to find out whether it's really over the component or not.Note that when the mouse button is being held down, then the only component for which this method will return true is the one that was originally clicked on.Also note that on a touchscreen device, this will only return true when a finger is actually down as soon as all touch is released, isMouseOver will always return false.If includeChildren is true, then this will also return true if the mouse is over any of the component's children (recursively) as well as the component itself.See alsoisMouseButtonDown. isMouseOverOrDragging, mouseDrag