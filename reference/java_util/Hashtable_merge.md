#### merge

```
public V merge(K key,
               V value,
               BiFunction<? super V,? super V,? extends V> remappingFunction)
```
Description copied from interface: `Map`
If the specified key is not already associated with a value or is
associated with null, associates it with the given non-null value.
Otherwise, replaces the associated value with the results of the given
remapping function, or removes if the result is `null`. This
method may be of use when combining multiple mapped values for a key.
For example, to either create or append a `String msg` to a
value mapping:
```
 
 map.merge(key, msg, String::concat)
 
```
If the function returns `null` the mapping is removed. If the
function itself throws an (unchecked) exception, the exception is
rethrown, and the current mapping is left unchanged.
Specified by:
`merge` in interface `Map<K,V>`
Parameters:
`key` - key with which the resulting value is to be associated
`value` - the non-null value to be merged with the existing value
associated with the key or, if no existing value or a null value
is associated with the key, to be associated with the key
`remappingFunction` - the function to recompute a value if present
Returns:
the new value associated with the specified key, or null if no
value is associated with the key




