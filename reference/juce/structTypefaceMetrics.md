Font metrics using JUCE conventions.

Member Data Documentation


◆ ascent


 float TypefaceMetrics::ascent {} 
 

The proportion of the typeface's height that it above the baseline, as a value between 0 and 1.Note that 'height' here refers to the result of adding the absolute ascent and descent values. That is, the sum of the ascent and descent will equal 1. The sum of the ascent and descent will normally differ from the em size of the font. That is, for a font size of 14pt, there will be 14 points per em, but the sum of the ascent and descent in points is unlikely to be equal to 14.

◆ heightToPoints


 float TypefaceMetrics::heightToPoints {} 
 

The factor by which a JUCE font height should be multiplied in order to convert to a font size in points.

The documentation for this struct was generated from the following file:juce\_Typeface.h
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