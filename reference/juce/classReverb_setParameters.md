#### setParameters()


 void Reverb::setParameters ( const Parameters & newParams ) 
 

Applies a new set of parameters to the reverb.Note that this doesn't attempt to lock the reverb, so if you call this in parallel with the process method, you may get artifacts.References Reverb::Parameters::dryLevel, Reverb::Parameters::freezeMode, SmoothedValue< FloatType, SmoothingType >::setTargetValue(), Reverb::Parameters::wetLevel, and Reverb::Parameters::width.Referenced by Reverb().