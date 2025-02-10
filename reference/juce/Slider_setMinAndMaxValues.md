#### setMinAndMaxValues()


 void Slider::setMinAndMaxValues ( double newMinValue, 
 
 double newMaxValue, 
 NotificationType notification = sendNotificationAsync ) 

For a slider with two or three thumbs, this sets the minimum and maximum thumb positions.This will trigger a callback to Slider::Listener::sliderValueChanged() for any listeners that are registered, and will synchronously call the valueChanged() method in case subclasses want to handle it.Parameters

 newMinValue the new minimum value to set this will be snapped to the nearest interval if one has been set. 
 
 newMaxValue the new minimum value to set this will be snapped to the nearest interval if one has been set. 
 notification can be one of the NotificationType values, to request a synchronous or asynchronous call to the valueChanged() method of any Slider::Listeners that are registered. A notification will only be sent if one or more of the values has changed. 



See alsosetMaxValue, setMinValue, setValue