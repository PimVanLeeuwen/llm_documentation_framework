#### putInt

```
public abstract void putInt(String key,
                            int value)
```
Associates a string representing the specified int value with the
specified key in this preference node. The associated string is the
one that would be returned if the int value were passed to
`Integer.toString(int)`. This method is intended for use in
conjunction with `getInt(java.lang.String, int)`.
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
`getInt(String,int)`

