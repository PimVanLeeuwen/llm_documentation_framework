#### propertyNames

```
public Enumeration<?> propertyNames()
```
Returns an enumeration of all the keys in this property list,
including distinct keys in the default property list if a key
of the same name has not already been found from the main
properties list.
Returns:
an enumeration of all the keys in this property list, including
the keys in the default property list.
Throws:
`ClassCastException` - if any key in this property list
is not a string.
See Also:
`Enumeration`,
`defaults`,
`stringPropertyNames()`

