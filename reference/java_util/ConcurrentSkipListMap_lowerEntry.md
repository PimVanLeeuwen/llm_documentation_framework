#### lowerEntry

```
public Map.Entry<K,V> lowerEntry(K key)
```
Returns a key-value mapping associated with the greatest key
strictly less than the given key, or `null` if there is
no such key. The returned entry does not support the
`Entry.setValue` method.
Specified by:
`lowerEntry` in interface `NavigableMap<K,V>`
Parameters:
`key` - the key
Returns:
an entry with the greatest key less than `key`,
or `null` if there is no such key
Throws:
`ClassCastException` - if the specified key cannot be compared
with the keys currently in the map
`NullPointerException` - if the specified key is null

