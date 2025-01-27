#### setDoublePrecisionProcessing()


 void AudioProcessorPlayer::setDoublePrecisionProcessing ( bool doublePrecision ) 
 

Switch between double and single floating point precisions processing.The audio IO callbacks will still operate in single floating point precision, however, all internal processing including the AudioProcessor will be processed in double floating point precision if the AudioProcessor supports it (see AudioProcessor::supportsDoublePrecisionProcessing()). Otherwise, the processing will remain single precision irrespective of the parameter doublePrecision.