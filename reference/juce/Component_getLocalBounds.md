#### getLocalBounds()


 Rectangle< int > Component::getLocalBounds ( ) const noexcept 
 

Returns the component's bounds, relative to its own origin.This is like getBounds(), but returns the rectangle in local coordinates, In practice, it'll return a rectangle with position (0, 0), and the same size as this component.