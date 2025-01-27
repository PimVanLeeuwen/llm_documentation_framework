#### makePeakFilter()


template<typename NumericType > 

 static std::array< NumericType, 6 > dsp::IIR::ArrayCoefficients< NumericType >::makePeakFilter ( double sampleRate, NumericType centreFrequency, NumericType Q, NumericType gainFactor ) static 
 

Returns the coefficients for a peak filter centred around a given frequency, with a variable Q and gain.The gain is a scale factor that the centre frequencies are multiplied by, so values greater than 1.0 will boost the centre frequencies, values less than 1.0 will attenuate them.

The documentation for this struct was generated from the following file:juce\_dsp/processors/juce\_IIRFilter.h
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