#### navigableKeySet

```
NavigableSet<K> navigableKeySet()
```
Returns a `NavigableSet` view of the keys contained in this map.
The set's iterator returns the keys in ascending order.
The set is backed by the map, so changes to the map are
reflected in the set, and vice-versa. The set supports element
removal, which removes the corresponding mapping from the map,
via the `Iterator.remove`, `Set.remove`,
`removeAll`, `retainAll`, and `clear`
operations. It does not support the `add` or `addAll`
operations.The view's iterators and spliterators are
weakly consistent.
Specified by:
`navigableKeySet` in interface `NavigableMap<K,V>`
Returns:
a navigable set view of the keys in this map

