#### removeNodeSpi

```
protected abstract void removeNodeSpi()
                               throws BackingStoreException
```
Removes this preference node, invalidating it and any preferences that
it contains. The named child will have no descendants at the time this
invocation is made (i.e., the `Preferences.removeNode()` method
invokes this method repeatedly in a bottom-up fashion, removing each of
a node's descendants before removing the node itself).This method is invoked with the lock held on this node and its
parent (and all ancestors that are being removed as a
result of a single invocation to `Preferences.removeNode()`).The removal of a node needn't become persistent until the
flush method is invoked on this node (or an ancestor).If this node throws a BackingStoreException, the exception
will propagate out beyond the enclosing `removeNode()`
invocation.
Throws:
`BackingStoreException` - if this operation cannot be completed
due to a failure in the backing store, or inability to
communicate with it.

