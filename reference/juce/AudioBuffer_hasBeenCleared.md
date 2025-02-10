#### hasBeenCleared()


template<typename Type > 

 bool AudioBuffer< Type >::hasBeenCleared ( ) const noexcept 
 

Returns true if the buffer has been entirely cleared.Note that this does not actually measure the contents of the buffer it simply returns a flag that is set when the buffer is cleared, and which is reset whenever functions like getWritePointer are invoked. That means the method is quick, but it may return false negatives when in fact the buffer is still empty.Referenced by AudioBuffer< Type >::makeCopyOf().