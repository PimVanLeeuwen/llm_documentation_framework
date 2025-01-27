#### toMcoded7()


 static std::vector< std::byte > midi\_ci::Encodings::toMcoded7 ( Span< const std::byte > bytes ) static 
 

Each group of seven stored bytes is transmitted as eight bytes.First, the sign bits of the seven bytes are sent, followed by the loworder 7 bits of each byte.