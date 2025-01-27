#### put

```
public V put(K key,
             V value)
```
Maps the specified key to the specified value in this table.
Neither the key nor the value can be null.The value can be retrieved by calling the `get` method
with a key that is equal to the original key.
Specified by:
`put` in interface `Map<K,V>`
Overrides:
`put` in class `AbstractMap<K,V>`
Parameters:
`key` - key with which the specified value is to be associated
`value` - value to be associated with the specified key
Returns:
the previous value associated with `key`, or
`null` if there was no mapping for `key`
Throws:
`NullPointerException` - if the specified key or value is null

