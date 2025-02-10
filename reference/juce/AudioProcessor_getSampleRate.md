#### getSampleRate()


 double AudioProcessor::getSampleRate ( ) const noexcept 
 

Returns the current sample rate.This can be called from your processBlock() method it's not guaranteed to be valid at any other time, and may return 0 if it's unknown.