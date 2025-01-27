#### containsAll

```
public boolean containsAll(Collection<?> c)
```
Returns true if this collection contains all of the elements
in the specified collection.This implementation iterates over the specified collection,
checking each element returned by the iterator in turn to see
if it's contained in this collection. If all elements are so
contained true is returned, otherwise false.
Specified by:
`containsAll` in interface `Collection<E>`
Parameters:
`c` - collection to be checked for containment in this collection
Returns:
true if this collection contains all of the elements
in the specified collection
Throws:
`ClassCastException` - if the types of one or more elements
in the specified collection are incompatible with this
collection
(optional)
`NullPointerException` - if the specified collection contains one
or more null elements and this collection does not permit null
elements
(optional),
or if the specified collection is null.
See Also:
`contains(Object)`

