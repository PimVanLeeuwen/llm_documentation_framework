#### setSampleRate()


 void Reverb::setSampleRate ( const double sampleRate ) 
 

Sets the sample rate that will be used for the reverb.You must call this before the process methods, in order to tell it the correct sample rate.References jassert, and SmoothedValue< FloatType, SmoothingType >::reset().Referenced by Reverb().