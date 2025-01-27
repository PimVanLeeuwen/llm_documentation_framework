#### retainAll

```
boolean retainAll(Collection<?> c)
```
Retains only the elements in this collection that are contained in the
specified collection (optional operation). In other words, removes from
this collection all of its elements that are not contained in the
specified collection.
Parameters:
`c` - collection containing elements to be retained in this collection
Returns:
true if this collection changed as a result of the call
Throws:
`UnsupportedOperationException` - if the retainAll operation
is not supported by this collection
`ClassCastException` - if the types of one or more elements
in this collection are incompatible with the specified
collection
(optional)
`NullPointerException` - if this collection contains one or more
null elements and the specified collection does not permit null
elements
(optional),
or if the specified collection is null
See Also:
`remove(Object)`,
`contains(Object)`

