#### remove

```
public V remove(Object key)
```
Removes the mapping for this key from this TreeMap if present.
Specified by:
`remove` in interface `Map<K,V>`
Overrides:
`remove` in class `AbstractMap<K,V>`
Parameters:
`key` - key for which mapping should be removed
Returns:
the previous value associated with `key`, or
`null` if there was no mapping for `key`.
(A `null` return can also indicate that the map
previously associated `null` with `key`.)
Throws:
`ClassCastException` - if the specified key cannot be compared
with the keys currently in the map
`NullPointerException` - if the specified key is null
and this map uses natural ordering, or its comparator
does not permit null keys

