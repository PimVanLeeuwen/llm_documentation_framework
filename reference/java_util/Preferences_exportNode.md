#### exportNode

```
public abstract void exportNode(OutputStream os)
                         throws IOException,
                                BackingStoreException
```
Emits on the specified output stream an XML document representing all
of the preferences contained in this node (but not its descendants).
This XML document is, in effect, an offline backup of the node.The XML document will have the following DOCTYPE declaration:
```

 <!DOCTYPE preferences SYSTEM "http://java.sun.com/dtd/preferences.dtd">
 
```
The UTF-8 character encoding will be used.This method is an exception to the general rule that the results of
concurrently executing multiple methods in this class yields
results equivalent to some serial execution. If the preferences
at this node are modified concurrently with an invocation of this
method, the exported preferences comprise a "fuzzy snapshot" of the
preferences contained in the node; some of the concurrent modifications
may be reflected in the exported data while others may not.
Parameters:
`os` - the output stream on which to emit the XML document.
Throws:
`IOException` - if writing to the specified output stream
results in an IOException.
`BackingStoreException` - if preference data cannot be read from
backing store.
`IllegalStateException` - if this node (or an ancestor) has been
removed with the `removeNode()` method.
See Also:
`importPreferences(InputStream)`

