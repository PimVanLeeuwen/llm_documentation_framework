#### remove

```
public boolean remove(Object o)
```
Removes the specified element from this set if it is present.
More formally, removes an element `e` such that
(o==null ? e==null : o.equals(e)),
if this set contains such an element. Returns `true` if
this set contained the element (or equivalently, if this set
changed as a result of the call). (This set will not contain the
element once the call returns.)
Specified by:
`remove` in interface `Collection<E>`
Specified by:
`remove` in interface `Set<E>`
Overrides:
`remove` in class `AbstractCollection<E>`
Parameters:
`o` - object to be removed from this set, if present
Returns:
`true` if this set contained the specified element
Throws:
`ClassCastException` - if the specified object cannot be compared
with the elements currently in this set
`NullPointerException` - if the specified element is null
and this set uses natural ordering, or its comparator
does not permit null elements

