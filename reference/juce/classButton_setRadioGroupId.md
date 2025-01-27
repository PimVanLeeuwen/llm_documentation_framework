#### setRadioGroupId()


 void Button::setRadioGroupId ( int newGroupId, 
 
 NotificationType notification = sendNotification ) 

Enables the button to act as a member of a mutuallyexclusive group of 'radio buttons'.If the group ID is set to a nonzero number, then this button will act as part of a group of buttons with the same ID, only one of which can be 'on' at the same time. Note that when it's part of a group, clicking a togglebutton that's 'on' won't turn it off.To find other buttons with the same ID, this button will search through its sibling components for ToggleButtons, so all the buttons for a particular group must be placed inside the same parent component.Set the group ID back to zero if you want it to act as a normal toggle button again.The notification argument lets you specify how other buttons should react to being turned on or off in response to this call.See alsogetRadioGroupId