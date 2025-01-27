#### equals

```
public boolean equals(Object o)
```
Compares the specified object with this list for equality.
Returns `true` if the specified object is the same object
as this object, or if it is also a `List` and the sequence
of elements returned by an iterator
over the specified list is the same as the sequence returned by
an iterator over this list. The two sequences are considered to
be the same if they have the same length and corresponding
elements at the same position in the sequence are equal.
Two elements `e1` and `e2` are considered
equal if `(e1==null ? e2==null : e1.equals(e2))`.
Specified by:
`equals` in interface `Collection<E>`
Specified by:
`equals` in interface `List<E>`
Overrides:
`equals` in class `Object`
Parameters:
`o` - the object to be compared for equality with this list
Returns:
`true` if the specified object is equal to this list
See Also:
`Object.hashCode()`,
`HashMap`

