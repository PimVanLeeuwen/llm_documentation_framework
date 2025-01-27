#### setProcessingPrecision()


 void AudioProcessor::setProcessingPrecision ( ProcessingPrecision newPrecision ) noexcept 
 

Changes the processing precision of the receiver.A client of the AudioProcessor calls this function to indicate which version of processBlock (single or double precision) it intends to call. The client MUST call this function before calling the prepareToPlay method so that the receiver can do any necessary allocations in the prepareToPlay() method. An implementation of prepareToPlay() should call getProcessingPrecision() to determine with which precision it should allocate it's internal buffers.Note that setting the processing precision to double floating point precision on a receiver which does not support double precision processing (i.e. supportsDoublePrecisionProcessing() returns false) will result in an assertion.See alsogetProcessingPrecision, supportsDoublePrecisionProcessing