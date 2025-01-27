#### childrenNamesSpi

```
protected abstract String[] childrenNamesSpi()
                                      throws BackingStoreException
```
Returns the names of the children of this preference node. (The
returned array will be of size zero if this node has no children.)
This method need not return the names of any nodes already cached,
but may do so without harm.This method is invoked with the lock on this node held.If this node throws a BackingStoreException, the exception
will propagate out beyond the enclosing `childrenNames()`
invocation.
Returns:
an array containing the names of the children of this
preference node.
Throws:
`BackingStoreException` - if this operation cannot be completed
due to a failure in the backing store, or inability to
communicate with it.

