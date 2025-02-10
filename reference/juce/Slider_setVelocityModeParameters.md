#### setVelocityModeParameters()


 void Slider::setVelocityModeParameters ( double sensitivity = 1.0, 
 
 int threshold = 1, 
 double offset = 0.0, 
 bool userCanPressKeyToSwapMode = true, 
 ModifierKeys::Flags modifiersToSwapModes = ModifierKeys::ctrlAltCommandModifiers ) 

Changes aspects of the scaling used when in velocitysensitive mode.These apply when you've used setVelocityBasedMode() to turn on velocity mode, or if you're holding down ctrl.Parameters

 sensitivity higher values than 1.0 increase the range of acceleration used 
 
 threshold the minimum number of pixels that the mouse needs to move for it to be treated as a movement 
 offset values greater than 0.0 increase the minimum speed that will be used when the threshold is reached 
 userCanPressKeyToSwapMode if true, then the user can hold down the ctrl or command key to toggle velocitysensitive mode 
 modifiersToSwapModes this is a set of modifier flags which will be tested when determining whether to enable/disable velocitysensitive mode