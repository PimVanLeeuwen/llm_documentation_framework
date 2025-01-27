#### getWritePointer() [2/2]


template<typename Type > 

 Type \* AudioBuffer< Type >::getWritePointer ( int channelNumber, int sampleIndex ) noexcept 
 

Returns a writeable pointer to one of the buffer's channels.For speed, this doesn't check whether the channel number or index are out of range, so be careful when using it!Note that if you're not planning on writing to the data, you should use getReadPointer instead.This will mark the buffer as not cleared and the hasBeenCleared method will return false after this call. If you retain this write pointer and write some data to the buffer after calling its clear method, subsequent clear calls will do nothing. To avoid this either call this method each time you need to write data, or use the setNotClear method to force the internal cleared flag to false.See alsosetNotClear References isPositiveAndBelow(), and jassert.