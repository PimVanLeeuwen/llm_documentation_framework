#### withShortenedStart()


template<typename ValueType > 

 Line Line< ValueType >::withShortenedStart ( ValueType distanceToShortenBy ) const noexcept 
 

Returns a shortened copy of this line.This will chop off part of the start of this line by a certain amount, (leaving the endpoint the same), and return the new line.References Line< ValueType >::getLength(), Line< ValueType >::getPointAlongLine(), and jmin().Referenced by Line< ValueType >::withLengthenedStart().