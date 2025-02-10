#### moveScrollbarInPages()


 bool ScrollBar::moveScrollbarInPages ( int howManyPages, 
 
 NotificationType notification = sendNotificationAsync ) 

Moves the scroll bar up or down in pages.This will move the bar by a multiple of its current thumb size, effectively doing a pageup or down.A positive value here will move the bar down or to the right, a negative value moves it up or to the left.Parameters

 howManyPages the number of pages to move the scrollbar 
 
 notification whether to send a notification of the change to listeners. A notification will only be sent if the position has changed. 



Returnstrue if the scrollbar's position actually changed.