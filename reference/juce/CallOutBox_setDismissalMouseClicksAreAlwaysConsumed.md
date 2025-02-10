#### setDismissalMouseClicksAreAlwaysConsumed()


 void CallOutBox::setDismissalMouseClicksAreAlwaysConsumed ( bool shouldAlwaysBeConsumed ) noexcept 
 

Determines whether the mouse events for clicks outside the calloutbox are consumed, or allowed to arrive at the other component that they were aimed at.By default this is false, so that when you click on something outside the calloutbox, that event will also be sent to the component that was clicked on. If you set it to true, then the first click will always just dismiss the box and not be sent to anything else.