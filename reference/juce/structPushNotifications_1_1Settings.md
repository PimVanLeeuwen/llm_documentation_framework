Describes settings we want to use for current device.Note that at the moment this is only used on iOS and partially on OSX.On OSX only allow\* flags are used and they control remote notifications only. To control sound, alert and badge settings for local notifications on OSX, use Notifications settings in System Preferences.To setup push notifications for current device, provide permissions required, as well as register categories of notifications you want to support. Each category needs to have a unique identifier and it can optionally have multiple actions. Each action also needs to have a unique identifier. The example setup may look as follows:using Action = PushNotifications::Settings::Action;
using Category = PushNotifications::Settings::Category;
 
Action okAction;
okAction.identifier = "okAction";
okAction.title = "OK!";
okAction.style = Action::button;
okAction.triggerInBackground = true;
 
Action cancelAction;
cancelAction.identifier = "cancelAction";
cancelAction.title = "Cancel";
cancelAction.style = Action::button;
cancelAction.triggerInBackground = true;
cancelAction.destructive = true;
 
Action textAction;
textAction.identifier = "textAction";
textAction.title = "Enter text";
textAction.style = Action::text;
textAction.triggerInBackground = true;
textAction.destructive = false;
textAction.textInputButtonText = "Ok";
textAction.textInputPlaceholder = "Enter text...";
 
Category okCategory;
okCategory.identifier = "okCategory";
okCategory.actions = { okAction };
 
Category okCancelCategory;
okCancelCategory.identifier = "okCancelCategory";
okCancelCategory.actions = { okAction, cancelAction };
 
Category textCategory;
textCategory.identifier = "textCategory";
textCategory.actions = { textAction };
textCategory.sendDismissAction = true;
 
PushNotifications::Settings settings;
settings.allowAlert = true;
settings.allowBadge = true;
settings.allowSound = true;
settings.categories = { okCategory, okCancelCategory, textCategory };
PushNotifications::Notification::ActionRepresents an action on a notification that can be presented as a button or a text input.Definition juce\_PushNotifications.h:79
PushNotifications::Notification::Action::identifierString identifierRequired: unique identifier.Definition juce\_PushNotifications.h:98
PushNotifications::Notification::Action::styleStyle styleDefinition juce\_PushNotifications.h:89
PushNotifications::Notification::Action::titleString titleRequired.Definition juce\_PushNotifications.h:90
PushNotifications::Notification::Action::button@ buttonShow this action as a button.Definition juce\_PushNotifications.h:83
PushNotifications::Notification::Action::text@ textShow this action as a text input field (on Android API 20 or higher is required).Definition juce\_PushNotifications.h:84
PushNotifications::Notification::Action::triggerInBackgroundbool triggerInBackgroundWhether the app can process the action in background.Definition juce\_PushNotifications.h:100
PushNotifications::Notification::Action::destructivebool destructiveWhether to display the action as destructive.Definition juce\_PushNotifications.h:101
PushNotifications::Notification::Action::textInputPlaceholderString textInputPlaceholderOptional: placeholder text for text input notification.Definition juce\_PushNotifications.h:91
PushNotifications::Notification::Action::textInputButtonTextString textInputButtonTextOptional: Text displayed on text input notification button.Definition juce\_PushNotifications.h:102
PushNotifications::Settings::CategoryDescribes a category of a notification.Definition juce\_PushNotifications.h:408
PushNotifications::Settings::Category::identifierString identifierunique identifierDefinition juce\_PushNotifications.h:409
PushNotifications::Settings::Category::actionsArray< Action > actionsoptional list of actions within this categoryDefinition juce\_PushNotifications.h:410
PushNotifications::SettingsDescribes settings we want to use for current device.Definition juce\_PushNotifications.h:399
PushNotifications::Settings::ActionNotification::Action ActionDefinition juce\_PushNotifications.h:400
PushNotifications::Settings::allowBadgebool allowBadgewhether the app may badge its icon upon notificationDefinition juce\_PushNotifications.h:416
PushNotifications::Settings::categoriesArray< Category > categorieslist of categories the app wants to supportDefinition juce\_PushNotifications.h:417
PushNotifications::Settings::allowSoundbool allowSoundwhether the app should play a sound upon notificationDefinition juce\_PushNotifications.h:414
PushNotifications::Settings::allowAlertbool allowAlertwhether the app should present an alert upon notificationDefinition juce\_PushNotifications.h:415
 

Member Typedef Documentation


◆ Action


 using PushNotifications::Settings::Action = Notification::Action 
 


Member Data Documentation


◆ allowSound


 bool PushNotifications::Settings::allowSound = false 
 

whether the app should play a sound upon notification

◆ allowAlert


 bool PushNotifications::Settings::allowAlert = false 
 

whether the app should present an alert upon notification

◆ allowBadge


 bool PushNotifications::Settings::allowBadge = false 
 

whether the app may badge its icon upon notification

◆ categories


 Array<Category> PushNotifications::Settings::categories 
 

list of categories the app wants to support

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