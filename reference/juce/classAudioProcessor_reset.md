#### reset()


 virtual void AudioProcessor::reset ( ) virtual 
 

A plugin can override this to be told when it should reset any playing voices.The default implementation does nothing, but a host may call this to tell the plugin that it should stop any tails or sounds that have been left running.Reimplemented in AudioProcessorGraph.