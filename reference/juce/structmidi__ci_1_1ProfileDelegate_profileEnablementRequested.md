#### profileEnablementRequested()


 virtual void midi\_ci::ProfileDelegate::profileEnablementRequested ( MUID x, ProfileAtAddress profileAtAddress, int numChannels, bool enabled ) pure virtual 
 

Called when a remote device requests that a profile is enabled or disabled.Old MIDICI implementations on remote devices may request that a profile is enabled with zero channels active in this situation, it is recommended that you use ProfileHost::enableProfile to enable the default number of channels for that profile.Additionally, profiles for entire groups or function blocks may be enabled with zero active channels. In this case, the profile should be enabled on the entire group or function block.

The documentation for this struct was generated from the following file:juce\_CIProfileDelegate.h
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