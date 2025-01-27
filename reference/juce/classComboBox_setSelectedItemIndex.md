#### setSelectedItemIndex()


 void ComboBox::setSelectedItemIndex ( int newItemIndex, 
 
 NotificationType notification = sendNotificationAsync ) 

Sets one of the items to be the current selection.This will set the ComboBox's text to that of the item at the given index in the list.Parameters

 newItemIndex the new item to select 
 
 notification determines the type of change notification that will be sent to listeners if the value changes 



See alsogetSelectedItemIndex, setSelectedId, setText