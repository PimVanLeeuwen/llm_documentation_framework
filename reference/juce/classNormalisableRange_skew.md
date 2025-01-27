#### skew


template<typename ValueType > 

 ValueType NormalisableRange< ValueType >::skew = 1 
 

An optional skew factor that alters the way values are distribute across the range.The skew factor lets you skew the mapping logarithmically so that larger or smaller values are given a larger proportion of the available space.A factor of 1.0 has no skewing effect at all. If the factor is < 1.0, the lower end of the range will fill more of the slider's length; if the factor is > 1.0, the upper end of the range will be expanded.If you have used lambda functions for convertFrom0to1Func and convertFrom0to1Func in the constructor of this class then the skew value is ignored.Referenced by NormalisableRange< ValueType >::convertFrom0to1(), NormalisableRange< ValueType >::convertTo0to1(), and NormalisableRange< ValueType >::setSkewForCentre().