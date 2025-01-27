#### getArrayOfWritePointers()


template<typename Type > 

 Type \*const \* AudioBuffer< Type >::getArrayOfWritePointers ( ) noexcept 
 

Returns an array of pointers to the channels in the buffer.Don't modify any of the pointers that are returned, and bear in mind that these will become invalid if the buffer is resized.This will mark the buffer as not cleared and the hasBeenCleared method will return false after this call. If you retain this write pointer and write some data to the buffer after calling its clear method, subsequent clear calls will do nothing. To avoid this either call this method each time you need to write data, or use the setNotClear method to force the internal cleared flag to false.See alsosetNotClear Referenced by AudioProcessor::getBusBuffer().