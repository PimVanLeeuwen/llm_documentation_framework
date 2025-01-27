#### get

```
public V get(Object key)
```
Returns the value to which the specified key is mapped,
or `null` if this map contains no mapping for the key.More formally, if this map contains a mapping from a key
`k` to a value `v` such that `(key.equals(k))`,
then this method returns `v`; otherwise it returns
`null`. (There can be at most one such mapping.)
Specified by:
`get` in interface `Map<K,V>`
Specified by:
`get` in class `Dictionary<K,V>`
Parameters:
`key` - the key whose associated value is to be returned
Returns:
the value to which the specified key is mapped, or
`null` if this map contains no mapping for the key
Throws:
`NullPointerException` - if the specified key is null
See Also:
`put(Object, Object)`

