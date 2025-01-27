#### setPositioner()


 void Component::setPositioner ( Positioner \* newPositioner ) 
 

Sets a new Positioner object for this component.If there's currently another positioner set, it will be deleted. The object that is passed in will be deleted automatically by this component when it's no longer required. Pass a null pointer to clear the current positioner.See alsogetPositioner()