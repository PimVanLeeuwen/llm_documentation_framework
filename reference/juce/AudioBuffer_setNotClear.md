#### setNotClear()


template<typename Type > 

 void AudioBuffer< Type >::setNotClear ( ) noexcept 
 

Forces the internal cleared flag of the buffer to false.This may be useful in the case where you are holding on to a write pointer and call the clear method before writing some data. You can then use this method to mark the buffer as containing data so that subsequent clear calls will succeed. However a better solution is to call getWritePointer each time you need to write data.