#### equals

```
public boolean equals(Object o)
```
Compares the specified object with this map for equality. Returns
true if the given object is also a map and the two maps
represent identical object-reference mappings. More formally, this
map is equal to another map m if and only if
this.entrySet().equals(m.entrySet()).Owing to the reference-equality-based semantics of this map it is
possible that the symmetry and transitivity requirements of the
Object.equals contract may be violated if this map is compared
to a normal map. However, the Object.equals contract is
guaranteed to hold among IdentityHashMap instances.
Specified by:
`equals` in interface `Map<K,V>`
Overrides:
`equals` in class `AbstractMap<K,V>`
Parameters:
`o` - object to be compared for equality with this map
Returns:
true if the specified object is equal to this map
See Also:
`Object.equals(Object)`

