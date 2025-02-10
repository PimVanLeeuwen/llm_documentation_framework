#### removeChildComponent() [2/2]


 Component \* Component::removeChildComponent ( int childIndexToRemove ) 
 

Removes one of this component's childcomponents by index.This will return a pointer to the component that was removed, or null if the index was outofrange.Note that removing a child will not delete it! But it's ok to delete a component without first removing it doing so will automatically remove it and send out the appropriate notifications before the deletion completes.See alsoaddChildComponent, ComponentListener::componentChildrenChanged