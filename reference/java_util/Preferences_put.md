#### put

```
public abstract void put(String key,
                         String value)
```
Associates the specified value with the specified key in this
preference node.
Parameters:
`key` - key with which the specified value is to be associated.
`value` - value to be associated with the specified key.
Throws:
`NullPointerException` - if key or value is null.
`IllegalArgumentException` - if key.length() exceeds
MAX\_KEY\_LENGTH or if value.length exceeds
MAX\_VALUE\_LENGTH.
`IllegalStateException` - if this node (or an ancestor) has been
removed with the `removeNode()` method.

