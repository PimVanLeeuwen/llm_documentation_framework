#### entrySet

```
public Set<Map.Entry<K,V>> entrySet()
```
Returns a `Set` view of the mappings contained in this map.
The set is backed by the map, so changes to the map are
reflected in the set, and vice-versa. The set supports element
removal, which removes the corresponding mapping from the map,
via the `Iterator.remove`, `Set.remove`,
`removeAll`, `retainAll`, and `clear`
operations.The view's iterators and spliterators are
weakly consistent.The view's `spliterator` reports `Spliterator.CONCURRENT`,
`Spliterator.DISTINCT`, and `Spliterator.NONNULL`.
Specified by:
`entrySet` in interface `Map<K,V>`
Specified by:
`entrySet` in class `AbstractMap<K,V>`
Returns:
the set view

