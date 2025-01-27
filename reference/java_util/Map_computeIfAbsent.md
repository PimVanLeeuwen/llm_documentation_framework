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

Implementation Requirements:
The default implementation is equivalent to the following steps for this
`map`, then returning the current value or `null` if now
absent:
```
 
 if (map.get(key) == null) {
     V newValue = mappingFunction.apply(key);
     if (newValue != null)
         map.put(key, newValue);
 }
 
```
The default implementation makes no guarantees about synchronization
or atomicity properties of this method. Any implementation providing
atomicity guarantees must override this method and document its
concurrency properties. In particular, all implementations of
subinterface `ConcurrentMap` must document
whether the function is applied once atomically only if the value is not
present.
Parameters:
`key` - key with which the specified value is to be associated
`mappingFunction` - the function to compute a value
Returns:
the current (existing or computed) value associated with
the specified key, or null if the computed value is null
Throws:
`NullPointerException` - if the specified key is null and
this map does not support null keys, or the mappingFunction
is null
`UnsupportedOperationException` - if the `put` operation
is not supported by this map
(optional)
`ClassCastException` - if the class of the specified key or value
prevents it from being stored in this map
(optional)
Since:
1.8

