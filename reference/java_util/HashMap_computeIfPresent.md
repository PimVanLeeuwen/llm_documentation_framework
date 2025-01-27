#### computeIfPresent

```
public V computeIfPresent(K key,
                          BiFunction<? super K,? super V,? extends V> remappingFunction)
```
Description copied from interface: `Map`
If the value for the specified key is present and non-null, attempts to
compute a new mapping given the key and its current mapped value.If the function returns `null`, the mapping is removed. If the
function itself throws an (unchecked) exception, the exception is
rethrown, and the current mapping is left unchanged.
Specified by:
`computeIfPresent` in interface `Map<K,V>`
Parameters:
`key` - key with which the specified value is to be associated
`remappingFunction` - the function to compute a value
Returns:
the new value associated with the specified key, or null if none

