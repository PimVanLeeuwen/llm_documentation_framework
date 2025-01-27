#### replaceAll

```
public void replaceAll(BiFunction<? super K,? super V,? extends V> function)
```
Description copied from interface: `ConcurrentMap`
Replaces each entry's value with the result of invoking the given
function on that entry until all entries have been processed or the
function throws an exception. Exceptions thrown by the function are
relayed to the caller.
Specified by:
`replaceAll` in interface `ConcurrentMap<K,V>`
Specified by:
`replaceAll` in interface `Map<K,V>`
Parameters:
`function` - the function to apply to each entry




