#### keySet

```
public Set<K> keySet()
```
Returns a `Set` view of the keys contained in this map.
The set is backed by the map, so changes to the map are
reflected in the set, and vice-versa. If the map is modified
while an iteration over the set is in progress (except through
the iterator's own remove operation), the results of
the iteration are undefined. The set supports element removal,
which removes the corresponding mapping from the map, via the
Iterator.remove, Set.remove,
removeAll, retainAll, and clear
operations. It does not support the add or addAll
operations.
Specified by:
`keySet` in interface `Map<K,V>`
Implementation Requirements:
This implementation returns a set that subclasses `AbstractSet`.
The subclass's iterator method returns a "wrapper object" over this
map's entrySet() iterator. The size method
delegates to this map's size method and the
contains method delegates to this map's
containsKey method.The set is created the first time this method is called,
and returned in response to all subsequent calls. No synchronization
is performed, so there is a slight chance that multiple calls to this
method will not all return the same set.
Returns:
a set view of the keys contained in this map

