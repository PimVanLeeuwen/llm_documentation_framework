#### entrySet

```
public abstract Set<Map.Entry<K,V>> entrySet()
```
Description copied from interface: `Map`
Returns a `Set` view of the mappings contained in this map.
The set is backed by the map, so changes to the map are
reflected in the set, and vice-versa. If the map is modified
while an iteration over the set is in progress (except through
the iterator's own remove operation, or through the
setValue operation on a map entry returned by the
iterator) the results of the iteration are undefined. The set
supports element removal, which removes the corresponding
mapping from the map, via the Iterator.remove,
Set.remove, removeAll, retainAll and
clear operations. It does not support the
add or addAll operations.
Specified by:
`entrySet` in interface `Map<K,V>`
Returns:
a set view of the mappings contained in this map

