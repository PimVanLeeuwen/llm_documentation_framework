#### getOrDefault

```
default V getOrDefault(Object key,
                       V defaultValue)
```
Returns the value to which the specified key is mapped, or
`defaultValue` if this map contains no mapping for the key.
Specified by:
`getOrDefault` in interface `Map<K,V>`
Implementation Note:
This implementation assumes that the ConcurrentMap cannot
contain null values and `get()` returning null unambiguously means
the key is absent. Implementations which support null values
must override this default implementation.
Parameters:
`key` - the key whose associated value is to be returned
`defaultValue` - the default mapping of the key
Returns:
the value to which the specified key is mapped, or
`defaultValue` if this map contains no mapping for the key
Throws:
`ClassCastException` - if the key is of an inappropriate type for
this map
(optional)
`NullPointerException` - if the specified key is null and this map
does not permit null keys
(optional)
Since:
1.8

