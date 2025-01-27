#### setCurrentRangeStart()


 void ScrollBar::setCurrentRangeStart ( double newStart, 
 
 NotificationType notification = sendNotificationAsync ) 

Moves the bar's thumb position.This will move the thumb position without changing the thumb size. Note that the maximum thumb start position is (getMaximumRangeLimit() getCurrentRangeSize()).If this method call actually changes the scrollbar's position, it will trigger an asynchronous call to ScrollBar::Listener::scrollBarMoved() for all the listeners that are registered.See alsosetCurrentRange