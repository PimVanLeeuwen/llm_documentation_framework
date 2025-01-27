Represents a MIDI RPN (registered parameter number) or NRPN (nonregistered parameter number) message.

Member Data Documentation


◆ channel


 int MidiRPNMessage::channel 
 

Midi channel of the message, in the range 1 to 16.

◆ parameterNumber


 int MidiRPNMessage::parameterNumber 
 

The 14bit parameter index, in the range 0 to 16383 (0x3fff).

◆ value


 int MidiRPNMessage::value 
 

The parameter value, in the range 0 to 16383 (0x3fff).If the message contains no value LSB, the value will be in the range 0 to 127 (0x7f).

◆ isNRPN


 bool MidiRPNMessage::isNRPN 
 

True if this message is an NRPN; false if it is an RPN.

◆ is14BitValue


 bool MidiRPNMessage::is14BitValue 
 

True if the value uses 14bit resolution (LSB + MSB); false if the value is 7bit (MSB only).

The documentation for this struct was generated from the following file:juce\_MidiRPN.h
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