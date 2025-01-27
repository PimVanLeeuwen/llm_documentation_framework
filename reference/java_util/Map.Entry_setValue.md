#### setValue

```
V setValue(V value)
```
Replaces the value corresponding to this entry with the specified
value (optional operation). (Writes through to the map.) The
behavior of this call is undefined if the mapping has already been
removed from the map (by the iterator's remove operation).
Parameters:
`value` - new value to be stored in this entry
Returns:
old value corresponding to the entry
Throws:
`UnsupportedOperationException` - if the put operation
is not supported by the backing map
`ClassCastException` - if the class of the specified value
prevents it from being stored in the backing map
`NullPointerException` - if the backing map does not permit
null values, and the specified value is null
`IllegalArgumentException` - if some property of this value
prevents it from being stored in the backing map
`IllegalStateException` - implementations may, but are not
required to, throw this exception if the entry has been
removed from the backing map.

