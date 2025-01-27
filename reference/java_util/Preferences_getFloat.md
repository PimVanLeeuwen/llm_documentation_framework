#### getFloat

```
public abstract float getFloat(String key,
                               float def)
```
Returns the float value represented by the string associated with the
specified key in this preference node. The string is converted to an
integer as by `Float.parseFloat(String)`. Returns the specified
default if there is no value associated with the key, the backing store
is inaccessible, or if Float.parseFloat(String) would throw a
`NumberFormatException` if the associated value were passed.
This method is intended for use in conjunction with `putFloat(java.lang.String, float)`.If the implementation supports stored defaults and such a
default exists, is accessible, and could be converted to a float
with Float.parseFloat, this float is returned in preference to
the specified default.
Parameters:
`key` - key whose associated value is to be returned as a float.
`def` - the value to be returned in the event that this
preference node has no value associated with key
or the associated value cannot be interpreted as a float,
or the backing store is inaccessible.
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
`putFloat(String,float)`,
`get(String,String)`

