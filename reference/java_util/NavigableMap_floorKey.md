#### floorKey

```
K floorKey(K key)
```
Returns the greatest key less than or equal to the given key,
or `null` if there is no such key.
Parameters:
`key` - the key
Returns:
the greatest key less than or equal to `key`,
or `null` if there is no such key
Throws:
`ClassCastException` - if the specified key cannot be compared
with the keys currently in the map
`NullPointerException` - if the specified key is null
and this map does not permit null keys

