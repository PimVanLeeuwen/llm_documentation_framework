#### remove

```
public V remove(Object key)
```
Removes the mapping for a key from this weak hash map if it is present.
More formally, if this map contains a mapping from key k to
value v such that `(key==null ? k==null :
key.equals(k))`, that mapping is removed. (The map can contain
at most one such mapping.)Returns the value to which this map previously associated the key,
or null if the map contained no mapping for the key. A
return value of null does not necessarily indicate
that the map contained no mapping for the key; it's also possible
that the map explicitly mapped the key to null.The map will not contain a mapping for the specified key once the
call returns.
Specified by:
`remove` in interface `Map<K,V>`
Overrides:
`remove` in class `AbstractMap<K,V>`
Parameters:
`key` - key whose mapping is to be removed from the map
Returns:
the previous value associated with key, or
null if there was no mapping for key

