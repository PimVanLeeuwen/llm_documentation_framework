#### inputAttemptWhenModal()


 virtual void Component::inputAttemptWhenModal ( ) virtual 
 

Called when the user tries to click on a component that is blocked by another modal component.When a component is modal and the user clicks on one of the other components, the modal component will receive this callback.The default implementation of this method will play a beep, and bring the currently modal component to the front, but it can be overridden to do other tasks.See alsoisCurrentlyBlockedByAnotherModalComponent, canModalEventBeSentToComponent Reimplemented in CallOutBox, and Label.