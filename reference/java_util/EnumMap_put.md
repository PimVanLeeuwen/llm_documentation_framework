#### put

```
public V put(K key,
             V value)
```
Associates the specified value with the specified key in this map.
If the map previously contained a mapping for this key, the old
value is replaced.
Specified by:
`put` in interface `Map<K extends Enum<K>,V>`
Overrides:
`put` in class `AbstractMap<K extends Enum<K>,V>`
Parameters:
`key` - the key with which the specified value is to be associated
`value` - the value to be associated with the specified key
Returns:
the previous value associated with specified key, or
null if there was no mapping for key. (A null
return can also indicate that the map previously associated
null with the specified key.)
Throws:
`NullPointerException` - if the specified key is null

