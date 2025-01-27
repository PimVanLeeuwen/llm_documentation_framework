#### merge

```
public V merge(K key,
               V value,
               BiFunction<? super V,? super V,? extends V> remappingFunction)
```
If the specified key is not already associated with a
(non-null) value, associates it with the given value.
Otherwise, replaces the value with the results of the given
remapping function, or removes if `null`. The entire
method invocation is performed atomically. Some attempted
update operations on this map by other threads may be blocked
while computation is in progress, so the computation should be
short and simple, and must not attempt to update any other
mappings of this Map.
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
`NullPointerException` - if the specified key or the
remappingFunction is null
`RuntimeException` - or Error if the remappingFunction does so,
in which case the mapping is unchanged

