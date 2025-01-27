#### messageNotAcknowledged()


 virtual void midi\_ci::DeviceListener::messageNotAcknowledged ( MUID x, Message::NAK ) virtual 
 

Called to indicate that a NAK message was received.This is useful e.g. to display a diagnostic to the user, or to cache the failed request details and retry the request at a later date.The message field of the NAK is 7bit text. You can convert it to a string using Encodings::stringFrom7BitText().