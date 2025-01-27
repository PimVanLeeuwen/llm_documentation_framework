#### removeNode

```
public abstract void removeNode()
                         throws BackingStoreException
```
Removes this preference node and all of its descendants, invalidating
any preferences contained in the removed nodes. Once a node has been
removed, attempting any method other than `name()`,
`absolutePath()`, `isUserNode()`, `flush()` or
`nodeExists("")` on the corresponding
Preferences instance will fail with an
IllegalStateException. (The methods defined on `Object`
can still be invoked on a node after it has been removed; they will not
throw IllegalStateException.)The removal is not guaranteed to be persistent until the
flush method is called on this node (or an ancestor).If this implementation supports stored defaults, removing a
node exposes any stored defaults at or below this node. Thus, a
subsequent call to nodeExists on this node's path name may
return true, and a subsequent call to node on this
path name may return a (different) Preferences instance
representing a non-empty collection of preferences and/or children.
Throws:
`BackingStoreException` - if this operation cannot be completed
due to a failure in the backing store, or inability to
communicate with it.
`IllegalStateException` - if this node (or an ancestor) has already
been removed with the `removeNode()` method.
`UnsupportedOperationException` - if this method is invoked on
the root node.
See Also:
`flush()`

