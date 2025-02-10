#### getNumMouseSources()


 int Desktop::getNumMouseSources ( ) const noexcept 
 

Returns the number of MouseInputSource objects the system has at its disposal.In a traditional singlemouse system, there might be only one MouseInputSource. On a multitouch system, there could be one input source per potential finger. The number of mouse sources returned here may increase dynamically as the program runs. To find out how many mouse events are currently happening, use getNumDraggingMouseSources().See alsogetMouseSource