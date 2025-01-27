#### supportsDoublePrecisionProcessing()


 virtual bool AudioProcessor::supportsDoublePrecisionProcessing ( ) const virtual 
 

Returns true if the Audio processor supports double precision floating point processing.The default implementation will always return false. If you return true here then you must override the double precision versions of processBlock. Additionally, you must call getProcessingPrecision() in your prepareToPlay method to determine the precision with which you need to allocate your internal buffers.See alsogetProcessingPrecision, setProcessingPrecision Reimplemented in AudioProcessorGraph::AudioGraphIOProcessor, and AudioProcessorGraph.