#### sync

```
public void sync()
          throws BackingStoreException
```
Implements the sync method as per the specification in
`Preferences.sync()`.This implementation calls a recursive helper method that locks this
node, invokes syncSpi() on it, unlocks this node, and recursively
invokes this method on each "cached child." A cached child is a child
of this node that has been created in this VM and not subsequently
removed. In effect, this method does a depth first traversal of the
"cached subtree" rooted at this node, calling syncSpi() on each node in
the subTree while only that node is locked. Note that syncSpi() is
invoked top-down.
Specified by:
`sync` in class `Preferences`
Throws:
`BackingStoreException` - if this operation cannot be completed
due to a failure in the backing store, or inability to
communicate with it.
`IllegalStateException` - if this node (or an ancestor) has been
removed with the `removeNode()` method.
See Also:
`flush()`

