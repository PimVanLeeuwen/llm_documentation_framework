#### stringTo7BitText()


 static std::vector< std::byte > midi\_ci::Encodings::stringTo7BitText ( const String & text ) static 
 

Text in ACK and NAK messages can't be utf8 or ASCII because each byte only has 7 usable bits.The encoding rules are in section 5.10.4 of the CI spec.Referenced by jsonTo7BitText().