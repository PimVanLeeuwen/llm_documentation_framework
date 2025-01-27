#### computeIfAbsent

```
public V computeIfAbsent(K key,
                         Function<? super K,? extends V> mappingFunction)
```
If the specified key is not already associated with a value,
attempts to compute its value using the given mapping function
and enters it into this map unless `null`. The function
is NOT guaranteed to be applied once atomically only
if the value is not present.
Specified by:
`computeIfAbsent` in interface `ConcurrentMap<K,V>`
Specified by:
`computeIfAbsent` in interface `Map<K,V>`
Parameters:
`key` - key with which the specified value is to be associated
`mappingFunction` - the function to compute a value
Returns:
the current (existing or computed) value associated with
the specified key, or null if the computed value is null
Throws:
`NullPointerException` - if the specified key is null
or the mappingFunction is null
Since:
1.8

