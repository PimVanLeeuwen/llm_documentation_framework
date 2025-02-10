#### setValue()


 void Slider::setValue ( double newValue, 
 
 NotificationType notification = sendNotificationAsync ) 

Changes the slider's current value.This will trigger a callback to Slider::Listener::sliderValueChanged() for any listeners that are registered, and will synchronously call the valueChanged() method in case subclasses want to handle it.Parameters

 newValue the new value to set this will be restricted by the minimum and maximum range, and will be snapped to the nearest interval if one has been set 
 
 notification can be one of the NotificationType values, to request a synchronous or asynchronous call to the valueChanged() method of any Slider::Listeners that are registered. A notification will only be sent if the Slider's value has changed.