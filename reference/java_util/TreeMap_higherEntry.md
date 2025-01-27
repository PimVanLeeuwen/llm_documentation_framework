#### higherEntry

```
public Map.Entry<K,V> higherEntry(K key)
```
Description copied from interface: `NavigableMap`
Returns a key-value mapping associated with the least key
strictly greater than the given key, or `null` if there
is no such key.
Specified by:
`higherEntry` in interface `NavigableMap<K,V>`
Parameters:
`key` - the key
Returns:
an entry with the least key greater than `key`,
or `null` if there is no such key
Throws:
`ClassCastException` - if the specified key cannot be compared
with the keys currently in the map
`NullPointerException` - if the specified key is null
and this map uses natural ordering, or its comparator
does not permit null keys
Since:
1.6

