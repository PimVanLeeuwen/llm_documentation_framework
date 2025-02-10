#### addValue()


template<typename FloatType > 

 void StatisticsAccumulator< FloatType >::addValue ( FloatType v ) noexcept 
 

Add a new value to the accumulator.This will update all running statistics accordingly.References jassert, and juce\_isfinite().