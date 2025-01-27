#### descendingMap

```
NavigableMap<K,V> descendingMap()
```
Returns a reverse order view of the mappings contained in this map.
The descending map is backed by this map, so changes to the map are
reflected in the descending map, and vice-versa. If either map is
modified while an iteration over a collection view of either map
is in progress (except through the iterator's own `remove`
operation), the results of the iteration are undefined.The returned map has an ordering equivalent to
`Collections.reverseOrder`(comparator()).
The expression `m.descendingMap().descendingMap()` returns a
view of `m` essentially equivalent to `m`.
Returns:
a reverse order view of this map

