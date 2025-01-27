#### retainAll

```
public boolean retainAll(Collection<?> c)
```
Retains only the elements in this list that are contained in the
specified collection. In other words, removes from this list all
of its elements that are not contained in the specified collection.
Specified by:
`retainAll` in interface `Collection<E>`
Specified by:
`retainAll` in interface `List<E>`
Overrides:
`retainAll` in class `AbstractCollection<E>`
Parameters:
`c` - collection containing elements to be retained in this list
Returns:
`true` if this list changed as a result of the call
Throws:
`ClassCastException` - if the class of an element of this list
is incompatible with the specified collection
(optional)
`NullPointerException` - if this list contains a null element and the
specified collection does not permit null elements
(optional),
or if the specified collection is null
See Also:
`Collection.contains(Object)`

