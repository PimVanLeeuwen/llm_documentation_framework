#### advance()


template<typename Type > 

 Type dsp::Phase< Type >::advance ( Type increment ) noexcept 
 

Returns the current value, and increments the phase by the given increment.The increment must be a positive value, it can't go backwards! The new value of the phase after calling this function will be (phase + increment) % (2 \* pi).References jassert, and dsp::Phase< Type >::phase.Referenced by dsp::Oscillator< SampleType >::process(), and dsp::Oscillator< SampleType >::processSample().

Member Data Documentation