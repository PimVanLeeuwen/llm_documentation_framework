#### keySet

```
public Set<K> keySet()
```
Returns a `Set` view of the keys contained in this map.The set's iterator returns the keys in ascending order.
The set's spliterator is
late-binding,
fail-fast, and additionally reports `Spliterator.SORTED`
and `Spliterator.ORDERED` with an encounter order that is ascending
key order. The spliterator's comparator (see
`Spliterator.getComparator()`) is `null` if
the tree map's comparator (see `comparator()`) is `null`.
Otherwise, the spliterator's comparator is the same as or imposes the
same total ordering as the tree map's comparator.The set is backed by the map, so changes to the map are
reflected in the set, and vice-versa. If the map is modified
while an iteration over the set is in progress (except through
the iterator's own `remove` operation), the results of
the iteration are undefined. The set supports element removal,
which removes the corresponding mapping from the map, via the
`Iterator.remove`, `Set.remove`,
`removeAll`, `retainAll`, and `clear`
operations. It does not support the `add` or `addAll`
operations.
Specified by:
`keySet` in interface `Map<K,V>`
Specified by:
`keySet` in interface `SortedMap<K,V>`
Overrides:
`keySet` in class `AbstractMap<K,V>`
Returns:
a set view of the keys contained in this map

