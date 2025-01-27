#### getDouble

```
public abstract double getDouble(String key,
                                 double def)
```
Returns the double value represented by the string associated with the
specified key in this preference node. The string is converted to an
integer as by `Double.parseDouble(String)`. Returns the specified
default if there is no value associated with the key, the backing store
is inaccessible, or if Double.parseDouble(String) would throw a
`NumberFormatException` if the associated value were passed.
This method is intended for use in conjunction with `putDouble(java.lang.String, double)`.If the implementation supports stored defaults and such a
default exists, is accessible, and could be converted to a double
with Double.parseDouble, this double is returned in preference
to the specified default.
Parameters:
`key` - key whose associated value is to be returned as a double.
`def` - the value to be returned in the event that this
preference node has no value associated with key
or the associated value cannot be interpreted as a double,
or the backing store is inaccessible.
Returns:
the double value represented by the string associated with
key in this preference node, or def if the
associated value does not exist or cannot be interpreted as
a double.
Throws:
`IllegalStateException` - if this node (or an ancestor) has been
removed with the `removeNode()` method.
`NullPointerException` - if key is null.
See Also:
`putDouble(String,double)`,
`get(String,String)`

