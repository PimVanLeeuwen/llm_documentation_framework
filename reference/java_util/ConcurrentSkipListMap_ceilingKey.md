#### ceilingKey

```
public K ceilingKey(K key)
```
Description copied from interface: `NavigableMap`
Returns the least key greater than or equal to the given key,
or `null` if there is no such key.
Specified by:
`ceilingKey` in interface `NavigableMap<K,V>`
Parameters:
`key` - the key
Returns:
the least key greater than or equal to `key`,
or `null` if there is no such key
Throws:
`ClassCastException` - if the specified key cannot be compared
with the keys currently in the map
`NullPointerException` - if the specified key is null

