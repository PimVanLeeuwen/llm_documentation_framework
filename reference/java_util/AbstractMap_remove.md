#### remove

```
public V remove(Object key)
```
Removes the mapping for a key from this map if it is present
(optional operation). More formally, if this map contains a mapping
from key k to value v such that
`(key==null ? k==null : key.equals(k))`, that mapping
is removed. (The map can contain at most one such mapping.)Returns the value to which this map previously associated the key,
or null if the map contained no mapping for the key.If this map permits null values, then a return value of
null does not necessarily indicate that the map
contained no mapping for the key; it's also possible that the map
explicitly mapped the key to null.The map will not contain a mapping for the specified key once the
call returns.
Specified by:
`remove` in interface `Map<K,V>`
Implementation Requirements:
This implementation iterates over entrySet() searching for an
entry with the specified key. If such an entry is found, its value is
obtained with its getValue operation, the entry is removed
from the collection (and the backing map) with the iterator's
remove operation, and the saved value is returned. If the
iteration terminates without finding such an entry, null is
returned. Note that this implementation requires linear time in the
size of the map; many implementations will override this method.Note that this implementation throws an
UnsupportedOperationException if the entrySet
iterator does not support the remove method and this map
contains a mapping for the specified key.
Parameters:
`key` - key whose mapping is to be removed from the map
Returns:
the previous value associated with key, or
null if there was no mapping for key.
Throws:
`UnsupportedOperationException` - if the remove operation
is not supported by this map
`ClassCastException` - if the key is of an inappropriate type for
this map
(optional)
`NullPointerException` - if the specified key is null and this
map does not permit null keys
(optional)

