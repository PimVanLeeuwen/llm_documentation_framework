#### newKeySet

```
public static <K> ConcurrentHashMap.KeySetView<K,Boolean> newKeySet(int initialCapacity)
```
Creates a new `Set` backed by a ConcurrentHashMap
from the given type to `Boolean.TRUE`.
Type Parameters:
`K` - the element type of the returned set
Parameters:
`initialCapacity` - The implementation performs internal
sizing to accommodate this many elements.
Returns:
the new set
Throws:
`IllegalArgumentException` - if the initial capacity of
elements is negative
Since:
1.8

