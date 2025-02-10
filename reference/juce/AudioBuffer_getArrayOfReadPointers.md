#### getArrayOfReadPointers()


template<typename Type > 

 const Type \*const \* AudioBuffer< Type >::getArrayOfReadPointers ( ) const noexcept 
 

Returns an array of pointers to the channels in the buffer.Don't modify any of the pointers that are returned, and bear in mind that these will become invalid if the buffer is resized.