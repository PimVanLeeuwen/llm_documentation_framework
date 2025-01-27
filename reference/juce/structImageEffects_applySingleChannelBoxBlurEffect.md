#### applySingleChannelBoxBlurEffect()


 static void ImageEffects::applySingleChannelBoxBlurEffect ( int radius, const Image & input, Image & result ) static 
 

Applies a blur to this image, placing the blurred image in the result outparameter.This will attempt to call the applySingleChannelBoxBlurEffect() member of the input image's underlying ImagePixelData, which will use hardware acceleration if available. If this fails, then a software blur will be applied instead.This kind of blur is only capable of blurring singlechannel images, which is useful when rendering drop shadows. The blur is implemented as several boxblurs in series. The results should be visually similar to a Gaussian blur, but less accurate.If result is already the correct size, then its storage will be reused directly. Otherwise, new storage may be allocated for the blurred image.

The documentation for this struct was generated from the following file:juce\_Image.h
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