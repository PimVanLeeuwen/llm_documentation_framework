#### snapToZero()


template<typename SampleType > 

 void dsp::BallisticsFilter< SampleType >::snapToZero ( ) noexcept 
 

Ensure that the state variables are rounded to zero if the state variables are denormals.This is only needed if you are doing sample by sample processing.Referenced by dsp::BallisticsFilter< SampleType >::process().