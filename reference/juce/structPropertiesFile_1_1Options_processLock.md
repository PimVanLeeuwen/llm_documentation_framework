#### processLock


 InterProcessLock\* PropertiesFile::Options::processLock 
 

An optional InterprocessLock object that will be used to prevent multiple threads or processes from writing to the file at the same time.The PropertiesFile will keep a pointer to this object but will not take ownership of it the caller is responsible for making sure that the lock doesn't get deleted before the PropertiesFile has been deleted. The default constructor initialises this value to nullptr, so you don't need to touch it unless you want to use a lock.

The documentation for this struct was generated from the following file:juce\_PropertiesFile.h
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