Contains contextual details about the invocation of a command.

Member Enumeration Documentation


◆ InvocationMethod


 enum ApplicationCommandTarget::InvocationInfo::InvocationMethod 
 

The types of context in which the command might be called.

Enumerator
 
 direct The command is being invoked directly by a piece of code. 
 fromKeyPress The command is being invoked by a keypress. 
 fromMenu The command is being invoked by a menu selection. 
 fromButton The command is being invoked by a button click. 


Constructor & Destructor Documentation


◆ InvocationInfo()


 ApplicationCommandTarget::InvocationInfo::InvocationInfo ( CommandID commandID ) 
 


Member Data Documentation


◆ commandID


 CommandID ApplicationCommandTarget::InvocationInfo::commandID 
 

The UID of the command that should be performed.

◆ commandFlags


 int ApplicationCommandTarget::InvocationInfo::commandFlags 
 

The command's flags.See ApplicationCommandInfo for a description of these flag values.

◆ invocationMethod


 InvocationMethod ApplicationCommandTarget::InvocationInfo::invocationMethod 
 

The type of event that triggered this command.

◆ originatingComponent


 Component\* ApplicationCommandTarget::InvocationInfo::originatingComponent 
 

If triggered by a keypress or menu, this will be the component that had the keyboard focus at the time.If triggered by a button, it may be set to that component, or it may be null.

◆ keyPress


 KeyPress ApplicationCommandTarget::InvocationInfo::keyPress 
 

The keypress that was used to invoke it.Note that this will be an invalid keypress if the command was invoked by some other means than a keyboard shortcut.

◆ isKeyDown


 bool ApplicationCommandTarget::InvocationInfo::isKeyDown 
 

True if the callback is being invoked when the key is pressed, false if the key is being released.See alsoKeyPressMappingSet::addCommand() 


◆ millisecsSinceKeyPressed


 int ApplicationCommandTarget::InvocationInfo::millisecsSinceKeyPressed 
 

If the key is being released, this indicates how long it had been held down for.(Only relevant if isKeyDown is false.)

The documentation for this struct was generated from the following file:juce\_ApplicationCommandTarget.h
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