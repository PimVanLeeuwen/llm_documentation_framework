#### productDownloadFinished()


 virtual void InAppPurchases::Listener::productDownloadFinished ( Download & , const URL & ) virtual 
 

iOS only: Called when a product download finishes (successfully or not).Call Download::getStatus() to check if the downloaded finished successfully.It is your responsibility to move the download content into your app directory and to clean up any files that are no longer needed.After the download is finished, the download object is destroyed and should not be accessed anymore.

The documentation for this struct was generated from the following file:juce\_InAppPurchases.h
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