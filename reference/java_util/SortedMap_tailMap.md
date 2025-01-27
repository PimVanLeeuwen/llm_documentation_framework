#### tailMap

```
SortedMap<K,V> tailMap(K fromKey)
```
Returns a view of the portion of this map whose keys are
greater than or equal to `fromKey`. The returned map is
backed by this map, so changes in the returned map are
reflected in this map, and vice-versa. The returned map
supports all optional map operations that this map supports.The returned map will throw an `IllegalArgumentException`
on an attempt to insert a key outside its range.
Parameters:
`fromKey` - low endpoint (inclusive) of the keys in the returned map
Returns:
a view of the portion of this map whose keys are greater
than or equal to `fromKey`
Throws:
`ClassCastException` - if `fromKey` is not compatible
with this map's comparator (or, if the map has no comparator,
if `fromKey` does not implement `Comparable`).
Implementations may, but are not required to, throw this
exception if `fromKey` cannot be compared to keys
currently in the map.
`NullPointerException` - if `fromKey` is null and
this map does not permit null keys
`IllegalArgumentException` - if this map itself has a
restricted range, and `fromKey` lies outside the
bounds of the range

