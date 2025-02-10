#### getQualityOptions()


 virtual StringArray AudioFormat::getQualityOptions ( ) virtual 
 

Returns a list of different qualities that can be used when writing.Noncompressed formats will just return an empty array, but for something like OggVorbis or MP3, it might return a list of bitrates, etc.When calling createWriterFor(), an index from this array is passed in to tell the format which option is required.Reimplemented in FlacAudioFormat, LAMEEncoderAudioFormat, MP3AudioFormat, and OggVorbisAudioFormat.