#### childrenNames

```
public abstract String[] childrenNames()
                                throws BackingStoreException
```
Returns the names of the children of this preference node, relative to
this node. (The returned array will be of size zero if this node has
no children.)
Returns:
the names of the children of this preference node.
Throws:
`BackingStoreException` - if this operation cannot be completed
due to a failure in the backing store, or inability to
communicate with it.
`IllegalStateException` - if this node (or an ancestor) has been
removed with the `removeNode()` method.

