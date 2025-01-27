#### operator=() [2/2]


template<class ElementType , bool throwOnFailure = false> 
template<class OtherElementType , bool otherThrowOnFailure, typename = AllowConversion<OtherElementType>> 

 HeapBlock & HeapBlock< ElementType, throwOnFailure >::operator= ( HeapBlock< OtherElementType, otherThrowOnFailure > && other ) noexcept 
 

Converting move assignment operator.Only enabled if this is a HeapBlock<Base\*> and the other object is a HeapBlock<Derived\*>, where std::is\_base\_of\_v<Base, Derived> == true.References HeapBlock< ElementType, throwOnFailure >::free().