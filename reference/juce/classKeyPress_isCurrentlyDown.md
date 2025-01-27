#### isCurrentlyDown()


 bool KeyPress::isCurrentlyDown ( ) const 
 

Checks whether the user is currently holding down the keys that make up this KeyPress.Note that this will return false if any extra modifier keys are down e.g. if the keypress is CTRL+X and the user is actually holding CTRL+ALT+x then it will be false.