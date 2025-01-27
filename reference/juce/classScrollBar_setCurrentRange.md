#### setCurrentRange() [2/2]


 void ScrollBar::setCurrentRange ( double newStart, 
 
 double newSize, 
 NotificationType notification = sendNotificationAsync ) 

Changes the position of the scrollbar's 'thumb'.This sets both the position and size of the thumb to just set the position without changing the size, you can use setCurrentRangeStart().Parameters

 newStart the top (or left) of the thumb, in the range getMinimumRangeLimit() <= newStart <= getMaximumRangeLimit(). If the value is beyond these limits, it will be clipped. 
 
 newSize the size of the thumb, such that getMinimumRangeLimit() <= newStart + newSize <= getMaximumRangeLimit(). If the size is beyond these limits, it will be clipped. 
 notification specifies if and how a callback should be made to any listeners if the range actually changes 



See alsosetCurrentRangeStart, getCurrentRangeStart, getCurrentRangeSize