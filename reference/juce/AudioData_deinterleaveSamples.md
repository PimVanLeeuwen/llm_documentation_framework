#### deinterleaveSamples()


template<typename... SourceFormat, typename... DestFormat> 

 static void AudioData::deinterleaveSamples ( InterleavedSource< SourceFormat... > source, NonInterleavedDest< DestFormat... > dest, int numSamples ) static 
 

A helper function for converting a sequence of samples from an interleaved source to a noninterleaved destination.When calling this method you need to specify the source and destination data format and endianness from the AudioData SampleFormat and Endianness types and provide the data and number of channels for each. For example, to convert a floatingpoint stream of big endian samples to an noninterleaved, native endian stream of 16bit integer samples you would do the following:using SourceFormat = AudioData::Format<AudioData::Float32, AudioData::BigEndian>;
using DestFormat = AudioData::Format<AudioData::Int16, AudioData::NativeEndian>;
 
AudioData::deinterleaveSamples (AudioData::InterleavedSource<SourceFormat> { sourceData, numSourceChannels },
 AudioData::NonInterleavedDest<DestFormat> { destData, numDestChannels },
 numSamples);
AudioData::deinterleaveSamplesstatic void deinterleaveSamples(InterleavedSource< SourceFormat... > source, NonInterleavedDest< DestFormat... > dest, int numSamples)A helper function for converting a sequence of samples from an interleaved source to a noninterleave...Definition juce\_AudioDataConverters.h:782
AudioData::NonInterleavedDestChannelData< false, false, Format... > NonInterleavedDestA sequence of noninterleaved samples used as the destination for the deinterleaveSamples() method.Definition juce\_AudioDataConverters.h:718
AudioData::InterleavedSourceChannelData< true, true, Format... > InterleavedSourceA sequence of interleaved samples used as the source for the deinterleaveSamples() method.Definition juce\_AudioDataConverters.h:712
References addBytesToPointer().