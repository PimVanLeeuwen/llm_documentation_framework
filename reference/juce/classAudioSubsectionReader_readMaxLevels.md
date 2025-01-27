#### readMaxLevels() [2/2]


 virtual void AudioFormatReader::readMaxLevels ( int64 startSample, int64 numSamples, float & lowestLeft, float & highestLeft, float & lowestRight, float & highestRight ) virtual 
 

Finds the highest and lowest sample levels from a section of the audio stream.This will read a block of samples from the stream, and measure the highest and lowest sample levels from the channels in that section, returning these as normalised floatingpoint levels.Parameters

 startSample the offset into the audio stream to start reading from. It's ok for this to be beyond the start or end of the stream. 
 
 numSamples how many samples to read 
 lowestLeft on return, this is the lowest absolute sample from the left channel 
 highestLeft on return, this is the highest absolute sample from the left channel 
 lowestRight on return, this is the lowest absolute sample from the right channel (if there is one) 
 highestRight on return, this is the highest absolute sample from the right channel (if there is one) 



See alsoread Reimplemented from AudioFormatReader.