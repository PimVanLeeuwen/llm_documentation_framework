#### snapToZero()


template<typename SampleType > 

 void dsp::StateVariableTPTFilter< SampleType >::snapToZero ( ) noexcept 
 

Ensure that the state variables are rounded to zero if the state variables are denormals.This is only needed if you are doing sample by sample processing.Referenced by dsp::StateVariableTPTFilter< SampleType >::process().