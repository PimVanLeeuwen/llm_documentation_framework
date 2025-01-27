Represents an action on a notification that can be presented as a button or a text input.On Android, each notification has its action specified explicitly, on iOS you configure an allowed set of actions on startup and pack them into categories (see Settings).

Member Enumeration Documentation


◆ Style


 enum PushNotifications::Notification::Action::Style 
 

Controls the appearance of this action.

Enumerator
 
 button Show this action as a button. 
 text Show this action as a text input field (on Android API 20 or higher is required). 


Member Data Documentation


◆ style


 Style PushNotifications::Notification::Action::style = button 
 



◆ title


 String PushNotifications::Notification::Action::title 
 

Required.the name of the action displayed to the user.

◆ textInputPlaceholder


 String PushNotifications::Notification::Action::textInputPlaceholder 
 

Optional: placeholder text for text input notification.Note that it will be ignored if button style is used.

◆ parameters


 var PushNotifications::Notification::Action::parameters 
 

Optional: additional parameters that can be passed.

◆ identifier


 String PushNotifications::Notification::Action::identifier 
 

Required: unique identifier.This should be one of the identifiers set with requestPermissionsWithSettings().

◆ triggerInBackground


 bool PushNotifications::Notification::Action::triggerInBackground = false 
 

Whether the app can process the action in background.

◆ destructive


 bool PushNotifications::Notification::Action::destructive = false 
 

Whether to display the action as destructive.

◆ textInputButtonText


 String PushNotifications::Notification::Action::textInputButtonText 
 

Optional: Text displayed on text input notification button.Note that it will be ignored if style is set to Style::button.

◆ icon


 String PushNotifications::Notification::Action::icon 
 

Optional: name of an icon file (without an extension) to be used for this action.This must be the name of one of the image files included into resources when exporting an Android project (see "Extra Android Raw Resources" setting in Projucer). Note that not all Android versions support an icon for an action, though it is recommended to provide it nevertheless.

◆ allowedResponses


 StringArray PushNotifications::Notification::Action::allowedResponses 
 

Optional: a list of possible answers if the answer set is limited.When left empty, then the user will be able to input any text.

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