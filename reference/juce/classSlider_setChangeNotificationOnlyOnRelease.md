#### setChangeNotificationOnlyOnRelease()


 void Slider::setChangeNotificationOnlyOnRelease ( bool onlyNotifyOnRelease ) 
 

Tells the slider whether to keep sending change messages while the user is dragging the slider.If set to true, a change message will only be sent when the user has dragged the slider and let go. If set to false (the default), then messages will be continuously sent as they drag it while the mouse button is still held down.