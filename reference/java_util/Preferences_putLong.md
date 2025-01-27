#### putLong

```
public abstract void putLong(String key,
                             long value)
```
Associates a string representing the specified long value with the
specified key in this preference node. The associated string is the
one that would be returned if the long value were passed to
`Long.toString(long)`. This method is intended for use in
conjunction with `getLong(java.lang.String, long)`.
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
`getLong(String,long)`

