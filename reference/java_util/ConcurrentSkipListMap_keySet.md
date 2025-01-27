#### keySet

```
public NavigableSet<K> keySet()
```
Returns a `NavigableSet` view of the keys contained in this map.The set's iterator returns the keys in ascending order.
The set's spliterator additionally reports `Spliterator.CONCURRENT`,
`Spliterator.NONNULL`, `Spliterator.SORTED` and
`Spliterator.ORDERED`, with an encounter order that is ascending
key order. The spliterator's comparator (see
`Spliterator.getComparator()`) is `null` if
the map's comparator (see `comparator()`) is `null`.
Otherwise, the spliterator's comparator is the same as or imposes the
same total ordering as the map's comparator.The set is backed by the map, so changes to the map are
reflected in the set, and vice-versa. The set supports element
removal, which removes the corresponding mapping from the map,
via the `Iterator.remove`, `Set.remove`,
`removeAll`, `retainAll`, and `clear`
operations. It does not support the `add` or `addAll`
operations.The view's iterators and spliterators are
weakly consistent.This method is equivalent to method `navigableKeySet`.
Specified by:
`keySet` in interface `ConcurrentNavigableMap<K,V>`
Specified by:
`keySet` in interface `Map<K,V>`
Specified by:
`keySet` in interface `SortedMap<K,V>`
Overrides:
`keySet` in class `AbstractMap<K,V>`
Returns:
a navigable set view of the keys in this map

