#### computeIfPresent

```
default V computeIfPresent(K key,
                           BiFunction<? super K,? super V,? extends V> remappingFunction)
```
If the value for the specified key is present and non-null, attempts to
compute a new mapping given the key and its current mapped value.If the function returns `null`, the mapping is removed. If the
function itself throws an (unchecked) exception, the exception is
rethrown, and the current mapping is left unchanged.
Implementation Requirements:
The default implementation is equivalent to performing the following
steps for this `map`, then returning the current value or
`null` if now absent:
```
 
 if (map.get(key) != null) {
     V oldValue = map.get(key);
     V newValue = remappingFunction.apply(key, oldValue);
     if (newValue != null)
         map.put(key, newValue);
     else
         map.remove(key);
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
`remappingFunction` - the function to compute a value
Returns:
the new value associated with the specified key, or null if none
Throws:
`NullPointerException` - if the specified key is null and
this map does not support null keys, or the
remappingFunction is null
`UnsupportedOperationException` - if the `put` operation
is not supported by this map
(optional)
`ClassCastException` - if the class of the specified key or value
prevents it from being stored in this map
(optional)
Since:
1.8

