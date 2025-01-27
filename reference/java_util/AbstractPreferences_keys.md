#### keys

```
public String[] keys()
              throws BackingStoreException
```
Implements the keys method as per the specification in
`Preferences.keys()`.This implementation obtains this preference node's lock, checks that
the node has not been removed and invokes `keysSpi()`.
Specified by:
`keys` in class `Preferences`
Returns:
an array of the keys that have an associated value in this
preference node.
Throws:
`BackingStoreException` - if this operation cannot be completed
due to a failure in the backing store, or inability to
communicate with it.
`IllegalStateException` - if this node (or an ancestor) has been
removed with the `removeNode()` method.

