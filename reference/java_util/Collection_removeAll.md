#### removeAll

```
boolean removeAll(Collection<?> c)
```
Removes all of this collection's elements that are also contained in the
specified collection (optional operation). After this call returns,
this collection will contain no elements in common with the specified
collection.
Parameters:
`c` - collection containing elements to be removed from this collection
Returns:
true if this collection changed as a result of the
call
Throws:
`UnsupportedOperationException` - if the removeAll method
is not supported by this collection
`ClassCastException` - if the types of one or more elements
in this collection are incompatible with the specified
collection
(optional)
`NullPointerException` - if this collection contains one or more
null elements and the specified collection does not support
null elements
(optional),
or if the specified collection is null
See Also:
`remove(Object)`,
`contains(Object)`

