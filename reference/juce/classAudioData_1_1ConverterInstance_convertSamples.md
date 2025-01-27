#### convertSamples() [2/2]


template<class SourceSampleType , class DestSampleType > 

 void AudioData::ConverterInstance< SourceSampleType, DestSampleType >::convertSamples ( void \* destSamples, int destSubChannel, const void \* sourceSamples, int sourceSubChannel, int numSamples ) const overridevirtual 
 

Converts a sequence of samples from the converter's source format into the dest format.This method takes subchannel indexes, which can be used with interleaved formats in order to choose a particular subchannel of the data to be used.Implements AudioData::Converter.References addBytesToPointer(), and jassert.