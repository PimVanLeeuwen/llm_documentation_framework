#### setAvailableRange()


 void KeyboardComponentBase::setAvailableRange ( int lowestNote, 
 
 int highestNote ) 

Sets the range of midi notes that the keyboard will be limited to.By default the range is 0 to 127 (inclusive), but you can limit this if you only want a restricted set of the keys to be shown.Note that the values here are inclusive and must be between 0 and 127.