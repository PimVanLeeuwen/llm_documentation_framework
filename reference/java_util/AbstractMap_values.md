#### values

```
public Collection<V> values()
```
Returns a `Collection` view of the values contained in this map.
The collection is backed by the map, so changes to the map are
reflected in the collection, and vice-versa. If the map is
modified while an iteration over the collection is in progress
(except through the iterator's own remove operation),
the results of the iteration are undefined. The collection
supports element removal, which removes the corresponding
mapping from the map, via the Iterator.remove,
Collection.remove, removeAll,
retainAll and clear operations. It does not
support the add or addAll operations.
Specified by:
`values` in interface `Map<K,V>`
Implementation Requirements:
This implementation returns a collection that subclasses `AbstractCollection`. The subclass's iterator method returns a
"wrapper object" over this map's entrySet() iterator.
The size method delegates to this map's size
method and the contains method delegates to this map's
containsValue method.The collection is created the first time this method is called, and
returned in response to all subsequent calls. No synchronization is
performed, so there is a slight chance that multiple calls to this
method will not all return the same collection.
Returns:
a collection view of the values contained in this map

