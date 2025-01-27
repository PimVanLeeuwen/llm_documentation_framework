#### setSelectedRows()


 void ListBox::setSelectedRows ( const SparseSet< int > & setOfRowsToBeSelected, 
 
 NotificationType sendNotificationEventToModel = sendNotification ) 

Sets the rows that should be selected, based on an explicit set of ranges.If sendNotificationEventToModel is true, the ListBoxModel::selectedRowsChanged() method will be called. If it's false, no notification will be sent to the model.See alsogetSelectedRows