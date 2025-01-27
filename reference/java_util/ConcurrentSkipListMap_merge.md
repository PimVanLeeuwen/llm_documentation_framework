#### merge

```
public V merge(K key,
               V value,
               BiFunction<? super V,? super V,? extends V> remappingFunction)
```
If the specified key is not already associated with a value,
associates it with the given value. Otherwise, replaces the
value with the results of the given remapping function, or
removes if `null`. The function is NOT
guaranteed to be applied once atomically.
Specified by:
`merge` in interface `ConcurrentMap<K,V>`
Specified by:
`merge` in interface `Map<K,V>`
Parameters:
`key` - key with which the specified value is to be associated
`value` - the value to use if absent
`remappingFunction` - the function to recompute a value if present
Returns:
the new value associated with the specified key, or null if none
Throws:
`NullPointerException` - if the specified key or value is null
or the remappingFunction is null
Since:
1.8

