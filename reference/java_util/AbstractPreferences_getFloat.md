#### getFloat

```
public float getFloat(String key,
                      float def)
```
Implements the getFloat method as per the specification in
`Preferences.getFloat(String,float)`.This implementation invokes `get(key,
null)`. If the return value is non-null, the implementation
attempts to translate it to an float with
`Float.parseFloat(String)`. If the attempt succeeds, the return
value is returned by this method. Otherwise, def is returned.
Specified by:
`getFloat` in class `Preferences`
Parameters:
`key` - key whose associated value is to be returned as a float.
`def` - the value to be returned in the event that this
preference node has no value associated with key
or the associated value cannot be interpreted as a float.
Returns:
the float value represented by the string associated with
key in this preference node, or def if the
associated value does not exist or cannot be interpreted as
a float.
Throws:
`IllegalStateException` - if this node (or an ancestor) has been
removed with the `removeNode()` method.
`NullPointerException` - if key is null.
See Also:
`Preferences.putFloat(String,float)`,
`Preferences.get(String,String)`

