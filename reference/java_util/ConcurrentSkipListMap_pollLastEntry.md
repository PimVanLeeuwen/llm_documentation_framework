#### pollLastEntry

```
public Map.Entry<K,V> pollLastEntry()
```
Removes and returns a key-value mapping associated with
the greatest key in this map, or `null` if the map is empty.
The returned entry does not support
the `Entry.setValue` method.
Specified by:
`pollLastEntry` in interface `NavigableMap<K,V>`
Returns:
the removed last entry of this map,
or `null` if this map is empty

