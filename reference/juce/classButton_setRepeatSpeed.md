#### setRepeatSpeed()


 void Button::setRepeatSpeed ( int initialDelayInMillisecs, int repeatDelayInMillisecs, int minimumDelayInMillisecs = 1 ) noexcept 
 

Sets an autorepeat speed for the button when it is held down.(Autorepeat is disabled by default).Parameters

 initialDelayInMillisecs how long to wait after the mouse is pressed before triggering the next click. If this is zero, autorepeat is disabled 
 
 repeatDelayInMillisecs the frequently subsequent repeated clicks should be triggered 
 minimumDelayInMillisecs if this is greater than 0, the autorepeat speed will get faster, the longer the button is held down, up to the minimum interval specified here