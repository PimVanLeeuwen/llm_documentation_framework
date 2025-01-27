#### getOrDefault

```
default V getOrDefault(Object key,
                       V defaultValue)
```
Returns the value to which the specified key is mapped, or
`defaultValue` if this map contains no mapping for the key.
Implementation Requirements:
The default implementation makes no guarantees about synchronization
or atomicity properties of this method. Any implementation providing
atomicity guarantees must override this method and document its
concurrency properties.
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

