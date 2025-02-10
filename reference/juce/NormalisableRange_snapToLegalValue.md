#### snapToLegalValue()


template<typename ValueType > 

 ValueType NormalisableRange< ValueType >::snapToLegalValue ( ValueType v ) const noexcept 
 

Takes a nonnormalised value and snaps it based on either the interval property of this NormalisableRange or the lambda function supplied to the constructor.References NormalisableRange< ValueType >::end, NormalisableRange< ValueType >::interval, and NormalisableRange< ValueType >::start.