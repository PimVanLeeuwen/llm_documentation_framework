#### getOrDefault

```
public V getOrDefault(Object key,
                      V defaultValue)
```
Returns the value to which the specified key is mapped,
or the given defaultValue if this map contains no mapping for the key.
Specified by:
`getOrDefault` in interface `ConcurrentMap<K,V>`
Specified by:
`getOrDefault` in interface `Map<K,V>`
Parameters:
`key` - the key
`defaultValue` - the value to return if this map contains
no mapping for the given key
Returns:
the mapping for the key, if present; else the defaultValue
Throws:
`NullPointerException` - if the specified key is null
Since:
1.8

