#### moveScrollbarInSteps()


 bool ScrollBar::moveScrollbarInSteps ( int howManySteps, 
 
 NotificationType notification = sendNotificationAsync ) 

Moves the scrollbar by a number of singlesteps.This will move the bar by a multiple of its singlestep interval (as specified using the setSingleStepSize() method).A positive value here will move the bar down or to the right, a negative value moves it up or to the left.Parameters

 howManySteps the number of steps to move the scrollbar 
 
 notification whether to send a notification of the change to listeners. A notification will only be sent if the position has changed. 



Returnstrue if the scrollbar's position actually changed.