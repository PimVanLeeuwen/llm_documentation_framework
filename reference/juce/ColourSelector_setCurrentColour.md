#### setCurrentColour()


 void ColourSelector::setCurrentColour ( Colour newColour, 
 
 NotificationType notificationType = sendNotification ) 

Changes the colour that is currently being shown.Parameters

 newColour the new colour to show 
 
 notificationType whether to send a notification of the change to listeners. A notification will only be sent if the colour has changed.