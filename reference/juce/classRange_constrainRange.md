#### constrainRange()


template<typename ValueType > 

 Range Range< ValueType >::constrainRange ( Range< ValueType > rangeToConstrain ) const noexcept 
 

Returns a given range, after moving it forwards or backwards to fit it within this range.If the supplied range has a greater length than this one, the return value will be this range.Otherwise, if the supplied range is smaller than this one, the return value will be the new range, shifted forwards or backwards so that it doesn't extend beyond this one, but keeping its original length.References Range< ValueType >::getLength(), and jlimit().