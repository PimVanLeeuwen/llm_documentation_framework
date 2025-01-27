template<typename Fn>
struct ScopeGuard< Fn >An easy way to ensure that a function is called at the end of the current scope.Usage:{
 if (flag == true)
 return;
 
 // While this code executes, flag is true e.g. to prevent reentrancy
 flag = true;
 // When we exit this scope, flag must be false
 const ScopeGuard scope { [&] { flag = false; } };
 
 if (checkInitialCondition())
 return; // Scope's lambda will fire here...
 
 if (checkCriticalCondition())
 throw std::runtime\_error{}; // ...or here...
 
 doWorkHavingEstablishedPreconditions();
} // ...or here!
ScopeGuardAn easy way to ensure that a function is called at the end of the current scope.Definition juce\_ScopeGuard.h:67
 

Constructor & Destructor Documentation


◆ ~ScopeGuard()


template<typename Fn > 

 ScopeGuard< Fn >::~ScopeGuard ( ) 
 

References ScopeGuard< Fn >::~ScopeGuard().Referenced by ScopeGuard< Fn >::~ScopeGuard().

The documentation for this struct was generated from the following file:juce\_ScopeGuard.h
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