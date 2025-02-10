#### getVariance()


template<typename FloatType > 

 FloatType StatisticsAccumulator< FloatType >::getVariance ( ) const noexcept 
 

Returns the variance of all previously added values.If no values have been added yet, this will return zero.Referenced by StatisticsAccumulator< FloatType >::getStandardDeviation().