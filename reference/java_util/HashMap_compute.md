#### compute

```
public V compute(K key,
                 BiFunction<? super K,? super V,? extends V> remappingFunction)
```
Description copied from interface: `Map`
Attempts to compute a mapping for the specified key and its current
mapped value (or `null` if there is no current mapping). For
example, to either create or append a `String` msg to a value
mapping:
```
 
 map.compute(key, (k, v) -> (v == null) ? msg : v.concat(msg))
```
(Method `merge()` is often simpler to use for such purposes.)If the function returns `null`, the mapping is removed (or
remains absent if initially absent). If the function itself throws an
(unchecked) exception, the exception is rethrown, and the current mapping
is left unchanged.
Specified by:
`compute` in interface `Map<K,V>`
Parameters:
`key` - key with which the specified value is to be associated
`remappingFunction` - the function to compute a value
Returns:
the new value associated with the specified key, or null if none

