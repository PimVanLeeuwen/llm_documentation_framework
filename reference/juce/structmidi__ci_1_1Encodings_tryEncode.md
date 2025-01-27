#### tryEncode()


 static std::optional< std::vector< std::byte > > midi\_ci::Encodings::tryEncode ( Span< const std::byte > bytes, Encoding mutualEncoding ) static 
 

Attempts to encode the provided byte span using the specified encoding.The ASCII encoding does not make any changes to the input stream, but encoding will fail if any byte has its most significant bit set.