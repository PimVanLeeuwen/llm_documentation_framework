#### clear

```
public void clear()
           throws BackingStoreException
```
Implements the clear method as per the specification in
`Preferences.clear()`.This implementation obtains this preference node's lock,
invokes `keys()` to obtain an array of keys, and
iterates over the array invoking `remove(String)` on each key.
Specified by:
`clear` in class `Preferences`
Throws:
`BackingStoreException` - if this operation cannot be completed
due to a failure in the backing store, or inability to
communicate with it.
`IllegalStateException` - if this node (or an ancestor) has been
removed with the `removeNode()` method.
See Also:
`Preferences.removeNode()`

