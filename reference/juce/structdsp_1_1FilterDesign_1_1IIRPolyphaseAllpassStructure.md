template<typename FloatType>
struct dsp::FilterDesign< FloatType >::IIRPolyphaseAllpassStructureThe structure returned by the function designIIRLowpassHalfBandPolyphaseAllpassMethod.The two first members of this structure directPath and delayedPath are arrays of IIR::Coefficients, made of polyphase second order allpass filters and an additional delay in the second array, that can be used in cascaded filters processed in two parallel paths, which must be summed at the end to get the high order efficient lowpass filtering. The last member is an array with the useful parameters for simulating the structure using any custom processing function.

Member Data Documentation


◆ directPath


template<typename FloatType > 

 ReferenceCountedArray<IIRCoefficients> dsp::FilterDesign< FloatType >::IIRPolyphaseAllpassStructure::directPath 
 



◆ delayedPath


template<typename FloatType > 

 ReferenceCountedArray<IIRCoefficients> dsp::FilterDesign< FloatType >::IIRPolyphaseAllpassStructure::delayedPath 
 



◆ alpha


template<typename FloatType > 

 Array<double> dsp::FilterDesign< FloatType >::IIRPolyphaseAllpassStructure::alpha 
 



The documentation for this struct was generated from the following file:juce\_FilterDesign.h
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