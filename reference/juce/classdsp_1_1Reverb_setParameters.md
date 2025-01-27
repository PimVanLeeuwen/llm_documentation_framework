#### setParameters()


 void dsp::Reverb::setParameters ( const Parameters & newParams ) 
 

Applies a new set of parameters to the reverb.Note that this doesn't attempt to lock the reverb, so if you call this in parallel with the process method, you may get artifacts.