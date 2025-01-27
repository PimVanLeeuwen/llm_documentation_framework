#### getChild

```
protected AbstractPreferences getChild(String nodeName)
                                throws BackingStoreException
```
Returns the named child if it exists, or null if it does not.
It is guaranteed that nodeName is non-null, non-empty,
does not contain the slash character ('/'), and is no longer than
`Preferences.MAX_NAME_LENGTH` characters. Also, it is guaranteed
that this node has not been removed. (The implementor needn't check
for any of these things if he chooses to override this method.)Finally, it is guaranteed that the named node has not been returned
by a previous invocation of this method or `childSpi(java.lang.String)` after the
last time that it was removed. In other words, a cached value will
always be used in preference to invoking this method. (The implementor
needn't maintain his own cache of previously returned children if he
chooses to override this method.)This implementation obtains this preference node's lock, invokes
`childrenNames()` to get an array of the names of this node's
children, and iterates over the array comparing the name of each child
with the specified node name. If a child node has the correct name,
the `childSpi(String)` method is invoked and the resulting
node is returned. If the iteration completes without finding the
specified name, null is returned.
Parameters:
`nodeName` - name of the child to be searched for.
Returns:
the named child if it exists, or null if it does not.
Throws:
`BackingStoreException` - if this operation cannot be completed
due to a failure in the backing store, or inability to
communicate with it.

