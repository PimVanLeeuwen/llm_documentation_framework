#### setSkewForCentre()


template<typename ValueType > 

 void NormalisableRange< ValueType >::setSkewForCentre ( ValueType centrePointValue ) noexcept 
 

Given a value which is between the start and end points, this sets the skew such that convertFrom0to1 (0.5) will return this value.If you have used lambda functions for convertFrom0to1Func and convertFrom0to1Func in the constructor of this class then the skew value is ignored.Parameters

 centrePointValue this must be greater than the start of the range and less than the end. 
 


References NormalisableRange< ValueType >::end, jassert, NormalisableRange< ValueType >::skew, NormalisableRange< ValueType >::start, and NormalisableRange< ValueType >::symmetricSkew.

Member Data Documentation