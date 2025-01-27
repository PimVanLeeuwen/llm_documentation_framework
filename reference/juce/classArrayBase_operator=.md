#### operator=() [2/2]


template<class ElementType , class TypeOfCriticalSectionToUse > 
template<class OtherElementType , class OtherCriticalSection , typename = AllowConversion<OtherElementType, OtherCriticalSection>> 

 ArrayBase & ArrayBase< ElementType, TypeOfCriticalSectionToUse >::operator= ( ArrayBase< OtherElementType, OtherCriticalSection > && other ) noexcept 
 

Converting move assignment operator.Only enabled when the other array has a different type to this one. If you see a compile error here, it's probably because you're attempting a conversion that HeapBlock won't allow.