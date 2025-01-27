#### getReadPointer() [2/2]


template<typename Type > 

 const Type \* AudioBuffer< Type >::getReadPointer ( int channelNumber, int sampleIndex ) const noexcept 
 

Returns a pointer to an array of readonly samples in one of the buffer's channels.For speed, this doesn't check whether the channel number or index are out of range, so be careful when using it!If you need to write to the data, do NOT call this method and const\_cast the result! Instead, you must call getWritePointer so that the buffer knows you're planning on modifying the data.References isPositiveAndBelow(), and jassert.