#### clear

```
public abstract void clear()
                    throws BackingStoreException
```
Removes all of the preferences (key-value associations) in this
preference node. This call has no effect on any descendants
of this node.If this implementation supports stored defaults, and this
node in the preferences hierarchy contains any such defaults,
the stored defaults will be "exposed" by this call, in the sense that
they will be returned by succeeding calls to get.
Throws:
`BackingStoreException` - if this operation cannot be completed
due to a failure in the backing store, or inability to
communicate with it.
`IllegalStateException` - if this node (or an ancestor) has been
removed with the `removeNode()` method.
See Also:
`removeNode()`

