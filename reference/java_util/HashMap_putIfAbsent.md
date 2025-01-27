#### putIfAbsent

```
public V putIfAbsent(K key,
                     V value)
```
Description copied from interface: `Map`
If the specified key is not already associated with a value (or is mapped
to `null`) associates it with the given value and returns
`null`, else returns the current value.
Specified by:
`putIfAbsent` in interface `Map<K,V>`
Parameters:
`key` - key with which the specified value is to be associated
`value` - value to be associated with the specified key
Returns:
the previous value associated with the specified key, or
`null` if there was no mapping for the key.
(A `null` return can also indicate that the map
previously associated `null` with the key,
if the implementation supports null values.)

