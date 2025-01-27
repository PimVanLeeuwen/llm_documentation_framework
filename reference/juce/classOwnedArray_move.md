#### move()


template<class ObjectClass , class TypeOfCriticalSectionToUse = DummyCriticalSection> 

 void OwnedArray< ObjectClass, TypeOfCriticalSectionToUse >::move ( int currentIndex, int newIndex ) noexcept 
 

Moves one of the objects to a different position.This will move the object to a specified index, shuffling along any intervening elements as required.So for example, if you have the array { 0, 1, 2, 3, 4, 5 } then calling move (2, 4) would result in { 0, 1, 3, 4, 2, 5 }.Parameters

 currentIndex the index of the object to be moved. If this isn't a valid index, then nothing will be done 
 
 newIndex the index at which you'd like this object to end up. If this is less than zero, it will be moved to the end of the array 


References OwnedArray< ObjectClass, TypeOfCriticalSectionToUse >::getLock().