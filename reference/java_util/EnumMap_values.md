#### values

```
public Collection<V> values()
```
Returns a `Collection` view of the values contained in this map.
The returned collection obeys the general contract outlined in
`Map.values()`. The collection's iterator will return the
values in the order their corresponding keys appear in map,
which is their natural order (the order in which the enum constants
are declared).
Specified by:
`values` in interface `Map<K extends Enum<K>,V>`
Overrides:
`values` in class `AbstractMap<K extends Enum<K>,V>`
Returns:
a collection view of the values contained in this map

