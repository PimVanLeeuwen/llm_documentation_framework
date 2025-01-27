#### sync

```
public abstract void sync()
                   throws BackingStoreException
```
Ensures that future reads from this preference node and its
descendants reflect any changes that were committed to the persistent
store (from any VM) prior to the sync invocation. As a
side-effect, forces any changes in the contents of this preference node
and its descendants to the persistent store, as if the flush
method had been invoked on this node.
Throws:
`BackingStoreException` - if this operation cannot be completed
due to a failure in the backing store, or inability to
communicate with it.
`IllegalStateException` - if this node (or an ancestor) has been
removed with the `removeNode()` method.
See Also:
`flush()`

