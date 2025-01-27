#### compute

```
default V compute(K key,
                  BiFunction<? super K,? super V,? extends V> remappingFunction)
```
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
Implementation Requirements:
The default implementation is equivalent to performing the following
steps for this `map`, then returning the current value or
`null` if absent:
```
 
 V oldValue = map.get(key);
 V newValue = remappingFunction.apply(key, oldValue);
 if (oldValue != null ) {
    if (newValue != null)
       map.replace(key, oldValue, newValue);
    else
       map.remove(key, oldValue);
 } else {
    if (newValue != null)
       map.putIfAbsent(key, newValue);
    else
       return null;
 }
 
```
The default implementation may retry these steps when multiple
threads attempt updates including potentially calling the remapping
function multiple times.This implementation assumes that the ConcurrentMap cannot contain null
values and `get()` returning null unambiguously means the key is
absent. Implementations which support null values must
override this default implementation.
Parameters:
`key` - key with which the specified value is to be associated
`remappingFunction` - the function to compute a value
Returns:
the new value associated with the specified key, or null if none
Throws:
`UnsupportedOperationException` - if the `put` operation
is not supported by this map
(optional)
`ClassCastException` - if the class of the specified key or value
prevents it from being stored in this map
(optional)
`NullPointerException` - if the specified key is null and
this map does not support null keys, or the
remappingFunction is null
Since:
1.8

