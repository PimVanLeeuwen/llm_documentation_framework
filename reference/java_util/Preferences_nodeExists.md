#### nodeExists

```
public abstract boolean nodeExists(String pathName)
                            throws BackingStoreException
```
Returns true if the named preference node exists in the same tree
as this node. Relative path names (which do not begin with the slash
character ('/')) are interpreted relative to this preference
node.If this node (or an ancestor) has already been removed with the
`removeNode()` method, it is legal to invoke this method,
but only with the path name ""; the invocation will return
false. Thus, the idiom p.nodeExists("") may be
used to test whether p has been removed.
Parameters:
`pathName` - the path name of the node whose existence
is to be checked.
Returns:
true if the specified node exists.
Throws:
`BackingStoreException` - if this operation cannot be completed
due to a failure in the backing store, or inability to
communicate with it.
`IllegalArgumentException` - if the path name is invalid (i.e.,
it contains multiple consecutive slash characters, or ends
with a slash character and is more than one character long).
`NullPointerException` - if path name is null.
`IllegalStateException` - if this node (or an ancestor) has been
removed with the `removeNode()` method and
pathName is not the empty string ("").

