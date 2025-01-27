#### exportNode

```
public void exportNode(OutputStream os)
                throws IOException,
                       BackingStoreException
```
Implements the exportNode method as per the specification in
`Preferences.exportNode(OutputStream)`.
Specified by:
`exportNode` in class `Preferences`
Parameters:
`os` - the output stream on which to emit the XML document.
Throws:
`IOException` - if writing to the specified output stream
results in an IOException.
`BackingStoreException` - if preference data cannot be read from
backing store.
See Also:
`Preferences.importPreferences(InputStream)`

