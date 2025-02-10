#### componentParentHierarchyChanged()


 void ComponentMovementWatcher::componentParentHierarchyChanged ( Component & component ) overridevirtual 
 

Called to indicate that the component's parents have changed.When a component is added or removed from its parent, all of its children will produce this notification (recursively so all children of its children will also be called as well).Parameters

 component the component that this listener is registered with 
 



See alsoComponent::parentHierarchyChanged Reimplemented from ComponentListener.