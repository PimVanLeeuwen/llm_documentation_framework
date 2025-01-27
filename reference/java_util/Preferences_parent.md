#### parent

```
public abstract Preferences parent()
```
Returns the parent of this preference node, or null if this is
the root.
Returns:
the parent of this preference node.
Throws:
`IllegalStateException` - if this node (or an ancestor) has been
removed with the `removeNode()` method.

