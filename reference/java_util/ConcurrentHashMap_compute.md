#### compute

```
public V compute(K key,
                 BiFunction<? super K,? super V,? extends V> remappingFunction)
```
Attempts to compute a mapping for the specified key and its
current mapped value (or `null` if there is no current
mapping). The entire method invocation is performed atomically.
Some attempted update operations on this map by other threads
may be blocked while computation is in progress, so the
computation should be short and simple, and must not attempt to
update any other mappings of this Map.
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
`NullPointerException` - if the specified key or remappingFunction
is null
`IllegalStateException` - if the computation detectably
attempts a recursive update to this map that would
otherwise never complete
`RuntimeException` - or Error if the remappingFunction does so,
in which case the mapping is unchanged

