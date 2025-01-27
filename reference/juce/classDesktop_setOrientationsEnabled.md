#### setOrientationsEnabled()


 void Desktop::setOrientationsEnabled ( int allowedOrientations ) 
 

Sets which orientations the display is allowed to autorotate to.For devices that support rotating desktops, this lets you specify which of the orientations your app can use.The parameter is a bitwise ored combination of the values in DisplayOrientation, and must contain at least one set bit.