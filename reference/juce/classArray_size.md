#### size()


template<typename ElementType , typename TypeOfCriticalSectionToUse = DummyCriticalSection, int minimumAllocatedSize = 0> 

 int Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::size ( ) const noexcept 
 

Returns the current number of elements in the array.References Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::getLock().Referenced by HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::clear(), SelectedItemSet< SelectableItemType >::deselectAll(), dsp::FIR::Coefficients< NumericType >::getFilterOrder(), Grid::getNumberOfColumns(), Grid::getNumberOfRows(), StretchableObjectResizer::getNumItems(), dsp::LookupTable< FloatType >::getNumPoints(), SparseSet< Type >::getNumRanges(), SelectedItemSet< SelectableItemType >::getNumSelected(), HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::getNumSlots(), dsp::Polynomial< FloatingType >::getOrder(), dsp::Polynomial< FloatingType >::getProductWith(), dsp::Polynomial< FloatingType >::getSumWith(), Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::isEmpty(), dsp::LookupTable< FloatType >::isInitialised(), dsp::Polynomial< FloatingType >::operator()(), SelectedItemSet< SelectableItemType >::operator=(), dsp::Oscillator< SampleType >::process(), SparseSet< Type >::removeRange(), and SelectedItemSet< SelectableItemType >::selectOnly().