#### getBusBuffer()


template<typename FloatType > 

 AudioBuffer< FloatType > AudioProcessor::getBusBuffer ( AudioBuffer< FloatType > & processBlockBuffer, 
 
 bool isInput, 
 int busIndex ) const 

Returns an AudioBuffer containing a set of channel pointers for a specific bus.This can be called in processBlock to get a buffer containing a subgroup of the master AudioBuffer which contains all the plugin channels.References AudioBuffer< Type >::getArrayOfWritePointers(), and AudioBuffer< Type >::getNumSamples().