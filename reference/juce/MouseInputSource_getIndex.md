#### getIndex()


 int MouseInputSource::getIndex ( ) const noexcept 
 

Returns this source's index in the global list of possible sources.If the system only has a single mouse, there will only be a single MouseInputSource with an index of 0.If the system supports multitouch input, then the index will represent a finger number, starting from 0. When the first touch event begins, it will have finger number 0, and then if a second touch happens while the first is still down, it will have index 1, etc.