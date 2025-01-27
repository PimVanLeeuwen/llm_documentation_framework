Contains status information about a mouse wheel event.See alsoMouseListener, MouseEvent 

Member Data Documentation


◆ deltaX


 float MouseWheelDetails::deltaX 
 

The amount that the wheel has been moved in the X axis.If isReversed is true, then a negative deltaX means that the wheel has been pushed physically to the left. If isReversed is false, then a negative deltaX means that the wheel has been pushed physically to the right.

◆ deltaY


 float MouseWheelDetails::deltaY 
 

The amount that the wheel has been moved in the Y axis.If isReversed is true, then a negative deltaY means that the wheel has been pushed physically upwards. If isReversed is false, then a negative deltaY means that the wheel has been pushed physically downwards.

◆ isReversed


 bool MouseWheelDetails::isReversed 
 

Indicates whether the user has reversed the direction of the wheel.See deltaX and deltaY for an explanation of the effects of this value.

◆ isSmooth


 bool MouseWheelDetails::isSmooth 
 

If true, then the wheel has continuous, unstepped motion.

◆ isInertial


 bool MouseWheelDetails::isInertial 
 

If true, then this event is part of the inertial momentum phase that follows the wheel being released.

The documentation for this struct was generated from the following file:juce\_MouseEvent.h
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