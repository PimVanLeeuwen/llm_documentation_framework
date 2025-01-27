#### createWriterFor() [2/2]


 virtual AudioFormatWriter \* AudioFormat::createWriterFor ( OutputStream \* streamToWriteTo, double sampleRateToUse, const AudioChannelSet & channelLayout, int bitsPerSample, const StringPairArray & metadataValues, int qualityOptionIndex ) virtual 
 

Tries to create an object that can write to a stream with this audio format.The writer object that is returned can be used to write to the stream, and should then be deleted by the caller.If the stream can't be created for some reason (e.g. the parameters passed in here aren't suitable), this will return nullptr.Parameters

 streamToWriteTo the stream that the data will go to this will be deleted by the AudioFormatWriter object when it's no longer needed. If no AudioFormatWriter can be created by this method, the stream will NOT be deleted, so that the caller can reuse it to try to open a different format, etc 
 
 sampleRateToUse the sample rate for the file, which must be one of the ones returned by getPossibleSampleRates() 
 channelLayout the channel layout for the file. Use isChannelLayoutSupported to check if the writer supports this layout. 
 bitsPerSample the bits per sample to use this must be one of the values returned by getPossibleBitDepths() 
 metadataValues a set of metadata values that the writer should try to write to the stream. Exactly what these are depends on the format, and the subclass doesn't actually have to do anything with them if it doesn't want to. Have a look at the specific format implementation classes to see possible values that can be used 
 qualityOptionIndex the index of one of compression qualities returned by the getQualityOptions() method. If there aren't any quality options for this format, just pass 0 in this parameter, as it'll be ignored 



See alsoAudioFormatWriter Reimplemented in AiffAudioFormat, CoreAudioFormat, FlacAudioFormat, LAMEEncoderAudioFormat, MP3AudioFormat, OggVorbisAudioFormat, WavAudioFormat, and WindowsMediaAudioFormat.