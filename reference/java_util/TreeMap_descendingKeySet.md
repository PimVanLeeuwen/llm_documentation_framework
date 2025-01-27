#### descendingKeySet

```
public NavigableSet<K> descendingKeySet()
```
Description copied from interface: `NavigableMap`
Returns a reverse order `NavigableSet` view of the keys contained in this map.
The set's iterator returns the keys in descending order.
The set is backed by the map, so changes to the map are reflected in
the set, and vice-versa. If the map is modified while an iteration
over the set is in progress (except through the iterator's own `remove` operation), the results of the iteration are undefined. The
set supports element removal, which removes the corresponding mapping
from the map, via the `Iterator.remove`, `Set.remove`,
`removeAll`, `retainAll`, and `clear` operations.
It does not support the `add` or `addAll` operations.
Specified by:
`descendingKeySet` in interface `NavigableMap<K,V>`
Returns:
a reverse order navigable set view of the keys in this map
Since:
1.6

