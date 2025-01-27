#### put

```
public V put(K key,
             V value)
```
Associates the specified value with the specified key in this map
(optional operation). If the map previously contained a mapping for
the key, the old value is replaced by the specified value. (A map
m is said to contain a mapping for a key k if and only
if `m.containsKey(k)` would return
true.)
Specified by:
`put` in interface `Map<K,V>`
Implementation Requirements:
This implementation always throws an
UnsupportedOperationException.
Parameters:
`key` - key with which the specified value is to be associated
`value` - value to be associated with the specified key
Returns:
the previous value associated with key, or
null if there was no mapping for key.
(A null return can also indicate that the map
previously associated null with key,
if the implementation supports null values.)
Throws:
`UnsupportedOperationException` - if the put operation
is not supported by this map
`ClassCastException` - if the class of the specified key or value
prevents it from being stored in this map
`NullPointerException` - if the specified key or value is null
and this map does not permit null keys or values
`IllegalArgumentException` - if some property of the specified key
or value prevents it from being stored in this map

