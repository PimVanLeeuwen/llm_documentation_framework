#### getLast()


template<class ObjectType > 

 LinkedListPointer & LinkedListPointer< ObjectType >::getLast ( ) noexcept 
 

Returns the last item in the list which this pointer points to.This will iterate the list and return the last item found. Obviously the speed of this operation will be proportional to the size of the list. If the list is empty the return value will be this object. If you're planning on appending a number of items to your list, it's much more efficient to use the Appender class than to repeatedly call getLast() to find the end.Referenced by LinkedListPointer< ObjectType >::append().