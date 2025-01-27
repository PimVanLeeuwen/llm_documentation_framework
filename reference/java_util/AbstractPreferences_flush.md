#### flush

```
public void flush()
           throws BackingStoreException
```
Implements the flush method as per the specification in
`Preferences.flush()`.This implementation calls a recursive helper method that locks this
node, invokes flushSpi() on it, unlocks this node, and recursively
invokes this method on each "cached child." A cached child is a child
of this node that has been created in this VM and not subsequently
removed. In effect, this method does a depth first traversal of the
"cached subtree" rooted at this node, calling flushSpi() on each node in
the subTree while only that node is locked. Note that flushSpi() is
invoked top-down.If this method is invoked on a node that has been removed with
the `removeNode()` method, flushSpi() is invoked on this node,
but not on others.
Specified by:
`flush` in class `Preferences`
Throws:
`BackingStoreException` - if this operation cannot be completed
due to a failure in the backing store, or inability to
communicate with it.
See Also:
`flush()`

