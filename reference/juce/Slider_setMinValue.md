#### setMinValue()


 void Slider::setMinValue ( double newValue, 
 
 NotificationType notification = sendNotificationAsync, 
 bool allowNudgingOfOtherValues = false ) 

For a slider with two or three thumbs, this sets the lower of its values.This will trigger a callback to Slider::Listener::sliderValueChanged() for any listeners that are registered, and will synchronously call the valueChanged() method in case subclasses want to handle it.Parameters

 newValue the new value to set this will be restricted by the minimum and maximum range, and will be snapped to the nearest interval if one has been set. 
 
 notification can be one of the NotificationType values, to request a synchronous or asynchronous call to the valueChanged() method of any Slider::Listeners that are registered. A notification will only be sent if this value has changed. 
 allowNudgingOfOtherValues if false, this value will be restricted to being below the max value (in a twovalue slider) or the mid value (in a threevalue slider). If true, then if this value goes beyond those values, it will push them along with it. 



See alsogetMinValue, setMaxValue, setValue