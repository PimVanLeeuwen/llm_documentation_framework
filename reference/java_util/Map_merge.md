#### merge

```
default V merge(K key,
                V value,
                BiFunction<? super V,? super V,? extends V> remappingFunction)
```
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
Implementation Requirements:
The default implementation is equivalent to performing the following
steps for this `map`, then returning the current value or
`null` if absent:
```
 
 V oldValue = map.get(key);
 V newValue = (oldValue == null) ? value :
              remappingFunction.apply(oldValue, value);
 if (newValue == null)
     map.remove(key);
 else
     map.put(key, newValue);
 
```
The default implementation makes no guarantees about synchronization
or atomicity properties of this method. Any implementation providing
atomicity guarantees must override this method and document its
concurrency properties. In particular, all implementations of
subinterface `ConcurrentMap` must document
whether the function is applied once atomically only if the value is not
present.
Parameters:
`key` - key with which the resulting value is to be associated
`value` - the non-null value to be merged with the existing value
associated with the key or, if no existing value or a null value
is associated with the key, to be associated with the key
`remappingFunction` - the function to recompute a value if present
Returns:
the new value associated with the specified key, or null if no
value is associated with the key
Throws:
`UnsupportedOperationException` - if the `put` operation
is not supported by this map
(optional)
`ClassCastException` - if the class of the specified key or value
prevents it from being stored in this map
(optional)
`NullPointerException` - if the specified key is null and this map
does not support null keys or the value or remappingFunction is
null
Since:
1.8




