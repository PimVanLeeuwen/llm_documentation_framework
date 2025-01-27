#### containsValue

```
boolean containsValue(Object value)
```
Returns true if this map maps one or more keys to the
specified value. More formally, returns true if and only if
this map contains at least one mapping to a value v such that
(value==null ? v==null : value.equals(v)). This operation
will probably require time linear in the map size for most
implementations of the Map interface.
Parameters:
`value` - value whose presence in this map is to be tested
Returns:
true if this map maps one or more keys to the
specified value
Throws:
`ClassCastException` - if the value is of an inappropriate type for
this map
(optional)
`NullPointerException` - if the specified value is null and this
map does not permit null values
(optional)

