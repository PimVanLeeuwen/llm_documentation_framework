#### constrainedWithin()


template<typename ValueType > 

 Rectangle Rectangle< ValueType >::constrainedWithin ( Rectangle< ValueType > areaToFitWithin ) const noexcept 
 

Tries to fit this rectangle within a target area, returning the result.If this rectangle is not completely inside the target area, then it'll be shifted (without changing its size) so that it lies within the target. If it is larger than the target rectangle in either dimension, then that dimension will be reduced to fit within the target.References jmin().