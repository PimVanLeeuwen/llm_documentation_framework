#### putBoolean

```
public abstract void putBoolean(String key,
                                boolean value)
```
Associates a string representing the specified boolean value with the
specified key in this preference node. The associated string is
"true" if the value is true, and "false" if it is
false. This method is intended for use in conjunction with
`getBoolean(java.lang.String, boolean)`.
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
`getBoolean(String,boolean)`,
`get(String,String)`

