#### isCurrentlyBlockedByAnotherModalComponent()


 bool Component::isCurrentlyBlockedByAnotherModalComponent ( ) const 
 

Checks whether there's a modal component somewhere that's stopping this one from receiving messages.If there is a modal component, its canModalEventBeSentToComponent() method will be called to see if it will still allow this component to receive events.See alsorunModalLoop, getCurrentlyModalComponent