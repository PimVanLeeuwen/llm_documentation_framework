#### setToggleState()


 void Button::setToggleState ( bool shouldBeOn, 
 
 NotificationType notification ) 

A button has an on/off state associated with it, and this changes that.By default buttons are 'off' and for simple buttons that you click to perform an action you won't change this. Toggle buttons, however will want to change their state when turned on or off.Parameters

 shouldBeOn whether to set the button's toggle state to be on or off. If it's a member of a button group, this will always try to turn it on, and to turn off any other buttons in the group 
 
 notification determines the behaviour if the value changes this can invoke a synchronous call to clicked(), but sendNotificationAsync is not supported 



See alsogetToggleState, setRadioGroupId