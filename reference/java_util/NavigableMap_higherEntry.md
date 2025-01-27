#### higherEntry

```
Map.Entry<K,V> higherEntry(K key)
```
Returns a key-value mapping associated with the least key
strictly greater than the given key, or `null` if there
is no such key.
Parameters:
`key` - the key
Returns:
an entry with the least key greater than `key`,
or `null` if there is no such key
Throws:
`ClassCastException` - if the specified key cannot be compared
with the keys currently in the map
`NullPointerException` - if the specified key is null
and this map does not permit null keys

