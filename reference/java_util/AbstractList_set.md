#### set

```
public E set(int index,
             E element)
```
Replaces the element at the specified position in this list with the
specified element (optional operation).This implementation always throws an
`UnsupportedOperationException`.
Specified by:
`set` in interface `List<E>`
Parameters:
`index` - index of the element to replace
`element` - element to be stored at the specified position
Returns:
the element previously at the specified position
Throws:
`UnsupportedOperationException` - if the set operation
is not supported by this list
`ClassCastException` - if the class of the specified element
prevents it from being added to this list
`NullPointerException` - if the specified element is null and
this list does not permit null elements
`IllegalArgumentException` - if some property of the specified
element prevents it from being added to this list
`IndexOutOfBoundsException` - if the index is out of range
(index < 0 || index >= size())

