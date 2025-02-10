#### getMouseSource()


 MouseInputSource \* Desktop::getMouseSource ( int index ) const noexcept 
 

Returns one of the system's MouseInputSource objects.The index should be from 0 to getNumMouseSources() 1. Outofrange indexes will return a null pointer. In a traditional singlemouse system, there might be only one object. On a multitouch system, there could be one input source per potential finger.