#### exitModalState()


 void Component::exitModalState ( int returnValue = 0 ) 
 

Ends a component's modal state.If this component is currently modal, this will turn off its modalness, and return a value to the runModalLoop() method that might have be running its modal loop.See alsorunModalLoop, enterModalState, isCurrentlyModal