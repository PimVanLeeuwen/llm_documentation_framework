#### removeNode

```
public void removeNode()
                throws BackingStoreException
```
Implements the removeNode() method as per the specification in
`Preferences.removeNode()`.This implementation checks to see that this node is the root; if so,
it throws an appropriate exception. Then, it locks this node's parent,
and calls a recursive helper method that traverses the subtree rooted at
this node. The recursive method locks the node on which it was called,
checks that it has not already been removed, and then ensures that all
of its children are cached: The `childrenNamesSpi()` method is
invoked and each returned child name is checked for containment in the
child-cache. If a child is not already cached, the `childSpi(String)` method is invoked to create a Preferences
instance for it, and this instance is put into the child-cache. Then
the helper method calls itself recursively on each node contained in its
child-cache. Next, it invokes `removeNodeSpi()`, marks itself
as removed, and removes itself from its parent's child-cache. Finally,
if there are any node change listeners, it enqueues a notification
event for processing by the event dispatch thread.Note that the helper method is always invoked with all ancestors up
to the "closest non-removed ancestor" locked.
Specified by:
`removeNode` in class `Preferences`
Throws:
`IllegalStateException` - if this node (or an ancestor) has already
been removed with the `removeNode()` method.
`UnsupportedOperationException` - if this method is invoked on
the root node.
`BackingStoreException` - if this operation cannot be completed
due to a failure in the backing store, or inability to
communicate with it.
See Also:
`Preferences.flush()`

