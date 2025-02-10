#### interval


template<typename ValueType > 

 ValueType NormalisableRange< ValueType >::interval = 0 
 

The snapping interval that should be used (for a nonnormalised value).Use 0 for a continuous range.If you have used a lambda function for snapToLegalValueFunction in the constructor of this class then the interval is ignored.Referenced by NormalisableRange< ValueType >::snapToLegalValue().