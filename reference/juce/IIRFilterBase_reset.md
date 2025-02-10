#### reset()


template<typename Mutex > 

 void IIRFilterBase< Mutex >::reset ( ) noexcept 
 

Resets the filter's processing pipeline, ready to start a new stream of data.Note that this clears the processing state, but the type of filter and its coefficients aren't changed. To put a filter into an inactive state, use the makeInactive() method.