#### setAddressPattern()


 void OSCMessage::setAddressPattern ( const OSCAddressPattern & ap ) noexcept 
 

Sets the address pattern of the OSCMessage.Parameters

 ap the address pattern of the message. This must be a valid OSC address (starting with a forward slash) and may contain OSC wildcard expressions. You can pass in a string literal or a juce String (they will be converted to an OSCAddressPattern automatically).