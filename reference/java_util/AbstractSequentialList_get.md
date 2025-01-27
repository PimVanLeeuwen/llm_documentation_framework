#### get

```
public E get(int index)
```
Returns the element at the specified position in this list.This implementation first gets a list iterator pointing to the
indexed element (with listIterator(index)). Then, it gets
the element using ListIterator.next and returns it.
Specified by:
`get` in interface `List<E>`
Specified by:
`get` in class `AbstractList<E>`
Parameters:
`index` - index of the element to return
Returns:
the element at the specified position in this list
Throws:
`IndexOutOfBoundsException` - if the index is out of range
(index < 0 || index >= size())

