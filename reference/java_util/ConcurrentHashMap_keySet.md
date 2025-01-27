#### keySet

```
public ConcurrentHashMap.KeySetView<K,V> keySet(V mappedValue)
```
Returns a `Set` view of the keys in this map, using the
given common mapped value for any additions (i.e., `Collection.add(E)` and `Collection.addAll(Collection)`).
This is of course only appropriate if it is acceptable to use
the same value for all additions from this view.
Parameters:
`mappedValue` - the mapped value to use for any additions
Returns:
the set view
Throws:
`NullPointerException` - if the mappedValue is null

