#### get

```
public String get(String key,
                  String def)
```
Implements the get method as per the specification in
`Preferences.get(String,String)`.This implementation first checks to see if key is
null throwing a NullPointerException if this is
the case. Then it obtains this preference node's lock,
checks that the node has not been removed, invokes `getSpi(String)`, and returns the result, unless the getSpi
invocation returns null or throws an exception, in which case
this invocation returns def.
Specified by:
`get` in class `Preferences`
Parameters:
`key` - key whose associated value is to be returned.
`def` - the value to be returned in the event that this
preference node has no value associated with key.
Returns:
the value associated with key, or def
if no value is associated with key.
Throws:
`IllegalStateException` - if this node (or an ancestor) has been
removed with the `removeNode()` method.
`NullPointerException` - if key is null. (A
null default is permitted.)

