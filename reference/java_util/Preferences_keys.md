#### keys

```
public abstract String[] keys()
                       throws BackingStoreException
```
Returns all of the keys that have an associated value in this
preference node. (The returned array will be of size zero if
this node has no preferences.)If the implementation supports stored defaults and there
are any such defaults at this node that have not been overridden,
by explicit preferences, the defaults are returned in the array in
addition to any explicit preferences.
Returns:
an array of the keys that have an associated value in this
preference node.
Throws:
`BackingStoreException` - if this operation cannot be completed
due to a failure in the backing store, or inability to
communicate with it.
`IllegalStateException` - if this node (or an ancestor) has been
removed with the `removeNode()` method.

