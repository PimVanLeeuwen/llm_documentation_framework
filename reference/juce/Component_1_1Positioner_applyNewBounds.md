#### applyNewBounds()


 virtual void Component::Positioner::applyNewBounds ( const Rectangle< int > & newBounds ) pure virtual 
 

Attempts to set the component's position to the given rectangle.Unlike simply calling Component::setBounds(), this may involve the positioner being smart enough to adjust itself to fit the new bounds.