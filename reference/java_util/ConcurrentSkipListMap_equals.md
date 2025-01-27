#### equals

```
public boolean equals(Object o)
```
Compares the specified object with this map for equality.
Returns `true` if the given object is also a map and the
two maps represent the same mappings. More formally, two maps
`m1` and `m2` represent the same mappings if
`m1.entrySet().equals(m2.entrySet())`. This
operation may return misleading results if either map is
concurrently modified during execution of this method.
Specified by:
`equals` in interface `Map<K,V>`
Overrides:
`equals` in class `AbstractMap<K,V>`
Parameters:
`o` - object to be compared for equality with this map
Returns:
`true` if the specified object is equal to this map
See Also:
`Object.hashCode()`,
`HashMap`

