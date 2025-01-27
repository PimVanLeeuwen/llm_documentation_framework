#### getInterceptsMouseClicks()


 void Component::getInterceptsMouseClicks ( bool & allowsClicksOnThisComponent, bool & allowsClicksOnChildComponents ) const noexcept 
 

Retrieves the current state of the mouseclick interception flags.On return, the two parameters are set to the state used in the last call to setInterceptsMouseClicks().See alsosetInterceptsMouseClicks