#### setAttackTime()


template<typename SampleType > 

 void dsp::BallisticsFilter< SampleType >::setAttackTime ( SampleType attackTimeMs ) 
 

Sets the attack time in ms.Attack times less than 0.001 ms will be snapped to zero and very long attack times will eventually saturate depending on the numerical precision used.