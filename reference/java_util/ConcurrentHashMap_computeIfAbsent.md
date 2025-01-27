#### computeIfAbsent

```
public V computeIfAbsent(K key,
                         Function<? super K,? extends V> mappingFunction)
```
If the specified key is not already associated with a value,
attempts to compute its value using the given mapping function
and enters it into this map unless `null`. The entire
method invocation is performed atomically, so the function is
applied at most once per key. Some attempted update operations
on this map by other threads may be blocked while computation
is in progress, so the computation should be short and simple,
and must not attempt to update any other mappings of this map.
Specified by:
`computeIfAbsent` in interface `ConcurrentMap<K,V>`
Specified by:
`computeIfAbsent` in interface `Map<K,V>`
Parameters:
`key` - key with which the specified value is to be associated
`mappingFunction` - the function to compute a value
Returns:
the current (existing or computed) value associated with
the specified key, or null if the computed value is null
Throws:
`NullPointerException` - if the specified key or mappingFunction
is null
`IllegalStateException` - if the computation detectably
attempts a recursive update to this map that would
otherwise never complete
`RuntimeException` - or Error if the mappingFunction does so,
in which case the mapping is left unestablished

