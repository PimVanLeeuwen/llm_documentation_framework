#### containsAll

```
boolean containsAll(Collection<?> c)
```
Returns true if this set contains all of the elements of the
specified collection. If the specified collection is also a set, this
method returns true if it is a subset of this set.
Specified by:
`containsAll` in interface `Collection<E>`
Parameters:
`c` - collection to be checked for containment in this set
Returns:
true if this set contains all of the elements of the
specified collection
Throws:
`ClassCastException` - if the types of one or more elements
in the specified collection are incompatible with this
set
(optional)
`NullPointerException` - if the specified collection contains one
or more null elements and this set does not permit null
elements
(optional),
or if the specified collection is null
See Also:
`contains(Object)`

