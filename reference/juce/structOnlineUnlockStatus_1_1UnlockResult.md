This provides some details about the reply that the server gave in a call to attemptWebserverUnlock().

Member Data Documentation


◆ errorMessage


 String OnlineUnlockStatus::UnlockResult::errorMessage 
 

If an unlock operation fails, this is the error message that the webserver supplied (or a message saying that the server couldn't be contacted)

◆ informativeMessage


 String OnlineUnlockStatus::UnlockResult::informativeMessage 
 

This is a message that the webserver returned, and which the user should be shown.It's not necessarily an error message, e.g. it might say that there's a new version of the app available or some other status update.

◆ urlToLaunch


 String OnlineUnlockStatus::UnlockResult::urlToLaunch 
 

If the webserver wants the user to be directed to a webpage for further information, this is the URL that it would like them to go to.

◆ succeeded


 bool OnlineUnlockStatus::UnlockResult::succeeded 
 

If the unlock operation succeeded, this will be set to true.

The documentation for this struct was generated from the following file:juce\_OnlineUnlockStatus.h
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