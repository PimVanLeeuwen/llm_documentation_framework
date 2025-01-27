#### getPageFileSearchPath()


 virtual File AAXClientExtensions::getPageFileSearchPath ( ) const virtual 
 

Optionally returns a search path for finding a page table file.This can be useful for specifying a location outside the plugin bundle so users can make changes to a page table file without breaking any code signatures.If this function returns a defaultconstructed File, then a default location will be used. The AAX SDK states this location will be `*.aaxplugin/Contents/Resources`.NoteThe returned path should be an absolute path to a directory.
See alsogetPageFileName 


The documentation for this struct was generated from the following file:juce\_AAXClientExtensions.h
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