This namespace contains a few template classes for helping work out class type variations.

Typedef Documentation


◆ SmallestFloatType


template<typename Type > 

 using TypeHelpers::SmallestFloatType = std::conditional\_t<std::is\_same\_v<Type, double>, double, float> 
 

These templates are designed to take a type, and if it's a double, they return a double type; for anything else, they return a float type.


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