#### getBoolean

```
public boolean getBoolean(String key,
                          boolean def)
```
Implements the getBoolean method as per the specification in
`Preferences.getBoolean(String,boolean)`.This implementation invokes `get(key,
null)`. If the return value is non-null, it is compared with
"true" using `String.equalsIgnoreCase(String)`. If the
comparison returns true, this invocation returns
true. Otherwise, the original return value is compared with
"false", again using `String.equalsIgnoreCase(String)`.
If the comparison returns true, this invocation returns
false. Otherwise, this invocation returns def.
Specified by:
`getBoolean` in class `Preferences`
Parameters:
`key` - key whose associated value is to be returned as a boolean.
`def` - the value to be returned in the event that this
preference node has no value associated with key
or the associated value cannot be interpreted as a boolean.
Returns:
the boolean value represented by the string associated with
key in this preference node, or def if the
associated value does not exist or cannot be interpreted as
a boolean.
Throws:
`IllegalStateException` - if this node (or an ancestor) has been
removed with the `removeNode()` method.
`NullPointerException` - if key is null.
See Also:
`Preferences.get(String,String)`,
`Preferences.putBoolean(String,boolean)`

