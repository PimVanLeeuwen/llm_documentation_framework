#### put

```
public V put(K key,
             V value)
```
Associates the specified value with the specified key in this identity
hash map. If the map previously contained a mapping for the key, the
old value is replaced.
Specified by:
`put` in interface `Map<K,V>`
Overrides:
`put` in class `AbstractMap<K,V>`
Parameters:
`key` - the key with which the specified value is to be associated
`value` - the value to be associated with the specified key
Returns:
the previous value associated with key, or
null if there was no mapping for key.
(A null return can also indicate that the map
previously associated null with key.)
See Also:
`Object.equals(Object)`,
`get(Object)`,
`containsKey(Object)`

