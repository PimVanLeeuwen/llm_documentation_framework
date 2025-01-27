#### replace

```
public V replace(K key,
                 V value)
```
Replaces the entry for a key only if currently mapped to some value.
This is equivalent to
```
 
 if (map.containsKey(key)) {
   return map.put(key, value);
 } else
   return null;
 
```
except that the action is performed atomically.
Specified by:
`replace` in interface `ConcurrentMap<K,V>`
Specified by:
`replace` in interface `Map<K,V>`
Parameters:
`key` - key with which the specified value is associated
`value` - value to be associated with the specified key
Returns:
the previous value associated with the specified key,
or `null` if there was no mapping for the key
Throws:
`ClassCastException` - if the specified key cannot be compared
with the keys currently in the map
`NullPointerException` - if the specified key or value is null

