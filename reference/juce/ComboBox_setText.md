#### setText()


 void ComboBox::setText ( const String & newText, 
 
 NotificationType notification = sendNotificationAsync ) 

Sets the contents of the combobox's text field.The text passedin will be set as the current text regardless of whether it is one of the items in the list. If the current text isn't one of the items, then getSelectedId() will return 0, otherwise it will return the appropriate ID.Parameters

 newText the text to select 
 
 notification determines the type of change notification that will be sent to listeners if the text changes 



See alsogetText