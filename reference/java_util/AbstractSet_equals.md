#### equals

```
public boolean equals(Object o)
```
Compares the specified object with this set for equality. Returns
true if the given object is also a set, the two sets have
the same size, and every member of the given set is contained in
this set. This ensures that the equals method works
properly across different implementations of the Set
interface.This implementation first checks if the specified object is this
set; if so it returns true. Then, it checks if the
specified object is a set whose size is identical to the size of
this set; if not, it returns false. If so, it returns
containsAll((Collection) o).
Specified by:
`equals` in interface `Collection<E>`
Specified by:
`equals` in interface `Set<E>`
Overrides:
`equals` in class `Object`
Parameters:
`o` - object to be compared for equality with this set
Returns:
true if the specified object is equal to this set
See Also:
`Object.hashCode()`,
`HashMap`

