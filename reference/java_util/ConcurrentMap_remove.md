#### remove

```
boolean remove(Object key,
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
`remove` in interface `Map<K,V>`
Implementation Note:
This implementation intentionally re-abstracts the
inappropriate default provided in `Map`.
Parameters:
`key` - key with which the specified value is associated
`value` - value expected to be associated with the specified key
Returns:
`true` if the value was removed
Throws:
`UnsupportedOperationException` - if the `remove` operation
is not supported by this map
`ClassCastException` - if the key or value is of an inappropriate
type for this map
(optional)
`NullPointerException` - if the specified key or value is null,
and this map does not permit null keys or values
(optional)

