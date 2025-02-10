#### interleaveSamples()


template<typename... SourceFormat, typename... DestFormat> 

 static void AudioData::interleaveSamples ( NonInterleavedSource< SourceFormat... > source, InterleavedDest< DestFormat... > dest, int numSamples ) static 
 

A helper function for converting a sequence of samples from a noninterleaved source to an interleaved destination.When calling this method you need to specify the source and destination data format and endianness from the AudioData SampleFormat and Endianness types and provide the data and number of channels for each. For example, to convert a floatingpoint stream of big endian samples to an interleaved, native endian stream of 16bit integer samples you would do the following:using SourceFormat = AudioData::Format<AudioData::Float32, AudioData::BigEndian>;
using DestFormat = AudioData::Format<AudioData::Int16, AudioData::NativeEndian>;
 
AudioData::interleaveSamples (AudioData::NonInterleavedSource<SourceFormat> { sourceData, numSourceChannels },
 AudioData::InterleavedDest<DestFormat> { destData, numDestChannels },
 numSamples);
AudioData::interleaveSamplesstatic void interleaveSamples(NonInterleavedSource< SourceFormat... > source, InterleavedDest< DestFormat... > dest, int numSamples)A helper function for converting a sequence of samples from a noninterleaved source to an interleave...Definition juce\_AudioDataConverters.h:738
AudioData::InterleavedDestChannelData< true, false, Format... > InterleavedDestA sequence of interleaved samples used as the destination for the interleaveSamples() method.Definition juce\_AudioDataConverters.h:714
AudioData::NonInterleavedSourceChannelData< false, true, Format... > NonInterleavedSourceA sequence of noninterleaved samples used as the source for the interleaveSamples() method.Definition juce\_AudioDataConverters.h:716
AudioData::FormatA struct that contains a SampleFormat and Endianness to be used with the source and destination types...Definition juce\_AudioDataConverters.h:669
References addBytesToPointer().