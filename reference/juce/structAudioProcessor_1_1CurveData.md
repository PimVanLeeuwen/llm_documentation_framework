Some plugins support sharing response curve data with the host so that it can display this curve on a console or in the mixer panel.For example, ProTools allows you to see the total EQ curve of a track. It does this by interrogating each plugin for their internal EQ curve.

Member Enumeration Documentation


◆ Type


 enum class AudioProcessor::CurveData::Type : int strong 
 

Enumerator
 
 EQ 
 Dynamics 
 GainReduction 
 Unknown 


Member Data Documentation


◆ curve


 std::function<float (float)> AudioProcessor::CurveData::curve 
 



◆ xRange


 Range<float> AudioProcessor::CurveData::xRange 
 



◆ yRange


 Range<float> AudioProcessor::CurveData::yRange 
 



◆ xMeterID


 String AudioProcessor::CurveData::xMeterID 
 



◆ yMeterID


 String AudioProcessor::CurveData::yMeterID 
 



The documentation for this struct was generated from the following file:juce\_AudioProcessor.h
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