#### computeIfPresent

```
public V computeIfPresent(K key,
                          BiFunction<? super K,? super V,? extends V> remappingFunction)
```
If the value for the specified key is present, attempts to
compute a new mapping given the key and its current mapped
value. The function is NOT guaranteed to be applied
once atomically.
Specified by:
`computeIfPresent` in interface `ConcurrentMap<K,V>`
Specified by:
`computeIfPresent` in interface `Map<K,V>`
Parameters:
`key` - key with which a value may be associated
`remappingFunction` - the function to compute a value
Returns:
the new value associated with the specified key, or null if none
Throws:
`NullPointerException` - if the specified key is null
or the remappingFunction is null
Since:
1.8

