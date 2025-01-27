#### putIfAbsent

```
public V putIfAbsent(K key,
                     V value)
```
If the specified key is not already associated
with a value, associate it with the given value.
This is equivalent to
```
 
 if (!map.containsKey(key))
   return map.put(key, value);
 else
   return map.get(key);
 
```
except that the action is performed atomically.
Specified by:
`putIfAbsent` in interface `ConcurrentMap<K,V>`
Specified by:
`putIfAbsent` in interface `Map<K,V>`
Parameters:
`key` - key with which the specified value is to be associated
`value` - value to be associated with the specified key
Returns:
the previous value associated with the specified key,
or `null` if there was no mapping for the key
Throws:
`ClassCastException` - if the specified key cannot be compared
with the keys currently in the map
`NullPointerException` - if the specified key or value is null

