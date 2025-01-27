#### setVelocityBasedMode()


 void Slider::setVelocityBasedMode ( bool isVelocityBased ) 
 

Changes the way the mouse is used when dragging the slider.If true, this will turn on velocitysensitive dragging, so that the faster the mouse moves, the bigger the movement to the slider. This helps when making accurate adjustments if the slider's range is quite large.If false, the slider will just try to snap to wherever the mouse is.