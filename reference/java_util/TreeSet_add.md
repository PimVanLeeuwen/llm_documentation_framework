#### add

```
public boolean add(E e)
```
Adds the specified element to this set if it is not already present.
More formally, adds the specified element `e` to this set if
the set contains no element `e2` such that
(e==null ? e2==null : e.equals(e2)).
If this set already contains the element, the call leaves the set
unchanged and returns `false`.
Specified by:
`add` in interface `Collection<E>`
Specified by:
`add` in interface `Set<E>`
Overrides:
`add` in class `AbstractCollection<E>`
Parameters:
`e` - element to be added to this set
Returns:
`true` if this set did not already contain the specified
element
Throws:
`ClassCastException` - if the specified object cannot be compared
with the elements currently in this set
`NullPointerException` - if the specified element is null
and this set uses natural ordering, or its comparator
does not permit null elements

