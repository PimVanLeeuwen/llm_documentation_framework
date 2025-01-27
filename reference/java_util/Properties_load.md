#### load

```
public void load(InputStream inStream)
          throws IOException
```
Reads a property list (key and element pairs) from the input
byte stream. The input stream is in a simple line-oriented
format as specified in
`load(Reader)` and is assumed to use
the ISO 8859-1 character encoding; that is each byte is one Latin1
character. Characters not in Latin1, and certain special characters,
are represented in keys and elements using Unicode escapes as defined in
section 3.3 of
The Java™ Language Specification.The specified stream remains open after this method returns.
Parameters:
`inStream` - the input stream.
Throws:
`IOException` - if an error occurred when reading from the
input stream.
`IllegalArgumentException` - if the input stream contains a
malformed Unicode escape sequence.
Since:
1.2

