#### getBus() [2/2]


 const Bus \* AudioProcessor::getBus ( bool isInput, int busIndex ) const noexcept 
 

Returns the audio bus with a given index and direction.If busIndex is invalid then this method will return a nullptr.