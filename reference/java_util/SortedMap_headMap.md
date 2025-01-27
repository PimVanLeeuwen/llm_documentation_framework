#### headMap

```
SortedMap<K,V> headMap(K toKey)
```
Returns a view of the portion of this map whose keys are
strictly less than `toKey`. The returned map is backed
by this map, so changes in the returned map are reflected in
this map, and vice-versa. The returned map supports all
optional map operations that this map supports.The returned map will throw an `IllegalArgumentException`
on an attempt to insert a key outside its range.
Parameters:
`toKey` - high endpoint (exclusive) of the keys in the returned map
Returns:
a view of the portion of this map whose keys are strictly
less than `toKey`
Throws:
`ClassCastException` - if `toKey` is not compatible
with this map's comparator (or, if the map has no comparator,
if `toKey` does not implement `Comparable`).
Implementations may, but are not required to, throw this
exception if `toKey` cannot be compared to keys
currently in the map.
`NullPointerException` - if `toKey` is null and
this map does not permit null keys
`IllegalArgumentException` - if this map itself has a
restricted range, and `toKey` lies outside the
bounds of the range

