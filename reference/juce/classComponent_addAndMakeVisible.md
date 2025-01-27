#### addAndMakeVisible() [2/2]


 void Component::addAndMakeVisible ( Component & child, 
 
 int zOrder = 1 ) 

Adds a child component to this one, and also makes the child visible if it isn't already.This is the same as calling setVisible (true) on the child and then addChildComponent(). See addChildComponent() for more details.Parameters

 child the new component to add. If the component passedin is already the child of another component, it'll first be removed from its current parent. 
 
 zOrder The index in the childlist at which this component should be inserted. A value of 1 will insert it in front of the others, 0 is the back.