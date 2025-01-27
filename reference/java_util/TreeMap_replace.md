#### replace

```
public V replace(K key,
                 V value)
```
Description copied from interface: `Map`
Replaces the entry for the specified key only if it is
currently mapped to some value.
Specified by:
`replace` in interface `Map<K,V>`
Parameters:
`key` - key with which the specified value is associated
`value` - value to be associated with the specified key
Returns:
the previous value associated with the specified key, or
`null` if there was no mapping for the key.
(A `null` return can also indicate that the map
previously associated `null` with the key,
if the implementation supports null values.)

