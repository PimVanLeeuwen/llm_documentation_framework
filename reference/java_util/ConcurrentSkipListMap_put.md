#### put

```
public V put(K key,
             V value)
```
Associates the specified value with the specified key in this map.
If the map previously contained a mapping for the key, the old
value is replaced.
Specified by:
`put` in interface `Map<K,V>`
Overrides:
`put` in class `AbstractMap<K,V>`
Parameters:
`key` - key with which the specified value is to be associated
`value` - value to be associated with the specified key
Returns:
the previous value associated with the specified key, or
`null` if there was no mapping for the key
Throws:
`ClassCastException` - if the specified key cannot be compared
with the keys currently in the map
`NullPointerException` - if the specified key or value is null

