#### computeIfAbsent

```
public V computeIfAbsent(K key,
                         Function<? super K,? extends V> mappingFunction)
```
Description copied from interface: `Map`
If the specified key is not already associated with a value (or is mapped
to `null`), attempts to compute its value using the given mapping
function and enters it into this map unless `null`.If the function returns `null` no mapping is recorded. If
the function itself throws an (unchecked) exception, the
exception is rethrown, and no mapping is recorded. The most
common usage is to construct a new object serving as an initial
mapped value or memoized result, as in:
```
 
 map.computeIfAbsent(key, k -> new Value(f(k)));
 
```
Or to implement a multi-value map, `Map<K,Collection<V>>`,
supporting multiple values per key:
```
 
 map.computeIfAbsent(key, k -> new HashSet<V>()).add(v);
 
```

Specified by:
`computeIfAbsent` in interface `Map<K,V>`
Parameters:
`key` - key with which the specified value is to be associated
`mappingFunction` - the function to compute a value
Returns:
the current (existing or computed) value associated with
the specified key, or null if the computed value is null

