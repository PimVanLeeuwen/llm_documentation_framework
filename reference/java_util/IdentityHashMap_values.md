#### values

```
public Collection<V> values()
```
Returns a `Collection` view of the values contained in this map.
The collection is backed by the map, so changes to the map are
reflected in the collection, and vice-versa. If the map is
modified while an iteration over the collection is in progress,
the results of the iteration are undefined. The collection
supports element removal, which removes the corresponding
mapping from the map, via the Iterator.remove,
Collection.remove, removeAll,
retainAll and clear methods. It does not
support the add or addAll methods.While the object returned by this method implements the
Collection interface, it does not obey
Collection's general contract. Like its backing map,
the collection returned by this method defines element equality as
reference-equality rather than object-equality. This affects the
behavior of its contains, remove and
containsAll methods.
Specified by:
`values` in interface `Map<K,V>`
Overrides:
`values` in class `AbstractMap<K,V>`
Returns:
a collection view of the values contained in this map

