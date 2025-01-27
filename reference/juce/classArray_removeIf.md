#### removeIf()


template<typename ElementType , typename TypeOfCriticalSectionToUse = DummyCriticalSection, int minimumAllocatedSize = 0> 
template<typename PredicateType > 

 int Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::removeIf ( PredicateType && predicate ) 
 

Removes items from the array.This will remove all objects from the array that match a condition. If no such items are found, no action is taken.Parameters

 predicate the condition when to remove an item. Must be a callable type that takes an ElementType and returns a bool 
 



Returnshow many objects were removed. 
See alsoremove, removeRange, removeAllInstancesOf References Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::getLock().