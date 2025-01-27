#### getBoolean

```
public abstract boolean getBoolean(String key,
                                   boolean def)
```
Returns the boolean value represented by the string associated with the
specified key in this preference node. Valid strings
are "true", which represents true, and "false", which
represents false. Case is ignored, so, for example, "TRUE"
and "False" are also valid. This method is intended for use in
conjunction with `putBoolean(java.lang.String, boolean)`.Returns the specified default if there is no value
associated with the key, the backing store is inaccessible, or if the
associated value is something other than "true" or
"false", ignoring case.If the implementation supports stored defaults and such a
default exists and is accessible, it is used in preference to the
specified default, unless the stored default is something other than
"true" or "false", ignoring case, in which case the
specified default is used.
Parameters:
`key` - key whose associated value is to be returned as a boolean.
`def` - the value to be returned in the event that this
preference node has no value associated with key
or the associated value cannot be interpreted as a boolean,
or the backing store is inaccessible.
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
`get(String,String)`,
`putBoolean(String,boolean)`

