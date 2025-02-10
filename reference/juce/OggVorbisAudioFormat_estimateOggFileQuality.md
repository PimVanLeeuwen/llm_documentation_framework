#### estimateOggFileQuality()


 int OggVorbisAudioFormat::estimateOggFileQuality ( const File & source ) 
 

Tries to estimate the quality level of an ogg file based on its size.If it can't read the file for some reason, this will just return 1 (medium quality), otherwise it will return the approximate quality setting that would have been used to create the file.See alsogetQualityOptions