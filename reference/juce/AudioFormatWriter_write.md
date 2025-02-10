#### write()


 virtual bool AudioFormatWriter::write ( const int \*\* samplesToWrite, int numSamples ) pure virtual 
 

Writes a set of samples to the audio stream.Note that if you're trying to write the contents of an AudioBuffer, you can use writeFromAudioSampleBuffer().Parameters

 samplesToWrite an array of arrays containing the sample data for each channel to write. This is a zeroterminated array of arrays, and can contain a different number of channels than the actual stream uses, and the writer should do its best to cope with this. If the format is fixedpoint, each channel will be formatted as an array of signed integers using the full 32bit range 0x80000000 to 0x7fffffff, regardless of the source's bitdepth. If it is a floatingpoint format, you should treat the arrays as arrays of floats, and just cast it to an (int\*\*) to pass it into the method. 
 
 numSamples the number of samples to write