#### storeToXML

```
public void storeToXML(OutputStream os,
                       String comment,
                       String encoding)
                throws IOException
```
Emits an XML document representing all of the properties contained
in this table, using the specified encoding.The XML document will have the following DOCTYPE declaration:
```

 <!DOCTYPE properties SYSTEM "http://java.sun.com/dtd/properties.dtd">
 
```
If the specified comment is `null` then no comment
will be stored in the document.An implementation is required to support writing of XML documents
that use the "`UTF-8`" or "`UTF-16`" encoding. An
implementation may support additional encodings.The specified stream remains open after this method returns.
Parameters:
`os` - the output stream on which to emit the XML document.
`comment` - a description of the property list, or `null`
if no comment is desired.
`encoding` - the name of a supported
character encoding
Throws:
`IOException` - if writing to the specified output stream
results in an IOException.
`UnsupportedEncodingException` - if the encoding is not
supported by the implementation.
`NullPointerException` - if `os` is `null`,
or if `encoding` is `null`.
`ClassCastException` - if this `Properties` object
contains any keys or values that are not
`Strings`.
Since:
1.5
See Also:
`loadFromXML(InputStream)`,
Character
Encoding in Entities

