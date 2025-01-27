#### values

```
public Collection<V> values()
```
Returns a `Collection` view of the values contained in this map.
The collection is backed by the map, so changes to the map are
reflected in the collection, and vice-versa. The collection
supports element removal, which removes the corresponding
mapping from this map, via the `Iterator.remove`,
`Collection.remove`, `removeAll`,
`retainAll`, and `clear` operations. It does not
support the `add` or `addAll` operations.The view's iterators and spliterators are
weakly consistent.The view's `spliterator` reports `Spliterator.CONCURRENT`
and `Spliterator.NONNULL`.
Specified by:
`values` in interface `Map<K,V>`
Overrides:
`values` in class `AbstractMap<K,V>`
Returns:
the collection view

