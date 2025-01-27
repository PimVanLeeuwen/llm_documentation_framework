#### replaceAll

```
default void replaceAll(BiFunction<? super K,? super V,? extends V> function)
```
Replaces each entry's value with the result of invoking the given
function on that entry until all entries have been processed or the
function throws an exception. Exceptions thrown by the function are
relayed to the caller.
Specified by:
`replaceAll` in interface `Map<K,V>`
Implementation Requirements:
The default implementation is equivalent to, for this `map`:
```
 
 for ((Map.Entry<K, V> entry : map.entrySet())
     do {
        K k = entry.getKey();
        V v = entry.getValue();
     } while(!replace(k, v, function.apply(k, v)));
 
```
The default implementation may retry these steps when multiple
threads attempt updates including potentially calling the function
repeatedly for a given key.This implementation assumes that the ConcurrentMap cannot contain null
values and `get()` returning null unambiguously means the key is
absent. Implementations which support null values must
override this default implementation.
Parameters:
`function` - the function to apply to each entry
Throws:
`UnsupportedOperationException` - if the `set` operation
is not supported by this map's entry set iterator.
`NullPointerException` - if function or a replacement value is null,
and this map does not permit null keys or values
(optional)
`ClassCastException` - if a replacement value is of an inappropriate
type for this map
(optional)
`IllegalArgumentException` - if some property of a replacement value
prevents it from being stored in this map
(optional)
Since:
1.8

