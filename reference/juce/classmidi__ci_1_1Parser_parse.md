#### parse() [2/2]


 static std::optional< Message::Parsed > midi\_ci::Parser::parse ( Span< const std::byte > message, Status \* = nullptr ) static 
 

Parses the provided message;.Call this with a full CI message. Don't include any "extra" bytes such as the leading/trailing 0xf0/0xf7 for messages that were originally in bytestream midi format, or the packetheader bytes from UMPformatted sysex messages.Returns nullopt if the message is malformed. Otherwise, returns a parsed header, and optionally a body. If the body is std::monostate, then something went wrong while parsing. For example, the body may be malformed, or the CI version might be unrecognised.