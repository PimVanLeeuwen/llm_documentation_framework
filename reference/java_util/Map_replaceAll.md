#### replaceAll

```
default void replaceAll(BiFunction<? super K,? super V,? extends V> function)
```
Replaces each entry's value with the result of invoking the given
function on that entry until all entries have been processed or the
function throws an exception. Exceptions thrown by the function are
relayed to the caller.
Implementation Requirements:
The default implementation is equivalent to, for this `map`:
```
 
 for (Map.Entry<K, V> entry : map.entrySet())
     entry.setValue(function.apply(entry.getKey(), entry.getValue()));
 
```
The default implementation makes no guarantees about synchronization
or atomicity properties of this method. Any implementation providing
atomicity guarantees must override this method and document its
concurrency properties.
Parameters:
`function` - the function to apply to each entry
Throws:
`UnsupportedOperationException` - if the `set` operation
is not supported by this map's entry set iterator.
`ClassCastException` - if the class of a replacement value
prevents it from being stored in this map
`NullPointerException` - if the specified function is null, or the
specified replacement value is null, and this map does not permit null
values
`ClassCastException` - if a replacement value is of an inappropriate
type for this map
(optional)
`NullPointerException` - if function or a replacement value is null,
and this map does not permit null keys or values
(optional)
`IllegalArgumentException` - if some property of a replacement value
prevents it from being stored in this map
(optional)
`ConcurrentModificationException` - if an entry is found to be
removed during iteration
Since:
1.8

