#### setSelectedId()


 void ComboBox::setSelectedId ( int newItemId, 
 
 NotificationType notification = sendNotificationAsync ) 

Sets one of the items to be the current selection.This will set the ComboBox's text to that of the item that matches this ID.Parameters

 newItemId the new item to select 
 
 notification determines the type of change notification that will be sent to listeners if the value changes 



See alsogetSelectedId, setSelectedItemIndex, setText