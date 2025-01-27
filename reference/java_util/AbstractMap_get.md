#### get

```
public V get(Object key)
```
Returns the value to which the specified key is mapped,
or `null` if this map contains no mapping for the key.More formally, if this map contains a mapping from a key
`k` to a value `v` such that `(key==null ? k==null :
key.equals(k))`, then this method returns `v`; otherwise
it returns `null`. (There can be at most one such mapping.)If this map permits null values, then a return value of
`null` does not necessarily indicate that the map
contains no mapping for the key; it's also possible that the map
explicitly maps the key to `null`. The `containsKey` operation may be used to distinguish these two cases.
Specified by:
`get` in interface `Map<K,V>`
Implementation Requirements:
This implementation iterates over entrySet() searching
for an entry with the specified key. If such an entry is found,
the entry's value is returned. If the iteration terminates without
finding such an entry, null is returned. Note that this
implementation requires linear time in the size of the map; many
implementations will override this method.
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

