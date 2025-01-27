#### values

```
public Collection<V> values()
```
Returns a `Collection` view of the values contained in this map.The collection's iterator returns the values in ascending order
of the corresponding keys. The collections's spliterator additionally
reports `Spliterator.CONCURRENT`, `Spliterator.NONNULL` and
`Spliterator.ORDERED`, with an encounter order that is ascending
order of the corresponding keys.The collection is backed by the map, so changes to the map are
reflected in the collection, and vice-versa. The collection
supports element removal, which removes the corresponding
mapping from the map, via the `Iterator.remove`,
`Collection.remove`, `removeAll`,
`retainAll` and `clear` operations. It does not
support the `add` or `addAll` operations.The view's iterators and spliterators are
weakly consistent.
Specified by:
`values` in interface `Map<K,V>`
Specified by:
`values` in interface `SortedMap<K,V>`
Overrides:
`values` in class `AbstractMap<K,V>`
Returns:
a collection view of the values contained in this map

