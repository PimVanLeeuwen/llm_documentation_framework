#### swapWith()


template<typename ValueType > 

 void RectangleList< ValueType >::swapWith ( RectangleList< ValueType > & otherList ) noexcept 
 

Swaps the contents of this and another list.This swaps their internal pointers, so is hugely faster than using copybyvalue to swap them.Referenced by RectangleList< ValueType >::clipTo().