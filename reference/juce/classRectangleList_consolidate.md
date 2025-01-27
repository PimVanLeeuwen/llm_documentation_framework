#### consolidate()


template<typename ValueType > 

 void RectangleList< ValueType >::consolidate ( ) 
 

Optimises the list into a minimum number of constituent rectangles.This will try to combine any adjacent rectangles into larger ones where possible, to simplify lists that might have been fragmented by repeated add/subtract calls.