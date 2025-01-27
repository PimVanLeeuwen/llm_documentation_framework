#### remove

```
public boolean remove(Object key,
                      Object value)
```
Removes the entry for a key only if currently mapped to a given value.
This is equivalent to
```
 
 if (map.containsKey(key) && Objects.equals(map.get(key), value)) {
   map.remove(key);
   return true;
 } else
   return false;
 
```
except that the action is performed atomically.
Specified by:
`remove` in interface `ConcurrentMap<K,V>`
Specified by:
`remove` in interface `Map<K,V>`
Parameters:
`key` - key with which the specified value is associated
`value` - value expected to be associated with the specified key
Returns:
`true` if the value was removed
Throws:
`ClassCastException` - if the specified key cannot be compared
with the keys currently in the map
`NullPointerException` - if the specified key is null

