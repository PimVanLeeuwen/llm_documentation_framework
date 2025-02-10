#### setMousePosition()


 static void Desktop::setMousePosition ( Point< int > newPosition ) static 
 

Makes the mouse pointer jump to a given location.The coordinates are relative to the topleft of the main monitor. Note that this is a pretty old method, kept around mainly for backwardscompatibility, and you should use the MouseInputSource class directly in new code.