#### descendingMap

```
public ConcurrentNavigableMap<K,V> descendingMap()
```
Description copied from interface: `ConcurrentNavigableMap`
Returns a reverse order view of the mappings contained in this map.
The descending map is backed by this map, so changes to the map are
reflected in the descending map, and vice-versa.The returned map has an ordering equivalent to
`Collections.reverseOrder``(comparator())`.
The expression `m.descendingMap().descendingMap()` returns a
view of `m` essentially equivalent to `m`.
Specified by:
`descendingMap` in interface `ConcurrentNavigableMap<K,V>`
Specified by:
`descendingMap` in interface `NavigableMap<K,V>`
Returns:
a reverse order view of this map

