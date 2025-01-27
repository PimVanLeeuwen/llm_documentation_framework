#### stringFrom7BitText()


 static String midi\_ci::Encodings::stringFrom7BitText ( Span< const std::byte > bytes ) static 
 

Text in ACK and NAK messages can't be utf8 or ASCII because each byte only has 7 usable bits.The encoding rules are in section 5.10.4 of the CI spec.Referenced by midi\_ci::Message::ACK::getMessageTextAsString(), midi\_ci::Message::NAK::getMessageTextAsString(), and jsonFrom7BitText().