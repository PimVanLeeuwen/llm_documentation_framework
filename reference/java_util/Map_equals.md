#### equals

```
boolean equals(Object o)
```
Compares the specified object with this map for equality. Returns
true if the given object is also a map and the two maps
represent the same mappings. More formally, two maps m1 and
m2 represent the same mappings if
m1.entrySet().equals(m2.entrySet()). This ensures that the
equals method works properly across different implementations
of the Map interface.
Overrides:
`equals` in class `Object`
Parameters:
`o` - object to be compared for equality with this map
Returns:
true if the specified object is equal to this map
See Also:
`Object.hashCode()`,
`HashMap`

