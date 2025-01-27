#### scrollToBottom()


 bool ScrollBar::scrollToBottom ( NotificationType notification = sendNotificationAsync ) 
 

Scrolls to the bottom (or right).This is the same as calling setCurrentRangeStart (getMaximumRangeLimit() getCurrentRangeSize());Parameters

 notification whether to send a notification of the change to listeners. A notification will only be sent if the position has changed. 
 



Returnstrue if the scrollbar's position actually changed.