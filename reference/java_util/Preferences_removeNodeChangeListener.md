#### removeNodeChangeListener

```
public abstract void removeNodeChangeListener(NodeChangeListener ncl)
```
Removes the specified NodeChangeListener, so it no longer
receives change events.
Parameters:
`ncl` - The NodeChangeListener to remove.
Throws:
`IllegalArgumentException` - if ncl was not a registered
NodeChangeListener on this node.
`IllegalStateException` - if this node (or an ancestor) has been
removed with the `removeNode()` method.
See Also:
`addNodeChangeListener(NodeChangeListener)`

