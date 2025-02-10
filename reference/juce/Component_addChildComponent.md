#### addChildComponent() [2/2]


 void Component::addChildComponent ( Component & child, 
 
 int zOrder = 1 ) 

Adds a child component to this one.Adding a child component does not mean that the component will own or delete the child it's your responsibility to delete the component. Note that it's safe to delete a component without first removing it from its parent doing so will automatically remove it and send out the appropriate notifications before the deletion completes.If the child is already a child of this component, then no action will be taken, and its zorder will be left unchanged.Parameters

 child the new component to add. If the component passedin is already the child of another component, it'll first be removed from its current parent. 
 
 zOrder The index in the childlist at which this component should be inserted. A value of 1 will insert it in front of the others, 0 is the back. 



See alsoremoveChildComponent, addAndMakeVisible, addChildAndSetID, getChild, ComponentListener::componentChildrenChanged