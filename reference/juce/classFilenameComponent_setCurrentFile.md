#### setCurrentFile()


 void FilenameComponent::setCurrentFile ( File newFile, 
 
 bool addToRecentlyUsedList, 
 NotificationType notification = sendNotificationAsync ) 

Changes the current filename.Parameters

 newFile the new filename to use 
 
 addToRecentlyUsedList if true, the filename will also be added to the dropdown list of recent files. 
 notification whether to send a notification of the change to listeners. A notification will only be sent if the filename has changed.