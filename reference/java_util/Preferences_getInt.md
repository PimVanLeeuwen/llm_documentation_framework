#### getInt

```
public abstract int getInt(String key,
                           int def)
```
Returns the int value represented by the string associated with the
specified key in this preference node. The string is converted to
an integer as by `Integer.parseInt(String)`. Returns the
specified default if there is no value associated with the key,
the backing store is inaccessible, or if
Integer.parseInt(String) would throw a `NumberFormatException` if the associated value were passed. This
method is intended for use in conjunction with `putInt(java.lang.String, int)`.If the implementation supports stored defaults and such a
default exists, is accessible, and could be converted to an int
with Integer.parseInt, this int is returned in preference to
the specified default.
Parameters:
`key` - key whose associated value is to be returned as an int.
`def` - the value to be returned in the event that this
preference node has no value associated with key
or the associated value cannot be interpreted as an int,
or the backing store is inaccessible.
Returns:
the int value represented by the string associated with
key in this preference node, or def if the
associated value does not exist or cannot be interpreted as
an int.
Throws:
`IllegalStateException` - if this node (or an ancestor) has been
removed with the `removeNode()` method.
`NullPointerException` - if key is null.
See Also:
`putInt(String,int)`,
`get(String,String)`

