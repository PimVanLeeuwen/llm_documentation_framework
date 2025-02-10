#### addCopyOfList()


template<class ObjectType > 

 void LinkedListPointer< ObjectType >::addCopyOfList ( const LinkedListPointer< ObjectType > & other ) 
 

Creates copies of all the items in another list and adds them to this one.This will use the ObjectType's copy constructor to try to create copies of each item in the other list, and appends them to this list.