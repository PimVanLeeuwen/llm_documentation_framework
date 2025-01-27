#### computeIfAbsent

```
default V computeIfAbsent(K key,
                          Function<? super K,? extends V> mappingFunction)
```
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
Implementation Requirements:
The default implementation is equivalent to the following steps for this
`map`, then returning the current value or `null` if now
absent:
```
 
 if (map.get(key) == null) {
     V newValue = mappingFunction.apply(key);
     if (newValue != null)
         return map.putIfAbsent(key, newValue);
 }
 
```
The default implementation may retry these steps when multiple
threads attempt updates including potentially calling the mapping
function multiple times.This implementation assumes that the ConcurrentMap cannot contain null
values and `get()` returning null unambiguously means the key is
absent. Implementations which support null values must
override this default implementation.
Parameters:
`key` - key with which the specified value is to be associated
`mappingFunction` - the function to compute a value
Returns:
the current (existing or computed) value associated with
the specified key, or null if the computed value is null
Throws:
`UnsupportedOperationException` - if the `put` operation
is not supported by this map
(optional)
`ClassCastException` - if the class of the specified key or value
prevents it from being stored in this map
(optional)
`NullPointerException` - if the specified key is null and
this map does not support null keys, or the mappingFunction
is null
Since:
1.8

