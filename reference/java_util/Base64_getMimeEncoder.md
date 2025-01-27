#### getMimeEncoder

```
public static Base64.Encoder getMimeEncoder(int lineLength,
                                            byte[] lineSeparator)
```
Returns a `Base64.Encoder` that encodes using the
MIME type base64 encoding scheme
with specified line length and line separators.
Parameters:
`lineLength` - the length of each output line (rounded down to nearest multiple
of 4). If `lineLength <= 0` the output will not be separated
in lines
`lineSeparator` - the line separator for each output line
Returns:
A Base64 encoder.
Throws:
`IllegalArgumentException` - if `lineSeparator` includes any
character of "The Base64 Alphabet" as specified in Table 1 of
RFC 2045.

