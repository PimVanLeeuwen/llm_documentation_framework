#### pollFirstEntry

```
public Map.Entry<K,V> pollFirstEntry()
```
Removes and returns a key-value mapping associated with
the least key in this map, or `null` if the map is empty.
The returned entry does not support
the `Entry.setValue` method.
Specified by:
`pollFirstEntry` in interface `NavigableMap<K,V>`
Returns:
the removed first entry of this map,
or `null` if this map is empty

