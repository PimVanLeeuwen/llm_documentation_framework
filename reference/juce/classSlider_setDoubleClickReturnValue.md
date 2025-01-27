#### setDoubleClickReturnValue()


 void Slider::setDoubleClickReturnValue ( bool shouldDoubleClickBeEnabled, 
 
 double valueToSetOnDoubleClick, 
 ModifierKeys singleClickModifiers = ModifierKeys::altModifier ) 

This lets you choose whether doubleclicking or singleclicking with a specified key modifier moves the slider to a given position.By default this is turned off, but it's handy if you want either of these actions to act as a quick way of resetting a slider. Just pass in the value you want it to go to when doubleclicked. By default the key modifier is the alt key but you can pass in another key modifier, or none to disable this behaviour.See alsogetDoubleClickReturnValue