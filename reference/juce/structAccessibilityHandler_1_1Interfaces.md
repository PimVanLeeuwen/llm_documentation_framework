Utility struct which holds one or more accessibility interfaces.The main purpose of this class is to provide convenience constructors from each of the four types of accessibility interface.

Constructor & Destructor Documentation


◆ Interfaces() [1/6]


 AccessibilityHandler::Interfaces::Interfaces ( ) default 
 



◆ Interfaces() [2/6]


 AccessibilityHandler::Interfaces::Interfaces ( std::unique\_ptr< AccessibilityValueInterface > ptr ) 
 



◆ Interfaces() [3/6]


 AccessibilityHandler::Interfaces::Interfaces ( std::unique\_ptr< AccessibilityTextInterface > ptr ) 
 



◆ Interfaces() [4/6]


 AccessibilityHandler::Interfaces::Interfaces ( std::unique\_ptr< AccessibilityTableInterface > ptr ) 
 



◆ Interfaces() [5/6]


 AccessibilityHandler::Interfaces::Interfaces ( std::unique\_ptr< AccessibilityCellInterface > ptr ) 
 



◆ Interfaces() [6/6]


 AccessibilityHandler::Interfaces::Interfaces ( std::unique\_ptr< AccessibilityValueInterface > valueIn, 
 
 std::unique\_ptr< AccessibilityTextInterface > textIn, 
 std::unique\_ptr< AccessibilityTableInterface > tableIn, 
 std::unique\_ptr< AccessibilityCellInterface > cellIn ) 


Member Data Documentation


◆ value


 std::unique\_ptr<AccessibilityValueInterface> AccessibilityHandler::Interfaces::value 
 



◆ text


 std::unique\_ptr<AccessibilityTextInterface> AccessibilityHandler::Interfaces::text 
 



◆ table


 std::unique\_ptr<AccessibilityTableInterface> AccessibilityHandler::Interfaces::table 
 



◆ cell


 std::unique\_ptr<AccessibilityCellInterface> AccessibilityHandler::Interfaces::cell 
 



The documentation for this struct was generated from the following file:juce\_AccessibilityHandler.h
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