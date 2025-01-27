template<typename Type>
struct TypeHelpers::ParameterType< Type >The ParameterType struct is used to find the best type to use when passing some kind of object as a parameter.Of course, this is only likely to be useful in certain esoteric template situations.E.g. "myFunction (typename TypeHelpers::ParameterType<int>::type, typename TypeHelpers::ParameterType<MyObject>::type)" would evaluate to "myfunction (int, const MyObject&)", keeping any primitive types as passbyvalue, but passing objects as a const reference, to avoid copying.

Member Typedef Documentation


◆ type


template<typename Type > 

 using TypeHelpers::ParameterType< Type >::type = const Type& 
 



The documentation for this struct was generated from the following file:juce\_MathsFunctions.h
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