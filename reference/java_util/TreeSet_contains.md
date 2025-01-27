#### contains

```
public boolean contains(Object o)
```
Returns `true` if this set contains the specified element.
More formally, returns `true` if and only if this set
contains an element `e` such that
(o==null ? e==null : o.equals(e)).
Specified by:
`contains` in interface `Collection<E>`
Specified by:
`contains` in interface `Set<E>`
Overrides:
`contains` in class `AbstractCollection<E>`
Parameters:
`o` - object to be checked for containment in this set
Returns:
`true` if this set contains the specified element
Throws:
`ClassCastException` - if the specified object cannot be compared
with the elements currently in the set
`NullPointerException` - if the specified element is null
and this set uses natural ordering, or its comparator
does not permit null elements

