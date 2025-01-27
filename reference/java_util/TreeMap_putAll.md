#### putAll

```
public void putAll(Map<? extends K,? extends V> map)
```
Copies all of the mappings from the specified map to this map.
These mappings replace any mappings that this map had for any
of the keys currently in the specified map.
Specified by:
`putAll` in interface `Map<K,V>`
Overrides:
`putAll` in class `AbstractMap<K,V>`
Parameters:
`map` - mappings to be stored in this map
Throws:
`ClassCastException` - if the class of a key or value in
the specified map prevents it from being stored in this map
`NullPointerException` - if the specified map is null or
the specified map contains a null key and this map does not
permit null keys

