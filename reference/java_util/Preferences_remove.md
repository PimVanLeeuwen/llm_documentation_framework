#### remove

```
public abstract void remove(String key)
```
Removes the value associated with the specified key in this preference
node, if any.If this implementation supports stored defaults, and there is
such a default for the specified preference, the stored default will be
"exposed" by this call, in the sense that it will be returned
by a succeeding call to get.
Parameters:
`key` - key whose mapping is to be removed from the preference node.
Throws:
`NullPointerException` - if key is null.
`IllegalStateException` - if this node (or an ancestor) has been
removed with the `removeNode()` method.

