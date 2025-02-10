#### writeFromAudioReader()


 bool AudioFormatWriter::writeFromAudioReader ( AudioFormatReader & reader, 
 
 int64 startSample, 
 int64 numSamplesToRead ) 

Reads a section of samples from an AudioFormatReader, and writes these to the output.This will take care of any floatingpoint conversion that's required to convert between the two formats. It won't deal with samplerate conversion, though.If numSamplesToRead < 0, it will write the entire length of the reader.Returnsfalse if it can't read or write properly during the operation