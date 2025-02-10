#### withShortenedEnd()


template<typename ValueType > 

 Line Line< ValueType >::withShortenedEnd ( ValueType distanceToShortenBy ) const noexcept 
 

Returns a shortened copy of this line.This will chop off part of the end of this line by a certain amount, (leaving the startpoint the same), and return the new line.References Line< ValueType >::getLength(), Line< ValueType >::getPointAlongLine(), and jmin().Referenced by Line< ValueType >::withLengthenedEnd().