#### get

```
public V get(Object key)
```
Returns the value to which the specified key is mapped,
or `null` if this map contains no mapping for the key.More formally, if this map contains a mapping from a key
`k` to a value `v` such that `(key==null ? k==null :
key.equals(k))`, then this method returns `v`; otherwise
it returns `null`. (There can be at most one such mapping.)A return value of `null` does not necessarily
indicate that the map contains no mapping for the key; it's also
possible that the map explicitly maps the key to `null`.
The `containsKey` operation may be used to
distinguish these two cases.
Specified by:
`get` in interface `Map<K,V>`
Overrides:
`get` in class `HashMap<K,V>`
Parameters:
`key` - the key whose associated value is to be returned
Returns:
the value to which the specified key is mapped, or
`null` if this map contains no mapping for the key
See Also:
`HashMap.put(Object, Object)`

