#### scrollToTop()


 bool ScrollBar::scrollToTop ( NotificationType notification = sendNotificationAsync ) 
 

Scrolls to the top (or left).This is the same as calling setCurrentRangeStart (getMinimumRangeLimit());Parameters

 notification whether to send a notification of the change to listeners. A notification will only be sent if the position has changed. 
 



Returnstrue if the scrollbar's position actually changed.