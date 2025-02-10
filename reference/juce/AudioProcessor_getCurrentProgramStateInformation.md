#### getCurrentProgramStateInformation()


 virtual void AudioProcessor::getCurrentProgramStateInformation ( juce::MemoryBlock & destData ) virtual 
 

The host will call this method if it wants to save the state of just the processor's current program.Unlike getStateInformation, this should only return the current program's state.Not all hosts support this, and if you don't implement it, the base class method just calls getStateInformation() instead. If you do implement it, be sure to also implement getCurrentProgramStateInformation.See alsogetStateInformation, setCurrentProgramStateInformation