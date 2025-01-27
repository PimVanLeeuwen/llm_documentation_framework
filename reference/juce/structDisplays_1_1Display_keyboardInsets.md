#### keyboardInsets


 BorderSize<int> Displays::Display::keyboardInsets 
 

Represents the area of this display in logical pixels that is obscured by an onscreen keyboard.This is currently only supported on iOS, and on Android 11+.This will only return the bounds of the keyboard when it is in 'docked' mode. If the keyboard is floating (e.g. on an iPad using the split keyboard mode), no insets will be reported.