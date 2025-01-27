#### setRangeLimits() [2/2]


 void ScrollBar::setRangeLimits ( double minimum, 
 
 double maximum, 
 NotificationType notification = sendNotificationAsync ) 

Sets the minimum and maximum values that the bar will move between.The bar's thumb will always be constrained so that the entire thumb lies within this range.Parameters

 minimum the new range minimum. 
 
 maximum the new range maximum. 
 notification whether to send a notification of the change to listeners. A notification will only be sent if the range has changed. 



See alsosetCurrentRange