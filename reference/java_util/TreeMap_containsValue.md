#### containsValue

```
public boolean containsValue(Object value)
```
Returns `true` if this map maps one or more keys to the
specified value. More formally, returns `true` if and only if
this map contains at least one mapping to a value `v` such
that `(value==null ? v==null : value.equals(v))`. This
operation will probably require time linear in the map size for
most implementations.
Specified by:
`containsValue` in interface `Map<K,V>`
Overrides:
`containsValue` in class `AbstractMap<K,V>`
Parameters:
`value` - value whose presence in this map is to be tested
Returns:
`true` if a mapping to `value` exists;
`false` otherwise
Since:
1.2

