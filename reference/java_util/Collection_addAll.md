#### addAll

```
boolean addAll(Collection<? extends E> c)
```
Adds all of the elements in the specified collection to this collection
(optional operation). The behavior of this operation is undefined if
the specified collection is modified while the operation is in progress.
(This implies that the behavior of this call is undefined if the
specified collection is this collection, and this collection is
nonempty.)
Parameters:
`c` - collection containing elements to be added to this collection
Returns:
true if this collection changed as a result of the call
Throws:
`UnsupportedOperationException` - if the addAll operation
is not supported by this collection
`ClassCastException` - if the class of an element of the specified
collection prevents it from being added to this collection
`NullPointerException` - if the specified collection contains a
null element and this collection does not permit null elements,
or if the specified collection is null
`IllegalArgumentException` - if some property of an element of the
specified collection prevents it from being added to this
collection
`IllegalStateException` - if not all the elements can be added at
this time due to insertion restrictions
See Also:
`add(Object)`

