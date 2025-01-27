Represents a connected display device.

Member Data Documentation


◆ isMain


 bool Displays::Display::isMain 
 

This will be true if this is the user's main display device.

◆ totalArea


 Rectangle<int> Displays::Display::totalArea 
 

The total area of this display in logical pixels including any OSdependent objects like the taskbar, menu bar, etc.

◆ userArea


 Rectangle<int> Displays::Display::userArea 
 

The total area of this display in logical pixels which isn't covered by OSdependent objects like the taskbar, menu bar, etc.Referenced by StandaloneFilterWindow::StandaloneFilterWindow().

◆ safeAreaInsets


 BorderSize<int> Displays::Display::safeAreaInsets 
 

Represents the area of this display in logical pixels that is not functional for displaying content.On mobile devices this may be the area covered by display cutouts and notches, where you still want to draw a background but should not position important content.

◆ keyboardInsets


 BorderSize<int> Displays::Display::keyboardInsets 
 

Represents the area of this display in logical pixels that is obscured by an onscreen keyboard.This is currently only supported on iOS, and on Android 11+.This will only return the bounds of the keyboard when it is in 'docked' mode. If the keyboard is floating (e.g. on an iPad using the split keyboard mode), no insets will be reported.

◆ topLeftPhysical


 Point<int> Displays::Display::topLeftPhysical 
 

The topleft of this display in physical coordinates.

◆ scale


 double Displays::Display::scale 
 

The scale factor of this display.For higherresolution displays, or displays with a userdefined scale factor set, this may be a value other than 1.0.This value is used to convert between physical and logical pixels. For example, a Component with size 10x10 will use 20x20 physical pixels on a display with a scale factor of 2.0.

◆ dpi


 double Displays::Display::dpi 
 

The DPI of the display.This is the number of physical pixels per inch. To get the number of logical pixels per inch, divide this by the Display::scale value.

◆ verticalFrequencyHz


 std::optional<double> Displays::Display::verticalFrequencyHz 
 

The vertical refresh rate of the display if applicable.Currently this is only used on Linux for display rate repainting.

The documentation for this struct was generated from the following file:juce\_Displays.h
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