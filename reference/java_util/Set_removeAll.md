#### removeAll

```
boolean removeAll(Collection<?> c)
```
Removes from this set all of its elements that are contained in the
specified collection (optional operation). If the specified
collection is also a set, this operation effectively modifies this
set so that its value is the asymmetric set difference of
the two sets.
Specified by:
`removeAll` in interface `Collection<E>`
Parameters:
`c` - collection containing elements to be removed from this set
Returns:
true if this set changed as a result of the call
Throws:
`UnsupportedOperationException` - if the removeAll operation
is not supported by this set
`ClassCastException` - if the class of an element of this set
is incompatible with the specified collection
(optional)
`NullPointerException` - if this set contains a null element and the
specified collection does not permit null elements
(optional),
or if the specified collection is null
See Also:
`remove(Object)`,
`contains(Object)`

