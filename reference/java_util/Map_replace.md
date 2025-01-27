#### replace

```
default V replace(K key,
                  V value)
```
Replaces the entry for the specified key only if it is
currently mapped to some value.
Implementation Requirements:
The default implementation is equivalent to, for this `map`:
```
 
 if (map.containsKey(key)) {
     return map.put(key, value);
 } else
     return null;
 
```
The default implementation makes no guarantees about synchronization
or atomicity properties of this method. Any implementation providing
atomicity guarantees must override this method and document its
concurrency properties.
Parameters:
`key` - key with which the specified value is associated
`value` - value to be associated with the specified key
Returns:
the previous value associated with the specified key, or
`null` if there was no mapping for the key.
(A `null` return can also indicate that the map
previously associated `null` with the key,
if the implementation supports null values.)
Throws:
`UnsupportedOperationException` - if the `put` operation
is not supported by this map
(optional)
`ClassCastException` - if the class of the specified key or value
prevents it from being stored in this map
(optional)
`NullPointerException` - if the specified key or value is null,
and this map does not permit null keys or values
`IllegalArgumentException` - if some property of the specified key
or value prevents it from being stored in this map
Since:
1.8

