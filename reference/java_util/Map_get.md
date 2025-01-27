#### get

```
V get(Object key)
```
Returns the value to which the specified key is mapped,
or `null` if this map contains no mapping for the key.More formally, if this map contains a mapping from a key
`k` to a value `v` such that `(key==null ? k==null :
key.equals(k))`, then this method returns `v`; otherwise
it returns `null`. (There can be at most one such mapping.)If this map permits null values, then a return value of
`null` does not necessarily indicate that the map
contains no mapping for the key; it's also possible that the map
explicitly maps the key to `null`. The `containsKey` operation may be used to distinguish these two cases.
Parameters:
`key` - the key whose associated value is to be returned
Returns:
the value to which the specified key is mapped, or
`null` if this map contains no mapping for the key
Throws:
`ClassCastException` - if the key is of an inappropriate type for
this map
(optional)
`NullPointerException` - if the specified key is null and this map
does not permit null keys
(optional)

