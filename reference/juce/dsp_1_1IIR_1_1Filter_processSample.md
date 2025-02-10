#### processSample()


template<typename SampleType > 

 SampleType JUCE\_VECTOR\_CALLTYPE dsp::IIR::Filter< SampleType >::processSample ( SampleType sample ) noexcept 
 

Processes a single sample, without any locking.Use this if you need processing of a single value.Moreover, you might need the function snapToZero after a few calls to avoid potential denormalisation issues.