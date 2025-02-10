#### removeFromBottom()


template<typename ValueType > 

 Rectangle Rectangle< ValueType >::removeFromBottom ( ValueType amountToRemove ) noexcept 
 

Removes a strip from the bottom of this rectangle, reducing this rectangle by the specified amount and returning the section that was removed.E.g. if this rectangle is (100, 100, 300, 300) and amountToRemove is 50, this will return (100, 350, 300, 50) and leave this rectangle as (100, 100, 300, 250).If amountToRemove is greater than the height of this rectangle, it'll be clipped to that value.References jmin().