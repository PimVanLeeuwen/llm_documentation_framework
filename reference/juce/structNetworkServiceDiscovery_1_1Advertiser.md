An object which runs a thread to repeatedly broadcast the existence of a discoverable service.To use, simply create an instance of an Advertiser and it'll broadcast until you delete it.

Constructor & Destructor Documentation


◆ Advertiser()


 NetworkServiceDiscovery::Advertiser::Advertiser ( const String & serviceTypeUID, 
 
 const String & serviceDescription, 
 int broadcastPort, 
 int connectionPort, 
 RelativeTime minTimeBetweenBroadcasts = RelativeTime::seconds(1.5) ) 

Creates and starts an Advertiser thread, broadcasting with the given properties.Parameters

 serviceTypeUID A usersupplied string to define the type of service this represents 
 
 serviceDescription A description string that will appear in the Service::description field for clients 
 broadcastPort The port number on which to broadcast the service discovery packets 
 connectionPort The port number that will be sent to appear in the Service::port field 
 minTimeBetweenBroadcasts The interval to wait between sending broadcast messages 





◆ ~Advertiser()


 NetworkServiceDiscovery::Advertiser::~Advertiser ( ) override 
 

Destructor.

The documentation for this struct was generated from the following file:juce\_NetworkServiceDiscovery.h
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