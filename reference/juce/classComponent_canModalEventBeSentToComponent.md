#### canModalEventBeSentToComponent()


 virtual bool Component::canModalEventBeSentToComponent ( const Component \* targetComponent ) virtual 
 

When a component is modal, this callback allows it to choose which other components can still receive events.When a modal component is active and the user clicks on a nonmodal component, this method is called on the modal component, and if it returns true, the event is allowed to reach its target. If it returns false, the event is blocked and the inputAttemptWhenModal() callback is made.It called by the isCurrentlyBlockedByAnotherModalComponent() method. The default implementation just returns false in all cases.