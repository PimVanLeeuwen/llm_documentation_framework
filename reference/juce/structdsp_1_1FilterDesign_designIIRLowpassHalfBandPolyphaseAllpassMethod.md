#### designIIRLowpassHalfBandPolyphaseAllpassMethod()


template<typename FloatType > 

 static IIRPolyphaseAllpassStructure dsp::FilterDesign< FloatType >::designIIRLowpassHalfBandPolyphaseAllpassMethod ( FloatType normalisedTransitionWidth, FloatType stopbandAmplitudedB ) static 
 

This method generates arrays of IIR::Coefficients for a lowpass filter, with a cutoff frequency at half band, using an algorithm described in the article "Digital Signal Processing Schemes for efficient interpolation and decimation" from Pavel Valenzuela and Constantinides.The result is a IIRPolyphaseAllpassStructure object.The two members of this structure directPath and delayedPath are arrays of IIR::Coefficients, made of polyphase second order allpass filters and an additional delay in the second array, that can be used in cascaded filters processed in two parallel paths, which must be summed at the end to get the high order efficient lowpass filtering.The gain of the resulting passband is 6 dB, so don't forget to compensate it if you want to use that method for something else than two times oversampling.Parameters

 normalisedTransitionWidth the normalised size between 0 and 0.5 of the transition between the pass band and the stop band 
 
 stopbandAmplitudedB the maximum amplitude in dB expected in the stop band (must be negative) 





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