This structure is passed into a DSP algorithm's prepare() method, and contains information about various aspects of the context in which it can expect to be called.

Member Data Documentation


◆ sampleRate


 double dsp::ProcessSpec::sampleRate 
 

The sample rate that will be used for the data that is sent to the processor.Referenced by dsp::Reverb::prepare().

◆ maximumBlockSize


 uint32 dsp::ProcessSpec::maximumBlockSize 
 

The maximum number of samples that will be in the blocks sent to process() method.

◆ numChannels


 uint32 dsp::ProcessSpec::numChannels 
 

The number of channels that the process() method will be expected to handle.Referenced by dsp::ProcessorDuplicator< MonoProcessorType, StateType >::prepare().

The documentation for this struct was generated from the following file:juce\_ProcessContext.h
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