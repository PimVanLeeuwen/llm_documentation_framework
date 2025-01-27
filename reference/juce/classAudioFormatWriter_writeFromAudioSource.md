#### writeFromAudioSource()


 bool AudioFormatWriter::writeFromAudioSource ( AudioSource & source, 
 
 int numSamplesToRead, 
 int samplesPerBlock = 2048 ) 

Reads some samples from an AudioSource, and writes these to the output.The source must already have been initialised with the AudioSource::prepareToPlay() methodParameters

 source the source to read from 
 
 numSamplesToRead total number of samples to read and write 
 samplesPerBlock the maximum number of samples to fetch from the source 



Returnsfalse if it can't read or write properly during the operation