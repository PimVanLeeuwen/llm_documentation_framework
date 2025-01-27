#### get

```
public abstract String get(String key,
                           String def)
```
Returns the value associated with the specified key in this preference
node. Returns the specified default if there is no value associated
with the key, or the backing store is inaccessible.Some implementations may store default values in their backing
stores. If there is no value associated with the specified key
but there is such a stored default, it is returned in
preference to the specified default.
Parameters:
`key` - key whose associated value is to be returned.
`def` - the value to be returned in the event that this
preference node has no value associated with key.
Returns:
the value associated with key, or def
if no value is associated with key, or the backing
store is inaccessible.
Throws:
`IllegalStateException` - if this node (or an ancestor) has been
removed with the `removeNode()` method.
`NullPointerException` - if key is null. (A
null value for def is permitted.)

