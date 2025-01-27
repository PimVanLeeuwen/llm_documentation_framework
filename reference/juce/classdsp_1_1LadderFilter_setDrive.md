#### setDrive()


template<typename SampleType > 

 void dsp::LadderFilter< SampleType >::setDrive ( SampleType newDrive ) noexcept 
 

Sets the amount of saturation in the filter.Parameters

 newDrive saturation amount; it can be any number greater than or equal to one. Higher values result in more distortion.