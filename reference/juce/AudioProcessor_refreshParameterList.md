#### refreshParameterList()


 virtual void AudioProcessor::refreshParameterList ( ) virtual 
 

A processor should implement this method so that the host can ask it to rebuild its parameter tree.For most plugins it's enough to simply add your parameters in the constructor and leave this unimplemented.