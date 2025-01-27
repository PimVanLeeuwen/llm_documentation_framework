#### entrySet

```
public Set<Map.Entry<K,V>> entrySet()
```
Returns a `Set` view of the mappings contained in this map.The set's iterator returns the entries in ascending key order. The
set's spliterator additionally reports `Spliterator.CONCURRENT`,
`Spliterator.NONNULL`, `Spliterator.SORTED` and
`Spliterator.ORDERED`, with an encounter order that is ascending
key order.The set is backed by the map, so changes to the map are
reflected in the set, and vice-versa. The set supports element
removal, which removes the corresponding mapping from the map,
via the `Iterator.remove`, `Set.remove`,
`removeAll`, `retainAll` and `clear`
operations. It does not support the `add` or
`addAll` operations.The view's iterators and spliterators are
weakly consistent.The `Map.Entry` elements traversed by the `iterator`
or `spliterator` do not support the `setValue`
operation.
Specified by:
`entrySet` in interface `Map<K,V>`
Specified by:
`entrySet` in interface `SortedMap<K,V>`
Specified by:
`entrySet` in class `AbstractMap<K,V>`
Returns:
a set view of the mappings contained in this map,
sorted in ascending key order

