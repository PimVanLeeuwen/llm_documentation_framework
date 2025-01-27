#### setCurrentProgramStateInformation()


 virtual void AudioProcessor::setCurrentProgramStateInformation ( const void \* data, int sizeInBytes ) virtual 
 

The host will call this method if it wants to restore the state of just the processor's current program.Not all hosts support this, and if you don't implement it, the base class method just calls setStateInformation() instead. If you do implement it, be sure to also implement getCurrentProgramStateInformation.See alsosetStateInformation, getCurrentProgramStateInformation