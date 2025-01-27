#### putDouble

```
public abstract void putDouble(String key,
                               double value)
```
Associates a string representing the specified double value with the
specified key in this preference node. The associated string is the
one that would be returned if the double value were passed to
`Double.toString(double)`. This method is intended for use in
conjunction with `getDouble(java.lang.String, double)`.
Parameters:
`key` - key with which the string form of value is to be associated.
`value` - value whose string form is to be associated with key.
Throws:
`NullPointerException` - if key is null.
`IllegalArgumentException` - if key.length() exceeds
MAX\_KEY\_LENGTH.
`IllegalStateException` - if this node (or an ancestor) has been
removed with the `removeNode()` method.
See Also:
`getDouble(String,double)`

