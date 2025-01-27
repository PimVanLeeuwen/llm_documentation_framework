#### equals

```
public boolean equals(Object o)
```
Compares the specified object with this set for equality.
Returns `true` if the specified object is the same object
as this object, or if it is also a `Set` and the elements
returned by an iterator over the
specified set are the same as the elements returned by an
iterator over this set. More formally, the two iterators are
considered to return the same elements if they return the same
number of elements and for every element `e1` returned by
the iterator over the specified set, there is an element
`e2` returned by the iterator over this set such that
`(e1==null ? e2==null : e1.equals(e2))`.
Specified by:
`equals` in interface `Collection<E>`
Specified by:
`equals` in interface `Set<E>`
Overrides:
`equals` in class `AbstractSet<E>`
Parameters:
`o` - object to be compared for equality with this set
Returns:
`true` if the specified object is equal to this set
See Also:
`Object.hashCode()`,
`HashMap`

