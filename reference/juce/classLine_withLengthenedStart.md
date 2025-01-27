#### withLengthenedStart()


template<typename ValueType > 

 Line Line< ValueType >::withLengthenedStart ( ValueType distanceToLengthenBy ) const noexcept 
 

Returns a lengthened copy of this line.This will extend the line by a certain amount by moving the start away from the end (leaving the endpoint the same), and return the new line.References Line< ValueType >::withShortenedStart().