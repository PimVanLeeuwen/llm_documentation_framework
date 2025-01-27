#### bwavTimeReference


 const char\* const WavAudioFormat::bwavTimeReference static 
 

Metadata property name used in BWAV chunks.This is the number of samples from the start of an edit that the file is supposed to begin at. Seems like an obvious mistake to only allow a file to occur in an edit once, but that's the way it is..See alsoAudioFormatReader::metadataValues, createWriterFor