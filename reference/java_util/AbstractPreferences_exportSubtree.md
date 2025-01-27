#### exportSubtree

```
public void exportSubtree(OutputStream os)
                   throws IOException,
                          BackingStoreException
```
Implements the exportSubtree method as per the specification in
`Preferences.exportSubtree(OutputStream)`.
Specified by:
`exportSubtree` in class `Preferences`
Parameters:
`os` - the output stream on which to emit the XML document.
Throws:
`IOException` - if writing to the specified output stream
results in an IOException.
`BackingStoreException` - if preference data cannot be read from
backing store.
See Also:
`Preferences.importPreferences(InputStream)`,
`Preferences.exportNode(OutputStream)`




