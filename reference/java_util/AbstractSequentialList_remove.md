#### remove

```
public E remove(int index)
```
Removes the element at the specified position in this list (optional
operation). Shifts any subsequent elements to the left (subtracts one
from their indices). Returns the element that was removed from the
list.This implementation first gets a list iterator pointing to the
indexed element (with listIterator(index)). Then, it removes
the element with ListIterator.remove.Note that this implementation will throw an
UnsupportedOperationException if the list iterator does not
implement the remove operation.
Specified by:
`remove` in interface `List<E>`
Overrides:
`remove` in class `AbstractList<E>`
Parameters:
`index` - the index of the element to be removed
Returns:
the element previously at the specified position
Throws:
`UnsupportedOperationException` - if the remove operation
is not supported by this list
`IndexOutOfBoundsException` - if the index is out of range
(index < 0 || index >= size())

