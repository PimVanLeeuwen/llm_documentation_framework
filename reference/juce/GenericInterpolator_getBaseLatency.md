#### getBaseLatency()


template<class InterpolatorTraits , int memorySize> 

 static constexpr float GenericInterpolator< InterpolatorTraits, memorySize >::getBaseLatency ( ) staticconstexprnoexcept 
 

Returns the latency of the interpolation algorithm in isolation.In the context of resampling the total latency of a process using the interpolator is the base latency divided by the speed ratio.