#### convertFrom0to1()


template<typename ValueType > 

 ValueType NormalisableRange< ValueType >::convertFrom0to1 ( ValueType proportion ) const noexcept 
 

Uses the properties of this mapping to convert a normalised 0>1 value to its fullrange representation.References NormalisableRange< ValueType >::end, exactlyEqual(), NormalisableRange< ValueType >::skew, NormalisableRange< ValueType >::start, and NormalisableRange< ValueType >::symmetricSkew.