#### removeFromRight()


template<typename ValueType > 

 Rectangle Rectangle< ValueType >::removeFromRight ( ValueType amountToRemove ) noexcept 
 

Removes a strip from the righthand edge of this rectangle, reducing this rectangle by the specified amount and returning the section that was removed.E.g. if this rectangle is (100, 100, 300, 300) and amountToRemove is 50, this will return (350, 100, 50, 300) and leave this rectangle as (100, 100, 250, 300).If amountToRemove is greater than the width of this rectangle, it'll be clipped to that value.References jmin().