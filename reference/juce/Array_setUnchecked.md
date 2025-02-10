#### setUnchecked()


template<typename ElementType , typename TypeOfCriticalSectionToUse = DummyCriticalSection, int minimumAllocatedSize = 0> 

 void Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::setUnchecked ( int indexToChange, 
 
 ParameterType newValue ) 

Replaces an element with a new value without doing any boundschecking.This just sets a value directly in the array's internal storage, so you'd better make sure it's in range!Parameters

 indexToChange the index whose value you want to change 
 
 newValue the new value to set for this index. 



See alsoset, getUnchecked References Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::getLock(), isPositiveAndBelow(), and jassert.