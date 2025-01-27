```
public class Base64
extends Object
```
This class consists exclusively of static methods for obtaining
encoders and decoders for the Base64 encoding scheme. The
implementation of this class supports the following types of Base64
as specified in
RFC 4648 and
RFC 2045.BasicUses "The Base64 Alphabet" as specified in Table 1 of
RFC 4648 and RFC 2045 for encoding and decoding operation.
The encoder does not add any line feed (line separator)
character. The decoder rejects data that contains characters
outside the base64 alphabet.URL and Filename safeUses the "URL and Filename safe Base64 Alphabet" as specified
in Table 2 of RFC 4648 for encoding and decoding. The
encoder does not add any line feed (line separator) character.
The decoder rejects data that contains characters outside the
base64 alphabet.MIMEUses the "The Base64 Alphabet" as specified in Table 1 of
RFC 2045 for encoding and decoding operation. The encoded output
must be represented in lines of no more than 76 characters each
and uses a carriage return `'\r'` followed immediately by
a linefeed `'\n'` as the line separator. No line separator
is added to the end of the encoded output. All line separators
or other characters not found in the base64 alphabet table are
ignored in decoding operation.Unless otherwise noted, passing a `null` argument to a
method of this class will cause a `NullPointerException` to be thrown.
Since:
1.8
