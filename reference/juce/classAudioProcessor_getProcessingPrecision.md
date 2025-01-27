#### getProcessingPrecision()


 ProcessingPrecision AudioProcessor::getProcessingPrecision ( ) const noexcept 
 

Returns the precisionmode of the processor.Depending on the result of this method you MUST call the corresponding version of processBlock. The default processing precision is single precision.See alsosetProcessingPrecision, supportsDoublePrecisionProcessing