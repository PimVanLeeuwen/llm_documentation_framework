#### computeIfPresent

```
public V computeIfPresent(K key,
                          BiFunction<? super K,? super V,? extends V> remappingFunction)
```
If the value for the specified key is present, attempts to
compute a new mapping given the key and its current mapped
value. The entire method invocation is performed atomically.
Some attempted update operations on this map by other threads
may be blocked while computation is in progress, so the
computation should be short and simple, and must not attempt to
update any other mappings of this map.
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
`NullPointerException` - if the specified key or remappingFunction
is null
`IllegalStateException` - if the computation detectably
attempts a recursive update to this map that would
otherwise never complete
`RuntimeException` - or Error if the remappingFunction does so,
in which case the mapping is unchanged

