#### loadFromXML

```
public void loadFromXML(InputStream in)
                 throws IOException,
                        InvalidPropertiesFormatException
```
Loads all of the properties represented by the XML document on the
specified input stream into this properties table.The XML document must have the following DOCTYPE declaration:
```

 <!DOCTYPE properties SYSTEM "http://java.sun.com/dtd/properties.dtd">
 
```
Furthermore, the document must satisfy the properties DTD described
above.An implementation is required to read XML documents that use the
"`UTF-8`" or "`UTF-16`" encoding. An implementation may
support additional encodings.The specified stream is closed after this method returns.
Parameters:
`in` - the input stream from which to read the XML document.
Throws:
`IOException` - if reading from the specified input stream
results in an IOException.
`UnsupportedEncodingException` - if the document's encoding
declaration can be read and it specifies an encoding that is not
supported
`InvalidPropertiesFormatException` - Data on input stream does not
constitute a valid XML document with the mandated document type.
`NullPointerException` - if `in` is null.
Since:
1.5
See Also:
`storeToXML(OutputStream, String, String)`,
Character
Encoding in Entities

