#### put

```
public Object put(Object name,
                  Object value)
```
Associates the specified value with the specified attribute name
(key) in this Map. If the Map previously contained a mapping for
the attribute name, the old value is replaced.
Specified by:
`put` in interface `Map<Object,Object>`
Parameters:
`name` - the attribute name
`value` - the attribute value
Returns:
the previous value of the attribute, or null if none
Throws:
`ClassCastException` - if the name is not a Attributes.Name
or the value is not a String

