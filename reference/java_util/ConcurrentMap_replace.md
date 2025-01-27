#### replace

```
V replace(K key,
          V value)
```
Replaces the entry for a key only if currently mapped to some value.
This is equivalent to
```
 
 if (map.containsKey(key)) {
   return map.put(key, value);
 } else
   return null;
 
```
except that the action is performed atomically.
Specified by:
`replace` in interface `Map<K,V>`
Implementation Note:
This implementation intentionally re-abstracts the
inappropriate default provided in `Map`.
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
`ClassCastException` - if the class of the specified key or value
prevents it from being stored in this map
`NullPointerException` - if the specified key or value is null,
and this map does not permit null keys or values
`IllegalArgumentException` - if some property of the specified key
or value prevents it from being stored in this map

