#### isSmoothing()


template<typename SmoothedValueType > 

 bool SmoothedValueBase< SmoothedValueType >::isSmoothing ( ) const noexcept 
 

Returns true if the current value is currently being interpolated.References SmoothedValueBase< SmoothedValueType >::countdown.Referenced by SmoothedValueBase< SmoothedValueType >::applyGain(), SmoothedValueBase< SmoothedValueType >::applyGain(), SmoothedValueBase< SmoothedValueType >::applyGain(), and dsp::Oscillator< SampleType >::process().