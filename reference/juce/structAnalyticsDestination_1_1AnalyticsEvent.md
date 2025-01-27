Contains information about an event to be logged.

Member Data Documentation


◆ name


 String AnalyticsDestination::AnalyticsEvent::name 
 

The name of the event.

◆ eventType


 int AnalyticsDestination::AnalyticsEvent::eventType 
 

An optional integer representing the type of the event.You can use this to indicate if the event was a screenview, session start, exception, etc.

◆ timestamp


 uint32 AnalyticsDestination::AnalyticsEvent::timestamp 
 

The timestamp of the event.Timestamps are automatically applied by an Analytics object and are derived from Time::getMillisecondCounter(). As such these timestamps do not represent absolute times, but relative timings of events for each user in each session will be accurate.

◆ parameters


 StringPairArray AnalyticsDestination::AnalyticsEvent::parameters 
 

The parameters of the event.

◆ userID


 String AnalyticsDestination::AnalyticsEvent::userID 
 

The user ID associated with the event.

◆ userProperties


 StringPairArray AnalyticsDestination::AnalyticsEvent::userProperties 
 

Properties associated with the user.

The documentation for this struct was generated from the following file:juce\_AnalyticsDestination.h
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