#### setRight()


template<typename ValueType > 

 void Rectangle< ValueType >::setRight ( ValueType newRight ) noexcept 
 

Adjusts the width so that the righthand edge of the rectangle has this new value.If the new right is below the current X value, the X will be pushed down to match it.See alsogetRight, withRight References jmin().