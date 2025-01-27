#### get

```
public abstract V get(Object key)
```
Returns the value to which the key is mapped in this dictionary.
The general contract for the isEmpty method is that if this
dictionary contains an entry for the specified key, the associated
value is returned; otherwise, null is returned.
Parameters:
`key` - a key in this dictionary.
`null` if the key is not mapped to any value in
this dictionary.
Returns:
the value to which the key is mapped in this dictionary;
Throws:
`NullPointerException` - if the key is null.
See Also:
`put(java.lang.Object, java.lang.Object)`

