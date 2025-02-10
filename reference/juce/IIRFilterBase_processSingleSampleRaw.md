#### processSingleSampleRaw()


template<typename Mutex > 

 float IIRFilterBase< Mutex >::processSingleSampleRaw ( float sample ) noexcept 
 

Processes a single sample, without any locking or checking.Use this if you need fast processing of a single value, but be aware that this isn't threadsafe in the way that processSamples() is.