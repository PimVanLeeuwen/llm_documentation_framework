#### removeAll

```
public boolean removeAll(Collection<?> c)
```
Removes from this list all of its elements that are contained in
the specified collection. This is a particularly expensive operation
in this class because of the need for an internal temporary array.
Specified by:
`removeAll` in interface `Collection<E>`
Specified by:
`removeAll` in interface `List<E>`
Parameters:
`c` - collection containing elements to be removed from this list
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
`remove(Object)`

