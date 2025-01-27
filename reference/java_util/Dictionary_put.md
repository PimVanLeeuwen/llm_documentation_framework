#### put

```
public abstract V put(K key,
                      V value)
```
Maps the specified `key` to the specified
`value` in this dictionary. Neither the key nor the
value can be `null`.If this dictionary already contains an entry for the specified
key, the value already in this dictionary for that
key is returned, after modifying the entry to contain the
new element.If this dictionary does not already have an entry
for the specified key, an entry is created for the
specified key and value, and null is
returned.The `value` can be retrieved by calling the
`get` method with a `key` that is equal to
the original `key`.
Parameters:
`key` - the hashtable key.
`value` - the value.
Returns:
the previous value to which the `key` was mapped
in this dictionary, or `null` if the key did not
have a previous mapping.
Throws:
`NullPointerException` - if the `key` or
`value` is `null`.
See Also:
`Object.equals(java.lang.Object)`,
`get(java.lang.Object)`

