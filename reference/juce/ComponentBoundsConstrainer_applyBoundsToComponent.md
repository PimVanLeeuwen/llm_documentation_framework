#### applyBoundsToComponent()


 virtual void ComponentBoundsConstrainer::applyBoundsToComponent ( Component & , Rectangle< int > bounds ) virtual 
 

Called by setBoundsForComponent() to apply a new constrained size to a component.By default this just calls setBounds(), but is virtual in case it's needed for extremely cunning purposes.