#### getStandardDeviation()


template<typename FloatType > 

 FloatType StatisticsAccumulator< FloatType >::getStandardDeviation ( ) const noexcept 
 

Returns the standard deviation of all previously added values.If no values have been added yet, this will return zero.References StatisticsAccumulator< FloatType >::getVariance().