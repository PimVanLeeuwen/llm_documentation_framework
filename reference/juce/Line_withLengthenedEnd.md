#### withLengthenedEnd()


template<typename ValueType > 

 Line Line< ValueType >::withLengthenedEnd ( ValueType distanceToLengthenBy ) const noexcept 
 

Returns a lengthened copy of this line.This will extend the line by a certain amount by moving the end away from the start (leaving the startpoint the same), and return the new line.References Line< ValueType >::withShortenedEnd().