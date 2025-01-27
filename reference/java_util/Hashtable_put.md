#### put

```
public V put(K key,
             V value)
```
Maps the specified `key` to the specified
`value` in this hashtable. Neither the key nor the
value can be `null`.The value can be retrieved by calling the `get` method
with a key that is equal to the original key.
Specified by:
`put` in interface `Map<K,V>`
Specified by:
`put` in class `Dictionary<K,V>`
Parameters:
`key` - the hashtable key
`value` - the value
Returns:
the previous value of the specified key in this hashtable,
or `null` if it did not have one
Throws:
`NullPointerException` - if the key or value is
`null`
See Also:
`Object.equals(Object)`,
`get(Object)`

