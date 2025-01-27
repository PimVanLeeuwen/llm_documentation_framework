#### containsKey

```
public boolean containsKey(Object key)
```
Returns `true` if this map contains a mapping for the specified
key.
Specified by:
`containsKey` in interface `Map<K,V>`
Overrides:
`containsKey` in class `AbstractMap<K,V>`
Parameters:
`key` - key whose presence in this map is to be tested
Returns:
`true` if this map contains a mapping for the
specified key
Throws:
`ClassCastException` - if the specified key cannot be compared
with the keys currently in the map
`NullPointerException` - if the specified key is null
and this map uses natural ordering, or its comparator
does not permit null keys

