#### compute

```
public V compute(K key,
                 BiFunction<? super K,? super V,? extends V> remappingFunction)
```
Attempts to compute a mapping for the specified key and its
current mapped value (or `null` if there is no current
mapping). The function is NOT guaranteed to be applied
once atomically.
Specified by:
`compute` in interface `ConcurrentMap<K,V>`
Specified by:
`compute` in interface `Map<K,V>`
Parameters:
`key` - key with which the specified value is to be associated
`remappingFunction` - the function to compute a value
Returns:
the new value associated with the specified key, or null if none
Throws:
`NullPointerException` - if the specified key is null
or the remappingFunction is null
Since:
1.8

