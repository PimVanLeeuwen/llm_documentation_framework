#### lowerEntry

```
public Map.Entry<K,V> lowerEntry(K key)
```
Description copied from interface: `NavigableMap`
Returns a key-value mapping associated with the greatest key
strictly less than the given key, or `null` if there is
no such key.
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
and this map uses natural ordering, or its comparator
does not permit null keys
Since:
1.6

