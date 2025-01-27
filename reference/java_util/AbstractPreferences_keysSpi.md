#### keysSpi

```
protected abstract String[] keysSpi()
                             throws BackingStoreException
```
Returns all of the keys that have an associated value in this
preference node. (The returned array will be of size zero if
this node has no preferences.) It is guaranteed that this node has not
been removed.This method is invoked with the lock on this node held.If this node throws a BackingStoreException, the exception
will propagate out beyond the enclosing `keys()` invocation.
Returns:
an array of the keys that have an associated value in this
preference node.
Throws:
`BackingStoreException` - if this operation cannot be completed
due to a failure in the backing store, or inability to
communicate with it.

