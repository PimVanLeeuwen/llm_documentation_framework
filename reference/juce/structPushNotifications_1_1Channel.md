Android API level 26 or higher only: Represents notification channel through which notifications will be sent.Starting from Android API level 26, you should call setupChannels() at the start of your application, before posting any notifications. Then, when sending notifications, assign a channel to each created notification.

Member Enumeration Documentation


◆ Importance


 enum PushNotifications::Channel::Importance 
 

Controls how interruptive the notification posted on this channel are.

Enumerator
 
 none 
 min 
 low 
 normal 
 high 
 max 


Member Data Documentation


◆ identifier


 String PushNotifications::Channel::identifier 
 

Required: Unique channel identifier.

◆ name


 String PushNotifications::Channel::name 
 

Required: User facing name of the channel.

◆ importance


 Importance PushNotifications::Channel::importance = normal 
 

Required.

◆ lockScreenAppearance


 Notification::LockScreenAppearance PushNotifications::Channel::lockScreenAppearance = Notification::showPartially 
 

Optional.

◆ description


 String PushNotifications::Channel::description 
 

Optional: user visible description of the channel.

◆ groupId


 String PushNotifications::Channel::groupId 
 

Required: group this channel belongs to (see ChannelGroup).

◆ ledColour


 Colour PushNotifications::Channel::ledColour 
 

Optional: sets the led colour for notifications in this channel.

◆ bypassDoNotDisturb


 bool PushNotifications::Channel::bypassDoNotDisturb = false 
 

Optional: true if notifications in this channel can bypass do not disturb setting.

◆ canShowBadge


 bool PushNotifications::Channel::canShowBadge = false 
 

Optional: true if notifications in this channel can show badges in a Launcher application.

◆ enableLights


 bool PushNotifications::Channel::enableLights = false 
 

Optional: true if notifications in this channel should show lights (subject to hardware support).

◆ enableVibration


 bool PushNotifications::Channel::enableVibration = false 
 

Optional: true if notifications in this channel should trigger vibrations.

◆ soundToPlay


 URL PushNotifications::Channel::soundToPlay 
 

Optional: sound to play in this channel.See Notification::soundToPlay for more info.

◆ vibrationPattern


 Array<int> PushNotifications::Channel::vibrationPattern 
 

Optional: vibration pattern for this channel.See Notification::vibrationPattern for more info.

The documentation for this struct was generated from the following file:juce\_PushNotifications.h
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