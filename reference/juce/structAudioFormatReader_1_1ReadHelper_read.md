#### read()


template<class DestSampleType , class SourceSampleType , class SourceEndianness > 
template<typename TargetType > 

 static void AudioFormatReader::ReadHelper< DestSampleType, SourceSampleType, SourceEndianness >::read ( TargetType \*const \* destData, int destOffset, int numDestChannels, const void \* sourceData, int numSourceChannels, int numSamples ) staticnoexcept 
 

References addBytesToPointer(), AudioData::Pointer< SampleFormat, Endianness, InterleavingType, Constness >::clearSamples(), and AudioData::Pointer< SampleFormat, Endianness, InterleavingType, Constness >::convertSamples().

The documentation for this struct was generated from the following file:juce\_AudioFormatReader.h
### Purchase

Get JUCE
### Discover

What's New in JUCEFeatures
### Learn

DocumentaionTutorialsMade with JUCEResources
### Support

JUCE ForumNewsletterArchive
### About

Contact UsJUCE LegalJUCE Licensing FAQ
### Events

Audio Developer Conference
Visit our FacebookVisit our TwitterVisit our LinkedInVisit our YouTube channel© Raw Material Software Limited
linkedin




facebook


pinterest


youtube


rss


twitter


instagram




facebookblank


rssblank


linkedinblank


pinterest


youtube


twitter


instagram