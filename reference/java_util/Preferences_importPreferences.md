#### importPreferences

```
public static void importPreferences(InputStream is)
                              throws IOException,
                                     InvalidPreferencesFormatException
```
Imports all of the preferences represented by the XML document on the
specified input stream. The document may represent user preferences or
system preferences. If it represents user preferences, the preferences
will be imported into the calling user's preference tree (even if they
originally came from a different user's preference tree). If any of
the preferences described by the document inhabit preference nodes that
do not exist, the nodes will be created.The XML document must have the following DOCTYPE declaration:
```

 <!DOCTYPE preferences SYSTEM "http://java.sun.com/dtd/preferences.dtd">
 
```
(This method is designed for use in conjunction with
`exportNode(OutputStream)` and
`exportSubtree(OutputStream)`.This method is an exception to the general rule that the results of
concurrently executing multiple methods in this class yields
results equivalent to some serial execution. The method behaves
as if implemented on top of the other public methods in this class,
notably `node(String)` and `put(String, String)`.
Parameters:
`is` - the input stream from which to read the XML document.
Throws:
`IOException` - if reading from the specified input stream
results in an IOException.
`InvalidPreferencesFormatException` - Data on input stream does not
constitute a valid XML document with the mandated document type.
`SecurityException` - If a security manager is present and
it denies RuntimePermission("preferences").
See Also:
`RuntimePermission`




