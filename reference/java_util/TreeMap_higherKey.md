#### higherKey

```
public K higherKey(K key)
```
Description copied from interface: `NavigableMap`
Returns the least key strictly greater than the given key, or
`null` if there is no such key.
Specified by:
`higherKey` in interface `NavigableMap<K,V>`
Parameters:
`key` - the key
Returns:
the least key greater than `key`,
or `null` if there is no such key
Throws:
`ClassCastException` - if the specified key cannot be compared
with the keys currently in the map
`NullPointerException` - if the specified key is null
and this map uses natural ordering, or its comparator
does not permit null keys
Since:
1.6

