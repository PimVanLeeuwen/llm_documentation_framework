#### nodeExists

```
public boolean nodeExists(String path)
                   throws BackingStoreException
```
Implements the nodeExists method as per the specification in
`Preferences.nodeExists(String)`.This implementation is very similar to `node(String)`,
except that `getChild(String)` is used instead of `childSpi(String)`.
Specified by:
`nodeExists` in class `Preferences`
Parameters:
`path` - the path name of the node whose existence is to be checked.
Returns:
true if the specified node exists.
Throws:
`BackingStoreException` - if this operation cannot be completed
due to a failure in the backing store, or inability to
communicate with it.
`IllegalArgumentException` - if the path name is invalid (i.e.,
it contains multiple consecutive slash characters, or ends
with a slash character and is more than one character long).
`IllegalStateException` - if this node (or an ancestor) has been
removed with the `removeNode()` method and
pathname is not the empty string ("").

